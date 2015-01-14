from netapp.netapp_object import NetAppObject

class FileDirectorySecurityPolicy(NetAppObject):
    """
    File/folder security policy management
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
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Specifies the name of the policy. To preserve the
        security configuration of a file(or, folder) or set of
        files(or, folders) security policy has been defined.
        Policy is a container for tasks and a task associates a
        file/folder path name and the security descriptor that
        needs to be set on the file/folder. Every task in a
        policy is uniquely identified by the file/folder path.
        Policy can't have duplicate task entries and there is
        only one task per path.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    @staticmethod
    def get_api_name():
          return "file-directory-security-policy"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'policy-name',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
