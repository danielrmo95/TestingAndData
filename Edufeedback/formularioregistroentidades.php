<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Registro</title>
</head>
<body>
    <h2>Formulario de Registro de Comentarios</h2>
    <form method="POST" action="procesar_registro_entidad.php">
        <label for="nombre_entidad">Nombre Entidad:</label>
        <input type="text" id="nombre_entidad" name="nombre_entidad" required maxlength="100"><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required maxlength="100"><br><br>

        <label for="contrasena">Contraseña:</label>
        <input type="password" id="contrasena" name="contrasena" required maxlength="255"><br><br>

        <label for="nombre_representante">Nombre del Representante:</label>
        <input type="text" id="nombre_representante" name="nombre_representante" required maxlength="100"><br><br>

        <label for="telefono_representante">Teléfono del Representante:</label>
        <input type="tel" id="telefono_representante" name="telefono_representante" maxlength="15"><br><br>

        <button type="submit">Enviar</button>
    </form>
    <br>
    <!-- Botón Volver -->
    <button onclick="window.location.href='http://localhost/edufeedback/'">Volver</button>
</body>
</html>
