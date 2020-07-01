import os
key = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
server = 'kms.srv.crsoo.com'
os.system('slmgr /ipk '+key)
os.system('slmgr /skms '+server)
os.system('slmgr /ato')
