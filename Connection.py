import pyone
import ssl
import sys
from datetime import datetime,timedelta
import json
import logging

#http://docs.opennebula.io/5.12/integration/system_interfaces/api.html

strFileLog = "logs/{}-{}".format(datetime.now().strftime("%Y%m%d"), __file__.replace(".py",".log") )

#with open('src/config/config.json') as json_data_file:
#    cfg = json.load(json_data_file)


# add filemode="w" to overwrite
logging.basicConfig(filename=strFileLog, level=logging.DEBUG)



class Connection():
	"""docstring for ClassName"""

	def __init__(self):
		value = ""

	def conectar (self, ip, user, pwd):
		self.HPVS = "http://{}:2633/RPC2".format(ip)
		credencial = "{}:{}".format(user,pwd)

		self.one = pyone.OneServer(self.HPVS
			, session=credencial
			, context=ssl._create_unverified_context() )



if __name__=='__main__':  #Cuerpo Principal
	try:
		timeStart = datetime.now()
		cfg = ""
		with open('src/config/config.json') as json_data_file:
			cfg = json.load(json_data_file)

		#for key, value in cfg['HIPERVISOR'].items()
		#print cfg
		user 	= cfg['HIPERVISOR']['LAX4']['CRED']['USER']
		pwd 	= "123" #cfg['HIPERVISOR']['LAX4']['CRED']['PWD']
		ip 		= cfg['HIPERVISOR']['LAX4']['IP']
		conection = Connection()
		conection.conectar(ip,user,pwd)

		print (conection.one)	

		logging.info("Conectado")
		conection = None
	except pyone.OneAuthenticationException as e:
		
		logging.debug(e)
	except Exception as e:
		logging.info( e)
