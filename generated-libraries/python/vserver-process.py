from netapp.vserver import VserverConnection
from netapp.volume import VolumeConnection
from netapp.vserver.vserver_info import VserverInfo
from netapp.volume.volume_attributes import VolumeAttributes
from netapp.volume.volume_id_attributes import VolumeIdAttributes

conn = VserverConnection("192.168.135.100", "admin", "mehmeh123")
vserver_name = "vserv_process"

# Create a vserver:
# -------------------------------------------------------------------
print "Attempting creating vserver {}...".format( vserver_name )
result = conn.vserver_create(
    vserver_name,
    [ "file" ],
    "aggr2",
    "unix",
    "vserv_process_root",
    comment="Testing the vserver create via the API",
    language="C.UTF-8",
    name_mapping_switch=[ "file" ] )
print "Vserver {} created".format( vserver_name )

# Verify that the vserver exists:
# -------------------------------------------------------------------

response = conn.vserver_get_iter( query=VserverInfo(vserver_name=vserver_name) )
if len(response) > 0:
    print "Found vserver by name: {}".format( response[0] )
else:
    print "No matching vservers..."

print ""

conn2 = VolumeConnection("192.168.135.111", "admin", "mehmeh123", vserver=vserver_name)
for vol in conn2.volume_get_iter( query=VolumeAttributes(volume_id_attributes=VolumeIdAttributes( owning_vserver_name=vserver_name )) ):
    print "Removing volume {}...".format( vol.volume_id_attributes.name )
    conn2.volume_destroy( vol.volume_id_attributes.name, unmount_and_offline=True )
    print " -> Removed."

print "Removing vserver {}...".format( vserver_name )
result = conn.vserver_destroy("vserv_process")

response = conn.vserver_get_iter( query=VserverInfo(vserver_name=vserver_name) )
if len(response) > 0:
    print "Found vserver by name: {}".format( response[0] )
else:
    print "No matching vservers..."