<?php include 'includes/db_connect.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESAMU - Economics Students Association</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #003087;">
            <div class="container">
                <a class="navbar-brand" href="index.php">ESAMU</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="index.php">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="calendar.php">Calendar</a></li>
                        <li class="nav-item"><a class="nav-link" href="events.php">Events</a></li>
                        <li class="nav-item"><a class="nav-link" href="resources.php">Resources</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.php">Contact</a></li>
                        <li class="nav-item"><a class="nav-link" href="admin/">Admin</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <section class="hero" style="background: url('assets/images/lake-victoria-sunset.jpg') no-repeat center center/cover; height: 80vh; position: relative;">
        <div class="hero-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5);"></div>
        <div class="hero-content text-center text-white" style="position: relative; z-index: 1; padding-top: 20vh;">
            <h1 class="display-4">Welcome to ESAMU</h1>
            <p class="lead">Economics Students Association of Maseno University - Skilad Economics!</p>
            <a href="calendar.php" class="btn btn-warning btn-lg">Check Calendar</a>
        </div>
    </section>

    <section class="container my-5">
        <h2>About ESAMU</h2>
        <p>We empower Maseno economics students with knowledge, events, and opportunities. Join us for Debate Day, Fun Day, and more!</p>
    </section>

    <footer class="text-center py-3" style="background-color: #003087; color: #fff;">
        <p>&copy; 2025 ESAMU - Maseno University. All Rights Reserved.</p>
        <p><a href="https://wa.me/+254123456789" class="text-warning">WhatsApp Us</a> | Donate via M-Pesa: Paybill 123456</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/main.js"></script>
</body>
</html>