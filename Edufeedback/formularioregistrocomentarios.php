<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario de Registro de Comentarios</title>
</head>
<body>
    <h2>Formulario de Registro de Comentarios</h2>
    <form action="procesar_registro_comentario.php" method="POST">
        <label for="entidad">Entidad:</label>
        <select id="entidad" name="entidad" required>
            <?php include 'cargar_entidades.php'; ?>
        </select><br><br>

        <label for="curso">Curso:</label>
        <select id="curso" name="curso" required>
            <?php include 'cargar_cursos.php'; ?>
        </select><br><br>

        <label for="calificacion">Calificación (1-5):</label>
        <input type="number" id="calificacion" name="calificacion" min="1" max="5" required><br><br>

        <label for="comentario">Comentario:</label>
        <textarea id="comentario" name="comentario" rows="4" maxlength="2000" required></textarea><br><br>

        <button type="submit">Enviar</button>
    </form>

    <br>
    <!-- Botón Volver -->
    <button onclick="window.location.href='http://localhost/edufeedback/'">Volver</button>
</body>
</html>
