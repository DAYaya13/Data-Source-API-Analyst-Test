📘 Google Colab Notebook: GitHub API Extraction
En la carpeta /Postman_Collection/ se encuentra el archivo Github_API_Extraction_Final.ipynb, el cual documenta el proceso completo de autenticación y extracción de datos desde la API de GitHub utilizando Python.

🧩 Contenido del notebook:
Autenticación mediante token personal (PAT) usando headers recomendados por GitHub.

Extracción de datos desde los siguientes endpoints de la API REST:

GET /search/repositories: búsqueda de repositorios públicos por palabra clave.

GET /repos/{owner}/{repo}/commits: historial de commits recientes en un repositorio.

GET /repos/{owner}/{repo}/contents/{path}: lectura de archivos específicos como README.md.

Paginación para recorrer múltiples páginas de resultados (per_page y page).

Exportación a CSV de los datos obtenidos usando pandas.

💡 Notas:
El notebook puede ser ejecutado directamente en Google Colab.

Requiere que el usuario proporcione un token personal válido de GitHub.

Incluye validaciones de errores y ejemplos de respuesta.

