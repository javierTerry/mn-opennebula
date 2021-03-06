import pyone
import ssl
import sys
from datetime import datetime,timedelta
import json
import logging


strFileLog = "logs/{}-{}".format(datetime.now().strftime("%Y%m%d"), __file__.replace(".py",".log") )

#with open('src/config/config.json') as json_data_file:
#    cfg = json.load(json_data_file)


# add filemode="w" to overwrite
logging.basicConfig(filename=strFileLog, level=logging.DEBUG)

STATE_DICT = {"-2":	"Any state / including DONE",
"-1":	"Any state, except DONE",
0:	"INIT"
,1:	"PENDING"
,2:	"HOLD"
,3:	"ACTIVE"
,4:	"STOPPED"
,5:	"SUSPENDED"
,6:	"DONE"
,8:	"POWEROFF"
,9:	"UNDEPLOYED"
,10: "CLONING"
,11: "CLONING_FAILURE"}



class Instancia():
	"""docstring for ClassName"""
	def __init__(self):
		value = ""
		

	def Conectar (self, ip, user, passwd):
		self.HPVS = "http://{}:2633/RPC2".format(ip)
		credencial = "{}:{}".format(user,passwd)

		self.one = pyone.OneServer(self.HPVS
			, session=credencial
			, context=ssl._create_unverified_context() )

	def info(self,debuging=False, colEspecifico=0):
		#vm_template = self.one.templatepool.info(-1, -1, -1).VMTEMPLATE[0]
		#print dir(vm_template)
		#sys.exit()

		self.objVM = self.one.vmpool.info(-1,-1,-1,-1)
		#print self.one.vmpool.info(-1,-1,-1,-1)
		#print "fin info fucntion"

	def list_csv(self,DC):
		try:		
#			print dir(self.objVM)
#			sys.exit()

			for cont, objVM in enumerate(self.objVM.VM):
				
				#print objVM.__dict__
				#sys.exit()
				setting = objVM.get_TEMPLATE()
				if setting.get('NIC') is None :
					IP = None
					MAC = None
				else :
					#print "mas de una ip "
					#print len( setting.get('NIC') )
					#print type(setting.get('NIC') )

					if (len( setting.get('NIC') ) > 1) and (isinstance( setting.get('NIC'), list) ):
						listIP = []
						listMAC = []
						for listNIC in setting.get('NIC'):
							#print addIP.get('IP')
							listIP.append( listNIC.get('IP') )
							IP = "|".join(listIP)

							listMAC.append( listNIC.get('MAC') )
							MAC = "|".join(listMAC)
					else:
						#print "Solo una una"
						IP = setting.get('NIC').get('IP')
						MAC = setting.get('NIC').get('MAC')
				

				print "{},{},{},{},{},{},{},{},{},{}".format(DC, self.HPVS, objVM.ID, objVM.NAME,IP,MAC
					, STATE_DICT[objVM.STATE], setting.get('MEMORY'), setting.get('CPU') , setting.get('VCPU') 
					)

		except Exception as e:
			raise e
			
if __name__=='__main__':  #Cuerpo Principal
	try:
		timeStart = datetime.now()
	
		#strFileLog = "logs/{}-{}".format(datetime.now().strftime("%Y%m%d"),__file__.replace(".py",".log") )
		with open('src/config/config.json') as json_data_file:
			cfg = json.load(json_data_file)

		#print cfg
		print "UBICACION, HIPERVISOR, ID, NAME,IP, MAC, STATE, RAM, CPU,VCPU"
		#print cfg['HIPERVISOR']
		logging.info("Analizando hipervisor ")
		for key, value in cfg['HIPERVISOR'].items() :
			#	print key
			#print value
			#print "---------------------------------------------" + key
			one = Instancia()
			#print value['IP']+ value['CRED']['USER']+value['CRED']['PWD']
			logging.info(value['IP'])
			one.Conectar(value['IP'], value['CRED']['USER'], value['CRED']['PWD'])
			one.info()
			one.list_csv(value['DC'])	
		

	        
		timeEnd = datetime.now() 
		descripcionTiempo = " Tiempo de inicio {}, tiempo de termino {}".format(timeStart, timeEnd )
		timeDelta = timeEnd - timeStart
		logging.info(descripcionTiempo)

		descripcionTdelta = "EL proceso tardo {} dias {} horas {} minutos {} segundos ".format(
		    timeDelta.days, timeDelta.seconds / 3600, timeDelta.seconds / 60, timeDelta.seconds % 60 )
		logging.info(descripcionTdelta)


	    #subject = "Inventario - {} - {}".format(vm.args.vsphere,"Temporal")
	    #msj =  "Numero Total de VMs {} \n {}".format(vm.countVMs,descripcionTdelta)
	    #print cfg['NOTIFICATION']['RECEIVERS']
	    #print ""
	    #smpt = Smtp()
	    #smpt.send(subject, cfg['NOTIFICATION']['RECEIVERS'], msj)

	    #logging.removeHandler(fh)
	   
	except pyone.OneAuthenticationException as e:
		
		logging.debug(e)
	except Exception as e:
			logging.info( e)




	