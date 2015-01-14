from netapp.connection import NaErrorResponse, NaPagedResponse
from netapp.aggr import AggrConnection

conn = AggrConnection("192.168.135.100", "admin", "mehmeh123")

print "LISTING ALL Aggregates:"
print "-----------------------------------------------"

response = conn.aggr_get_iter()
for ag in response:
    print "{}".format( ag )