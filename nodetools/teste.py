#!/bin/python 
from  PyWaves import address as pw

myAddress = pw.Address(privateKey='EUx6ir5XQfN8wCpMbbk8iE3FNCcBhLne6oQGmgQStm38')

print("Your asset balance is %18d" % myAddress.balance())
#print otherAddress = pw.Address('37ZKvWcYAByQpvi2ff5kQaDnmK3jXJqnysH')
#myAddress.sendWaves(otherAddress, 50000000)


