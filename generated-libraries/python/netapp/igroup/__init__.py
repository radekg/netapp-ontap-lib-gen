from netapp.connection import NaConnection
from initiator_group_info import InitiatorGroupInfo # 14 properties
from initiator_info import InitiatorInfo # 1 properties
from initiator_group_os_type import InitiatorGroupOsType # 0 properties
from igroup_get_iter_key_td import IgroupGetIterKeyTd # 2 properties
from igroup_attribute_enum import IgroupAttributeEnum # 0 properties
from initiator_group_list_info import InitiatorGroupListInfo # 1 properties

class IgroupConnection(NaConnection):
    
    def igroup_bind_portset(self, portset_name, initiator_group_name):
        """
        Bind an existing igroup to a given portset.
        
        :param portset_name: Name of portset.
        
        :param initiator_group_name: Name of initiator group to bind the portset to.
        """
        return self.request( "igroup-bind-portset", {
            'portset_name': [ portset_name, 'portset-name', [ basestring, 'None' ], False ],
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def igroup_lookup_lun(self, initiator_group_name, lun_id):
        """
        Find the path to the lun mapped at a given lun-id
        for a given initiator group.
        
        :param initiator_group_name: Name of initiator group to search.
        
        :param lun_id: Lun-id (Logical Unit Number) to search for.
        """
        return self.request( "igroup-lookup-lun", {
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
            'lun_id': [ lun_id, 'lun-id', [ int, 'None' ], False ],
        }, {
            'path': [ basestring, False ],
        } )
    
    def igroup_destroy(self, initiator_group_name, force=None):
        """
        Destroys an existing initiator group. By default a group
        cannot be destroyed if there are existing lun maps
        defined for that group. This behaviour can be overridden
        with the use of force option set to "true" which will
        destroy the initiator group and any associated lun maps.
        
        :param initiator_group_name: Name of initiator group.
        
        :param force: Forcibly destroy the initiator group, even if there are
                existing lun maps.   Best practice is to attempt to unmap
                all the luns associated with a group before destroying it.
        """
        return self.request( "igroup-destroy", {
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def igroup_add(self, initiator, initiator_group_name, force=None):
        """
        Adds initiator to an existing initiator group.
        
        :param initiator: WWPN or Alias of Initiator to add.
        
        :param initiator_group_name: Name of initiator group.
        
        :param force: Forcibly add the initiator, disabling mapping and type
                conflict checks with the high-availability partner.
                If not specified all conflict checks are performed.
                In Data ONTAP Cluster-Mode, this field is accepted for backwards
                compatibility and is ignored.
        """
        return self.request( "igroup-add", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def igroup_rename(self, initiator_group_name, initiator_group_new_name):
        """
        Rename an existing initiator group. The rename operation
        is non-disruptive.
        
        :param initiator_group_name: Name of initiator group to be renamed.
        
        :param initiator_group_new_name: New name to be given to initiator group.
        """
        return self.request( "igroup-rename", {
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
            'initiator_group_new_name': [ initiator_group_new_name, 'initiator-group-new-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def igroup_list_info(self, initiator_group_name=None):
        """
        Get information for initiator group(s).
        
        :param initiator_group_name: Name of initiator group.  If specified, only information
                for that group is returned.  If not specified, information
                for all inititor groups are returned.
        """
        return self.request( "igroup-list-info", {
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
        }, {
            'initiator-groups': [ InitiatorGroupInfo, True ],
        } )
    
    def igroup_set_attribute(self, attribute, initiator_group_name, value, force=None):
        """
        Sets an attribute for an initiator group.
        
        :param attribute: Name of the attribute to change.
                Possible values: "alua", "os-type", "throttle_borrow",
                "throttle_reserve", "report_scsi_name".
                "alua" is available in Data ONTAP 7.2 or later.
                "report_scsi_name" is available in Data ONTAP
                8.1.0 or later.
                "throttle_reserve","throttle_borrow" and
                "report_scsi_name" are not available
                in Data ONTAP Cluster-Mode.
        
        :param initiator_group_name: Name of initiator group.
        
        :param value: Value for the attribute.
                The valid values for "os-type" are the supported os-types
                listed in the igroup-create API.
                In Data ONTAP 7-Mode, setting the "os-type"
                attribute will perform checks with the high-availability
                partner if this filer is running in the 'single_image'
                fcp cfmode and this igroup is an FCP igroup.  The optional
                force argument can be used to override these checks if
                the high-availability partner can not be reached.
                It is also strongly recommended the "default" os-type not
                be used. Using "default" may cause problems with LUN access.
                API to always require the proper OS type information
                The valid values for "throttle_reserve" are 0-99
                The valid values for "throttle_borrow" are true or false
                The valid values for "alua" are true or false
                The valid values for "report_scsi_name" are true or false
        
        :param force: If the requested attribute is "os-type", forcibly set
                the attribute, disabling conflict checks with the
                high-availability partner where and when applicable.
                If not specified all conflict checks are performed.
                This field is ignored in Data ONTAP Cluster-Mode or
                if the requested attribute is not "os-type".
        """
        return self.request( "igroup-set-attribute", {
            'attribute': [ attribute, 'attribute', [ basestring, 'None' ], False ],
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'value': [ value, 'value', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def igroup_disable_aix_support(self):
        """
        auto generated : Disables SAN AIX support on the cluster
        """
        return self.request( "igroup-disable-aix-support", {
        }, {
        } )
    
    def igroup_unbind_portset(self, initiator_group_name):
        """
        Unbind an existing igroup from a portset.
        
        :param initiator_group_name: Name of initiator group to unbind from the portset.
        """
        return self.request( "igroup-unbind-portset", {
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def igroup_remove(self, initiator, initiator_group_name, force=None):
        """
        Removes node(s) from an initiator group. The operation is
        prohibited if there are existing lun maps defined for
        that group. The force option set to "true" can be used
        to forcibly remove the node regardless of mappings.
        
        :param initiator: WWPN or WWPN Alias of Initiator to remove.
        
        :param initiator_group_name: Name of initiator group.
        
        :param force: Forcibly remove the initiator even if there are existing
                LUNs mapped to this initiator group.  Best practice is
                to attempt to unmap all the luns associated with a group
                before removing the initiator.
        """
        return self.request( "igroup-remove", {
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
            'force': [ force, 'force', [ bool, 'None' ], False ],
        }, {
        } )
    
    def igroup_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of igroup objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                igroup object.
                All igroup objects matching this query up to 'max-records' will
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
        return self.request( "igroup-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ InitiatorGroupInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ InitiatorGroupInfo, 'None' ], False ],
        }, {
            'attributes-list': [ InitiatorGroupInfo, True ],
        } )
    
    def igroup_create(self, initiator_group_name, initiator_group_type, os_type=None, ostype=None, bind_portset=None):
        """
        Creates a new initiator group.
        In Data ONTAP 7.3 and upto ONTAP 8.0, the ALUA (Asymmetiric Logical
        Unit Access) attribute will be enabled by default if
        initiator-group-type is "fcp" and os-type is "aix", "hpux",
        or "linux. In Data ONTAP 7-mode 8.1 and later, the ALUA attribute
        is enabled by default for all os-type if
        initiator-group-type is "fcp".
        In Data ONTAP Cluster-Mode 8.1 and later, the ALUA attribute
        is enabled by default on all initiator groups.
        
        :param initiator_group_name: Name of initiator group.
        
        :param initiator_group_type: Type of the initiator group. Possible values: "fcp", "iscsi",
                "mixed".
                "mixed" is available in Data ONTAP Cluster-Mode 8.1 or later only.
        
        :param os_type: OS type of the initiators within the group. The default
                value if not specified is "default".
                The os type applies to all initiators within the group and governs
                the finer details of SCSI protocol interaction with these
                initiators.
                It is strongly recommended for the caller of this API
                to specify an OS type that is not "default".  Some host
                OSes require this type field be set correctly in order to
                function properly.
        
        :param ostype: Deprecated: use os-type instead
        
        :param bind_portset: Name of a current portset to bind to the newly created
                igroup.
        """
        return self.request( "igroup-create", {
            'os_type': [ os_type, 'os-type', [ basestring, 'initiator-group-os-type' ], False ],
            'ostype': [ ostype, 'ostype', [ basestring, 'initiator-group-os-type' ], False ],
            'initiator_group_name': [ initiator_group_name, 'initiator-group-name', [ basestring, 'None' ], False ],
            'initiator_group_type': [ initiator_group_type, 'initiator-group-type', [ basestring, 'None' ], False ],
            'bind_portset': [ bind_portset, 'bind-portset', [ basestring, 'None' ], False ],
        }, {
        } )
