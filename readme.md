<p>Client provides its unique identifier in JSON format:
<br><kbd>
{"unique_identifier": "client's unique identifier"}
</kbd>
<br><br>
The unique identifier must be of type String. If the identifier format is not String, then the client will receive an error response in JSON format
<br><kbd>{"status": "error", "message": "no string format"}</kbd>

<br>
Client receive response in JSON format with unique code:
<br>
<kbd>{"unique_code": "client's unique code"}</kbd>
<br><br>
Docker run command with Volume:<br>

<kbd>docker run -d --rm --name serverapp -v sqlite:/usr/src/app/sqlite -p 8000:8000 serverapp</kbd>

Docker run command with mounted folder: <br><br>
<kbd>
docker run -d --rm --name serverapp -v C:/code/problem3/sqlite:/usr/src/app/sqlite -p 8000:8000 serverapp
</kbd>

Run app with command:<br>
<kbd>
docker compose up -d
</kbd>

Connect to Docker container:<br>
<kbd>
docker exec -ti [CONTEINER-ID] ash 
</kbd>
</p>

Path to log-file in container:<br>
<kbd>
/usr/src/app/log/messages.log
</kbd>

Path to clients.db in container:<br>
<kbd>
/usr/src/app/sqlite/clients.db
</kbd>