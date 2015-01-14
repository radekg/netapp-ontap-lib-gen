from netapp.netapp_object import NetAppObject

class ActiveDirectoryAccountConfig(NetAppObject):
    """
    Active Directory configuration information for the Vserver.
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
    
    _domain_workgroup = None
    @property
    def domain_workgroup(self):
        """
        NetBios domain/workgroup name.
        Attributes: non-creatable, non-modifiable
        """
        return self._domain_workgroup
    @domain_workgroup.setter
    def domain_workgroup(self, val):
        if val != None:
            self.validate('domain_workgroup', val)
        self._domain_workgroup = val
    
    _domain = None
    @property
    def domain(self):
        """
        Fully qualified domain name.
        Attributes: required-for-create, modifiable
        """
        return self._domain
    @domain.setter
    def domain(self, val):
        if val != None:
            self.validate('domain', val)
        self._domain = val
    
    _account_name = None
    @property
    def account_name(self):
        """
        Active Directory account NetBIOS name.
        Attributes: required-for-create, non-modifiable
        """
        return self._account_name
    @account_name.setter
    def account_name(self, val):
        if val != None:
            self.validate('account_name', val)
        self._account_name = val
    
    _organizational_unit = None
    @property
    def organizational_unit(self):
        """
        Organizational unit under which the Active Directory
        account resides.
        Attributes: optional-for-create, non-modifiable
        """
        return self._organizational_unit
    @organizational_unit.setter
    def organizational_unit(self, val):
        if val != None:
            self.validate('organizational_unit', val)
        self._organizational_unit = val
    
    @staticmethod
    def get_api_name():
          return "active-directory-account-config"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vserver',
            'domain-workgroup',
            'domain',
            'account-name',
            'organizational-unit',
        ]
    
    def describe_properties(self):
        return {
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'domain_workgroup': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'account_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'organizational_unit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
