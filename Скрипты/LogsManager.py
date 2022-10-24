import logging

logpaths = [

'logs/info_log.txt',
'logs/debug_log.txt',
'logs/warning_log.txt',
'logs/critical_log.txt',
'logs/error_log.txt',

]

loglevels = [ logging.INFO , logging.WARNING , logging.ERROR , logging.CRITICAL , logging.DEBUG ]

logformats = [

'%(asctime)s - %(levelname)s - %(message)s' ,

'%(levelname)s - %(asctime)s - %(message)s'

]

logging.basicConfig(filename =  logpaths[0] , level = loglevels[0], format = logformats[0])    #отключить протоколирование - logging.disable()