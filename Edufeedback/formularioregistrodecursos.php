<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Registro de Cursos</title>
</head>
<body>
    <h2>Formulario de Registro de Cursos</h2>
    <form action="procesar_registro_curso.php" method="POST">
        <label for="nombre_curso">Nombre del Curso:</label>
        <input type="text" id="nombre_curso" name="nombre_curso" required maxlength="150"><br><br>

        <label for="descripcion">Descripción:</label>
        <textarea id="descripcion" name="descripcion" rows="4" maxlength="2000"></textarea><br><br>

        <label for="instructor">Instructor:</label>
        <input type="text" id="instructor" name="instructor" maxlength="100"><br><br>

        <label for="entidad">Entidad:</label>
        <select id="entidad" name="entidad" required>
            <?php include 'cargar_entidades.php'; ?>
        </select><br><br>

        <button type="submit">Enviar</button>
    </form>

    <br>
    <!-- Botón Volver -->
    <button onclick="window.location.href='http://localhost/edufeedback/'">Volver</button>
</body>
</html>
