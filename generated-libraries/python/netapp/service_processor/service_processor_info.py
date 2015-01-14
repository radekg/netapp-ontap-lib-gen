from netapp.netapp_object import NetAppObject

class ServiceProcessorInfo(NetAppObject):
    """
    Service processor information
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
    
    _node = None
    @property
    def node(self):
        """
        Node on which the device is located
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _status = None
    @property
    def status(self):
        """
        Current status of the device
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "online"              - Device is up and running
        fine,
        <li> "offline"             - Device is out of
        communication,
        <li> "sp_daemon_offline"   - Daemon which communicates
        with the device is not running,
        <li> "node_offline"        - Node that hosts the device
        is out of communication,
        <li> "degraded"            - Node that hosts the device
        is missing heartbeat signals from the device,
        <li> "rebooting"           - Device is rebooting,
        <li> "unknown"             - Device status could not be
        determined
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _part_num = None
    @property
    def part_num(self):
        """
        Part number of the device. Applicable for RLM only
        Attributes: non-creatable, non-modifiable
        """
        return self._part_num
    @part_num.setter
    def part_num(self, val):
        if val != None:
            self.validate('part_num', val)
        self._part_num = val
    
    _serial_num = None
    @property
    def serial_num(self):
        """
        Serial number of the device. Applicable for RLM only
        Attributes: non-creatable, non-modifiable
        """
        return self._serial_num
    @serial_num.setter
    def serial_num(self, val):
        if val != None:
            self.validate('serial_num', val)
        self._serial_num = val
    
    _ipmi_version = None
    @property
    def ipmi_version(self):
        """
        IPMI version supported by the device
        Attributes: non-creatable, non-modifiable
        """
        return self._ipmi_version
    @ipmi_version.setter
    def ipmi_version(self, val):
        if val != None:
            self.validate('ipmi_version', val)
        self._ipmi_version = val
    
    _firmware_version = None
    @property
    def firmware_version(self):
        """
        Firmware version installed on the device
        Attributes: non-creatable, non-modifiable
        """
        return self._firmware_version
    @firmware_version.setter
    def firmware_version(self, val):
        if val != None:
            self.validate('firmware_version', val)
        self._firmware_version = val
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        Public IP addresses of the device
        Attributes: non-creatable, non-modifiable
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    _device_revision = None
    @property
    def device_revision(self):
        """
        Device revision. Applicable for RLM only
        Attributes: non-creatable, non-modifiable
        """
        return self._device_revision
    @device_revision.setter
    def device_revision(self, val):
        if val != None:
            self.validate('device_revision', val)
        self._device_revision = val
    
    _is_ip_configured = None
    @property
    def is_ip_configured(self):
        """
        Is network configured on the device to have at least one
        public IP address
        Attributes: non-creatable, non-modifiable
        """
        return self._is_ip_configured
    @is_ip_configured.setter
    def is_ip_configured(self, val):
        if val != None:
            self.validate('is_ip_configured', val)
        self._is_ip_configured = val
    
    _type = None
    @property
    def type(self):
        """
        Type of device
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "rlm"  - Remote LAN Module,
        <li> "sp"   - Service Processor,
        <li> "none" - None
        </ul>
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _mac_address = None
    @property
    def mac_address(self):
        """
        MAC address of the device
        Attributes: non-creatable, non-modifiable
        """
        return self._mac_address
    @mac_address.setter
    def mac_address(self, val):
        if val != None:
            self.validate('mac_address', val)
        self._mac_address = val
    
    _is_autoupdate_enabled = None
    @property
    def is_autoupdate_enabled(self):
        """
        Is firmware autoupdate enabled for the device
        Attributes: non-creatable, non-modifiable
        """
        return self._is_autoupdate_enabled
    @is_autoupdate_enabled.setter
    def is_autoupdate_enabled(self, val):
        if val != None:
            self.validate('is_autoupdate_enabled', val)
        self._is_autoupdate_enabled = val
    
    @staticmethod
    def get_api_name():
          return "service-processor-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'status',
            'part-num',
            'serial-num',
            'ipmi-version',
            'firmware-version',
            'ip-address',
            'device-revision',
            'is-ip-configured',
            'type',
            'mac-address',
            'is-autoupdate-enabled',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'part_num': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'serial_num': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ipmi_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'firmware_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ip_address': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'device_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_ip_configured': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'mac_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_autoupdate_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
