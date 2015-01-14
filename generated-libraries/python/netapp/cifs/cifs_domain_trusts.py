from netapp.netapp_object import NetAppObject

class CifsDomainTrusts(NetAppObject):
    """
    List of trusted domains discovered.
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
    
    _node = None
    @property
    def node(self):
        """
        The name of the node on which discovery was done.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The name of the Vserver which scopes the discovered
        trusted domains.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _trusted_domain = None
    @property
    def trusted_domain(self):
        """
        A domain that has a trust relationship with the home
        domain.
        Attributes: non-creatable, non-modifiable
        """
        return self._trusted_domain
    @trusted_domain.setter
    def trusted_domain(self, val):
        if val != None:
            self.validate('trusted_domain', val)
        self._trusted_domain = val
    
    _home_domain = None
    @property
    def home_domain(self):
        """
        The fully-qualified domain name of the Active Directory
        domain the CIFS server is joined to.
        Attributes: non-creatable, non-modifiable
        """
        return self._home_domain
    @home_domain.setter
    def home_domain(self, val):
        if val != None:
            self.validate('home_domain', val)
        self._home_domain = val
    
    @staticmethod
    def get_api_name():
          return "cifs-domain-trusts"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'vserver',
            'trusted-domain',
            'home-domain',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'trusted_domain': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'home_domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
