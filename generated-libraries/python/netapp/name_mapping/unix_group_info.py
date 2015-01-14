from netapp.name_mapping.unix_user_name import UnixUserName
from netapp.netapp_object import NetAppObject

class UnixGroupInfo(NetAppObject):
    """
    UNIX group information
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
        Specifies the Vserver for the group.
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
        Specifies UNIX group name.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._group_name
    @group_name.setter
    def group_name(self, val):
        if val != None:
            self.validate('group_name', val)
        self._group_name = val
    
    _group_id = None
    @property
    def group_id(self):
        """
        Specifies an identification number for the UNIX group.
        Attributes: required-for-create, modifiable
        """
        return self._group_id
    @group_id.setter
    def group_id(self, val):
        if val != None:
            self.validate('group_id', val)
        self._group_id = val
    
    _users = None
    @property
    def users(self):
        """
        Specifies the list of UNIX users that belong to the UNIX
        group.
        """
        return self._users
    @users.setter
    def users(self, val):
        if val != None:
            self.validate('users', val)
        self._users = val
    
    @staticmethod
    def get_api_name():
          return "unix-group-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'group-name',
            'group-id',
            'users',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'group_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'users': { 'class': UnixUserName, 'is_list': True, 'required': 'optional' },
        }
