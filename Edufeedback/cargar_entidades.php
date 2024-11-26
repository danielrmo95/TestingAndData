<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

// URL del API
$url = 'http://127.0.0.1:8000/getentidades';

// Inicializa cURL
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Ejecuta la solicitud
$response = curl_exec($ch);

// Verifica errores de cURL
if (curl_errno($ch)) {
    echo '<option>Error al conectar con el API: ' . curl_error($ch) . '</option>';
} else {
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    if ($http_code == 200) {
        $data = json_decode($response, true);

        if ($data) {
            foreach ($data as $entidad) {
                echo '<option value="' . htmlspecialchars($entidad['entidad_id']) . '">' . htmlspecialchars($entidad['nombre']) . '</option>';
            }
        } else {
            echo '<option>Error al procesar la respuesta del API</option>';
        }
    } else {
        echo '<option>Error: El API devolvió el código ' . $http_code . '</option>';
    }
}

// Cierra cURL
curl_close($ch);
?>