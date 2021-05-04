# WebService-FakeWhoIs
Docker project for a sample web service using Flask API and 'Contacts' webservice

Link to used container: https://github.com/augkik/contacts/

Server API is written using Python 3 and Flask.

# Usage
Run container:
```docker-compose up```
  
The api can be found at ```localhost:5000/whois_info/```

The Swagger UI can be found at ```localhost:5000/swagger```

# API

GET 

List of all whois entries:
```/whois_info/```

Whois entry with given id:
```/whois_info/<id>```

PUT

Update an entry by ID: ```/whois_info/<id>```

DELETE

Remove an entry by ID: ```/whois_info/<id>```

POST

Add new entry: ```/whois_info/```
