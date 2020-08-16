import pyone
import ssl
import sys
from datetime import datetime,timedelta
import json
import logging
import os

from Connection import Connection 
#http://docs.opennebula.io/5.12/integration/system_interfaces/api.html

class Host():
	"""docstring for ClassName"""
	def __init__(self, arg):
		self.conection = Connection()
		self.conection.conectar(value['IP'], value['CRED']['USER'], value['CRED']['PWD'])
		self.poolHost = self.conection.info("HOST")

	def listar(self):
		"""Listar host 
			Resulto se imprime en pantalla, opcion facil para obtener un csv
		"""
		

		print "CLUSTER, ID CLUSTER, ID HOST, NAME, STATE, NO INSTANCIAS,WILDS,ZOMBIES, INSTANCIAS IDS"
		for x in self.poolHost.HOST :
			#print (x.TEMPLATE)
			#print (x.TEMPLATE['WILDS'])
			#for y in x.TEMPLATE:
			#	print y
				#sys.exit()

			if 'TOTAL_ZOMBIES' in x.TEMPLATE :
				None
			else :
				x.TEMPLATE['TOTAL_ZOMBIES'] = 0
			if 'TOTAL_WILDS' in x.TEMPLATE :
				None
			else :
				x.TEMPLATE['TOTAL_WILDS'] = 0

			print "{}, {}, {}, {}, {}, {}, {},{}, {}".format(x.CLUSTER, x.CLUSTER_ID, x.ID, x.NAME, x.STATE, len(x.VMS.ID),x.TEMPLATE['TOTAL_ZOMBIES'],x.TEMPLATE['TOTAL_WILDS'], x.VMS.ID)
			
			#sys.exit()




if __name__=='__main__':  #Cuerpo Principal

	strFileLog = "logs/{}-{}".format(datetime.now().strftime("%Y%m%d"), os.path.basename(__file__).replace(".py",".log") )
	logging.basicConfig(filename=strFileLog, level=logging.DEBUG)

	try:
		timeStart = datetime.now()
	
		#strFileLog = "logs/{}-{}".format(datetime.now().strftime("%Y%m%d"),__file__.replace(".py",".log") )
		with open('src/config/config.json') as json_data_file:
			cfg = json.load(json_data_file)

		#print cfg
		
		#print cfg['HIPERVISOR']
		logging.info("Analizando hipervisor ")

		for key, value in cfg['HIPERVISOR'].items() :
			
			try:
				logging.debug("+++++++++++++  " + value['DC'])
				logging.info(value['IP']+ " "+value['DC'])
				host = Host(value)
				host.listar()
			except pyone.OneAuthenticationException as e:
				logging.debug("Error de autenticacion ")
			
			finally:
				logging.info("Finalizo el boque de " +value['IP']+ " "+value['DC'])
	   
	except Exception as e:
		logging.debug("exception main")
		#print e
		logging.info(e)
	finally:
		timeEnd = datetime.now() 
		descripcionTiempo = " Tiempo de inicio {}, tiempo de termino {}".format(timeStart, timeEnd )
		timeDelta = timeEnd - timeStart
		logging.info(descripcionTiempo)

		descripcionTdelta = "EL proceso tardo {} dias {} horas {} minutos {} segundos ".format(
		    timeDelta.days, timeDelta.seconds / 3600, timeDelta.seconds / 60, timeDelta.seconds % 60 )
		logging.info(descripcionTdelta)
		logging.info("Finalizo el script")



