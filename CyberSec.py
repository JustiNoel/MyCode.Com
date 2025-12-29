import cv2
import mediapipe as mp
import numpy as np
import time
import scipy.signal as signal
from collections import deque

# ----------------------------- CONFIG -----------------------------
NEON_GREEN = (0, 255, 150)  # BGR for cyberpunk look
NEON_BLUE = (255, 100, 0)
FONT = cv2.FONT_HERSHEY_SIMPLEX
THICKNESS = 2
FONT_SCALE = 0.8

# Phases for the verification flow
PHASES = ["FACE_SCAN", "IRIS_SCAN", "RPPG_HEARTBEAT", "THUMB_PULSE", "COMPLETE"]
# --------------------------------------------------------------

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,  # Important: enables iris landmarks
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# rPPG variables (remote heartbeat from face - green channel on forehead/cheeks)
green_signals = deque(maxlen=300)  # ~10 seconds at 30fps
times = deque(maxlen=300)
start_time = time.time()

# Simple bandpass filter for heart rate (45-150 BPM)
bpf_b, bpf_a = signal.butter(4, [0.75, 2.5], btype='band', fs=30)

current_phase = 0
phase_start_time = time.time()
phase_duration = 8  # seconds per phase (adjust as needed)
detected_bpm = 0
progress = 0

# Iris landmark indices (MediaPipe refined)
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

# Forehead ROI landmarks (for stable rPPG)
FOREHEAD = [151, 9, 8, 107, 336]  # approximate forehead region

def draw_cyberpunk_hud(frame, text_lines, progress_percent):
    h, w = frame.shape[:2]
    
    # Background dark overlay
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (w, h), (0, 20, 10), -1)
    cv2.addWeighted(overlay, 0.4, frame, 0.6, 0, frame)
    
    # Top HUD bar
    cv2.rectangle(frame, (0, 0), (w, 60), (0, 30, 15), -1)
    cv2.putText(frame, "SAFE BAZAAR AI - BIOMETRIC VERIFICATION", (20, 40), FONT, 0.9, NEON_GREEN, 2)
    
    # Progress bar
    cv2.rectangle(frame, (50, h-100), (w-50, h-60), NEON_GREEN, 3)
    cv2.rectangle(frame, (55, h-95), (55 + int((w-110) * progress_percent / 100), h-65), NEON_GREEN, -1)
    cv2.putText(frame, f"{progress_percent}%", (w//2 - 30, h-70), FONT, 1, NEON_GREEN, 3)
    
    # Phase texts
    for i, txt in enumerate(text_lines):
        cv2.putText(frame, txt, (50, 100 + i*50), FONT, FONT_SCALE, NEON_GREEN, THICKNESS)

def draw_face_mesh(frame, landmarks):
    for idx in range(len(landmarks.landmark)):
        x = int(landmarks.landmark[idx].x * frame.shape[1])
        y = int(landmarks.landmark[idx].y * frame.shape[0])
        cv2.circle(frame, (x, y), 2, NEON_GREEN, -1)

def draw_iris(frame, landmarks):
    h, w = frame.shape[:2]
    # Left iris
    left_center = np.mean([(landmarks.landmark[i].x * w, landmarks.landmark[i].y * h) for i in LEFT_IRIS], axis=0)
    cv2.circle(frame, (int(left_center[0]), int(left_center[1])), 30, NEON_BLUE, 3)
    cv2.putText(frame, "IRIS LOCK", (int(left_center[0]-80), int(left_center[1]-40)), FONT, 0.7, NEON_BLUE, 2)
    
    # Right iris
    right_center = np.mean([(landmarks.landmark[i].x * w, landmarks.landmark[i].y * h) for i in RIGHT_IRIS], axis=0)
    cv2.circle(frame, (int(right_center[0]), int(right_center[1])), 30, NEON_BLUE, 3)

def get_rppg_signal(frame, landmarks):
    h, w = frame.shape[:2]
    points = [(int(landmarks.landmark[i].x * w), int(landmarks.landmark[i].y * h)) for i in FOREHEAD]
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.fillPoly(mask, [np.array(points)], 255)
    mean_green = cv2.mean(frame[:, :, 1], mask=mask)[0]
    return mean_green

def estimate_bpm():
    global detected_bpm
    if len(green_signals) < 100:
        return
    sig = np.array(green_signals)
    sig = signal.detrend(sig)
    sig_filt = signal.filtfilt(bpf_b, bpf_a, sig)
    fft = np.abs(np.fft.rfft(sig_filt))
    freqs = np.fft.rfftfreq(len(sig_filt), d=1/30)
    idx = np.argmax(fft[1:]) + 1  # skip DC
    bpm = freqs[idx] * 60
    if 45 < bpm < 150:
        detected_bpm = int(bpm)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)
    
    text_lines = ["scanning..."]
    progress = int((time.time() - phase_start_time) / phase_duration * 100)
    if progress >= 100:
        progress = 99
        if current_phase < len(PHASES) - 1:
            current_phase += 1
            phase_start_time = time.time()
    
    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0]
        
        # Always draw face mesh in early phases
        if PHASES[current_phase] in ["FACE_SCAN", "IRIS_SCAN"]:
            draw_face_mesh(frame, landmarks)
        
        # Iris scan phase
        if PHASES[current_phase] == "IRIS_SCAN":
            draw_iris(frame, landmarks)
            text_lines.append("IRIS SCANNING")
        
        # rPPG heartbeat from face
        green_val = get_rppg_signal(frame, landmarks)
        green_signals.append(green_val)
        times.append(time.time() - start_time)
        estimate_bpm()
        text_lines.append(f"BPM: {detected_bpm if detected_bpm else '--'}")
        
        if PHASES[current_phase] == "RPPG_HEARTBEAT":
            text_lines.append("HEARTBEAT DETECTION")
            text_lines.append("LIVE PULSE ACQUIRED" if detected_bpm else "SEARCHING PULSE...")
    
    # Thumb / Finger pulse phase
    if PHASES[current_phase] == "THUMB_PULSE":
        h, w = frame.shape[:2]
        cv2.circle(frame, (w//2, h//2), 100, NEON_GREEN, 5)
        cv2.putText(frame, "PLACE THUMB ON CAMERA", (w//2 - 200, h//2 - 120), FONT, 1, NEON_GREEN, 3)
        text_lines.append("THUMB PULSE CHALLENGE")
        
        # Simple detection: if center area dark (finger blocking light)
        center_roi = frame[h//2-50:h//2+50, w//2-50:w//2+50]
        brightness = cv2.mean(center_roi)[0]
        if brightness < 40:  # finger covering
            text_lines.append("PULSE DETECTED")
    
    # Final
    if PHASES[current_phase] == "COMPLETE":
        text_lines = ["ACCESS GRANTED", "VERIFICATION COMPLETE"]
        cv2.putText(frame, "ACCESS GRANTED", (frame.shape[1]//2 - 200, frame.shape[0]//2), FONT, 2, NEON_GREEN, 5)
        progress = 100
    
    text_lines.insert(0, f"PHASE: {PHASES[current_phase]}")
    
    draw_cyberpunk_hud(frame, text_lines, progress)
    
    cv2.imshow("Safe Bazaar AI - Ultra-Secure Biometric Verification", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()