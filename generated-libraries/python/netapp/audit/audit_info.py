from netapp.netapp_object import NetAppObject

class AuditInfo(NetAppObject):
    """
    Administrative audit settings of the cluster.
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
    
    _cli_get = None
    @property
    def cli_get(self):
        """
        Enable auditing of CLI get operations
        Attributes: non-creatable, modifiable
        """
        return self._cli_get
    @cli_get.setter
    def cli_get(self, val):
        if val != None:
            self.validate('cli_get', val)
        self._cli_get = val
    
    _http_get = None
    @property
    def http_get(self):
        """
        Enable auditing of HTTP get operations
        Attributes: non-creatable, modifiable
        """
        return self._http_get
    @http_get.setter
    def http_get(self, val):
        if val != None:
            self.validate('http_get', val)
        self._http_get = val
    
    _ontapi_get = None
    @property
    def ontapi_get(self):
        """
        Enable auditing of Data ONTAP API get operations
        Attributes: non-creatable, modifiable
        """
        return self._ontapi_get
    @ontapi_get.setter
    def ontapi_get(self, val):
        if val != None:
            self.validate('ontapi_get', val)
        self._ontapi_get = val
    
    _http_set = None
    @property
    def http_set(self):
        """
        Enable auditing of HTTP set operations
        Attributes: non-creatable, modifiable
        """
        return self._http_set
    @http_set.setter
    def http_set(self, val):
        if val != None:
            self.validate('http_set', val)
        self._http_set = val
    
    _ontapi_set = None
    @property
    def ontapi_set(self):
        """
        Enable auditing of Data ONTAP API set operations
        Attributes: non-creatable, modifiable
        """
        return self._ontapi_set
    @ontapi_set.setter
    def ontapi_set(self, val):
        if val != None:
            self.validate('ontapi_set', val)
        self._ontapi_set = val
    
    _snmp_get = None
    @property
    def snmp_get(self):
        """
        Enable auditing of SNMP get operations
        Attributes: non-creatable, modifiable
        """
        return self._snmp_get
    @snmp_get.setter
    def snmp_get(self, val):
        if val != None:
            self.validate('snmp_get', val)
        self._snmp_get = val
    
    _cli_set = None
    @property
    def cli_set(self):
        """
        Enable auditing of CLI set operations
        Attributes: non-creatable, modifiable
        """
        return self._cli_set
    @cli_set.setter
    def cli_set(self, val):
        if val != None:
            self.validate('cli_set', val)
        self._cli_set = val
    
    _snmp_set = None
    @property
    def snmp_set(self):
        """
        Enable auditing of SNMP set operations
        Attributes: non-creatable, modifiable
        """
        return self._snmp_set
    @snmp_set.setter
    def snmp_set(self, val):
        if val != None:
            self.validate('snmp_set', val)
        self._snmp_set = val
    
    @staticmethod
    def get_api_name():
          return "audit-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'cli-get',
            'http-get',
            'ontapi-get',
            'http-set',
            'ontapi-set',
            'snmp-get',
            'cli-set',
            'snmp-set',
        ]
    
    def describe_properties(self):
        return {
            'cli_get': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'http_get': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ontapi_get': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'http_set': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'ontapi_set': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'snmp_get': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'cli_set': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'snmp_set': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
