<?php include 'includes/db_connect.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESAMU - Calendar</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <?php include 'includes/header.php'; ?>

    <section class="container my-5">
        <h2>Second Semester 2025 Calendar</h2>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Date</th>
                    <th>Event</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>September 1, 2025</td><td>Classes Begin</td></tr>
                <tr><td>September 12, 2025</td><td>Add/Drop Deadline</td></tr>
                <tr><td>October 20, 2025</td><td>Mashujaa Day (No Classes)</td></tr>
                <tr><td>November 7, 2025</td><td>Last Day to Withdraw</td></tr>
                <tr><td>December 1–12, 2025</td><td>End-of-Semester Exams</td></tr>
                <tr><td>December 13, 2025</td><td>Semester Ends</td></tr>
            </tbody>
        </table>
    </section>

    <?php include 'includes/footer.php'; ?>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/main.js"></script>
</body>
</html>