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
	
	@staticmethod
	def deserialize(dict):
		return Contact(dict['id'], dict['surname'], dict['name'], dict['number'], dict['email'])