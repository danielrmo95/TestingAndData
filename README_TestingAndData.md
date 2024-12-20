# Proyecto: TestingAndData

## Descripción
Este proyecto utiliza Docker para garantizar un entorno consistente y fácil de ejecutar para todos los usuarios. Incluye las dependencias y configuraciones necesarias para que cualquier persona pueda clonar el repositorio y ejecutar el proyecto sin configuraciones adicionales.

---

## Requisitos
Antes de comenzar, asegúrate de tener instalado lo siguiente:

1. [Git](https://git-scm.com/)
2. [Docker](https://www.docker.com/get-started)

---

## Paso a Paso

### 1. Clonar el Repositorio
Clona el repositorio en tu máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/danielrmo95/TestingAndData.git
cd TestingAndData
```

---

### 2. Autenticarse en Docker Hub
Si el repositorio de la imagen Docker es privado, necesitas autenticarte en Docker Hub:

```bash
docker login
```

Ingresa tu nombre de usuario y contraseña de Docker Hub o usa un token de acceso.

---

### 3. Descargar la Imagen Docker
Descarga la última versión de la imagen Docker del proyecto:

```bash
docker pull newyork360/testinganddata:latest
```

Este comando descargará la imagen desde Docker Hub.

---

### 4. Ejecutar el Contenedor Docker
Ejecuta el contenedor Docker con el siguiente comando:

```bash
docker run -d -p 8000:8000 newyork360/testinganddata:latest
```

Esto iniciará el proyecto en el puerto `8000`. Puedes acceder al proyecto desde tu navegador en:

[http://localhost:8000](http://localhost:8000)

---

### 5. Verificar el Funcionamiento
Accede a la API o a la interfaz que proporciona el proyecto (por ejemplo, [Swagger UI](http://localhost:8000/docs)) para asegurarte de que todo esté funcionando correctamente.

---

## Notas Importantes

1. **Repositorio Privado**:
   - Si el repositorio Docker es privado, asegúrate de que el propietario te haya agregado como colaborador en Docker Hub.
   - Si no tienes acceso al repositorio, contacta al administrador del proyecto.

2. **Problemas Comunes**:
   - Si no puedes descargar la imagen, verifica tu autenticación en Docker Hub.
   - Asegúrate de que Docker esté corriendo en tu máquina.

3. **Base de Datos u Otros Servicios**:
   - Si el proyecto depende de servicios externos, asegúrate de que estén configurados correctamente y accesibles desde tu máquina local.

---

## ¡Contribuciones!
Si deseas contribuir al proyecto, sigue estos pasos para enviar un Pull Request:

1. **Clonar el Repositorio**:
   - Clona el repositorio a tu máquina local:
     ```bash
     git clone https://github.com/danielrmo95/TestingAndData.git
     cd TestingAndData
     ```

2. **Crea una Rama Nueva**:
   - Crea una nueva rama para tu contribución:
     ```bash
     git checkout -b nombre-de-tu-rama
     ```

3. **Realiza Cambios**:
   - Haz los cambios necesarios en el proyecto y guarda los archivos modificados.

4. **Confirma tus Cambios**:
   - Añade los cambios al área de preparación y realiza un commit:
     ```bash
     git add .
     git commit -m "Descripción breve de los cambios"
     ```

5. **Sube tus Cambios**:
   - Sube los cambios a tu repositorio remoto en la nueva rama:
     ```bash
     git push origin nombre-de-tu-rama
     ```

6. **Abre un Pull Request**:
   - Ve al repositorio original en GitHub: [TestingAndData](https://github.com/danielrmo95/TestingAndData.git).
   - Haz clic en "Compare & pull request" y proporciona una descripción de los cambios que realizaste.

---

¡Gracias por usar TestingAndData! Si tienes alguna duda o problema, no dudes en abrir un Issue en el repositorio de GitHub.
