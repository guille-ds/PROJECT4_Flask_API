![Blade Runner Chat](/input/poster.png)
# API para análisis de conversaciones

Blade Runner (Ridley Scott,1982) comienza con una escena en la cual vemos dos personajes, sentados uno frente al otro.
Está teniendo lugar un test de Voight-Kampff mediante el cual se evalúa el nivel de empatía de un sujeto en función de las emociones reflejadas en las respuestas a unas sencillas preguntas. 

El objetivo de este proyecto es construir una API que analice características emocionales de conversaciones alojadas en una base de datos conectada a la misma.

La API permite:
- Introducir distintos elementos (usuarios, chats, mensajes) en una base de datos.
- Devolver listado de mensajes para un chat concreto.
- Analizar parámetros (subjetividad, polaridad, neutralidad...) de cada mensaje de un chat.

## introducción de datos [POST]

#### /user/create/<username>
  - Inserta un nuevo usuario en la base de datos
  - Comprueba si ya existe evitando duplicarlo
  
###### *Ej: Inserta nuevo usuario "Tom"*
```ruby
url = "http://localhost:3000/user/create/Tom"
requests.post(url).text
```

#### /chat/create/
  - Inserta un nuevo chat en la base de datos
  - Comprueba si ya existe evitando duplicarlo
  - Comprueba la existencia de los usuarios
  
###### *Ej: Inserta nuevo chat "datamad" con usuarios "alberto" y "tom"*
```ruby

todo = {"chat_name":"datamad", "users":['alberto', 'tom']}

url = "http://localhost:3000/chat/create",params=todo
requests.post(url).text

```
#### /chat/<chat_name>/addmessage
  - Inserta un nuevo mensaje en la base de datos
  - Permite duplicados
  
###### *Ej: Inserta nuevo mensaje de "alberto" en el chat "datamad"*
```ruby
chat_name = "datamad"
todo = {"user":"alberto","message":"qué tal va todo?"}

url = f"http://localhost:3000/chat/{chat_name}/addmessage"
requests.post(url,params=todo).text
```

## obtención de datos [GET]

#### /chat/<chat_name>/list
  
  - Devuelve todos los mensajes de un chat.
###### *Ej: Obtener mensajes del chat "datamad"*
```ruby
chat_name = "datamad"
url = f"http://localhost:3000/chat/{chat_name}/list"

requests.get(url).text
```
## análisis de datos [GET]

#### /chat/<chat_name>/sentiment
  
  - Devuelve los mensajes de un chat
  - Analiza y evalúa los mensajes mediante TextBlob y NLTK
###### *Ej: Inserta nuevo usuario Tom*
```ruby
chat_name = "datamad"
url = f"http://localhost:3000//chat/{chat_name}/sentiment"

requests.get(url).text
```




