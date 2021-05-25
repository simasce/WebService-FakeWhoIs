from spyne.model.complex import ComplexModel
from spyne import Integer, Unicode, Iterable, Array
from contact import Contact
import contactparser

class WhoisInfo(ComplexModel):
	_type_info = [
		('id', Integer),
		('website', Unicode),
		('ipaddress', Unicode),
		('contacts', Array(Contact)),
	]
		
	def serialize(self):
		return {
			'id': self.id,
			'website': self.website,
			'ipaddress': self.ipaddress,
			'contacts': self.getContactList()
		}
		
	#Note: would normally be in contacts.py however i'm too constrainted to resolve circular imports atm.
	def getContactList(self):
		retList = []
		for a in self.contacts:
			try:
				ret, status = contactparser.get_contact_raw(a.id)
				if status != 200:
					continue
				a.id = ret['id']
				a.surname = ret['surname']
				a.name = ret['name']
				a.number = ret['number']
				a.email = ret['email']
			except:
				break
			retList.append(a.serialize())		
		return retList
		
	def updateContactList(self):
		for a in self.contacts:
			try:
				ret, status = contactparser.get_contact_raw(a.id)
				if status != 200:
					continue
				a.id = ret['id']
				a.surname = ret['surname']
				a.name = ret['name']
				a.number = ret['number']
				a.email = ret['email']
			except:
				break
		
	@staticmethod	
	def create(id, website, ipaddress, contacts):
		ret = WhoisInfo()
		ret.id = id
		ret.website = website
		ret.ipaddress = ipaddress
		ret.contacts = contacts
		return ret
		
	@staticmethod
	def deserialize(dict):
		contacts_json = dict['contacts']
		contacts = []
		for contact in contacts_json:
			contacts.append(Contact.deserialize(contact))	
		return WhoisInfo.create(dict['id'], dict['website'], dict['ipaddress'], contacts)