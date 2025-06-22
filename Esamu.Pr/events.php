<?php
/*
Template Name: Events
*/
get_header(); ?>
<section class="hero" id="home">
  <h1>Welcome to Esamu Events</h1>
  <p>Join us for exciting events, learning, and fun!</p>
  <div id="countdown"></div>
</section>
<div class="container" id="events">
  <h2>Upcoming Events</h2>
  <div class="events-grid">
    <div class="event-card">
      <img src="https://www.istockphoto.com/photo/public-debate-gm1435365112-476728324?utm_campaign=srp_photos_top&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fdebate&utm_medium=affiliate&utm_source=unsplash&utm_term=debate%3A%3A%3A" alt="Debate Day">
      <h3>Debate Day</h3>
      <p>September 19, 2025 - Maseno Main Hall</p>
      <button onclick="rsvp('Debate Day')">RSVP</button>
    </div>
    <div class="event-card">
      <img src="https://www.istockphoto.com/photo/hippie-woman-stroll-on-mountain-gm612619528-105555089?utm_campaign=srp_photos_top&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Ffun-day&utm_medium=affiliate&utm_source=unsplash&utm_term=fun+day%3A%3A%3A" alt="Fun Day">
      <h3>Fun Day</h3>
      <p>October 24, 2025 - Kisumu Impala Sanctuary</p>
      <button onclick="rsvp('Fun Day')">RSVP</button>
    </div>
    <div class="event-card">
      <img src="https://www.istockphoto.com/photo/data-analysis-science-and-big-data-with-ai-technology-analyst-or-scientist-uses-a-gm1979289147-558917489?utm_campaign=srp_photos_top&utm_content=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fbusiness-ideas&utm_medium=affiliate&utm_source=unsplash&utm_term=business+ideas%3A%3A%3A" alt="Business Ideas Day">
      <h3>Business Ideas Day</h3>
      <p>November 14, 2025 - Maseno Library</p>
      <button onclick="rsvp('Business Ideas Day')">RSVP</button>
    </div>
  </div>
</div>
<div class="container" id="about">
  <h2>About Esamu</h2>
  <p>
    Esamu is a vibrant student organization dedicated to hosting events that inspire, educate, and connect students across the region. Join us for debates, fun days, business idea competitions, and more!
  </p>
</div>
<script src="js/main.js"></script>
<?php get_footer(); ?>
