<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Recopilar datos del formulario
    $nombre_curso = $_POST['nombre_curso'];
    $descripcion = $_POST['descripcion'];
    $instructor = $_POST['instructor'];
    $entidad_id = $_POST['entidad']; // ID de la entidad seleccionada

    // Crear el arreglo con la estructura esperada
    $formData = [
        "nombre_curso" => $nombre_curso,
        "descripcion" => $descripcion,
        "instructor" => $instructor,
        "entidad_id" => intval($entidad_id) // Convertir a entero
    ];

    // Convertir los datos a JSON
    $jsonData = json_encode($formData);

    // URL del endpoint FastAPI
    $url = 'http://127.0.0.1:8000/postcursos';

    // Inicializar cURL
    $ch = curl_init($url);

    // Configurar opciones de cURL
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);

    // Ejecutar la solicitud y obtener la respuesta
    $response = curl_exec($ch);

    // Manejar errores de cURL
    if ($response === false) {
        echo '<p>Error al enviar los datos: ' . curl_error($ch) . '</p>';
    } else {
        // Decodificar la respuesta del servidor
        $responseData = json_decode($response, true);
        echo '<p>Respuesta del servidor: ' . htmlspecialchars(print_r($responseData, true)) . '</p>';
    }

    // Cerrar cURL
    curl_close($ch);

        // Redirigir al usuario de vuelta a Edufeedback
        header('Location: http://localhost/edufeedback/');
        exit();
}
?>
