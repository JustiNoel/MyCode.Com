php
<!DOCTYPE html>
<<html lang="en">
<head>
  <meta charset="<?php bloginfo('charset'); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Economics Students Association of Maseno University - Join us for events, resources, and more!">
  <?php wp_head(); ?>
  <link rel="stylesheet" href="css/style.css">
</head>
<body <?php body_class(); ?>>
  <header>
    <nav class="navbar navbar-expand-lg" style="background: #003087; color: #fff;">
      <div class="container">
        <a class="navbar-brand" href="<?php echo home_url(); ?>">
          <img src="<?php echo get_template_directory_uri(); ?>/assets/images/esamu-logo.png" alt="ESAMU Logo" width="50">
        </a>
        <?php
        wp_nav_menu([
          'theme_location' => 'primary',
          'menu_class' => 'navbar-nav ms-auto',
          'container' => false,
        ]);
        ?>
      </div>
    </nav>
  </header>
