from netapp.netapp_object import NetAppObject

class GpoGpresultInfo(NetAppObject):
    """
    GPO RSoP(Resultant Set of Policy) that is currently defined on
    the Active Directory for a CIFS-enabled Vserver.
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
    
    _registry_hash_version = None
    @property
    def registry_hash_version(self):
        """
        Hash Version Support for BranchCache.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "all_versions"   - Version 1 and 2 (V1 and V2).,
        <li> "version1"       - Version 1 (V1).,
        <li> "version2"       - Version 2 (V2).
        </ul>
        """
        return self._registry_hash_version
    @registry_hash_version.setter
    def registry_hash_version(self, val):
        if val != None:
            self.validate('registry_hash_version', val)
        self._registry_hash_version = val
    
    _gpo_status = None
    @property
    def gpo_status(self):
        """
        GPO status for each listed GPO: enabled or disabled.
        Attributes: non-creatable, non-modifiable
        """
        return self._gpo_status
    @gpo_status.setter
    def gpo_status(self, val):
        if val != None:
            self.validate('gpo_status', val)
        self._gpo_status = val
    
    _registry_refresh_interval = None
    @property
    def registry_refresh_interval(self):
        """
        Registry refreshint time interval.
        Attributes: non-creatable, non-modifiable
        """
        return self._registry_refresh_interval
    @registry_refresh_interval.setter
    def registry_refresh_interval(self, val):
        if val != None:
            self.validate('registry_refresh_interval', val)
        self._registry_refresh_interval = val
    
    _gpo_name = None
    @property
    def gpo_name(self):
        """
        GPO name in text format.
        Attributes: non-creatable, non-modifiable
        """
        return self._gpo_name
    @gpo_name.setter
    def gpo_name(self, val):
        if val != None:
            self.validate('gpo_name', val)
        self._gpo_name = val
    
    _extension = None
    @property
    def extension(self):
        """
        List of the GPO extensions.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "registry"       - Registry Setting,
        <li> "diskquota"      - Disk Quota,
        <li> "scripts"        - Scripts,
        <li> "security"       - Security,
        <li> "efsrecovery"    - EFS Recovery,
        <li> "ipsecurity"     - IP Security,
        <li> "unsupport"      - Unsupported Feature
        </ul>
        """
        return self._extension
    @extension.setter
    def extension(self, val):
        if val != None:
            self.validate('extension', val)
        self._extension = val
    
    _gpo_index = None
    @property
    def gpo_index(self):
        """
        The index of the GPO in the GPO list of a Vserver.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._gpo_index
    @gpo_index.setter
    def gpo_index(self, val):
        if val != None:
            self.validate('gpo_index', val)
        self._gpo_index = val
    
    _filesyspath = None
    @property
    def filesyspath(self):
        """
        File System Path of a GPO policy file.
        Attributes: non-creatable, non-modifiable
        """
        return self._filesyspath
    @filesyspath.setter
    def filesyspath(self, val):
        if val != None:
            self.validate('filesyspath', val)
        self._filesyspath = val
    
    _security_kerberos_ticket_age = None
    @property
    def security_kerberos_ticket_age(self):
        """
        Kerberos maximum lifetime for user ticket.
        Attributes: non-creatable, non-modifiable
        """
        return self._security_kerberos_ticket_age
    @security_kerberos_ticket_age.setter
    def security_kerberos_ticket_age(self, val):
        if val != None:
            self.validate('security_kerberos_ticket_age', val)
        self._security_kerberos_ticket_age = val
    
    _gpo_uuid = None
    @property
    def gpo_uuid(self):
        """
        GPO name in UUID format.
        Attributes: non-creatable, non-modifiable
        """
        return self._gpo_uuid
    @gpo_uuid.setter
    def gpo_uuid(self, val):
        if val != None:
            self.validate('gpo_uuid', val)
        self._gpo_uuid = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver display name.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _version = None
    @property
    def version(self):
        """
        The individual GPO's update version.
        Attributes: non-creatable, non-modifiable
        """
        return self._version
    @version.setter
    def version(self, val):
        if val != None:
            self.validate('version', val)
        self._version = val
    
    _link = None
    @property
    def link(self):
        """
        Type of the GPO.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "local"               - Local,
        <li> "site"                - Site,
        <li> "domain"              - Domain,
        <li> "organizationalunit"  - Organizational Unit
        </ul>
        """
        return self._link
    @link.setter
    def link(self, val):
        if val != None:
            self.validate('link', val)
        self._link = val
    
    _security_privilege_take_ownership = None
    @property
    def security_privilege_take_ownership(self):
        """
        Privilege rights: Take Ownership.
        Attributes: non-creatable, non-modifiable
        """
        return self._security_privilege_take_ownership
    @security_privilege_take_ownership.setter
    def security_privilege_take_ownership(self, val):
        if val != None:
            self.validate('security_privilege_take_ownership', val)
        self._security_privilege_take_ownership = val
    
    _security_kerberos_renewal_age = None
    @property
    def security_kerberos_renewal_age(self):
        """
        Kerberos maximum lifetime for user ticket renewal.
        Attributes: non-creatable, non-modifiable
        """
        return self._security_kerberos_renewal_age
    @security_kerberos_renewal_age.setter
    def security_kerberos_renewal_age(self, val):
        if val != None:
            self.validate('security_kerberos_renewal_age', val)
        self._security_kerberos_renewal_age = val
    
    _security_kerberos_clock_skew = None
    @property
    def security_kerberos_clock_skew(self):
        """
        Kerberos maximum clock skew; Maximum tolerance for
        computer clock synchronization.
        Attributes: non-creatable, non-modifiable
        """
        return self._security_kerberos_clock_skew
    @security_kerberos_clock_skew.setter
    def security_kerberos_clock_skew(self, val):
        if val != None:
            self.validate('security_kerberos_clock_skew', val)
        self._security_kerberos_clock_skew = val
    
    _dspath = None
    @property
    def dspath(self):
        """
        LDAP DN path.
        Attributes: non-creatable, non-modifiable
        """
        return self._dspath
    @dspath.setter
    def dspath(self, val):
        if val != None:
            self.validate('dspath', val)
        self._dspath = val
    
    _registry_hash_publication = None
    @property
    def registry_hash_publication(self):
        """
        Hash Publication for BranchCache.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "per_share"      - Allow hash publication only for
        shared folders on which BranchCache is enabled.,
        <li> "disabled"       - Disallow hash publication on
        all shared folders.,
        <li> "all_shares"     - Allow hash publication for all
        shared folder.
        </ul>
        """
        return self._registry_hash_publication
    @registry_hash_publication.setter
    def registry_hash_publication(self, val):
        if val != None:
            self.validate('registry_hash_publication', val)
        self._registry_hash_publication = val
    
    _registry_refresh_random_offset = None
    @property
    def registry_refresh_random_offset(self):
        """
        Registry refreshing time random offset.
        Attributes: non-creatable, non-modifiable
        """
        return self._registry_refresh_random_offset
    @registry_refresh_random_offset.setter
    def registry_refresh_random_offset(self, val):
        if val != None:
            self.validate('registry_refresh_random_offset', val)
        self._registry_refresh_random_offset = val
    
    @staticmethod
    def get_api_name():
          return "gpo-gpresult-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'registry-hash-version',
            'gpo-status',
            'registry-refresh-interval',
            'gpo-name',
            'extension',
            'gpo-index',
            'filesyspath',
            'security-kerberos-ticket-age',
            'gpo-uuid',
            'vserver',
            'version',
            'link',
            'security-privilege-take-ownership',
            'security-kerberos-renewal-age',
            'security-kerberos-clock-skew',
            'dspath',
            'registry-hash-publication',
            'registry-refresh-random-offset',
        ]
    
    def describe_properties(self):
        return {
            'registry_hash_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'gpo_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'registry_refresh_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'gpo_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'extension': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'gpo_index': { 'class': int, 'is_list': False, 'required': 'optional' },
            'filesyspath': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'security_kerberos_ticket_age': { 'class': int, 'is_list': False, 'required': 'optional' },
            'gpo_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'version': { 'class': int, 'is_list': False, 'required': 'optional' },
            'link': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'security_privilege_take_ownership': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'security_kerberos_renewal_age': { 'class': int, 'is_list': False, 'required': 'optional' },
            'security_kerberos_clock_skew': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dspath': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'registry_hash_publication': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'registry_refresh_random_offset': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
