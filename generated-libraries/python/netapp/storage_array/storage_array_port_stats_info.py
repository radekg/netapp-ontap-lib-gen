from netapp.netapp_object import NetAppObject

class StorageArrayPortStatsInfo(NetAppObject):
    """
    Contains statistics about an array port.
    """
    
    _node = None
    @property
    def node(self):
        """
        Node name of array's target port.
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _wwnn = None
    @property
    def wwnn(self):
        """
        World wide node name of array's target port (64 chars).
        """
        return self._wwnn
    @wwnn.setter
    def wwnn(self, val):
        if val != None:
            self.validate('wwnn', val)
        self._wwnn = val
    
    _target_io_kbps = None
    @property
    def target_io_kbps(self):
        """
        Rolling average of kilobytes per second read and written to this target port.
        Range: [0..2^64-1]
        """
        return self._target_io_kbps
    @target_io_kbps.setter
    def target_io_kbps(self, val):
        if val != None:
            self.validate('target_io_kbps', val)
        self._target_io_kbps = val
    
    _average_pending = None
    @property
    def average_pending(self):
        """
        An average over time of how many commands are on the outstanding queue.
        Range: [0..2^32-1]
        """
        return self._average_pending
    @average_pending.setter
    def average_pending(self, val):
        if val != None:
            self.validate('average_pending', val)
        self._average_pending = val
    
    _path_link_errors = None
    @property
    def path_link_errors(self):
        """
        Number of link errors reported on the path.
        Range: [0..2^32-1]
        """
        return self._path_link_errors
    @path_link_errors.setter
    def path_link_errors(self, val):
        if val != None:
            self.validate('path_link_errors', val)
        self._path_link_errors = val
    
    _average_latency_per_iop = None
    @property
    def average_latency_per_iop(self):
        """
        The average latency for I/O operations performed by this controller on this target port.
        Range: [0..2^32-1]
        """
        return self._average_latency_per_iop
    @average_latency_per_iop.setter
    def average_latency_per_iop(self, val):
        if val != None:
            self.validate('average_latency_per_iop', val)
        self._average_latency_per_iop = val
    
    _array_id = None
    @property
    def array_id(self):
        """
        Primary key (system defined) for the array record.
        Range: [0..2^64-1]
        """
        return self._array_id
    @array_id.setter
    def array_id(self, val):
        if val != None:
            self.validate('array_id', val)
        self._array_id = val
    
    _target_iops = None
    @property
    def target_iops(self):
        """
        Rolling average of I/O operations per second read and written to this target port.
        Range: [0..2^64-1]
        """
        return self._target_iops
    @target_iops.setter
    def target_iops(self, val):
        if val != None:
            self.validate('target_iops', val)
        self._target_iops = val
    
    _target_port_speed = None
    @property
    def target_port_speed(self):
        """
        The speed that the target port has negotiated with its connected switch port, or initiator port if direct attached.
        """
        return self._target_port_speed
    @target_port_speed.setter
    def target_port_speed(self, val):
        if val != None:
            self.validate('target_port_speed', val)
        self._target_port_speed = val
    
    _max_pending = None
    @property
    def max_pending(self):
        """
        The largest number of commands observed on the outstanding queue.
        Range: [0..2^32-1]
        """
        return self._max_pending
    @max_pending.setter
    def max_pending(self, val):
        if val != None:
            self.validate('max_pending', val)
        self._max_pending = val
    
    _average_waiting = None
    @property
    def average_waiting(self):
        """
        An average over time of how many commands are on the waiting queue.
        Range: [0..2^32-1]
        """
        return self._average_waiting
    @average_waiting.setter
    def average_waiting(self, val):
        if val != None:
            self.validate('average_waiting', val)
        self._average_waiting = val
    
    _connection_type = None
    @property
    def connection_type(self):
        """
        Describes the type of connection between the controller and the back end storage.
        <p>Possible values are:
        <ul>
        <li>"direct" - Direct Attached
        <li>"fabric" - Fabric Attached
        </ul>
        """
        return self._connection_type
    @connection_type.setter
    def connection_type(self, val):
        if val != None:
            self.validate('connection_type', val)
        self._connection_type = val
    
    _percent_waiting = None
    @property
    def percent_waiting(self):
        """
        The percentage of time there are I/Os waiting on the waiting queue on the target port.
        Range: [0..100]
        """
        return self._percent_waiting
    @percent_waiting.setter
    def percent_waiting(self, val):
        if val != None:
            self.validate('percent_waiting', val)
        self._percent_waiting = val
    
    _max_waiting = None
    @property
    def max_waiting(self):
        """
        The largest number of commands observed on the waiting queue.
        Range: [0..2^32-1]
        """
        return self._max_waiting
    @max_waiting.setter
    def max_waiting(self, val):
        if val != None:
            self.validate('max_waiting', val)
        self._max_waiting = val
    
    _wwpn = None
    @property
    def wwpn(self):
        """
        World wide port name of array's target port (64 chars).
        """
        return self._wwpn
    @wwpn.setter
    def wwpn(self, val):
        if val != None:
            self.validate('wwpn', val)
        self._wwpn = val
    
    _target_lun_in_use_count = None
    @property
    def target_lun_in_use_count(self):
        """
        Number of disks in the IN-USE state on this target port.
        Range: [0..2^64-1]
        """
        return self._target_lun_in_use_count
    @target_lun_in_use_count.setter
    def target_lun_in_use_count(self, val):
        if val != None:
            self.validate('target_lun_in_use_count', val)
        self._target_lun_in_use_count = val
    
    _switch_port = None
    @property
    def switch_port(self):
        """
        For fabric attached connections, the switch port the array target port is connected to. N/A for direct attached.
        """
        return self._switch_port
    @switch_port.setter
    def switch_port(self, val):
        if val != None:
            self.validate('switch_port', val)
        self._switch_port = val
    
    _initiator_port = None
    @property
    def initiator_port(self):
        """
        Initiator port name, e.g. 0a.
        """
        return self._initiator_port
    @initiator_port.setter
    def initiator_port(self, val):
        if val != None:
            self.validate('initiator_port', val)
        self._initiator_port = val
    
    _percent_busy = None
    @property
    def percent_busy(self):
        """
        The percentage of time I/Os are outstanding on the port.
        Range: [0..100]
        """
        return self._percent_busy
    @percent_busy.setter
    def percent_busy(self, val):
        if val != None:
            self.validate('percent_busy', val)
        self._percent_busy = val
    
    @staticmethod
    def get_api_name():
          return "storage-array-port-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'wwnn',
            'target-io-kbps',
            'average-pending',
            'path-link-errors',
            'average-latency-per-iop',
            'array-id',
            'target-iops',
            'target-port-speed',
            'max-pending',
            'average-waiting',
            'connection-type',
            'percent-waiting',
            'max-waiting',
            'wwpn',
            'target-lun-in-use-count',
            'switch-port',
            'initiator-port',
            'percent-busy',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'wwnn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_io_kbps': { 'class': int, 'is_list': False, 'required': 'required' },
            'average_pending': { 'class': int, 'is_list': False, 'required': 'required' },
            'path_link_errors': { 'class': int, 'is_list': False, 'required': 'required' },
            'average_latency_per_iop': { 'class': int, 'is_list': False, 'required': 'required' },
            'array_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_iops': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_port_speed': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'max_pending': { 'class': int, 'is_list': False, 'required': 'required' },
            'average_waiting': { 'class': int, 'is_list': False, 'required': 'required' },
            'connection_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percent_waiting': { 'class': int, 'is_list': False, 'required': 'required' },
            'max_waiting': { 'class': int, 'is_list': False, 'required': 'required' },
            'wwpn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_lun_in_use_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'switch_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percent_busy': { 'class': int, 'is_list': False, 'required': 'required' },
        }
