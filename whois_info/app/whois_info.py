from contact import Contact
import contactparser

class WhoisInfo:
	def __init__(self, id, website, ipaddress, contacts):
		self.id = id
		self.website = website
		self.ipaddress = ipaddress
		self.contacts = contacts
		
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
		
		
	@staticmethod
	def deserialize(dict):
		contacts_json = dict['contacts']
		contacts = []
		for contact in contacts_json:
			contacts.append(Contact.deserialize(contact))
		return WhoisInfo(dict['id'], dict['website'], dict['ipaddress'], contacts)