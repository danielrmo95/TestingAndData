import requests

# URL de la página
url = 'https://www.despegar.com.co/shop/flights/results/roundtrip/BOG/SMR/2024-08-15/2024-08-16/1/0/0?from=SB&di=1&reSearch=true'

# Ruta donde se guardará el archivo
save_path = 'C:/Users/Daniel Romero/Desktop/fastapi-mysql-restapi/full_page.html'

# Descargar el contenido de la página
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    html_content = response.text
    # Guardar el HTML completo
    with open(save_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f'Página guardada en: {save_path}')
else:
    print(f'Error al descargar la página. Código de estado: {response.status_code}')
