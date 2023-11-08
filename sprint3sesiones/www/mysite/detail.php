<?php
// Conexión a la base de datos
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<body>
<?php
// Comprobación si se ha proporcionado un parámetro "cancion_id" en la URL
if (!isset($_GET['cancion_id'])) {
die('No se ha especificado una canción');
}
// Obtener el valor de "cancion_id" de la URL
$cancion_id = $_GET['cancion_id'];
// Consulta SQL para seleccionar la canción con el ID proporcionado
$query = 'SELECT * FROM tCanciones WHERE id='.$cancion_id;
$result = mysqli_query($db, $query) or die('Query error');
// Recuperar la única fila de resultado
$only_row = mysqli_fetch_array($result);
// Mostrar el nombre, imagen y género de la canción
echo '<h1>'.$only_row['nombre'].'</h1>';
echo '<img src='.$only_row['url_imagen'].'></img>';
echo '<h2>'.$only_row['genero'].'</h2>';

?>
<h3>Comentarios:</h3>
<ul>
<?php
// Consulta SQL para obtener los comentarios relacionados con la canción
$query2 = 'SELECT * FROM tComentarios WHERE cancion_id='.$cancion_id;
$result2 = mysqli_query($db, $query2) or die('Query error');
// Mostrar los comentarios y sus fechas
while ($row = mysqli_fetch_array($result2)) {
echo '<li>'.$row['comentario'].'</li>';
echo '<h3>'.$row['fecha'].'</h3> ' ;
}
// Cerrar la conexión a la base de datos
mysqli_close($db);
?>
</ul>
<p>Deja un nuevo comentario:</p>
<form action="/comment.php" method="post">
<textarea rows="4" cols="50" name="new_comment"></textarea><br>
<input type="hidden" name="cancion_id" value="<?php echo $cancion_id; ?>">
<input type="submit" value="Comentar">
</form>
</body>
</html>
