from spyne import Iterable, Array, Integer, Unicode, srpc, Application, Service, M
from spyne.protocol.http import HttpRpc
from spyne.protocol.soap import Soap11
from spyne.model.fault import Fault
from spyne.interface.wsdl import Wsdl11
from spyne.test.sort_wsdl import sort_wsdl
from entrycontainer import EntryContainer
from whois_info import WhoisInfo
from contact import Contact
from lxml import etree
from io import BytesIO
import time, contactparser, defaults

class WhoisServiceSOAP(Service):
	@srpc(_returns=Array(WhoisInfo))
	def list_whois_info():
		for entry in EntryContainer.entries:
			entry.updateContactList()
			yield entry
			
	@srpc(Integer, _returns=WhoisInfo)
	def get_whois_info(id):
		if id == None:
			raise Fault(faultcode="Client", faultstring="'id' field is empty")
		for entry in EntryContainer.entries:
			if entry.id == id:
				entry.updateContactList()
				return entry
		raise Fault(faultcode="Client", faultstring="Entry not found with given id!")
		
	@srpc(Integer, _returns=Unicode)
	def delete_whois_info(id):
		for entry in EntryContainer.entries:
			if entry.id == id:
				EntryContainer.entries.remove(entry)
				return "Item deleted!"
		raise Fault(faultcode="Client", faultstring="Entry not found with given id!")
				
	@srpc(Integer, WhoisInfo, _returns=WhoisInfo)
	def update_whois_info(id, wInfo):
		for entry in EntryContainer.entries:
			if entry.id == id:
				for contact in wInfo.contacts:
					if contactparser.contact_exists(contact.id):
						res, status = contactparser.edit_contact(contact.id, contact)
						if status != 200:
							raise Fault(faultcode="Server", faultstring="Internal error when updating contacts!")
					else:
						res, status = contactparser.add_contact(contact)
						if status != 201:
							raise Fault(faultcode="Server", faultstring="Internal error when adding contacts!")
				entry.id = wInfo.id
				entry.website = wInfo.website
				entry.ipaddress = wInfo.ipaddress
				entry.contacts = wInfo.contacts
				return wInfo				
		raise Fault(faultcode="Client", faultstring="Could not find entry with given id!")
	
	@srpc(WhoisInfo, _returns=WhoisInfo)
	def add_whois_info(wInfo):
		for entry in EntryContainer.entries:
			if entry.id == wInfo.id:
				raise Fault(faultcode="Client", faultstring="Item with given ID already exists")
		for contact in wInfo.contacts:
			if contactparser.contact_exists(contact.id):
				res, status = contactparser.edit_contact(contact.id, contact)
				if status != 200:
					raise Fault(faultcode="Server", faultstring="Internal error when updating contacts!")
			else:
				res, status = contactparser.add_contact(contact)
				if status != 201:
					raise Fault(faultcode="Server", faultstring="Internal error when adding contacts!")
		EntryContainer.entries.append(wInfo)	
		return wInfo
		
class UserDefinedContext(object):
	def __init__(self, flask_config):
		self.config = flask_config

def output_wsdl(app):
	app.transport = "no_transport_at_all"

	wsdl = Wsdl11(app.interface)

	wsdl.build_interface_document('http://localhost:5000/soap')
	doc = wsdl.get_interface_document()

	tree = etree.parse(BytesIO(doc))
	sort_wsdl(tree)

	file_name = 'wsdl.%s.xml' % "spyneapp"

	with open(file_name, 'wb') as f:
		f.write(etree.tostring(tree, pretty_print=True))
	
def create_app(flask_app):
	application = Application(
		[WhoisServiceSOAP], 'whoisinfo.service',
		in_protocol=Soap11(),
		out_protocol=Soap11(),
	)
	
	def _flask_config_context(ctx):
		ctx.udc = UserDefinedContext(flask_app.config)
	application.event_manager.add_listener('method_call', _flask_config_context)
	
	#output_wsdl(application) # to output wsdl file lul
	#wsdl output is found at 'http://localhost:5000/soap/?wsdl'
	
	return application