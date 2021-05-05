import contactparser
class Contact:
	def __init__(self, id, surname, name, number, email):
		self.id = id
		self.surname = surname
		self.name = name
		self.number = number
		self.email = email		
		
	def serialize(self):
		return {
			'id': self.id, 
			'surname': self.surname,
			'name': self.name,
			'number': self.number,
			'email': self.email,
		}

	def serialize_update(self):
		ret, status = contactparser.get_contact_raw(self.id)
		self.id = ret['id']
		self.surname = ret['surname']
		self.name = ret['name']
		self.number = ret['number']
		self.email = ret['email']
		return {
			'id': self.id, 
			'surname': self.surname,
			'name': self.name,
			'number': self.number,
			'email': self.email,
		}
		
	@staticmethod
	def deserialize(dict):
		return Contact(dict['id'], dict['surname'], dict['name'], dict['number'], dict['email'])