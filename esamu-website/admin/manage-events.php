<?php
session_start();
include '../includes/db_connect.php';
include '../includes/functions.php';

if (!isset($_SESSION['admin_logged_in'])) {
    header("Location: login.php");
    exit();
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['add_event'])) {
    $title = sanitize_input($_POST['title']);
    $date = sanitize_input($_POST['date']);
    $venue = sanitize_input($_POST['venue']);
    $description = sanitize_input($_POST['description']);
    $stmt = $pdo->prepare("INSERT INTO events (title, date, venue, description) VALUES (?, ?, ?, ?)");
    $stmt->execute([$title, $date, $venue, $description]);
}

if (isset($_GET['delete']) && is_numeric($_GET['delete'])) {
    $stmt = $pdo->prepare("DELETE FROM events WHERE id = ?");
    $stmt->execute([$_GET['delete']]);
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESAMU - Manage Events</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <?php include '../includes/header.php'; ?>

    <section class="container my-5">
        <h2>Manage Events</h2>
        <form method="post" class="mb-4">
            <div class="mb-3">
                <input type="text" name="title" class="form-control" placeholder="Event Title" required>
            </div>
            <div class="mb-3">
                <input type="date" name="date" class="form-control" required>
            </div>
            <div class="mb-3">
                <input type="text" name="venue" class="form-control" placeholder="Venue" required>
            </div>
            <div class="mb-3">
                <textarea name="description" class="form-control" placeholder="Description" required></textarea>
            </div>
            <button type="submit" name="add_event" class="btn btn-primary">Add Event</button>
        </form>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Date</th>
                    <th>Venue</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <?php
                $stmt = $pdo->query("SELECT * FROM events ORDER BY date ASC");
                while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($row['title']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['date']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['venue']) . "</td>";
                    echo "<td><a href='?delete=" . $row['id'] . "' class='btn btn-danger btn-sm' onclick='return confirm(\"Are you sure?\")'>Delete</a></td>";
                    echo "</tr>";
                }
                ?>
            </tbody>
        </table>
    </section>

    <?php include '../includes/footer.php'; ?>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>