from netapp.netapp_object import NetAppObject

class VolumeInfinitevolAttributes(NetAppObject):
    """
    Information about the state of an Infinite Volume.
    """
    
    _storage_service = None
    @property
    def storage_service(self):
        """
        The name of the initial storage service for the Infinite
        Volume. This can only be provided if
        is-managed-by-service is true.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._storage_service
    @storage_service.setter
    def storage_service(self, val):
        if val != None:
            self.validate('storage_service', val)
        self._storage_service = val
    
    _namespace_mirror_aggr_list = None
    @property
    def namespace_mirror_aggr_list(self):
        """
        Specifies an array of names of aggregates to be used for
        Infinite Volume Namespace Mirror constituents. If this
        input is not specified all the aggregates assigned to the
        Vserver are used. If the argument 'enable-snapdiff' is
        being set to 'true', and the Infinite Volume is managed
        by storage services, a value must be provided.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._namespace_mirror_aggr_list
    @namespace_mirror_aggr_list.setter
    def namespace_mirror_aggr_list(self, val):
        if val != None:
            self.validate('namespace_mirror_aggr_list', val)
        self._namespace_mirror_aggr_list = val
    
    _max_data_constituent_size = None
    @property
    def max_data_constituent_size(self):
        """
        The maximum size of each data constituent in bytes.  The
        default value is determined by checking the maximum
        FlexVol size setting on all nodes used by the Infinite
        Volume. The smallest value found is chosen as the default
        for the max-data-constituent-size for the Infinite
        Volume.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._max_data_constituent_size
    @max_data_constituent_size.setter
    def max_data_constituent_size(self, val):
        if val != None:
            self.validate('max_data_constituent_size', val)
        self._max_data_constituent_size = val
    
    _is_managed_by_service = None
    @property
    def is_managed_by_service(self):
        """
        Specifies if the volume is managed by GUI services. The
        deafult value is false.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._is_managed_by_service
    @is_managed_by_service.setter
    def is_managed_by_service(self, val):
        if val != None:
            self.validate('is_managed_by_service', val)
        self._is_managed_by_service = val
    
    _max_namespace_constituent_size = None
    @property
    def max_namespace_constituent_size(self):
        """
        The maximum size of the namespace constituent.  The
        default value is 10TB.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._max_namespace_constituent_size
    @max_namespace_constituent_size.setter
    def max_namespace_constituent_size(self, val):
        if val != None:
            self.validate('max_namespace_constituent_size', val)
        self._max_namespace_constituent_size = val
    
    _constituent_role = None
    @property
    def constituent_role(self):
        """
        This field specifies the role of a constituent within an
        Infinite Volume. This field is only supported for
        Infinite Volume constituents.
        <p>
        Possible values:
        <ul>
        <li> 'namespace' ... namespace constituent,
        <li> 'data' ... data constituent,
        <li> 'ns_mirror' ... namespace mirror constituent
        </ul>
        <p>
        Attributes: optional-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "namespace" ,
        <li> "data"      ,
        <li> "ols"       ,
        <li> "ns_mirror"
        </ul>
        """
        return self._constituent_role
    @constituent_role.setter
    def constituent_role(self, val):
        if val != None:
            self.validate('constituent_role', val)
        self._constituent_role = val
    
    _enable_snapdiff = None
    @property
    def enable_snapdiff(self):
        """
        Whether to enable Snapdiff. If enabled, the namespace
        mirrors will be created for Snapdiff use. The default
        value is false.
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._enable_snapdiff
    @enable_snapdiff.setter
    def enable_snapdiff(self, val):
        if val != None:
            self.validate('enable_snapdiff', val)
        self._enable_snapdiff = val
    
    @staticmethod
    def get_api_name():
          return "volume-infinitevol-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'storage-service',
            'namespace-mirror-aggr-list',
            'max-data-constituent-size',
            'is-managed-by-service',
            'max-namespace-constituent-size',
            'constituent-role',
            'enable-snapdiff',
        ]
    
    def describe_properties(self):
        return {
            'storage_service': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'namespace_mirror_aggr_list': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'max_data_constituent_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_managed_by_service': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'max_namespace_constituent_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'constituent_role': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enable_snapdiff': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
