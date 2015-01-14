from netapp.netapp_object import NetAppObject

class VscanStatusInfo(NetAppObject):
    """
    Vscan status information.
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
        Vserver
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _is_vscan_enabled = None
    @property
    def is_vscan_enabled(self):
        """
        Vscan status. When true, Vscan feature is enabled for the
        Vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_vscan_enabled
    @is_vscan_enabled.setter
    def is_vscan_enabled(self, val):
        if val != None:
            self.validate('is_vscan_enabled', val)
        self._is_vscan_enabled = val
    
    @staticmethod
    def get_api_name():
          return "vscan-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'is-vscan-enabled',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_vscan_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
