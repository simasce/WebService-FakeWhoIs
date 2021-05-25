from flask import Flask, request
from datetime import datetime
from whois_info import WhoisInfo
from contact import Contact
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication
from entrycontainer import EntryContainer
import time, contactparser, defaults
import json
import spyneapp

SWAGGER_URL = '/swagger' 
API_URL = '/static/swagger_api.json'  

app = Flask(__name__, static_url_path='/static')

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/soap': WsgiApplication(spyneapp.create_app(app))
})

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
	
def printd(str):
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime('%d-%b-%Y %H:%M:%S.%f')
	print(timestampStr + " : " + str, flush=True)
	
@app.route('/whois_info/', methods=['GET'])
def all_info():
	json_string = json.dumps([ob.serialize() for ob in EntryContainer.entries])
	return json_string, 200, {'Content-Type': 'application/json'}

@app.route('/whois_info/<int:id>', methods=['GET'])
def get_info(id):
	for entry in EntryContainer.entries:
		if entry.id == id:
			json_string = json.dumps(entry.serialize())
			return json_string, 200, {'Content-Type': 'application/json'}				
	return 'Could not find such item!', 404
	
@app.route('/whois_info/<int:id>', methods=['PUT'])
def update_info(id):
	jsn = request.get_json()
	if jsn == None:
		return 'Bad request, either non json or needs \'application/json\' set as Content-Type in headers', 400
	wInfo = WhoisInfo.deserialize(jsn)
	for entry in EntryContainer.entries:
		if entry.id == id:
			for contact in wInfo.contacts:
				if contactparser.contact_exists(contact.id):
					res, status = contactparser.edit_contact(contact.id, contact)
					if status != 200:
						return 'Internal error when updating contacts! ' + res, 500
				else:
					res, status = contactparser.add_contact(contact)
					if status != 201:
						return 'Internal error when adding contacts! ' + res, 500
			entry.id = wInfo.id
			entry.website = wInfo.website
			entry.ipaddress = wInfo.ipaddress
			entry.contacts = wInfo.contacts
			json_string = json.dumps(entry.serialize())
			return json_string, 201, {'Content-Type': 'application/json'}				
	return 'Could not find such item!', 404
	
@app.route('/whois_info/', methods=['POST'])
def add_info():
	jsn = request.get_json()
	if jsn == None:
		return 'Bad request, either non json or needs \'application/json\' set as Content-Type in headers', 400
	wInfo = WhoisInfo.deserialize(jsn)
	for entry in EntryContainer.entries:
		if entry.id == wInfo.id:
			return 'Item with such ID already exists!', 400
	for contact in wInfo.contacts:
		if contactparser.contact_exists(contact.id):
			res, status = contactparser.edit_contact(contact.id, contact)
			if status != 200:
				return 'Internal error when updating contacts! ' + res, 500
		else:
			res, status = contactparser.add_contact(contact)
			if status != 201:
				return 'Internal error when adding contacts! ' + res, 500
	EntryContainer.entries.append(wInfo)	
	json_string = json.dumps(wInfo.serialize())
	return json_string, 201, {'Content-Type': 'application/json'}
	
	
@app.route('/whois_info/<int:id>', methods=['DELETE'])
def delete_info(id):
	for entry in EntryContainer.entries:
		if entry.id == id:
			EntryContainer.entries.remove(entry)
			return 'Item deleted!', 200	
	return 'Item not found!', 404
	
	
if __name__ == '__main__':
	printd('Waiting 5s to start!')
	time.sleep(5)
	printd('Loading WhoisInfo defaults!')
	EntryContainer.entries = defaults.load()
	printd('Starting WhoisInfo application!')
	app.register_blueprint(swaggerui_blueprint)
	app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
	