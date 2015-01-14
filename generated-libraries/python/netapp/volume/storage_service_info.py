from netapp.netapp_object import NetAppObject

class StorageServiceInfo(NetAppObject):
    """
    Storage Services
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _volume = None
    @property
    def volume(self):
        """
        Volume Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _storage_service = None
    @property
    def storage_service(self):
        """
        Storage Service Name
        Attributes: non-creatable, non-modifiable
        """
        return self._storage_service
    @storage_service.setter
    def storage_service(self, val):
        if val != None:
            self.validate('storage_service', val)
        self._storage_service = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _constituent_group_id = None
    @property
    def constituent_group_id(self):
        """
        Constituent Group ID
        Attributes: non-creatable, non-modifiable
        """
        return self._constituent_group_id
    @constituent_group_id.setter
    def constituent_group_id(self, val):
        if val != None:
            self.validate('constituent_group_id', val)
        self._constituent_group_id = val
    
    _storage_service_id = None
    @property
    def storage_service_id(self):
        """
        Storage Service ID
        Attributes: key, non-creatable, non-modifiable
        """
        return self._storage_service_id
    @storage_service_id.setter
    def storage_service_id(self, val):
        if val != None:
            self.validate('storage_service_id', val)
        self._storage_service_id = val
    
    _storage_service_type = None
    @property
    def storage_service_type(self):
        """
        Storage Service Type
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "legacy"    - No Support for Storage Services,
        <li> "normal"    - Support For Storage Services
        </ul>
        """
        return self._storage_service_type
    @storage_service_type.setter
    def storage_service_type(self, val):
        if val != None:
            self.validate('storage_service_type', val)
        self._storage_service_type = val
    
    @staticmethod
    def get_api_name():
          return "storage-service-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume',
            'storage-service',
            'vserver',
            'constituent-group-id',
            'storage-service-id',
            'storage-service-type',
        ]
    
    def describe_properties(self):
        return {
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'storage_service': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'constituent_group_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'storage_service_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'storage_service_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
