# TallerHttp-Tobias-Andrada
Para la realizacion de este proyecto nos juntamos con mi equipo para poder ir hablando los temas, ademas de que ninguno tenia un amplio conocimiento sobre python por lo que el trabajar en conjunto nos permitio comprender mejor el problema.
Mis compañeros son: Santino Escobar y Matias Cerioli.

El GET es un metodo que sirve para leer un recurso, no lo modifica por lo que es seguro e idempotente y genera una respuesta que indica si la tarea existe.
El DELETE elimina la tarea seleccionada, es idempotente porque borrar algo que ya esta borrado no cambia nada, el resultado final es siempre el mismo, aunqe a partir de la segunda vez el servidor en lugar de responder 204 como la primera vez pasa a responder 404.
El PATCH sirve para modificar parcialmente un recurso que ya existe. Solo cambia los campos que mando en el body, el resto de la tarea queda igual, es idempotente porque ejecutar el mismo patch varias veces deja el recurso en el mismo estado.
El POST crea un recurso nuevo.
POST no es idempotente porque si realizas dos post seguidos, por mas que tengan el mismo nombre, sea crean 2 archivos con distinto ID, terminando con 2 tareas distintas en lugar de una sola tarea.
