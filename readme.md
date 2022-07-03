<p>Client provides its unique identifier in JSON format:
<br>
{"unique_identifier": "client's unique identifier"}
<br><br>
The unique identifier must be of type String. If the identifier format is not String, then the client will receive an error response in JSON format
<br>
{"status": "error", "message": "no string format"}
<br><br>
Client receive response in JSON format with unique code:
<br>
{"unique_code": "client's unique code"}
<br><br>
Docker run command:<br>
docker run -d --rm --name serverapp -v sqlite:/usr/src/app/sqlite -p 8000:8000 serverapp

<br>
</p>