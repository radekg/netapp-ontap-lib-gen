from netapp.netapp_object import NetAppObject

class VserverPeerTransitionInfo(NetAppObject):
    """
    Information about the transition peer.
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
    
    _local_vserver = None
    @property
    def local_vserver(self):
        """
        Local Vserver name
        Attributes: key, required-for-create, non-modifiable
        """
        return self._local_vserver
    @local_vserver.setter
    def local_vserver(self, val):
        if val != None:
            self.validate('local_vserver', val)
        self._local_vserver = val
    
    _src_filer_name = None
    @property
    def src_filer_name(self):
        """
        Source 7-Mode system
        Attributes: key, required-for-create, non-modifiable
        """
        return self._src_filer_name
    @src_filer_name.setter
    def src_filer_name(self, val):
        if val != None:
            self.validate('src_filer_name', val)
        self._src_filer_name = val
    
    _multi_path_address = None
    @property
    def multi_path_address(self):
        """
        Additional address for source 7-Mode system
        Attributes: optional-for-create, modifiable
        """
        return self._multi_path_address
    @multi_path_address.setter
    def multi_path_address(self, val):
        if val != None:
            self.validate('multi_path_address', val)
        self._multi_path_address = val
    
    @staticmethod
    def get_api_name():
          return "vserver-peer-transition-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'local-vserver',
            'src-filer-name',
            'multi-path-address',
        ]
    
    def describe_properties(self):
        return {
            'local_vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'src_filer_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'multi_path_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
