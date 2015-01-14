from netapp.netapp_object import NetAppObject

class InterimLicenseClusterInfo(NetAppObject):
    """
    Information about a single licensable service/feature.
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
    
    _code = None
    @property
    def code(self):
        """
        License code for the specified service/feature. 14
        Uppercase Alpha only characters.
        Attributes: required-for-create, non-modifiable
        """
        return self._code
    @code.setter
    def code(self, val):
        if val != None:
            self.validate('code', val)
        self._code = val
    
    _expiration_date = None
    @property
    def expiration_date(self):
        """
        Cluster license expiration date.
        Attributes: non-creatable, non-modifiable
        """
        return self._expiration_date
    @expiration_date.setter
    def expiration_date(self, val):
        if val != None:
            self.validate('expiration_date', val)
        self._expiration_date = val
    
    _description = None
    @property
    def description(self):
        """
        Description of the licensed service/feature
        Attributes: non-creatable, non-modifiable
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    _service = None
    @property
    def service(self):
        """
        Name of the licensed feature.
        Attributes: key, required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "base"                - Base License w/cluster
        size limit (nodes),
        <li> "mirror"              - Mirror License,
        <li> "flexvol_hpo"         - FlexVol HPO License,
        <li> "cifs"                - CIFS License,
        <li> "snaprestore"         - SnapRestore License,
        <li> "flexclone"           - FlexClone License,
        <li> "nfs"                 - NFS License,
        <li> "snapmirror_dp"       - SnapMirror Data Protection
        License,
        <li> "iscsi"               - iSCSI License,
        <li> "striped_volume"      - Striped Volume License,
        <li> "fcp"                 - FCP License,
        <li> "snapmanager_suite"   - SnapManager Suite
        License,
        <li> "spa"                 - SPA License,
        <li> "insight_balance"     - OnCommand Balance
        </ul>
        """
        return self._service
    @service.setter
    def service(self, val):
        if val != None:
            self.validate('service', val)
        self._service = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Cluster Serial Number
        Attributes: non-creatable, non-modifiable
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _limit = None
    @property
    def limit(self):
        """
        A feature specific data field most commonly interpreted
        as a node-count
        Attributes: non-creatable, non-modifiable
        """
        return self._limit
    @limit.setter
    def limit(self, val):
        if val != None:
            self.validate('limit', val)
        self._limit = val
    
    @staticmethod
    def get_api_name():
          return "interim-license-cluster-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'code',
            'expiration-date',
            'description',
            'service',
            'serial-number',
            'limit',
        ]
    
    def describe_properties(self):
        return {
            'code': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'expiration_date': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'service': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'limit': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
