<?php
	$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail'); // CONEXIÓN ENTRE PHP y la base de datos.
    $email = $_POST['email'];
    $password = $_POST['pass'];
    $registered = 0;
    $query = 'SELECT email FROM tUsuarios';
    $result = mysqli_query($db, $query) or die('Query error'); 
    while ($row = mysqli_fetch_array($result) and $registered == 0) { 
        if ($email == $row[0]) {$registered = 1;}
    }
    if ($registered == 0) {die('El correo no esta registrado');}
    $query2 = $db -> prepare('SELECT id,contraseña FROM tUsuarios WHERE email = ?');
    $query2 -> bind_param("s",$email);
    $query2 -> execute();
    $result2 = mysqli_stmt_get_result($query2);
    while ($row2 = mysqli_fetch_array($result2)) {
        if (password_verify($password,$row2[1])) {
            session_start();
            $_SESSION['user_id'] = $row2[0];
            header('Location: main.php');
        } else {
            die('Contraseña incorrecta');
        }
    }
    $query2 -> close();
    mysqli_close($db);
?>
