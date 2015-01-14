from netapp.netapp_object import NetAppObject

class CifsDomainPreferredDc(NetAppObject):
    """
    List of preferred domain controllers associated with an Active
    Directory domain, organized by Vserver.
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
    
    _domain = None
    @property
    def domain(self):
        """
        The fully qualified domain name of the Active Directory
        domain to which the domain controllers in the list
        belong.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._domain
    @domain.setter
    def domain(self, val):
        if val != None:
            self.validate('domain', val)
        self._domain = val
    
    _preferred_dc = None
    @property
    def preferred_dc(self):
        """
        The list of preferred domain controller IP addresses.
        Attributes: required-for-create, non-modifiable
        """
        return self._preferred_dc
    @preferred_dc.setter
    def preferred_dc(self, val):
        if val != None:
            self.validate('preferred_dc', val)
        self._preferred_dc = val
    
    @staticmethod
    def get_api_name():
          return "cifs-domain-preferred-dc"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'domain',
            'preferred-dc',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'preferred_dc': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
