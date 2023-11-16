<?php
// Establecer una conexión a la base de datos MySQL
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
    <body>
        <?php
// Obtener los valores enviados mediante el método POST
            $cancion_id = $_POST['cancion_id'];
            $comentario = $_POST['new_comment'];

            session_start();
            $user_id;
            if (!empty($_SESSION['user_id'])) {
            $user_id = $_SESSION['user_id'];
            }

// Obtener la fecha actual en el formato "ymd"
            $now = new DateTime('now');
            $now = $now-> format ('ymd');
// Construir la consulta SQL para insertar un nuevo comentario en la base de datos
            $query = "INSERT INTO tComentarios(comentario, cancion_id, usuario_id,fecha)
            VALUES ('".$comentario."',".$cancion_id.",NULL,".$now.")";
// Ejecutar la consulta SQL en la base de datos
            mysqli_query($db, $query) or die('Error');
// Mostrar un mensaje de éxito junto con el ID del comentario recién insertado
            echo "<p>Nuevo comentario ";
            echo mysqli_insert_id($db);
            echo " añadido</p>";
// Agregar un enlace para volver a la página de detalles de la canción
            echo "<a href='/detail.php?cancion_id=".$cancion_id."'>Volver</a>";
// Cerrar la conexión a la base de datos
            mysqli_close($db);
        ?>
    </body>
</html>
