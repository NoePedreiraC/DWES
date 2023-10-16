<html>
   <body>
	<h1>Jubilacion</h1
	<?php
	$edad=$_GET["edad"];

	function edad_en_5_annos($edad) {

	return $edad +5;
	}
	if (edad_en_5_annos($edad) >65){

	echo "En 5 años tendras edad de jubilación";
	} else {
	echo "Disfruta de tu tiempo!!";
	}
	?>
	<table>
	<tr>
	  <th>Edad</th>
	  <th>Info</th>
	</tr>

	<?php
	$lista = array (58,59,60,61,62);
	foreach ($lista as $valor){
	echo "<tr>";
	echo "<td>" ,$valor."</td>";
	echo "<td>".mensaje($valor)."</td>";
	echo"</tr>";
	}
	?>
   </body>
</html>
