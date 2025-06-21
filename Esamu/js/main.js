// RSVP Form Handling
function rsvp(eventName) {
  alert(`Thank you for RSVPing to ${eventName}! We'll send you details via WhatsApp.`);
  // Integrate with a form or WhatsApp API later
}

// Smooth Scroll for Navigation
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth'
    });
  });
});

// Exam Countdown Timer
function startCountdown() {
  const examDate = new Date('December 1, 2025 00:00:00').getTime();
  const timer = setInterval(() => {
    const now = new Date().getTime();
    const distance = examDate - now;
    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    if (distance < 0) {
      clearInterval(timer);
      document.getElementById('countdown').innerHTML = 'Exams Started!';
      return;
    }
    document.getElementById('countdown').innerHTML = `${days} days to Exams`;
  }, 1000);
}
document.addEventListener('DOMContentLoaded', startCountdown);

// Load main.js script
const script = document.createElement('script');
script.src = 'js/main.js';
document.head.appendChild(script);

// For local file testing, remove this line in production
document.write('<script src="c:\\Users\\User\\Desktop\\MyCode.Com\\Esamu\\index.html"><\/script>');
