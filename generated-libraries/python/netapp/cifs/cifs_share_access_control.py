from netapp.netapp_object import NetAppObject

class CifsShareAccessControl(NetAppObject):
    """
    The permissions that users and groups have to a CIFS share.
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
        The name of the Vserver associated with this CIFS
        server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _winsid = None
    @property
    def winsid(self):
        """
        The Windows SID for the user or group for which the
        permission is defined.
        Attributes: non-creatable, non-modifiable
        """
        return self._winsid
    @winsid.setter
    def winsid(self, val):
        if val != None:
            self.validate('winsid', val)
        self._winsid = val
    
    _share = None
    @property
    def share(self):
        """
        The CIFS share for which the permissions are defined.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._share
    @share.setter
    def share(self, val):
        if val != None:
            self.validate('share', val)
        self._share = val
    
    _user_or_group = None
    @property
    def user_or_group(self):
        """
        The user or group name for which the permissions are
        listed.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._user_or_group
    @user_or_group.setter
    def user_or_group(self, val):
        if val != None:
            self.validate('user_or_group', val)
        self._user_or_group = val
    
    _permission = None
    @property
    def permission(self):
        """
        The access rights that the user or group has on the
        defined CIFS share.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "no_access"      - No access,
        <li> "read"           - Read,
        <li> "change"         - Change,
        <li> "full_control"   - Full Control
        </ul>
        """
        return self._permission
    @permission.setter
    def permission(self, val):
        if val != None:
            self.validate('permission', val)
        self._permission = val
    
    @staticmethod
    def get_api_name():
          return "cifs-share-access-control"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'winsid',
            'share',
            'user-or-group',
            'permission',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'winsid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'share': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user_or_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'permission': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
