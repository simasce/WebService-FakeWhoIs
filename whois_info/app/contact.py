from spyne.model.complex import ComplexModel
from spyne import Integer, Unicode

class Contact(ComplexModel):
	_type_info = [
		('id', Integer),
		('surname', Unicode),
		('name', Unicode),
		('number', Unicode),
		('email', Unicode),
	]
		
	def serialize(self):
		return {
			'id': self.id, 
			'surname': self.surname,
			'name': self.name,
			'number': self.number,
			'email': self.email,
		}
		
	@staticmethod
	def create(id, surname, name, number, email):
		ret = Contact()
		ret.id = id
		ret.surname = surname
		ret.name = name
		ret.number = number
		ret.email = email		
		return ret
		
	@staticmethod
	def deserialize(dict):
		return Contact.create(dict['id'], dict['surname'], dict['name'], dict['number'], dict['email'])