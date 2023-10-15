<html>
   <body>
	<h1>Conversor de longitudes</h1
	<p> Combierte de la unidad especificada a metros </p>
	<p>
	<?php
	if  (isset($_POST["funidad"]) && iseet($_POST["fcantidad"])) {
		$cantidad = $_POST[""<fcantidad"];
		if ($_POST["funidad"]== "pulgada") {
		$metros = $cantidad * 0.254;
		echo $cantidad . " pulgada(s) = " . $metros . " metro(s)";
	}elseif ($_POST["funidad"]== "pie"){
		$metros = $cantidad *0.3048 ;
		echo $cantidad . " pie(s) = " . $metros . " metro(s)";
	}else {
		echo "Unidad no soportada";
	}
}
	<?php
	</p>
	<p>Realiza una nueva conversión;</p>
		<label for= "cantidad_input">Cantidad:</label><br>
		<imput type="text" id="cantidad_input"name="fcantidad"><br>
		<imput type="radio" id="pulgada_input"name= "funidad" value="pulgada">
		<label for= "pulgada_input">Pulgada(s)</label><br>
		<imput type= "radio" id="pie_input" name="funidad" value="pie">
		<label for="pie_input">Pie</label></br>
		<input type="radio" id="otro_input" name="funidad" value="otro">
		<label for="otro_input">Otro</label><br>
		<input type="submit">value="Convertir">
		</form>
   </body>
</html>

