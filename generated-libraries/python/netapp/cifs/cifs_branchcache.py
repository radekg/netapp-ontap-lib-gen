from netapp.netapp_object import NetAppObject

class CifsBranchcache(NetAppObject):
    """
    CIFS BranchCache configuration
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
    
    _versions = None
    @property
    def versions(self):
        """
        Versions of the BranchCache protocol that are supported.
        Attributes: optional-for-create, modifiable
        """
        return self._versions
    @versions.setter
    def versions(self, val):
        if val != None:
            self.validate('versions', val)
        self._versions = val
    
    _operating_mode = None
    @property
    def operating_mode(self):
        """
        The mode in which the BranchCache service will operate.
        Attributes: optional-for-create, modifiable
        """
        return self._operating_mode
    @operating_mode.setter
    def operating_mode(self, val):
        if val != None:
            self.validate('operating_mode', val)
        self._operating_mode = val
    
    _hash_store_path = None
    @property
    def hash_store_path(self):
        """
        Path to the directory where hash files are stored.
        Attributes: required-for-create, modifiable
        """
        return self._hash_store_path
    @hash_store_path.setter
    def hash_store_path(self, val):
        if val != None:
            self.validate('hash_store_path', val)
        self._hash_store_path = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver associated with this CIFS
        server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _server_key = None
    @property
    def server_key(self):
        """
        BranchCache server key.
        Attributes: optional-for-create, modifiable
        """
        return self._server_key
    @server_key.setter
    def server_key(self, val):
        if val != None:
            self.validate('server_key', val)
        self._server_key = val
    
    _hash_store_max_size = None
    @property
    def hash_store_max_size(self):
        """
        Maximum size the hash store can grow to.
        Attributes: optional-for-create, modifiable
        """
        return self._hash_store_max_size
    @hash_store_max_size.setter
    def hash_store_max_size(self, val):
        if val != None:
            self.validate('hash_store_max_size', val)
        self._hash_store_max_size = val
    
    @staticmethod
    def get_api_name():
          return "cifs-branchcache"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'versions',
            'operating-mode',
            'hash-store-path',
            'vserver',
            'server-key',
            'hash-store-max-size',
        ]
    
    def describe_properties(self):
        return {
            'versions': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'operating_mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'hash_store_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'server_key': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'hash_store_max_size': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
