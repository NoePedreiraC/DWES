<?php
// Establecer una conexión a la base de datos MySQL con los credenciales proporcionados
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<head>
<style>
        /* Estilos CSS para la página web */
        body {
            font-family: "Roboto", sans-serif;
            background-color: grey;
            color: #000000;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            font-weight: bold;
        }
        h1 {
            font-weight: bold;
            text-align: center;
            color:blue;
        }
        
        h3 {
            font-weight: bold;
            text-align: center;
            color: white;
        }
        .comment {
            border: 1px solid #fff;
            margin: 10px;
            padding: 10px;
            background-color: #fff;
            color: #000;
        }
        img {
            max-width: 500px;
            max-height: 5000px;
            display: block;
            margin: 0 auto;
            transition: opacity 0.5s ease; /* Agregamos una transición para la animación de fade-in */
        }
        img:hover {
            opacity: 0.7; /* Cambiamos la opacidad al hacer hover */
        }
        .song-info {
            transition: opacity 0.5s ease; /* Agregamos una transición para la animación de fade-in */
        }
        .song-info:hover {
            opacity: 0.7; /* Cambiamos la opacidad al hacer hover */
        }
    </style>
</head>
<body>
<h1>Conexión establecida</h1>
<!-- Título de la página -->
<title>JUEGOS</title>
	<!-- Descripción de la página -->
    <h3>Una selección de cinco canciones, su título, imagen del álbun, género al que pertenece y duración en segundos. Además de un enlace con información extra.</h3><br>

<?php
// Lanzar una query
$query = 'SELECT * FROM tCanciones';
// Ejecutar la consulta SQL en la base de datos
$result = mysqli_query($db, $query) or die('Query error');
mysqli_query($db, $query) or die('Query error');
// Recorrer el resultado y mostrar la información de las canciones
while ($row = mysqli_fetch_array($result)) {
    echo $row['nombre'];
    echo '<br>';
    echo '<img src="' . $row[2] . '" alt="Imagen de la cancion">';
    echo '<br>';
    echo $row['3'];
    echo '<br>';
    echo $row['4'];
    echo '<br>';
    echo "<a href='detail.php?cancion_id={$row['id']}'>Detalles</a>";
echo "<hr>";
}
// Cerrar la conexión a la base de datos
mysqli_close($db); 
?>

