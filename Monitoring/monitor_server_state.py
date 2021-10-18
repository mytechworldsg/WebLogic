uname = "weblogic"
pwd = ""
url = "t3://localhost:7001"
#url = "t3s://localhost:7961"

connect(uname, pwd, url)
servers=cmo.getServers()
print "-------------------------------------------------------"
print "\t"+cmo.getName()+" domain status"
print "-------------------------------------------------------"
for server in servers:
        state(server.getName(),server.getType())
print "-------------------------------------------------------"