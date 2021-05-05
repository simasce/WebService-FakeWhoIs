from contact import Contact
import requests

request_url = "http://contacts:5000/contacts/"

def get_contacts():
	ret = requests.get(request_url)
	if ret.ok:
		return ret.json(), 200
	return ret.text, ret.status_code
	
def get_contact_raw(id):
	ret = requests.get(request_url + str(id), timeout=1)
	if ret.ok:
		return ret.json(), 200
	return ret.text, ret.status_code
	
def get_contact(id):
	ret = requests.get(request_url + str(id))
	if ret.ok:
		return Contact.deserialize(ret.json()), 200
	return ret.text, ret.status_code
	
def edit_contact(id, contact):
	if id == contact.id:
		delete_contact(id) #the 'contacts' API has a bug (feature?) where it cannot edit existing IDs to same IDs
		ret, stat = add_contact(contact)
		if stat == 201:
			return ret, 200
		return ret, stat
	jsn = contact.serialize()
	ret = requests.put(request_url + str(id), json = jsn)
	if ret.ok:
		return "", 200
	return ret.text, ret.status_code
	
def add_contact(contact):
	jsn = contact.serialize()
	ret = requests.post(request_url, json = jsn)
	if ret.ok:
		return "", 201
	return ret.text, ret.status_code
	
def delete_contact(id):
	ret = requests.delete(request_url + str(id))
	if ret.ok:
		return "", 200
	return ret.text, ret.status_code

def contact_exists(id):
	ret, status = get_contact(id)
	if status != 200:
		return False
	return True
			