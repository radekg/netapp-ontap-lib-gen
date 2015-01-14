from netapp.connection import NaErrorResponse, NaPagedResponse
from netapp.net import NetConnection
from netapp.net.net_port_info import NetPortInfo

conn = NetConnection("192.168.135.100", "admin", "mehmeh123")

print "LISTING ALL PORTS:"
print "-----------------------------------------------"

query = NetPortInfo(node="radontap-02")

response = conn.net_port_get_iter( desired_attributes="node,port".split(","), query=query )

if isinstance(response, NaPagedResponse):
    
    for npi in response.output:
        print "{}: {}".format( npi.port, npi )

    while response.has_more():
        next = response.next()
        if isinstance(next.result, NaErrorResponse):
            print "There was an error: {} : {}".format( next.result.error_code, next.result.reason )
        else:
            for npi in next.output:
                print "{}: {}".format( npi.port, npi )

elif isinstance(response, NaErrorResponse):
    print "There was an error: {} : {}".format( response.error_code, response.reason )
else:
    for npi in response:
        print "{}: {}".format( npi.port, npi )

print "GET A SINGLE PORT:"
print "-----------------------------------------------"

port_info = conn.net_port_get( node="radontap-02", port="e0c", desired_attributes="node,port".split(",") )
print port_info