from netapp.connection import NaConnection
from traphost_info import TraphostInfo # 2 properties
from ctype import Ctype # 0 properties
from remote_inet_address import RemoteInetAddress # 0 properties
from oid import Oid # 0 properties
from community_info import CommunityInfo # 2 properties
from trap_info import TrapInfo # 17 properties

class SnmpConnection(NaConnection):
    
    def snmp_trap_delete(self, trap_name):
        """
        Delete a user defined trap.
        
        :param trap_name: Name of the trap to be deleted.
        """
        return self.request( "snmp-trap-delete", {
            'trap_name': [ trap_name, 'trap-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snmp_enable(self):
        """
        Enables snmp protocol.
        """
        return self.request( "snmp-enable", {
        }, {
        } )
    
    def snmp_trap_reset(self, trap_name=None):
        """
        Reloads one or all user defined traps from registry.
        
        :param trap_name: Name of the trap to be reset.  If absent, all traps
                are reset.
        """
        return self.request( "snmp-trap-reset", {
            'trap_name': [ trap_name, 'trap-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snmp_traphost_add(self, host):
        """
        Adds a host to the list of trap hosts.
        
        :param host: Specify the host to be added.  Host may be specified
                in Domain Name format such as MyHost.MyNetwork.com,
                or as an IP address such as 10.20.30.40.  If a Domain
                Name is used, the host must resolve to an IP address.
        """
        return self.request( "snmp-traphost-add", {
            'host': [ host, 'host', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snmp_prepare_to_downgrade(self):
        """
        auto generated : Change SNMP configuration to the default
        settings for releases earlier than Data ONTAP 8.2.1
        """
        return self.request( "snmp-prepare-to-downgrade", {
        }, {
        } )
    
    def snmp_community_delete_all(self):
        """
        Deletes all the communities.
        """
        return self.request( "snmp-community-delete-all", {
        }, {
        } )
    
    def snmp_trap_list(self):
        """
        List all user defined traps and their attributes.
        """
        return self.request( "snmp-trap-list", {
        }, {
            'trap-list': [ TrapInfo, True ],
        } )
    
    def snmp_trap_set(self, trap_def):
        """
        Set the named user defined trap and the enumerated attribute(s).
        The trap-name must be specified for this api.
        
        :param trap_def: Characterizes a user defined trap and its attributes.
        """
        return self.request( "snmp-trap-set", {
            'trap_def': [ trap_def, 'trap-def', [ TrapInfo, 'None' ], False ],
        }, {
        } )
    
    def snmp_get(self, object_id):
        """
        Retrieves the value of a snmp object.
        
        :param object_id: Fully qualified object identifier of a snmp object.
                Only numeric OID's (ex: .1.3.6.1.4.1.789.1.1.1.0) are allowed.
        """
        return self.request( "snmp-get", {
            'object_id': [ object_id, 'object-id', [ basestring, 'None' ], False ],
        }, {
            'is-value-hexadecimal': [ bool, False ],
            'value': [ basestring, False ],
        } )
    
    def snmp_status(self):
        """
        Returns configuration information of the SNMP agent daemon.
        """
        return self.request( "snmp-status", {
        }, {
            'communities': [ CommunityInfo, True ],
            'is-trap-enabled': [ bool, False ],
            'traphosts': [ TraphostInfo, True ],
            'location': [ basestring, False ],
            'contact': [ basestring, False ],
        } )
    
    def snmp_disable(self):
        """
        Disables snmp protocol.
        """
        return self.request( "snmp-disable", {
        }, {
        } )
    
    def snmp_trap_disable(self):
        """
        Disables snmp traps.
        """
        return self.request( "snmp-trap-disable", {
        }, {
        } )
    
    def snmp_traphost_delete(self, host):
        """
        Deletes a host from the list of trap hosts.
        
        :param host: Specify the host to be added.  Host may be specified
                in Domain Name format such as MyHost.MyNetwork.com,
                or as an IP address such as 10.20.30.40.  If a Domain
                Name is used, the host must resolve to an IP address.
        """
        return self.request( "snmp-traphost-delete", {
            'host': [ host, 'host', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snmp_get_next(self, object_id):
        """
        This is used to retrieve the next OID in the mib tree
        of data. Instead of returning the data you requested, it
        returns the next OID in the tree and its value.
        Unlike the snmp-get api, this api does return data for a
        OID which is too short or is missing the index part of the OID.
        
        :param object_id: Object Identifier of a snmp object. The OID can be
                a fully qualified OID or a partial OID.
                Only numeric OID's (ex: .1.3.6.1.4.1.789.1.1.1.0) are allowed.
        """
        return self.request( "snmp-get-next", {
            'object_id': [ object_id, 'object-id', [ basestring, 'None' ], False ],
        }, {
            'next-object-id': [ basestring, False ],
            'is-value-hexadecimal': [ bool, False ],
            'value': [ basestring, False ],
        } )
    
    def snmp_trap_enable(self):
        """
        Enables snmp traps.
        """
        return self.request( "snmp-trap-enable", {
        }, {
        } )
    
    def snmp_trap_load(self, filename):
        """
        Loads traps from a specified file.
        
        :param filename: Name, including full PATH, of the file specifying the
                user defined traps.  Example:  /etc/MyTraps.txt would
                open the MyTraps.txt file located on the filer's /etc
                directory.
        """
        return self.request( "snmp-trap-load", {
            'filename': [ filename, 'filename', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snmp_community_add(self, access_control, community):
        """
        Adds a community to the list of communities.
        
        :param access_control: Access control for the community. Possible values
                are "ro" (read-only) and "rw" (read-write). But, only
                "ro" (read-only) communities are supported.
        
        :param community: Community name to be added.
        """
        return self.request( "snmp-community-add", {
            'access_control': [ access_control, 'access-control', [ basestring, 'None' ], False ],
            'community': [ community, 'community', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snmp_community_delete(self, access_control, community):
        """
        Deletes a community from the list of communities.
        
        :param access_control: Access control for the community. Possible values
                are "ro" (read-only) and "rw" (read-write). But, only
                "ro" (read-only) communities are supported.
        
        :param community: Community name to be deleted.
        """
        return self.request( "snmp-community-delete", {
            'access_control': [ access_control, 'access-control', [ basestring, 'None' ], False ],
            'community': [ community, 'community', [ basestring, 'None' ], False ],
        }, {
        } )
