from netapp.netapp_object import NetAppObject

class CifsPrivilege(NetAppObject):
    """
    List of privileges assigned to local or Active Directory users or
    groups, organized by Vserver
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
    
    _privileges = None
    @property
    def privileges(self):
        """
        The privileges associated with a local or Active
        Directory user or group
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "setcbprivilege"           - Act as part of the
        operating system,
        <li> "sebackupprivilege"        - Back up files and
        directories, overriding any ACLs,
        <li> "serestoreprivilege"       - Restore files and
        directories, overriding any ACLs,
        <li> "setakeownershipprivilege" - Take ownership of
        files or other objects,
        <li> "sesecurityprivilege"      - Manage auditing and
        viewing/dumping/clearing the security log
        </ul>
        """
        return self._privileges
    @privileges.setter
    def privileges(self, val):
        if val != None:
            self.validate('privileges', val)
        self._privileges = val
    
    _user_or_group_name = None
    @property
    def user_or_group_name(self):
        """
        The name of the local or Active Directory user or group
        Attributes: non-creatable, non-modifiable
        """
        return self._user_or_group_name
    @user_or_group_name.setter
    def user_or_group_name(self, val):
        if val != None:
            self.validate('user_or_group_name', val)
        self._user_or_group_name = val
    
    @staticmethod
    def get_api_name():
          return "cifs-privilege"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'privileges',
            'user-or-group-name',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'privileges': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'user_or_group_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
