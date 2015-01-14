from netapp.connection import NaConnection
from portset_port_name import PortsetPortName # 0 properties
from portset_get_iter_key_td import PortsetGetIterKeyTd # 2 properties
from portset_info import PortsetInfo # 6 properties
from initiator_group_name import InitiatorGroupName # 0 properties

class PortsetConnection(NaConnection):
    
    def portset_list_info(self, portset_name=None):
        """
        Get information for port set(s).
        
        :param portset_name: Name of port set.  If specified, only information
                for that set is returned.  If not specified, information
                for all port sets are returned.
        """
        return self.request( "portset-list-info", {
            'portset_name': [ portset_name, 'portset-name', [ basestring, 'None' ], False ],
        }, {
            'portset-sets': [ PortsetInfo, True ],
        } )
    
    def portset_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of portset objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                portset object.
                All portset objects matching this query up to 'max-records' will
                be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "portset-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ PortsetInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ PortsetInfo, 'None' ], False ],
        }, {
            'attributes-list': [ PortsetInfo, True ],
        } )
    
    def portset_destroy(self, portset_name, force=None):
        """
        Destroys an existing port set. By default a set
        cannot be destroyed if there are existing igroup
        associated with that portset.
        
        :param portset_name: Name of the port set to destroy.
        
        :param force: If 'false' or not specified, the request will fail
                if there are any igroups bound to this portset.
                If 'true', forcibly destroy the portset, even if
                there are existing igroup bindings.
                Best practice is to unbind all the associated igroups
                before destroying the igroup.
        """
        return self.request( "portset-destroy", {
            'portset_name': [ portset_name, 'portset-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def portset_remove(self, portset_name, portset_port_name):
        """
        Removes a port from a port set.
        
        :param portset_name: Name of the port set.
        
        :param portset_port_name: This is the name of the port that is to be removed from the
                portset.
                In Data ONTAP 7-Mode, it can be input in two styles.
                The filername:slotletter format will remove the port from a
                specific filer.
                For example: "buxton:4a"
                The slotletter format will remove the port from both the
                local and partner filers.
                For example: "4a"
                In Data ONTAP Cluster-Mode, the port name is the name of either
                an FCP data lif or an iSCSI target portal group.
        """
        return self.request( "portset-remove", {
            'portset_name': [ portset_name, 'portset-name', [ basestring, 'None' ], False ],
            'portset_port_name': [ portset_port_name, 'portset-port-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def portset_create(self, portset_type, portset_name):
        """
        Create a port set
        
        :param portset_type: Protocols accepted for this portset.
                Possible values: "fcp", "iscsi", "mixed".
                "iscsi" and "mixed" are available in Data ONTAP Cluster-Mode only.
        
        :param portset_name: Name of the port set to create.
        """
        return self.request( "portset-create", {
            'portset_type': [ portset_type, 'portset-type', [ basestring, 'None' ], False ],
            'portset_name': [ portset_name, 'portset-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def portset_add(self, portset_name, portset_port_name):
        """
        Add a port to an existing port set
        
        :param portset_name: Name of port set.
        
        :param portset_port_name: This is the name of the port that is to be added to the
                portset.
                In Data ONTAP 7-Mode, it can be input in two styles.
                The filername:slotletter format will add the port from a
                specific filer.
                For example: "buxton:4a"
                The slotletter format will add the port from both the
                local and partner filers.
                For example: "4a"
                In Data ONTAP Cluster-Mode, the port name is the name of either
                an FCP data lif or an iSCSI target portal group.
        """
        return self.request( "portset-add", {
            'portset_name': [ portset_name, 'portset-name', [ basestring, 'None' ], False ],
            'portset_port_name': [ portset_port_name, 'portset-port-name', [ basestring, 'None' ], False ],
        }, {
        } )
