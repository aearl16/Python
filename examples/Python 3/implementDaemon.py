##########################################################################
## Daemon.py Implementer												##
## @Author: Aaron Earl													##
##																		##
## I wrote this simple program to show a simple implementation of the   ##
## Daemon.py class I had written. This can in turn be used to override  ##
## the run method and run any program using the Daemonizer and run      ##
## continuously.														##
##########################################################################

import sys, time
from Daemon import Daemon

# This will start the daemon service by way of the constructor and insert
# the program (ie self)
class MyDaemon(Daemon):
	def run(self):
		while True:
			time.sleep(1)

# To run the program you will have to enter:
# python implementDaemon.py start
if __name__ == "__main__":
	daemon = MyDaemon('/tmp/daemon-example.pid')
	if len(sys.argv) == 2:
		if('start' == sys.argv[1]):
			daemon.start()
		elif('stop' == sys.argv[1]):
			daemon.stop()
		elif('restart' == sys.argv[1]):
			daemon.restart()
		else:
			print("Unknown command")
			sys.exit(2)
		sys.exit(0)
	else:
		print("usage: %s start|stop|restart" % sys.argv[0])
		sys.exit(2)