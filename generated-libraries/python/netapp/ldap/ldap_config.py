from netapp.netapp_object import NetAppObject

class LdapConfig(NetAppObject):
    """
    Lightweight Directory Access Protocol (LDAP) configuration.
    Specifies the LDAP client configuration that is associated with
    this Vserver and whether the configuration is enabled.
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
    
    _client_config = None
    @property
    def client_config(self):
        """
        The name of an existing Lightweight Directory Access
        Protocol (LDAP) client configuration. The LDAP client
        configuration can be created using the ldap-client-create
        API. The ldap-client-get-iter API can be used to retrieve
        the list of available LDAP client configurations for the
        cluster.
        Attributes: required-for-create, modifiable
        """
        return self._client_config
    @client_config.setter
    def client_config(self, val):
        if val != None:
            self.validate('client_config', val)
        self._client_config = val
    
    _client_enabled = None
    @property
    def client_enabled(self):
        """
        If true, the corresponding Lightweight Directory Access
        Protocol (LDAP) configuration is enabled for this
        Vserver.
        Attributes: required-for-create, modifiable
        """
        return self._client_enabled
    @client_enabled.setter
    def client_enabled(self, val):
        if val != None:
            self.validate('client_enabled', val)
        self._client_enabled = val
    
    @staticmethod
    def get_api_name():
          return "ldap-config"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'client-config',
            'client-enabled',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'client_config': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'client_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
