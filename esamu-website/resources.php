<?php include 'includes/db_connect.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESAMU - Resources</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <?php include 'includes/header.php'; ?>

    <section class="container my-5">
        <h2>Resources</h2>
        <div class="row g-4">
            <?php
            $stmt = $pdo->query("SELECT * FROM resources ORDER BY uploaded_at DESC");
            while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                echo '<div class="col-md-4">';
                echo '<div class="card h-100">';
                echo '<div class="card-body text-center">';
                echo '<h5 class="card-title">' . htmlspecialchars($row['title']) . '</h5>';
                echo '<a href="' . htmlspecialchars($row['file_path']) . '" class="btn btn-success" download>Download</a>';
                echo '</div>';
                echo '</div>';
                echo '</div>';
            }
            ?>
        </div>
        <?php if (isset($_SESSION['admin_logged_in']) && $_SESSION['admin_logged_in']): ?>
            <h3>Upload New Resource</h3>
            <form method="post" enctype="multipart/form-data">
                <div class="mb-3">
                    <input type="text" name="title" class="form-control" placeholder="Resource Title" required>
                </div>
                <div class="mb-3">
                    <input type="file" name="file" class="form-control" required>
                </div>
                <button type="submit" name="upload_resource" class="btn btn-primary">Upload</button>
            </form>
            <?php
            if (isset($_POST['upload_resource'])) {
                $title = sanitize_input($_POST['title']);
                $file = $_FILES['file'];
                $file_path = upload_file($file);
                if ($file_path) {
                    $stmt = $pdo->prepare("INSERT INTO resources (title, file_path) VALUES (?, ?)");
                    $stmt->execute([$title, $file_path]);
                    echo "<p class='text-success'>Resource uploaded successfully!</p>";
                } else {
                    echo "<p class='text-danger'>Error uploading file.</p>";
                }
            }
            ?>
        <?php endif; ?>
    </section>

    <?php include 'includes/footer.php'; ?>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/main.js"></script>
</body>
</html>