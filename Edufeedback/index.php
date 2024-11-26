
<?php
// Cargar la configuración
$config = include 'config.php';
$baseUrl = $config['base_url'];
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page - Formularios</title>

    <style>
        /* Estilo general para la página */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }

        header {
            text-align: center;
            background-color: #4CAF50;
            color: white;
            padding: 20px 0;
        }

        footer {
            text-align: center;
            background-color: #4CAF50;
            color: white;
            padding: 10px 0;
        }

        /* Estilo para la cuadrícula de las gráficas */
        main {
            padding: 20px;
            display: grid;
            grid-template-columns: repeat(2, 1fr); /* Dos columnas */
            gap: 20px;
            justify-items: center;
        }

        /* Estilo para las imágenes de las gráficas */
        .graficas-container img {
            width: 100%;
            max-width: 500px; /* Máximo tamaño de las imágenes */
            height: auto;
            border: 2px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            cursor: pointer; /* Indicador de que se puede hacer clic en la imagen */
            transition: transform 0.3s ease-in-out; /* Efecto de transición */
        }

        .graficas-container img:hover {
            transform: scale(1.05); /* Efecto de ampliación al pasar el mouse */
        }

        /* Contenedor para las gráficas */
        .graficas-container {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            justify-items: center;
            margin-top: 20px;
        }

        /* Título de las gráficas */
        h2 {
            text-align: center;
            margin-bottom: 20px;
        }

        /* Estilo de los enlaces */
        ul {
            text-align: center;
            list-style-type: none;
            padding: 0;
        }

        ul li {
            margin: 10px 0;
        }

        a {
            text-decoration: none;
            color: #4CAF50;
            font-size: 18px;
        }

        a:hover {
            color: #45a049;
        }

        /* Estilo para la ventana emergente de imagen */
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            padding-top: 100px;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgb(0,0,0);
            background-color: rgba(0,0,0,0.9);
        }

        .modal-content {
            margin: auto;
            display: block;
            max-width: 1200px;
            max-height: 80%;
            object-fit: contain;
        }

        .close {
            position: absolute;
            top: 15px;
            right: 35px;
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
        }

        .close:hover,
        .close:focus {
            color: #bbb;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <header>
        <h1>Edufeedback</h1>
        <p>Por favor, selecciona el formulario al que deseas acceder:</p>
    </header>

    <main>
        <ul>
            <li><a href="<?php echo $baseUrl; ?>/edufeedback/formularioregistroentidades.php">Formulario de Registro de Entidades</a></li>
            <li><a href="<?php echo $baseUrl; ?>/edufeedback/formularioregistrodecursos.php">Formulario de Registro de Cursos</a></li>
            <li><a href="<?php echo $baseUrl; ?>/edufeedback/formularioregistrocomentarios.php">Formulario de Registro de Comentarios</a></li>
        </ul>

        <h2>Gráficas de Análisis de Cursos</h2>
        <!-- Contenedor para las gráficas -->
        <div class="graficas-container">
            <img src="<?php echo $baseUrl; ?>/Edufeedback/graficas/comentarios_por_curso.png" alt="Comentarios por Curso" class="grafica" onclick="mostrarImagen(this)">
            <img src="<?php echo $baseUrl; ?>/Edufeedback/graficas/comentarios_por_entidad.png" alt="Comentarios por Entidad Educativa" class="grafica" onclick="mostrarImagen(this)">
            <img src="<?php echo $baseUrl; ?>/Edufeedback/graficas/distribucion_calificaciones.png" alt="Distribución de Calificaciones" class="grafica" onclick="mostrarImagen(this)">
            <img src="<?php echo $baseUrl; ?>/Edufeedback/graficas/top_5_cursos.png" alt="Top 5 Cursos Mejor Valorados" class="grafica" onclick="mostrarImagen(this)">
        </div>
    </main>

    <footer>
        <p>© 2024 Todos los derechos reservados.</p>
    </footer>

    <!-- Modal para mostrar la imagen ampliada -->
    <div id="myModal" class="modal">
        <span class="close" onclick="cerrarModal()">&times;</span>
        <img class="modal-content" id="img01">
    </div>

    <script>
        // Función para mostrar la imagen en un modal
        function mostrarImagen(img) {
            var modal = document.getElementById("myModal");
            var modalImg = document.getElementById("img01");
            modal.style.display = "block";
            modalImg.src = img.src;
        }

        // Función para cerrar el modal
        function cerrarModal() {
            var modal = document.getElementById("myModal");
            modal.style.display = "none";
        }
    </script>
</body>
</html>
