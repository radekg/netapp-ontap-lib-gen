from netapp.netapp_object import NetAppObject

class ExportPolicyInfo(NetAppObject):
    """
    Information about the Export policy configuration.
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
        Vserver name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Export policy name.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _policy_id = None
    @property
    def policy_id(self):
        """
        Export policy id.
        Attributes: non-creatable, non-modifiable
        """
        return self._policy_id
    @policy_id.setter
    def policy_id(self, val):
        if val != None:
            self.validate('policy_id', val)
        self._policy_id = val
    
    @staticmethod
    def get_api_name():
          return "export-policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'policy-name',
            'policy-id',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_id': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
