from netapp.netapp_object import NetAppObject

class NisDomainConfigInfo(NetAppObject):
    """
    NIS domain configuration information
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
        Specifies the Vserver for the NIS domain configuration.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _is_active = None
    @property
    def is_active(self):
        """
        Specifies whether the NIS domain configuration is active
        or inactive.
        Attributes: required-for-create, modifiable
        """
        return self._is_active
    @is_active.setter
    def is_active(self, val):
        if val != None:
            self.validate('is_active', val)
        self._is_active = val
    
    _nis_domain = None
    @property
    def nis_domain(self):
        """
        Specifies the NIS domain.
        For example: 'example.com'
        Attributes: key, required-for-create, non-modifiable
        """
        return self._nis_domain
    @nis_domain.setter
    def nis_domain(self, val):
        if val != None:
            self.validate('nis_domain', val)
        self._nis_domain = val
    
    _nis_servers = None
    @property
    def nis_servers(self):
        """
        Specifies the IP address of one or more NIS servers in
        the domain.
        Attributes: required-for-create, modifiable
        """
        return self._nis_servers
    @nis_servers.setter
    def nis_servers(self, val):
        if val != None:
            self.validate('nis_servers', val)
        self._nis_servers = val
    
    @staticmethod
    def get_api_name():
          return "nis-domain-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'is-active',
            'nis-domain',
            'nis-servers',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_active': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nis_domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nis_servers': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
