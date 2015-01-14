from netapp.netapp_object import NetAppObject

class CifsLocalUserMembership(NetAppObject):
    """
    List of local users' membership information, organized by
    Vserver
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
    
    _user_name = None
    @property
    def user_name(self):
        """
        The name of the local user
        Attributes: key, non-creatable, non-modifiable
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    _membership = None
    @property
    def membership(self):
        """
        The membership of the local user
        Attributes: non-creatable, non-modifiable
        """
        return self._membership
    @membership.setter
    def membership(self, val):
        if val != None:
            self.validate('membership', val)
        self._membership = val
    
    @staticmethod
    def get_api_name():
          return "cifs-local-user-membership"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'user-name',
            'membership',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'membership': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
