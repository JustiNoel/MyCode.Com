php
<?php
// Theme setup
function esamu_theme_setup() {
  // Support for title tag
  add_theme_support('title-tag');
  // Support for custom logo
  add_theme_support('custom-logo');
  // Register navigation menu
  register_nav_menus([
    'primary' => __('Primary Menu', 'esamu'),
  ]);
  // Enqueue styles and scripts
  add_action('wp_enqueue_scripts', 'esamu_enqueue_scripts');
}
add_action('after_setup_theme', 'esamu_theme_setup');

function esamu_enqueue_scripts() {
  // Enqueue Bootstrap
  wp_enqueue_style('bootstrap', 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css');
  wp_enqueue_script('bootstrap-js', 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js', [], false, true);
  // Enqueue custom styles
  wp_enqueue_style('esamu-style', get_stylesheet_uri());
  // Enqueue custom JS
  wp_enqueue_script('esamu-js', get_template_directory_uri() . '/js/main.js', [], false, true);
}

// Register custom page templates
function esamu_page_templates($templates) {
  $templates['calendar.php'] = __('Calendar', 'esamu');
  $templates['events.php'] = __('Events', 'esamu');
  return $templates;
}
add_filter('theme_page_templates', 'esamu_page_templates');
