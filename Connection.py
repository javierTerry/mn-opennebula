#http://docs.opennebula.io/5.12/integration/system_interfaces/api.html

import pyone
import ssl
import sys
from datetime import datetime,timedelta
import json
import logging

import os


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

	def info(self,pool):
		
		if pool == "VM" :
			return _info_poolVM(self.one)
		elif pool == "HOST":
			return _info_poolHOST(self.one)
		else:
			raise ValueError("No se tiene el identificador "+pool)



def _info_poolVM(oneServer):
	return oneServer.vmpool.infoextended(-1,-1,-1,-1)

def _info_poolHOST(oneServer):
	return oneServer.hostpool.info()


if __name__=='__main__':  #Cuerpo Principal
	strFileLog = "logs/{}-{}".format(datetime.now().strftime("%Y%m%d"), os.path.basename(__file__).replace(".py",".log") )

	#with open('src/config/config.json') as json_data_file:
	#    cfg = json.load(json_data_file)


	# add filemode="w" to overwrite
	logging.basicConfig(filename=strFileLog, level=logging.DEBUG)



	try:
		timeStart = datetime.now()
		cfg = ""
		with open('src/config/config.json') as json_data_file:
			cfg = json.load(json_data_file)

		#for key, value in cfg['HIPERVISOR'].items()
		#print cfg
		user 	= cfg['HIPERVISOR']['LAX4']['CRED']['USER']
		pwd 	= cfg['HIPERVISOR']['LAX4']['CRED']['PWD']
		ip 		= cfg['HIPERVISOR']['LAX4']['IP']
		conection = Connection()
		conection.conectar(ip,user,pwd)
		pool = conection.info("VM")
		logging.info(pool)	

		logging.info("Conectado")
		conection = None
	except pyone.OneAuthenticationException as e:
		logging.debug("OneAuthenticationException")
		logging.debug(e)
	except Exception as e:
		logging.debug("Exception Main")
		logging.info(e)
	finally :
			logging.info("Finalizo el script")
