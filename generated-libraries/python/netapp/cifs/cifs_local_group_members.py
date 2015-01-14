from netapp.netapp_object import NetAppObject

class CifsLocalGroupMembers(NetAppObject):
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
        Attributes: key, non-creatable, non-modifiable
        """
        return self._group_name
    @group_name.setter
    def group_name(self, val):
        if val != None:
            self.validate('group_name', val)
        self._group_name = val
    
    _member = None
    @property
    def member(self):
        """
        The member of a local group
        Attributes: non-creatable, non-modifiable
        """
        return self._member
    @member.setter
    def member(self, val):
        if val != None:
            self.validate('member', val)
        self._member = val
    
    @staticmethod
    def get_api_name():
          return "cifs-local-group-members"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'group-name',
            'member',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'member': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
