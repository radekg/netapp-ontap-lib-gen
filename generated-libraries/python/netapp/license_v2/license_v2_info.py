from netapp.netapp_object import NetAppObject

class LicenseV2Info(NetAppObject):
    """
    Information about a licensable package.
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
    
    _grace_period_expiration = None
    @property
    def grace_period_expiration(self):
        """
        The grace period expiration date/time. This is only
        provided if is-in-grace-period is returned. If
        is-in-grace-period is true, then this is the expiration
        date/time of the grace period. If is-in-grace-period is
        false then this value will be 0.
        Attributes: non-creatable, non-modifiable
        """
        return self._grace_period_expiration
    @grace_period_expiration.setter
    def grace_period_expiration(self, val):
        if val != None:
            self.validate('grace_period_expiration', val)
        self._grace_period_expiration = val
    
    _legacy = None
    @property
    def legacy(self):
        """
        Legacy License. A legacy license indicates that the license was
        previously installed prior to this release. Returns true if the license was
        installed prior to this release and false otherwise.
        """
        return self._legacy
    @legacy.setter
    def legacy(self, val):
        if val != None:
            self.validate('legacy', val)
        self._legacy = val
    
    _description = None
    @property
    def description(self):
        """
        Description of the licensed package.
        Attributes: non-creatable, non-modifiable
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    _package = None
    @property
    def package(self):
        """
        Name of the licensed package.
        Attributes: key, required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "base"                - Cluster Base License,
        <li> "nfs"                 - NFS License,
        <li> "cifs"                - CIFS License,
        <li> "iscsi"               - iSCSI License,
        <li> "fcp"                 - FCP License,
        <li> "cdmi"                - CDMI License,
        <li> "snaprestore"         - SnapRestore License,
        <li> "snapmirror"          - SnapMirror License,
        <li> "flexclone"           - FlexClone License,
        <li> "snapvault"           - SnapVault License,
        <li> "snaplock"            - SnapLock License,
        <li> "snapmanagersuite"    - SnapManagerSuite License,
        <li> "snapprotectapps"     - SnapProtectApp License,
        <li> "v_storageattach"     - Virtual Attached Storage License
        </ul>
        """
        return self._package
    @package.setter
    def package(self, val):
        if val != None:
            self.validate('package', val)
        self._package = val
    
    _expiration_time = None
    @property
    def expiration_time(self):
        """
        License expiration time.
        Attributes: non-creatable, non-modifiable
        """
        return self._expiration_time
    @expiration_time.setter
    def expiration_time(self, val):
        if val != None:
            self.validate('expiration_time', val)
        self._expiration_time = val
    
    _customer_id = None
    @property
    def customer_id(self):
        """
        Customer Identification. This field is used to track site licenses
        issued to Enterprise Level Agreement customers. It will typical be
        set to "none" unless a unique customer id has been assigned. This
        value is reported in Auto Support, and can be used to correlate
        licensing information with backend business systems for tracking
        purposes.
        Attributes: non-creatable, non-modifiable
        """
        return self._customer_id
    @customer_id.setter
    def customer_id(self, val):
        if val != None:
            self.validate('customer_id', val)
        self._customer_id = val
    
    _is_in_grace_period = None
    @property
    def is_in_grace_period(self):
        """
        The system serial number grace period. Returns true
        if a system serial number change was detected and the
        system is currently in the grace period. During this grace
        period serial number checking for currently installed
        licenses will be ignored. The serial-number element
        for various package licenses may differ while valid
        licenses are being installed.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_in_grace_period
    @is_in_grace_period.setter
    def is_in_grace_period(self, val):
        if val != None:
            self.validate('is_in_grace_period', val)
        self._is_in_grace_period = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Serial number of the controller or cluster. The license serial-number
        is reported in Auto Support also and can be used to correlate
        controller or cluster wide licensing information.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _owner = None
    @property
    def owner(self):
        """
        Controller or Cluster that owns the serial number.
        Attributes: non-creatable, non-modifiable
        """
        return self._owner
    @owner.setter
    def owner(self, val):
        if val != None:
            self.validate('owner', val)
        self._owner = val
    
    _type = None
    @property
    def type(self):
        """
        License type.
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "license"   ,
        <li> "site"      ,
        <li> "demo"
        </ul>
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    @staticmethod
    def get_api_name():
          return "license-v2-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'grace-period-expiration',
            'legacy',
            'description',
            'package',
            'expiration-time',
            'customer-id',
            'is-in-grace-period',
            'serial-number',
            'owner',
            'type',
        ]
    
    def describe_properties(self):
        return {
            'grace_period_expiration': { 'class': int, 'is_list': False, 'required': 'optional' },
            'legacy': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'package': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'expiration_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'customer_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_in_grace_period': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
