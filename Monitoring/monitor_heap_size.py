waitTime=180000
THRESHOLD_PERCENT=90 #10%

uname = "weblogic"
pwd = "-LVJ%A8Y8nGZ.Jz]"
url = "t3://localhost:7001"
def monitorJVMHeapSize():
    connect(uname, pwd, url)
    #while 1:
    serverNames = getRunningServerNames()
    domainRuntime()
    for name in serverNames:
        print 'Now checking '+name.getName()
        try:
            cd("/ServerRuntimes/"+name.getName()+"/JVMRuntime/"+name.getName())
            print 'INFO: --- Monitoring Heap Usage ---'
            heapSizeCurrent = cmo.getHeapSizeCurrent()/1024/1024
            print 'INFO: HeapSizeCurrent=', heapSizeCurrent, 'MB'
            heapFreeCurrent = cmo.getHeapFreeCurrent()/1024/1024
            print 'INFO: HeapFreeCurrent=', heapFreeCurrent, 'MB'
            heapUsedCurrent = heapSizeCurrent - heapFreeCurrent
            print 'INFO: HeapUsedCurrent=', heapUsedCurrent, 'MB'
            heapSizeMax = cmo.getHeapSizeMax()/1024/1024
            print 'INFO: HeapSizeMax=', heapSizeMax, 'MB'
            heapFreePercent = cmo.getHeapFreePercent()
            print 'INFO: HeapFreePercent=', heapFreePercent, '%'
            if 100-heapFreePercent > THRESHOLD_PERCENT:
                # do whatever is neccessary, send alerts, send email etc
                print 'WARNING: The current HEAPSIZE ', heapUsedCurrent, 'MB is Greater than the Threshold ',THRESHOLD_PERCENT,'%'
            else:
                print "All okay"
            
            print 'INFO: --- Monitoring Thread Pool ---'
            cd("/ServerRuntimes/"+name.getName()+"/ThreadPoolRuntime/ThreadPoolRuntime")
            print 'ExecuteThreadTotalCount: ' + str(cmo.getExecuteThreadTotalCount())
            print 'Active/StuckThreadCount: ' + str(cmo.getExecuteThreadTotalCount() - cmo.getStandbyThreadCount())
            print 'ExecuteThreadIdleCount: ' + str(cmo.getExecuteThreadIdleCount())
            print 'StandbyThreadCount: ' + str(cmo.getStandbyThreadCount())
            print 'PendingUserRequestCount: ' + str(cmo.getPendingUserRequestCount())

            print 'INFO: --- Monitoring Sessions ---'
            #cd("/ServerRuntimes/"+name.getName()+"/ThreadPoolRuntime/ThreadPoolRuntime")
            #cd("/ServerRuntimes/AdminServer/ThreadPoolRuntime/ThreadPoolRuntime")

        except WLSTException,e:
            # this typically means the server is not active, just ignore
            # pass
            print "Ignoring exception " + e.getMessage()
            # java.lang.Thread.sleep(waitTime)

def getRunningServerNames():
        # only returns the currently running servers in the domain
        return domainRuntimeService.getServerRuntimes()

if __name__== "main":
    monitorJVMHeapSize()