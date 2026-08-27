from wsgiref.simple_server import make_server
import json

#almacenamiento tareas
task = {}
next_id = 1

def app(environ, start_response):

    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]

    print(f"Metodo: {method}")
    print(f"Ruta: {path}")

  
    if method == "GET" and path == "/":
        status = "302 found"
        headers = [("Location", "/tasks")]
        start_response(status, headers)
        return [b"rediriguiendo a /tasks"]

    elif method == "GET" and path == "/tasks":
        response_body = json.dumps(list(task.values()))
        status = "200 OK"
        headers = [("Location", "/tasks")]
        start_response(status,headers)
        return [response_body.encode()]    




    elif method == "GET" and path.startswith("/tasks/"):
        partes = path.split("/")
        task_id_texto = partes[2]
        task_id = int(task_id_texto)
        if task_id in task:
            tarea_encontrada = task[task_id]
            response_body = json.dumps(tarea_encontrada)
            status = "200 OK"
            headers = [("Content-Type", "application/json")]
            start_response(status,headers)
            return [response_body.encode()]
        else:
            status = "404 No Encontrado"
            headers = [("Content-Type", "text/plain")]
            start_response(status,headers)
            return [b"Esta tarea no existe"]
    elif method == "POST" and path == "/tasks":
        global next_id

        content_length = int(environ.get("CONTENT_LENGTH", 0) or 0)
        body_bytes = environ["wsgi.input"].read(content_length)
        data = json.loads(body_bytes)
        data["id"] = next_id
        task[next_id] = data
        next_id += 1

        response_body = json.dumps(data)
        status = "201 Created"
        headers = [("Content-Type", "application/json")]
        start_response(status,headers)
        return [response_body.encode()]

    elif method == "PATCH" and path.startswith("/tasks/"):
        partes = path.split("/")
        task_id_texto = partes[2]
        task_id = int(task_id_texto)
        if task_id in task:
            content_length = int(environ.get("CONTENT_LENGTH", 0) or 0)
            body_bytes = environ["wsgi.input"].read(content_length)
            cambios = json.loads(body_bytes)
            tarea_existente = task[task_id]
            tarea_existente.update(cambios)
            response_body = json.dumps(tarea_existente)
            status = "200 OK"
            headers = [("Content-Type", "application/json") ]
            start_response(status,headers )
            return[response_body.encode()]
        else:
            status = "404 Not Found"
            headers = [("Content-Type", "text/plain")]
            start_response(status,headers)
            return [b"Ruta no encontrada"]

    elif method == "DELETE" and path.startswith("/tasks/"):
            partes = path.split("/")
            task_id_texto = partes[2]
            task_id = int(task_id_texto)
            if task_id in task:
                del task[task_id]
                status = "204 No Content"
                headers = [("Content-Type", "text/plain")]
                start_response(status,headers)
                return[b""]
            else:
                status = "404 Not Found"
                headers = [("Content-Type", "text/plain")]
                start_response(status,headers)
                return[b"Ruta no encontrada"]
            
        
    
    
 

    else:
        status = "404 Not Found"
        headers = [("Content-Type", "text/plain")]
        start_response(status,headers)
        return[b"Ruta no encontrada"]
   

    

if __name__ == "__main__":
    with make_server("",9292, app) as server:
        print("servidor corriendo en http://localhost:9292")
        print("presiona Ctrl+C para detener")
        server.serve_forever()