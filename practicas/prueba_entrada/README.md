
### 3.2 API + jq

```bash
curl https://jsonplaceholder.typicode.com/posts/1 -s -o api_response.json;
```
Lo anterior realiza una petición a una API, viendo la estructura de la API y el valor obtenido, podemos decir que la API es para realizar una búsqueda de un posts por su id, el resultado que se obtiene se guarda en un archivo api_response.json

Ademas en el encabezado(header) `Content-Type` es de tipo `application/json`, esto indica que la respuesta está en formato JSON.

```bash
jq -r '.title' api_response.json > api_title.txt
```

jq es una herramienta de linea de comandos para JSON, con el comando anterior lo que se realiza realizar un filtro den el archivo `api_response.json` y extraer las coincidencias del filtro en otro archivo `api_title.txt`, en este caso con la opción -r le indicamos que extraeremos texto plano(sin las comillas), y el filtro seria '.title', esto indica que se busque la clave title desde la raíz(por el punto antes de title) del json