from netapp.netapp_object import NetAppObject

class DiskPathInfo(NetAppObject):
    """
    Contains per path statistics, errors and other related data.
    """
    
    _target_side_switch_port = None
    @property
    def target_side_switch_port(self):
        """
        Name of the switch port connected to the target
        array, or UNKNOWN if direct attached.
        """
        return self._target_side_switch_port
    @target_side_switch_port.setter
    def target_side_switch_port(self, val):
        if val != None:
            self.validate('target_side_switch_port', val)
        self._target_side_switch_port = val
    
    _tpgn = None
    @property
    def tpgn(self):
        """
        The Target Port Group Number of the array's target port.
        Range: [0..2^64-1]
        """
        return self._tpgn
    @tpgn.setter
    def tpgn(self, val):
        if val != None:
            self.validate('tpgn', val)
        self._tpgn = val
    
    _initiator_side_switch_port = None
    @property
    def initiator_side_switch_port(self):
        """
        The name of the switch connected to the controller's
        initiator port, or N/A when using direct attach
        """
        return self._initiator_side_switch_port
    @initiator_side_switch_port.setter
    def initiator_side_switch_port(self, val):
        if val != None:
            self.validate('initiator_side_switch_port', val)
        self._initiator_side_switch_port = val
    
    _path_io_kbps = None
    @property
    def path_io_kbps(self):
        """
        Rolling average of kilobytes per second read and written to this path.
        Range: [0..2^64-1]
        """
        return self._path_io_kbps
    @path_io_kbps.setter
    def path_io_kbps(self, val):
        if val != None:
            self.validate('path_io_kbps', val)
        self._path_io_kbps = val
    
    _lun_path_use_state = None
    @property
    def lun_path_use_state(self):
        """
        ONTAP's use of this path
        INU - (In Use) This path is currently used for I/O.
        RDY - (Ready) This path is not being used for I/O currently, but might transition
        to INU if storge errors or load balancing cause it to transition to INU.
        ERR - (High Error)  The weighted error total on this path is 20% or more of the error
        threshold.  Load balancing will not use it, and the error handling code will
        only use it as a last resort.
        QED - (Quiesced) : The disk is quiesced on this path.
        MCF - (Misconfigured) : The disk is misconfigured on this path. The path is not available
        for I/O. Refer to storage_initiator_errors_list_info for details.
        FAL - (Failed) The connectivity to this path is lost.
        """
        return self._lun_path_use_state
    @lun_path_use_state.setter
    def lun_path_use_state(self, val):
        if val != None:
            self.validate('lun_path_use_state', val)
        self._lun_path_use_state = val
    
    _preferred_target_port = None
    @property
    def preferred_target_port(self):
        """
        For a logical unit which reports asymmetric access, preferred-target-port indicates that
        a path, regardless of the current access state, routes to a preferred target port group.
        Possible values are:
        <ul>
        <li> true:   This path routes to a preferred target port group for this array LUN.
        <li> false: This path does not route to a preferred target port group or the array LUN
        reports that there is no preferred target port group.
        </ul>
        """
        return self._preferred_target_port
    @preferred_target_port.setter
    def preferred_target_port(self, val):
        if val != None:
            self.validate('preferred_target_port', val)
        self._preferred_target_port = val
    
    _disk_name = None
    @property
    def disk_name(self):
        """
        The name of the disk this path information is for
        """
        return self._disk_name
    @disk_name.setter
    def disk_name(self, val):
        if val != None:
            self.validate('disk_name', val)
        self._disk_name = val
    
    _array_name = None
    @property
    def array_name(self):
        """
        The name of the array providing the lun.
        """
        return self._array_name
    @array_name.setter
    def array_name(self, val):
        if val != None:
            self.validate('array_name', val)
        self._array_name = val
    
    _disk_port = None
    @property
    def disk_port(self):
        """
        Disk port associated with this path. Possible
        values are "A" or "B". Omitted for non-disk target.
        """
        return self._disk_port
    @disk_port.setter
    def disk_port(self, val):
        if val != None:
            self.validate('disk_port', val)
        self._disk_port = val
    
    _initiator_iops = None
    @property
    def initiator_iops(self):
        """
        Rolling average of I/O operations per second read and written over this initiator port.
        Range: [0..2^64-1]
        """
        return self._initiator_iops
    @initiator_iops.setter
    def initiator_iops(self, val):
        if val != None:
            self.validate('initiator_iops', val)
        self._initiator_iops = val
    
    _vmdisk_device_id = None
    @property
    def vmdisk_device_id(self):
        """
        The device id used for the virtual device (also used by the hypervisor)
        Range: [0..2^32-1]
        """
        return self._vmdisk_device_id
    @vmdisk_device_id.setter
    def vmdisk_device_id(self, val):
        if val != None:
            self.validate('vmdisk_device_id', val)
        self._vmdisk_device_id = val
    
    _lun_number = None
    @property
    def lun_number(self):
        """
        LU number.
        Range: [0..65535]
        """
        return self._lun_number
    @lun_number.setter
    def lun_number(self, val):
        if val != None:
            self.validate('lun_number', val)
        self._lun_number = val
    
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
    
    _node = None
    @property
    def node(self):
        """
        Controller with the initiator port for this path.
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _lun_iops = None
    @property
    def lun_iops(self):
        """
        Rolling average of I/O operations per second read and written to this LUN.
        Range: [0..2^64-1]
        """
        return self._lun_iops
    @lun_iops.setter
    def lun_iops(self, val):
        if val != None:
            self.validate('lun_iops', val)
        self._lun_iops = val
    
    _target_wwpn = None
    @property
    def target_wwpn(self):
        """
        World Wide Port Name of target port providing the disk.
        """
        return self._target_wwpn
    @target_wwpn.setter
    def target_wwpn(self, val):
        if val != None:
            self.validate('target_wwpn', val)
        self._target_wwpn = val
    
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
    
    _vmdisk_hypervisor_area_name = None
    @property
    def vmdisk_hypervisor_area_name(self):
        """
        The name of the storage area where the vmdisk is physically located.
        For ESX this is the name of a datastore.
        """
        return self._vmdisk_hypervisor_area_name
    @vmdisk_hypervisor_area_name.setter
    def vmdisk_hypervisor_area_name(self, val):
        if val != None:
            self.validate('vmdisk_hypervisor_area_name', val)
        self._vmdisk_hypervisor_area_name = val
    
    _initiator_lun_in_use_count = None
    @property
    def initiator_lun_in_use_count(self):
        """
        Number of LUNs in the IN-USE state on this initiator.
        Range: [0..2^64-1]
        """
        return self._initiator_lun_in_use_count
    @initiator_lun_in_use_count.setter
    def initiator_lun_in_use_count(self, val):
        if val != None:
            self.validate('initiator_lun_in_use_count', val)
        self._initiator_lun_in_use_count = val
    
    _vmdisk_hypervisor_file_name = None
    @property
    def vmdisk_hypervisor_file_name(self):
        """
        The file name of the virtual disk used by the hypervisor.
        For ESX this is the name of the disk's vmdk file.
        Example is "myvm/myvm_1.vmdk"
        """
        return self._vmdisk_hypervisor_file_name
    @vmdisk_hypervisor_file_name.setter
    def vmdisk_hypervisor_file_name(self, val):
        if val != None:
            self.validate('vmdisk_hypervisor_file_name', val)
        self._vmdisk_hypervisor_file_name = val
    
    _path_quality = None
    @property
    def path_quality(self):
        """
        The percentage of the error threshold.
        0%     NO ERROR
        1-20%  LOW ERROR, available to load balancing and
        error retry code.
        21-99% MEDIUM ERROR, load balancing and error retry code
        will not switch to this path.
        100-?  HIGH_ERROR, Excessive errors EMS event will be logged
        Range: [0..2^32-1]
        """
        return self._path_quality
    @path_quality.setter
    def path_quality(self, val):
        if val != None:
            self.validate('path_quality', val)
        self._path_quality = val
    
    _initiator_port_speed = None
    @property
    def initiator_port_speed(self):
        """
        The speed that the initiator port has negotiated with its
        connected switch, or target port if direct attached.
        """
        return self._initiator_port_speed
    @initiator_port_speed.setter
    def initiator_port_speed(self, val):
        if val != None:
            self.validate('initiator_port_speed', val)
        self._initiator_port_speed = val
    
    _path_lun_in_use_count = None
    @property
    def path_lun_in_use_count(self):
        """
        Number of LUNs in the IN-USE state on this path.
        Range: [0..2^64-1]
        """
        return self._path_lun_in_use_count
    @path_lun_in_use_count.setter
    def path_lun_in_use_count(self, val):
        if val != None:
            self.validate('path_lun_in_use_count', val)
        self._path_lun_in_use_count = val
    
    _initiator_io_kbps = None
    @property
    def initiator_io_kbps(self):
        """
        Rolling average of kilobytes per second read and written over this initiator port.
        Range: [0..2^64-1]
        """
        return self._initiator_io_kbps
    @initiator_io_kbps.setter
    def initiator_io_kbps(self, val):
        if val != None:
            self.validate('initiator_io_kbps', val)
        self._initiator_io_kbps = val
    
    _path_iops = None
    @property
    def path_iops(self):
        """
        Rolling average of I/O operations per second read and written to this path.
        Range: [0..2^64-1]
        """
        return self._path_iops
    @path_iops.setter
    def path_iops(self, val):
        if val != None:
            self.validate('path_iops', val)
        self._path_iops = val
    
    _target_lun_in_use_count = None
    @property
    def target_lun_in_use_count(self):
        """
        Number of LUNs in the IN-USE state on this target port.
        Range: [0..2^64-1]
        """
        return self._target_lun_in_use_count
    @target_lun_in_use_count.setter
    def target_lun_in_use_count(self, val):
        if val != None:
            self.validate('target_lun_in_use_count', val)
        self._target_lun_in_use_count = val
    
    _target_port_access_state = None
    @property
    def target_port_access_state(self):
        """
        failover optimization type
        """
        return self._target_port_access_state
    @target_port_access_state.setter
    def target_port_access_state(self, val):
        if val != None:
            self.validate('target_port_access_state', val)
        self._target_port_access_state = val
    
    _lun_io_kbps = None
    @property
    def lun_io_kbps(self):
        """
        Rolling average of kilobytes per second read and written to this LUN.
        Range: [0..2^64-1]
        """
        return self._lun_io_kbps
    @lun_io_kbps.setter
    def lun_io_kbps(self, val):
        if val != None:
            self.validate('lun_io_kbps', val)
        self._lun_io_kbps = val
    
    _disk_port_name = None
    @property
    def disk_port_name(self):
        """
        Disk port name associated with this path.  This has
        the form &lt;attachment-style&gt;:&lt;disk-port&gt;, where
        &lt;attachment-style&gt; is either "FC" for FibreChannel,
        or "SA" for SAS, and &lt;disk-port&gt; is either
        "A" or "B".  Omitted for non-disk target.
        <p>
        Possible values:
        <ul>
        <li> "FC:A"
        <li> "FC:B"
        <li> "SA:A"
        <li> "SA:B"
        </ul>
        """
        return self._disk_port_name
    @disk_port_name.setter
    def disk_port_name(self, val):
        if val != None:
            self.validate('disk_port_name', val)
        self._disk_port_name = val
    
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
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        Disk's UID, as supplied by the hardware, used to uniquely identify this disk.
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    @staticmethod
    def get_api_name():
          return "disk-path-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'target-side-switch-port',
            'tpgn',
            'initiator-side-switch-port',
            'path-io-kbps',
            'lun-path-use-state',
            'preferred-target-port',
            'disk-name',
            'array-name',
            'disk-port',
            'initiator-iops',
            'vmdisk-device-id',
            'lun-number',
            'initiator-port',
            'node',
            'lun-iops',
            'target-wwpn',
            'path-link-errors',
            'vmdisk-hypervisor-area-name',
            'initiator-lun-in-use-count',
            'vmdisk-hypervisor-file-name',
            'path-quality',
            'initiator-port-speed',
            'path-lun-in-use-count',
            'initiator-io-kbps',
            'path-iops',
            'target-lun-in-use-count',
            'target-port-access-state',
            'lun-io-kbps',
            'disk-port-name',
            'target-iops',
            'target-io-kbps',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'target_side_switch_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'tpgn': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_side_switch_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'path_io_kbps': { 'class': int, 'is_list': False, 'required': 'required' },
            'lun_path_use_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'preferred_target_port': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'disk_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'array_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'initiator_iops': { 'class': int, 'is_list': False, 'required': 'required' },
            'vmdisk_device_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lun_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_port': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'lun_iops': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_wwpn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'path_link_errors': { 'class': int, 'is_list': False, 'required': 'required' },
            'vmdisk_hypervisor_area_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'initiator_lun_in_use_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'vmdisk_hypervisor_file_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'path_quality': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_port_speed': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'path_lun_in_use_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'initiator_io_kbps': { 'class': int, 'is_list': False, 'required': 'required' },
            'path_iops': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_lun_in_use_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_port_access_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'lun_io_kbps': { 'class': int, 'is_list': False, 'required': 'required' },
            'disk_port_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'target_iops': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_io_kbps': { 'class': int, 'is_list': False, 'required': 'required' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
