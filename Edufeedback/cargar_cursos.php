<?php
// URL del endpoint FastAPI para obtener los cursos
$url = 'http://127.0.0.1:8000/getcursos';

// Inicializar cURL
$ch = curl_init($url);

// Configurar opciones de cURL
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Ejecutar la solicitud y obtener la respuesta
$response = curl_exec($ch);

// Manejar errores de cURL
if ($response === false) {
    echo '<p>Error al cargar los cursos: ' . curl_error($ch) . '</p>';
} else {
    // Decodificar la respuesta del servidor
    $cursos = json_decode($response, true);

    // Verificar si hay cursos
    if (count($cursos) > 0) {
        foreach ($cursos as $curso) {
            echo '<option value="' . $curso['curso_id'] . '">' . htmlspecialchars($curso['nombre_curso']) . '</option>';
        }
    } else {
        echo '<option value="">No se encontraron cursos disponibles</option>';
    }
}

// Cerrar cURL
curl_close($ch);
?>
