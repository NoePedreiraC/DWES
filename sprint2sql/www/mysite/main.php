<?php
$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
?>
<html>
<head>
    
    <style>
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
	 }
    </style>
</head>
<body>
<h1>Conexión establecida</h1>

<title>JUEGOS</title>
    <h3>Una selección de cinco canciones, su título, imagen del álbun, género al que pertenece y duración en segundos. Además de un enlace con información extra.</h3><br>

<?php
// Lanzar una query
$query = 'SELECT * FROM tCanciones';
$result = mysqli_query($db, $query) or die('Query error');
mysqli_query($db, $query) or die('Query error');
// Recorrer el resultado
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
//echo "<a href='/home/pra/compartido/detail.php?cancion_id='.$row['id'].'>'.$row['id'] Detalles</a>";
echo "<hr>";

}

mysqli_close($db); 
?>

http://localhost:8083/detail.php?cancion

