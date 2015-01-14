from netapp.storage_array.storage_array_port_stats import StorageArrayPortStats
from netapp.netapp_object import NetAppObject

class StorageArrayPort(NetAppObject):
    """
    Maps array definition to target port
    """
    
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
    
    _max_queue_depth = None
    @property
    def max_queue_depth(self):
        """
        The target port queue depth for this target port.
        Range: [0..2048]
        """
        return self._max_queue_depth
    @max_queue_depth.setter
    def max_queue_depth(self, val):
        if val != None:
            self.validate('max_queue_depth', val)
        self._max_queue_depth = val
    
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
    
    _port_stat_info = None
    @property
    def port_stat_info(self):
        """
        Contains statistics about each array port.
        """
        return self._port_stat_info
    @port_stat_info.setter
    def port_stat_info(self, val):
        if val != None:
            self.validate('port_stat_info', val)
        self._port_stat_info = val
    
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
    
    _array_name = None
    @property
    def array_name(self):
        """
        Name of the array in the array record. (28 char max)
        """
        return self._array_name
    @array_name.setter
    def array_name(self, val):
        if val != None:
            self.validate('array_name', val)
        self._array_name = val
    
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
    
    @staticmethod
    def get_api_name():
          return "storage-array-port"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'wwnn',
            'max-queue-depth',
            'array-id',
            'target-port-speed',
            'connection-type',
            'port-stat-info',
            'wwpn',
            'array-name',
            'switch-port',
        ]
    
    def describe_properties(self):
        return {
            'wwnn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'max_queue_depth': { 'class': int, 'is_list': False, 'required': 'optional' },
            'array_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_port_speed': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'connection_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_stat_info': { 'class': StorageArrayPortStats, 'is_list': True, 'required': 'optional' },
            'wwpn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'array_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'switch_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
