from netapp.netapp_object import NetAppObject

class FpolicyPolicyInfo(NetAppObject):
    """
    FPolicy policy information
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
    
    _engine_name = None
    @property
    def engine_name(self):
        """
        Name of the Engine. Default Engine is 'native'.
        Attributes: required-for-create, modifiable
        """
        return self._engine_name
    @engine_name.setter
    def engine_name(self, val):
        if val != None:
            self.validate('engine_name', val)
        self._engine_name = val
    
    _privileged_user_name = None
    @property
    def privileged_user_name(self):
        """
        User name for privileged access. No default value is set
        for this attribute.
        Attributes: optional-for-create, modifiable
        """
        return self._privileged_user_name
    @privileged_user_name.setter
    def privileged_user_name(self, val):
        if val != None:
            self.validate('privileged_user_name', val)
        self._privileged_user_name = val
    
    _policy_name = None
    @property
    def policy_name(self):
        """
        Name of the policy.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._policy_name
    @policy_name.setter
    def policy_name(self, val):
        if val != None:
            self.validate('policy_name', val)
        self._policy_name = val
    
    _allow_privileged_access = None
    @property
    def allow_privileged_access(self):
        """
        Indicator if privileged access should be given to FPolicy
        servers registered for the policy. Default Value is no.
        Attributes: optional-for-create, modifiable
        """
        return self._allow_privileged_access
    @allow_privileged_access.setter
    def allow_privileged_access(self, val):
        if val != None:
            self.validate('allow_privileged_access', val)
        self._allow_privileged_access = val
    
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
    
    _is_mandatory = None
    @property
    def is_mandatory(self):
        """
        Indicator if the screening with this policy is required,
        i.e. it will fail if no servers are able process the
        notification registered as a part of external engine. If
        set to true, the request will fail if there is no  server
        to evaluate it. If it's false, the request will succeed.
        Default value is true.
        Attributes: optional-for-create, modifiable
        """
        return self._is_mandatory
    @is_mandatory.setter
    def is_mandatory(self, val):
        if val != None:
            self.validate('is_mandatory', val)
        self._is_mandatory = val
    
    _events = None
    @property
    def events(self):
        """
        Events for file access monitoring.
        Attributes: required-for-create, modifiable
        """
        return self._events
    @events.setter
    def events(self, val):
        if val != None:
            self.validate('events', val)
        self._events = val
    
    @staticmethod
    def get_api_name():
          return "fpolicy-policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'engine-name',
            'privileged-user-name',
            'policy-name',
            'allow-privileged-access',
            'vserver',
            'is-mandatory',
            'events',
        ]
    
    def describe_properties(self):
        return {
            'engine_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'privileged_user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'policy_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'allow_privileged_access': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_mandatory': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'events': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
