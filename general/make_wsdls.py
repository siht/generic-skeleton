'''this module makes an interface for a soap service
it run in a console:
invoke:
python make_wsdls.py <wsdl_file>
'''
import sys
from SOAPpy import WSDL

PREAMBLE = "from SOAPpy import WSDL\n\n\
class {0}(object):\n\
    def __init__(self):\n\
        self._server = WSDL.Proxy('{1}')\n\n"

TEMPLATE_METHOD = "\
    def {0}(self):\n\
        return self._server.{0}().encode('utf-8')\n\n"

def get_service_name():
	return sys.argv[1]

def get_service_methods(service):
	return service.methods.keys()

def create_service_interface():
	wsdl_uri = get_service_name()
	_server = WSDL.Proxy(wsdl_uri)
	wsdl_methods = get_service_methods(_server)
	file_name = wsdl_uri.split('/')[-1].replace('?', '_') + '.py'
	file_name = file_name.lower()
	class_name = file_name[:-3].split('_')
	class_name = ''.join((word.capitalize() for word in class_name))
	try:
		interface_file = open(file_name, 'w')
		interface_file.write(PREAMBLE.format(class_name ,wsdl_uri))
		# to do:
		# put arguments
		for method in wsdl_methods:
			interface_file.write(TEMPLATE_METHOD.format(str(method)))
	finally:
		interface_file.close()

if __name__ == '__main__':
	create_service_interface()
