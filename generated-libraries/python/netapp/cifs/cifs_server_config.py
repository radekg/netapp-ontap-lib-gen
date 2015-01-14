from netapp.netapp_object import NetAppObject

class CifsServerConfig(NetAppObject):
    """
    Basic configuration information for the CIFS Server.
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
    
    _domain = None
    @property
    def domain(self):
        """
        The Fully Qualified Domain Name of the Windows Active
        Directory this CIFS server belongs to.
        Attributes: required-for-create, modifiable
        """
        return self._domain
    @domain.setter
    def domain(self, val):
        if val != None:
            self.validate('domain', val)
        self._domain = val
    
    _cifs_server = None
    @property
    def cifs_server(self):
        """
        The NetBIOS name of the CIFS server.
        Attributes: required-for-create, non-modifiable
        """
        return self._cifs_server
    @cifs_server.setter
    def cifs_server(self, val):
        if val != None:
            self.validate('cifs_server', val)
        self._cifs_server = val
    
    _default_site = None
    @property
    def default_site(self):
        """
        The default site used by LIFs that do not have a site
        membership.
        Attributes: optional-for-create, modifiable
        """
        return self._default_site
    @default_site.setter
    def default_site(self, val):
        if val != None:
            self.validate('default_site', val)
        self._default_site = val
    
    _domain_workgroup = None
    @property
    def domain_workgroup(self):
        """
        The NetBIOS name of the domain or workgroup this CIFS
        server belongs to.
        Attributes: non-creatable, non-modifiable
        """
        return self._domain_workgroup
    @domain_workgroup.setter
    def domain_workgroup(self, val):
        if val != None:
            self.validate('domain_workgroup', val)
        self._domain_workgroup = val
    
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
    
    _administrative_status = None
    @property
    def administrative_status(self):
        """
        CIFS Server Administrative Status.
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "down" ,
        <li> "up"
        </ul>
        """
        return self._administrative_status
    @administrative_status.setter
    def administrative_status(self, val):
        if val != None:
            self.validate('administrative_status', val)
        self._administrative_status = val
    
    _organizational_unit = None
    @property
    def organizational_unit(self):
        """
        The Organizational Unit (OU) within the Windows Active
        Directory this CIFS server belongs to.
        Attributes: optional-for-create, non-modifiable
        """
        return self._organizational_unit
    @organizational_unit.setter
    def organizational_unit(self, val):
        if val != None:
            self.validate('organizational_unit', val)
        self._organizational_unit = val
    
    _auth_style = None
    @property
    def auth_style(self):
        """
        The authentication style to be used for CIFS clients
        connecting to this CIFS server.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "domain"    - DOMAIN,
        <li> "workgroup" - WORKGROUP
        </ul>
        """
        return self._auth_style
    @auth_style.setter
    def auth_style(self, val):
        if val != None:
            self.validate('auth_style', val)
        self._auth_style = val
    
    @staticmethod
    def get_api_name():
          return "cifs-server-config"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'domain',
            'cifs-server',
            'default-site',
            'domain-workgroup',
            'vserver',
            'administrative-status',
            'organizational-unit',
            'auth-style',
        ]
    
    def describe_properties(self):
        return {
            'domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cifs_server': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'default_site': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'domain_workgroup': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'administrative_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'organizational_unit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'auth_style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
