<?php
/*
Template Name: Events
*/
get_header(); ?>
<div class="container">
  <h2>Upcoming Events</h2>
  <div class="events-grid">
    <div class="event-card">
      <img src="<?php echo get_template_directory_uri(); ?>/assets/images/debate-day.jpg" alt="Debate Day">
      <h3>Debate Day</h3>
      <p>September 19, 2025 - Maseno Main Hall</p>
      <button onclick="rsvp('Debate Day')">RSVP</button>
    </div>
    <div class="event-card">
      <img src="<?php echo get_template_directory_uri(); ?>/assets/images/fun-day.jpg" alt="Fun Day">
      <h3>Fun Day</h3>
      <p>October 24, 2025 - Kisumu Impala Sanctuary</p>
      <button onclick="rsvp('Fun Day')">RSVP</button>
    </div>
    <div class="event-card">
      <img src="<?php echo get_template_directory_uri(); ?>/assets/images/business-day.jpg" alt="Business Ideas Day">
      <h3>Business Ideas Day</h3>
      <p>November 14, 2025 - Maseno Library</p>
      <button onclick="rsvp('Business Ideas Day')">RSVP</button>
    </div>
  </div>
</div>
<script src="js/main.js"></script>
<?php get_footer(); ?>
