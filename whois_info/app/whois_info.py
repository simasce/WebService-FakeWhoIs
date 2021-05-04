from contact import Contact

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
			'contacts': [cn.serialize() for cn in self.contacts]
		}
		
	@staticmethod
	def deserialize(dict):
		contacts_json = dict['contacts']
		contacts = []
		for contact in contacts_json:
			contacts.append(Contact.deserialize(contact))
		return WhoisInfo(dict['id'], dict['website'], dict['ipaddress'], contacts)