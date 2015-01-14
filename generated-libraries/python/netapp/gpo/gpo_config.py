from netapp.netapp_object import NetAppObject

class GpoConfig(NetAppObject):
    """
    Group Policy configuration for Vservers.
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
        The name of the Vserver associated with this
        group-policy.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _is_gpo_enabled = None
    @property
    def is_gpo_enabled(self):
        """
        Group Policy Zapi Status.
        Attributes: non-creatable, modifiable
        """
        return self._is_gpo_enabled
    @is_gpo_enabled.setter
    def is_gpo_enabled(self, val):
        if val != None:
            self.validate('is_gpo_enabled', val)
        self._is_gpo_enabled = val
    
    @staticmethod
    def get_api_name():
          return "gpo-config"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'is-gpo-enabled',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_gpo_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
