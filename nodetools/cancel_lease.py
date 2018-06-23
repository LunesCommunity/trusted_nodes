#!/bin/python
from PyWaves import address as pw

myAddress = pw.Address(privateKey = 'EUx6ir5XQfN8wCpMbbk8iE3FNCcBhLne6oQGmgQStm38')
minerAddress = pw.Address('37mCm11kpfQWiYaJuPJJG65PhgyhCQtqLxL')


lieaseId = myAddress.lease(minerAddress, 4000000000000)
#myAddress.leaseCancel('GbSEKeXUTa85xHQRm9ZzHuHq493pCwtY9zrbHWf4b27D')
