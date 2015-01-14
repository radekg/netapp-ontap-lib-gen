from netapp.netapp_object import NetAppObject

class CifsDomainNameMappingSearch(NetAppObject):
    """
    List of trusted domains, organized by Vserver.
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
        Vserver containing the CIFS server.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _trusted_domains = None
    @property
    def trusted_domains(self):
        """
        The list of trusted domains used for name-mapping.
        Attributes: required-for-create, modifiable
        """
        return self._trusted_domains
    @trusted_domains.setter
    def trusted_domains(self, val):
        if val != None:
            self.validate('trusted_domains', val)
        self._trusted_domains = val
    
    @staticmethod
    def get_api_name():
          return "cifs-domain-name-mapping-search"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'trusted-domains',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'trusted_domains': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
