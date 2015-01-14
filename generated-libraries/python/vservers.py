from netapp.connection import NaErrorResponse, NaPagedResponse
from netapp.vserver import VserverConnection
from netapp.vserver.vserver_info import VserverInfo

conn = VserverConnection("192.168.135.100", "admin", "mehmeh123")

print "LISTING ALL VServers:"
print "-----------------------------------------------"

#query = NetPortInfo(node="radontap-02")
query = None

response = conn.vserver_get_iter( desired_attributes=None, query=query )

if isinstance(response, NaPagedResponse):
    
    for vs in response.output:
        print "{}".format( vs )

    while response.has_more():
        next = response.next()
        if isinstance(next.result, NaErrorResponse):
            print "There was an error: {} : {}".format( next.result.error_code, next.result.reason )
        else:
            for vs in next.output:
                print "{}".format( vs )

elif isinstance(response, NaErrorResponse):
    print "There was an error: {} : {}".format( response.error_code, response.reason )
else:
    for vs in response:
        print "{}".format( vs )

print "GET A SINGLE Vserver:"
print "-----------------------------------------------"

response = conn.vserver_get_iter( query=VserverInfo(vserver_name="mehmeh"), desired_attributes=None )
if len(response) > 0:
    print "Found vserver by name: {}".format( response[0] )
else:
    print "No matching vservers..."