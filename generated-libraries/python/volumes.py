from netapp.connection import NaErrorResponse, NaPagedResponse
from netapp.volume import VolumeConnection
from netapp.volume.volume_info import VolumeInfo

conn = VolumeConnection("192.168.135.100", "admin", "mehmeh123")

print "LISTING ALL VServers:"
print "-----------------------------------------------"

query = None
response = conn.volume_get_iter( desired_attributes=None, query=query )
if isinstance(response, NaErrorResponse):
    print "There was an error: {} : {}".format( response.error_code, response.reason )
else:
    for vs in response:
        print ""
        print "{}".format( vs )