from netapp.netapp_object import NetAppObject

class IscsiServiceInfo(NetAppObject):
    """
    iSCSI Target Service Configuration.
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
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver hosting the iSCSI service.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        The iSCSI target name of the Vserver.
        Attributes: optional-for-create, modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _alias_name = None
    @property
    def alias_name(self):
        """
        The iSCSI target alias of the Vserver.
        Attributes: optional-for-create, modifiable
        """
        return self._alias_name
    @alias_name.setter
    def alias_name(self, val):
        if val != None:
            self.validate('alias_name', val)
        self._alias_name = val
    
    _is_available = None
    @property
    def is_available(self):
        """
        true if the iSCSI Service is running, false otherwise.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_available
    @is_available.setter
    def is_available(self, val):
        if val != None:
            self.validate('is_available', val)
        self._is_available = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-service-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'node-name',
            'alias-name',
            'is-available',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alias_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_available': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
