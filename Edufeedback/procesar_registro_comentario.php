<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Recopilar datos del formulario
    $entidad_id = $_POST['entidad'];
    $curso_id = $_POST['curso'];
    $calificacion = $_POST['calificacion'];
    $comentario = $_POST['comentario'];

    // Crear el arreglo con la estructura esperada
    $formData = [
        "curso_id" => $curso_id,
        "entidad_id" => $entidad_id,
        "comentario" => $comentario,
        "fecha_comentario" => date('c') // Fecha y hora actual en formato ISO 8601
    ];

    // Convertir los datos a JSON
    $jsonData = json_encode($formData);

    // URL del endpoint FastAPI
    $url = 'http://127.0.0.1:8000/postcomentarios';

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
