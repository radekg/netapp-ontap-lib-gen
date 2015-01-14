from netapp.netapp_object import NetAppObject

class DummyVserverFcpInfo(NetAppObject):
    """
    Dummy FCP target configuration
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
        Vserver Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _dummy_is_available = None
    @property
    def dummy_is_available(self):
        """
        is-available
        Attributes: non-creatable, non-modifiable
        """
        return self._dummy_is_available
    @dummy_is_available.setter
    def dummy_is_available(self, val):
        if val != None:
            self.validate('dummy_is_available', val)
        self._dummy_is_available = val
    
    _dummy_nodename = None
    @property
    def dummy_nodename(self):
        """
        Node Name
        Attributes: optional-for-create, modifiable
        """
        return self._dummy_nodename
    @dummy_nodename.setter
    def dummy_nodename(self, val):
        if val != None:
            self.validate('dummy_nodename', val)
        self._dummy_nodename = val
    
    @staticmethod
    def get_api_name():
          return "dummy-vserver-fcp-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'dummy-is-available',
            'dummy-nodename',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dummy_is_available': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'dummy_nodename': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
