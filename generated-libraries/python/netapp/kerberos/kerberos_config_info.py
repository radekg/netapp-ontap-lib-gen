from netapp.netapp_object import NetAppObject

class KerberosConfigInfo(NetAppObject):
    """
    Kerberos configuration.
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
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Logical interface.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    _keytab_uri = None
    @property
    def keytab_uri(self):
        """
        Load Keytab from URI.
        Attributes: non-creatable, modifiable
        """
        return self._keytab_uri
    @keytab_uri.setter
    def keytab_uri(self, val):
        if val != None:
            self.validate('keytab_uri', val)
        self._keytab_uri = val
    
    _organizational_unit = None
    @property
    def organizational_unit(self):
        """
        Organization Unit. This option is available for a
        Microsoft AD KDC only.
        Attributes: non-creatable, modifiable
        """
        return self._organizational_unit
    @organizational_unit.setter
    def organizational_unit(self, val):
        if val != None:
            self.validate('organizational_unit', val)
        self._organizational_unit = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _is_kerberos_enabled = None
    @property
    def is_kerberos_enabled(self):
        """
        If 'true', then kerberos security is enabled.
        Attributes: non-creatable, modifiable
        """
        return self._is_kerberos_enabled
    @is_kerberos_enabled.setter
    def is_kerberos_enabled(self, val):
        if val != None:
            self.validate('is_kerberos_enabled', val)
        self._is_kerberos_enabled = val
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        Logical interface IP address.
        Attributes: non-creatable, non-modifiable
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    _admin_user_name = None
    @property
    def admin_user_name(self):
        """
        Administrator username.
        Attributes: non-creatable, modifiable
        """
        return self._admin_user_name
    @admin_user_name.setter
    def admin_user_name(self, val):
        if val != None:
            self.validate('admin_user_name', val)
        self._admin_user_name = val
    
    _service_principal_name = None
    @property
    def service_principal_name(self):
        """
        Kerberos service principal name.
        Attributes: non-creatable, modifiable
        """
        return self._service_principal_name
    @service_principal_name.setter
    def service_principal_name(self, val):
        if val != None:
            self.validate('service_principal_name', val)
        self._service_principal_name = val
    
    _admin_password = None
    @property
    def admin_password(self):
        """
        Administrator password.
        Attributes: non-creatable, modifiable
        """
        return self._admin_password
    @admin_password.setter
    def admin_password(self, val):
        if val != None:
            self.validate('admin_password', val)
        self._admin_password = val
    
    @staticmethod
    def get_api_name():
          return "kerberos-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'interface-name',
            'keytab-uri',
            'organizational-unit',
            'vserver',
            'is-kerberos-enabled',
            'ip-address',
            'admin-user-name',
            'service-principal-name',
            'admin-password',
        ]
    
    def describe_properties(self):
        return {
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'keytab_uri': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'organizational_unit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_kerberos_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'admin_user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'service_principal_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'admin_password': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
