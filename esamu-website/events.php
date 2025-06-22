<?php include 'includes/db_connect.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESAMU - Events</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <?php include 'includes/header.php'; ?>

    <section class="container my-5">
        <h2>Upcoming Events</h2>
        <div class="row g-4">
            <?php
            $stmt = $pdo->query("SELECT * FROM events ORDER BY date ASC");
            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                echo '<div class="col-md-4">';
                echo '<div class="card h-100">';
                echo '<div class="card-body text-center">';
                echo '<h5 class="card-title">' . htmlspecialchars($row['title']) . '</h5>';
                echo '<p class="card-text">Date: ' . htmlspecialchars($row['date']) . '<br>Venue: ' . htmlspecialchars($row['venue']) . '</p>';
                echo '<p>' . htmlspecialchars($row['description']) . '</p>';
                echo '<button class="btn btn-primary" onclick="rsvp(\'' . $row['title'] . '\')">RSVP</button>';
                echo '</div>';
                echo '</div>';
                echo '</div>';
            }
            ?>
        </div>
    </section>

    <?php include 'includes/footer.php'; ?>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/main.js"></script>
</body>
</html>