from netapp.storage_array.storage_array_error_info import StorageArrayErrorInfo
from netapp.netapp_object import NetAppObject

class StorageArrayProfile(NetAppObject):
    """
    data describing characteristics/parameters of/about a storage array
    """
    
    _errors = None
    @property
    def errors(self):
        """
        A list of all errors for the requested array.
        """
        return self._errors
    @errors.setter
    def errors(self, val):
        if val != None:
            self.validate('errors', val)
        self._errors = val
    
    _vendor = None
    @property
    def vendor(self):
        """
        The name of the array's vendor, e.g. NetApp. (8 chars max)
        """
        return self._vendor
    @vendor.setter
    def vendor(self, val):
        if val != None:
            self.validate('vendor', val)
        self._vendor = val
    
    _name = None
    @property
    def name(self):
        """
        A unique node-level user supplied name for the array. (28 char max)
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _array_id = None
    @property
    def array_id(self):
        """
        primary key (system defined) for the array record.  Range: [0..2^64-1]
        """
        return self._array_id
    @array_id.setter
    def array_id(self, val):
        if val != None:
            self.validate('array_id', val)
        self._array_id = val
    
    _firmware = None
    @property
    def firmware(self):
        """
        The firmware revision of the array. (64 chars max)
        """
        return self._firmware
    @firmware.setter
    def firmware(self, val):
        if val != None:
            self.validate('firmware', val)
        self._firmware = val
    
    _max_queue_depth = None
    @property
    def max_queue_depth(self):
        """
        The target port queue depth for all target ports on this array.
        Range: [8..2048]
        """
        return self._max_queue_depth
    @max_queue_depth.setter
    def max_queue_depth(self, val):
        if val != None:
            self.validate('max_queue_depth', val)
        self._max_queue_depth = val
    
    _options = None
    @property
    def options(self):
        """
        A comma separated list of name value pairs of array specific settings. (128 chars max)
        """
        return self._options
    @options.setter
    def options(self, val):
        if val != None:
            self.validate('options', val)
        self._options = val
    
    _prefix = None
    @property
    def prefix(self):
        """
        A unique user supplied 5 character code used to refer to this array and used in naming
        the array's LUNs.
        """
        return self._prefix
    @prefix.setter
    def prefix(self, val):
        if val != None:
            self.validate('prefix', val)
        self._prefix = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        The serial number of the array. (17 char max)
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _affinity = None
    @property
    def affinity(self):
        """
        Describes the affinity model supported by the array.
        <p>Possible values are:
        <ul>
        <li>"none" - None
        <li>"aaa" - Active/Active Asymmettric
        <li>"ap"   - Active/Passive
        <li>"mixed" - This array is presenting different affinity models to different controllers within the cluster.
        </ul>
        """
        return self._affinity
    @affinity.setter
    def affinity(self, val):
        if val != None:
            self.validate('affinity', val)
        self._affinity = val
    
    _port_failover_type = None
    @property
    def port_failover_type(self):
        """
        The pathing failover supported by the array, either ACTIVE-ACTIVE or ACTIVE-PASSIVE.
        """
        return self._port_failover_type
    @port_failover_type.setter
    def port_failover_type(self, val):
        if val != None:
            self.validate('port_failover_type', val)
        self._port_failover_type = val
    
    _optimization_policy = None
    @property
    def optimization_policy(self):
        """
        Describes the I/O optimization policy used by this array.
        <p>Possible values are:
        <ul>
        <li>"ialua" - The array supports iALUA.
        <li>"ealua"   - The array supports eALUA.
        <li>"symmetric"   - All ports on the array will be treated equally.
        <li>"proprietary"   - A vendor specific optimization is supported for this array.
        <li>"mixed" - This array supports multiple optimization policies, one per node.
        <li>"unknown"   - No known optimization method is supported for this array (will be treated as if Symmetric)
        </ul>
        """
        return self._optimization_policy
    @optimization_policy.setter
    def optimization_policy(self, val):
        if val != None:
            self.validate('optimization_policy', val)
        self._optimization_policy = val
    
    _lun_queue_depth = None
    @property
    def lun_queue_depth(self):
        """
        The default queue depths assigned to array LUNs from this array.
        Range: [3..32]
        """
        return self._lun_queue_depth
    @lun_queue_depth.setter
    def lun_queue_depth(self, val):
        if val != None:
            self.validate('lun_queue_depth', val)
        self._lun_queue_depth = val
    
    _network_address = None
    @property
    def network_address(self):
        """
        IP address/node name of the array's SNMP management port. (1024 char max)
        """
        return self._network_address
    @network_address.setter
    def network_address(self, val):
        if val != None:
            self.validate('network_address', val)
        self._network_address = val
    
    _is_upgrade_pending = None
    @property
    def is_upgrade_pending(self):
        """
        The is-upgrade-pending status for the array.
        """
        return self._is_upgrade_pending
    @is_upgrade_pending.setter
    def is_upgrade_pending(self, val):
        if val != None:
            self.validate('is_upgrade_pending', val)
        self._is_upgrade_pending = val
    
    _model = None
    @property
    def model(self):
        """
        The model name of the array. (16 chars max)
        """
        return self._model
    @model.setter
    def model(self, val):
        if val != None:
            self.validate('model', val)
        self._model = val
    
    @staticmethod
    def get_api_name():
          return "storage-array-profile"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'errors',
            'vendor',
            'name',
            'array-id',
            'firmware',
            'max-queue-depth',
            'options',
            'prefix',
            'serial-number',
            'affinity',
            'port-failover-type',
            'optimization-policy',
            'lun-queue-depth',
            'network-address',
            'is-upgrade-pending',
            'model',
        ]
    
    def describe_properties(self):
        return {
            'errors': { 'class': StorageArrayErrorInfo, 'is_list': True, 'required': 'optional' },
            'vendor': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'array_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'firmware': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'max_queue_depth': { 'class': int, 'is_list': False, 'required': 'required' },
            'options': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'prefix': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'affinity': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'port_failover_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'optimization_policy': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'lun_queue_depth': { 'class': int, 'is_list': False, 'required': 'required' },
            'network_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_upgrade_pending': { 'class': bool, 'is_list': False, 'required': 'required' },
            'model': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
