# WebService-FakeWhoIs
Docker project for a sample web service using Flask API and 'Contacts' webservice

Link to used container: https://github.com/augkik/contacts/

Server API is written using Python 3 and Flask.

# Installation
Clone repo:
```git clone https://github.com/simasce/WebService-FakeWhoIs --recursive ```

# Usage
Run container: ```docker-compose up```
  
  
The API can be found at ```localhost:5000/whois_info/```

The SOAP API can be found at ```localhost:5000/soap/?wsdl```

The WSDL definition can be found at ```localhost:5000/soap?```

The Swagger UI can be found at ```localhost:5000/swagger```


# REST API

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


# SOAP API

Examples can be found at ```soap_readme.txt```


List of all whois entries:
```list_whois_info()```

Whois entry with given id:
```get_whois_info()```

Update an entry by ID: 
```update_whois_info()```

Remove an entry by ID: 
```delete_whois_info()```

Add new entry:
```add_whois_info()```


