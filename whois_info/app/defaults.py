from contact import Contact
from whois_info import WhoisInfo
import contactparser

#Disclaimer: Data presented below is randomly generated, any resemblance to a certain person or website is purely coincidental.
 
defaultContacts = [
	Contact.create(100, "Bates" , "Jackson", "+37063244674", "jackson.b@gmail.com"),
	Contact.create(101, "Tyrone" , "Parker", "+37065472003", "parker.tyrone@outlook.com"),
	Contact.create(102, "Rodney" , "Wilson", "+37063148655", "rwilson@protonmail.com"),
	Contact.create(103, "Luke"   , "Briggs", "+37060248419", "briggsl44@gmail.com"),
	Contact.create(104, "Evelyn", "Despres", "+37067247967", "despresee@mail.com"),
	Contact.create(105, "Francis", "Howard", "+37015448632", "howard.j.francis@gmail.com")
]

defaultWhois = [
	WhoisInfo.create(1, "https://www.stylesellers.net", "52.14.128.122", [defaultContacts[2], defaultContacts[4]]),
	WhoisInfo.create(2, "https://www.newsoutlet.com", "144.1.32.88", [defaultContacts[0]]),
	WhoisInfo.create(3, "https://www.networkspecialists.net", "127.0.0.1", [defaultContacts[1], defaultContacts[2], defaultContacts[5]]),
	WhoisInfo.create(4, "https://www.movierentals.co.uk", "11.121.13.145", [defaultContacts[0], defaultContacts[3]]),
	WhoisInfo.create(5, "https://www.localservers.io", "192.168.1.1", [defaultContacts[0], defaultContacts[1], defaultContacts[3]])
]

def load():
	for contact in defaultContacts:
		contactparser.add_contact(contact)
	return defaultWhois