from netapp.netapp_object import NetAppObject

class CifsLocalGroup(NetAppObject):
    """
    List of local groups, organized by Vserver
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
    
    _group_name = None
    @property
    def group_name(self):
        """
        The name of the local group
        Attributes: key, required-for-create, non-modifiable
        """
        return self._group_name
    @group_name.setter
    def group_name(self, val):
        if val != None:
            self.validate('group_name', val)
        self._group_name = val
    
    _description = None
    @property
    def description(self):
        """
        The description of the local group
        Attributes: optional-for-create, modifiable
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    @staticmethod
    def get_api_name():
          return "cifs-local-group"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'group-name',
            'description',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
