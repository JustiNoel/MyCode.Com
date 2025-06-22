function rsvp(eventName) {
    if (confirm(`RSVP for ${eventName}? We'll contact you via WhatsApp.`)) {
        alert('RSVP recorded! Check your messages soon.');
        // Add backend integration (e.g., AJAX to save RSVP) later
    }
}

function startCountdown() {
    const examDate = new Date('December 1, 2025 00:00:00').getTime();
    const timer = setInterval(() => {
        const now = new Date().getTime();
        const distance = examDate - now;
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        if (distance < 0) {
            clearInterval(timer);
            document.getElementById('countdown')?.innerHTML = 'Exams Started!';
            return;
        }
        document.getElementById('countdown')?.innerHTML = `${days} days to Exams`;
    }, 1000);
}

document.addEventListener('DOMContentLoaded', startCountdown);