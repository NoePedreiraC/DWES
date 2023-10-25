<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<?php
$cancion_id = $_POST['cancion_id'];
$comentario = $_POST['new_comment'];
$now = new DateTime('now');
$now = $now-> format ('ymd');
$query = "INSERT INTO tComentarios(comentario, cancion_id, usuario_id,fecha)
VALUES ('".$comentario."',".$cancion_id.",NULL,".$now.")";
mysqli_query($db, $query) or die('Error');
echo "<p>Nuevo comentario ";
echo mysqli_insert_id($db);
echo " añadido</p>";
echo "<a href='/detail.php?cancion_id=".$cancion_id."'>Volver</a>";
mysqli_close($db);
?>
</body>
</html>