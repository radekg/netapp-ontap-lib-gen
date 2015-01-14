from netapp.netapp_object import NetAppObject

class LunInfo(NetAppObject):
    """
    Information of a LUN.
    """
    
    _comment = None
    @property
    def comment(self):
        """
        User-specified comment for the LUN.
        This field is unavailable when the LUN is in a snapshot or
        while the LUN fenced for a restore operation.
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _is_restore_inaccessible = None
    @property
    def is_restore_inaccessible(self):
        """
        If true, the LUN is fenced for I/O and management
        operations due to an ongoing restore operation. If
        false, the LUN is available for normal operations.
        """
        return self._is_restore_inaccessible
    @is_restore_inaccessible.setter
    def is_restore_inaccessible(self, val):
        if val != None:
            self.validate('is_restore_inaccessible', val)
        self._is_restore_inaccessible = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Serial number of the LUN.
        Prior to Data ONTAP 8.1 release, the serial number
        is a 12-character string formed
        of upper and lower-case letters, numbers, and slash (/)
        and hyphen (-) characters.
        Starting Data ONTAP 8.1 release, the serial number is a
        12-character string formed of upper and lower-case letters,
        numbers, and the characters /-#$%&*+<=>?[!]^~@ .
        This field is unavailable when the LUN is in a snapshot.
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _is_clone_autodelete_enabled = None
    @property
    def is_clone_autodelete_enabled(self):
        """
        "true" if the lun clone is allowed to be deleted by autodelete in try/disrupt mode.
        autodelete will be allowed to delete the lun clone in try/disrupt
        mode if configured.
        "false" otherwise. The lun clone will not be deleted by
        autodelete in try/disrupt mode if configured.
        """
        return self._is_clone_autodelete_enabled
    @is_clone_autodelete_enabled.setter
    def is_clone_autodelete_enabled(self, val):
        if val != None:
            self.validate('is_clone_autodelete_enabled', val)
        self._is_clone_autodelete_enabled = val
    
    _read_only = None
    @property
    def read_only(self):
        """
        "true" if the LUN is read only, "false" if read/write.
        This field is unavailable while the LUN is fenced for a restore
        operation.
        """
        return self._read_only
    @read_only.setter
    def read_only(self, val):
        if val != None:
            self.validate('read_only', val)
        self._read_only = val
    
    _size = None
    @property
    def size(self):
        """
        Size of this LUN in bytes in the active FS.
        This field is unavailable while the LUN is fenced for a restore
        operation.
        """
        return self._size
    @size.setter
    def size(self, val):
        if val != None:
            self.validate('size', val)
        self._size = val
    
    _staging = None
    @property
    def staging(self):
        """
        "true" if the LUN is a temporary staging LUN,
        "false" otherwise.
        """
        return self._staging
    @staging.setter
    def staging(self, val):
        if val != None:
            self.validate('staging', val)
        self._staging = val
    
    _block_size = None
    @property
    def block_size(self):
        """
        Disk block size of the LUN in bytes.
        This field is unavailable while the LUN is fenced for a restore
        operation.
        """
        return self._block_size
    @block_size.setter
    def block_size(self, val):
        if val != None:
            self.validate('block_size', val)
        self._block_size = val
    
    _suffix_size = None
    @property
    def suffix_size(self):
        """
        Size of the suffix stream for this LUN in bytes. This value is
        determined by the OS type of the LUN at creation time.
        This field is unavailable while the LUN is fenced for a restore
        operation.
        This field is available in Data ONTAP 8.1 and later.
        """
        return self._suffix_size
    @suffix_size.setter
    def suffix_size(self, val):
        if val != None:
            self.validate('suffix_size', val)
        self._suffix_size = val
    
    _device_text_id = None
    @property
    def device_text_id(self):
        """
        SCSI Peripheral Device Text Identifying Information
        returned in response to the SCSI command REPORT
        IDENTIFYING INFORMATION (INFORMATION TYPE 0000010b).
        Value is a free-form UTF-8 string between 1 and 255
        bytes in length. Only present if a Peripheral Device
        Text Identifying Information value has been set on
        the LUN.
        """
        return self._device_text_id
    @device_text_id.setter
    def device_text_id(self, val):
        if val != None:
            self.validate('device_text_id', val)
        self._device_text_id = val
    
    _backing_snapshot = None
    @property
    def backing_snapshot(self):
        """
        Path to the backing snapshot file for a LUN, if
        there is one.  Only returned if it has one.
        Note: This element is not returned for LUNs which
        are in snapshots.
        """
        return self._backing_snapshot
    @backing_snapshot.setter
    def backing_snapshot(self, val):
        if val != None:
            self.validate('backing_snapshot', val)
        self._backing_snapshot = val
    
    _prefix_size = None
    @property
    def prefix_size(self):
        """
        Size of the prefix stream for this LUN in bytes. This is either
        the default value for the OS type of the LUN or value specified
        in lun-create-by-size API.
        This field is unavailable while the LUN is fenced for a restore
        operation.
        This field is available in Data ONTAP 8.1 and later.
        """
        return self._prefix_size
    @prefix_size.setter
    def prefix_size(self, val):
        if val != None:
            self.validate('prefix_size', val)
        self._prefix_size = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver containing the LUN.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _size_used = None
    @property
    def size_used(self):
        """
        Number of bytes used by this LUN.
        This field is unavailable while the LUN is fenced for a restore
        operation.
        """
        return self._size_used
    @size_used.setter
    def size_used(self, val):
        if val != None:
            self.validate('size_used', val)
        self._size_used = val
    
    _alignment = None
    @property
    def alignment(self):
        """
        Alignment of the LUN. Possible values: "aligned",
        "misaligned", "partial_writes" or "indeterminate".
        """
        return self._alignment
    @alignment.setter
    def alignment(self, val):
        if val != None:
            self.validate('alignment', val)
        self._alignment = val
    
    _online = None
    @property
    def online(self):
        """
        State of the LUN, ("online" or "offline").
        "true" if online, "false" otherwise.
        """
        return self._online
    @online.setter
    def online(self, val):
        if val != None:
            self.validate('online', val)
        self._online = val
    
    _is_space_alloc_enabled = None
    @property
    def is_space_alloc_enabled(self):
        """
        Whether or not the LUN has space allocation enabled.
        This field is unavailable when the LUN is in a snapshot or
        while fenced for a restore operation.
        """
        return self._is_space_alloc_enabled
    @is_space_alloc_enabled.setter
    def is_space_alloc_enabled(self, val):
        if val != None:
            self.validate('is_space_alloc_enabled', val)
        self._is_space_alloc_enabled = val
    
    _device_id = None
    @property
    def device_id(self):
        """
        SCSI Peripheral Device Identifying Information returned
        in response to the vendor unique SCSI command
        GET DEV ID. Only present if a Peripheral Device
        Identifying Information	value appropriate for
        GET DEV ID has been set on the LUN.
        """
        return self._device_id
    @device_id.setter
    def device_id(self, val):
        if val != None:
            self.validate('device_id', val)
        self._device_id = val
    
    _volume = None
    @property
    def volume(self):
        """
        Name of the volume containing the LUN.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _multiprotocol_type = None
    @property
    def multiprotocol_type(self):
        """
        OS type of the LUN
        This field is unavailable while the LUN is fenced for a restore
        operation.
        """
        return self._multiprotocol_type
    @multiprotocol_type.setter
    def multiprotocol_type(self, val):
        if val != None:
            self.validate('multiprotocol_type', val)
        self._multiprotocol_type = val
    
    _share_state = None
    @property
    def share_state(self):
        """
        Share state of the LUN. Possible values: "all",
        "none", read", "unkown", "write".
        In the very rare case that the share state can not be
        determined, "unknown" is returned.
        """
        return self._share_state
    @share_state.setter
    def share_state(self, val):
        if val != None:
            self.validate('share_state', val)
        self._share_state = val
    
    _path = None
    @property
    def path(self):
        """
        Path of the LUN.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _is_space_reservation_enabled = None
    @property
    def is_space_reservation_enabled(self):
        """
        Whether or not the LUN has space reservation enabled.
        This field is unavailable when the LUN is in a snapshot or
        while fenced for a restore operation
        """
        return self._is_space_reservation_enabled
    @is_space_reservation_enabled.setter
    def is_space_reservation_enabled(self, val):
        if val != None:
            self.validate('is_space_reservation_enabled', val)
        self._is_space_reservation_enabled = val
    
    _class = None
    @property
    def class(self):
        """
        The class of the LUN. Possible values:
        <ul>
        <li>"regular" - The LUN is intended for normal blocks access,
        <li>"protocol_endpoint" - The LUN is a VMware vvol protocol endpoint,
        <li>"vvol" - The LUN is a VMware vvol data LUN.
        </ul>
        """
        return self._class
    @class.setter
    def class(self, val):
        if val != None:
            self.validate('class', val)
        self._class = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        Universal unique identifier (UUID) for the LUN.
        This field is unavailable when the LUN is in a snapshot.
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _creation_timestamp = None
    @property
    def creation_timestamp(self):
        """
        The time this LUN was created, in seconds since January 1, 1970.
        This field is unavailable when the LUN is in a snapshot or
        while the LUN fenced for a restore operation.
        """
        return self._creation_timestamp
    @creation_timestamp.setter
    def creation_timestamp(self, val):
        if val != None:
            self.validate('creation_timestamp', val)
        self._creation_timestamp = val
    
    _qos_policy_group = None
    @property
    def qos_policy_group(self):
        """
        QoS policy group defines measurable Service Level Objectives (SLOs)
        that apply to the storage objects with which the policy group is
        associated. This field is only present if the LUN is
        assigned to a QoS policy
        This field is available in Data ONTAP 8.2 and later.
        """
        return self._qos_policy_group
    @qos_policy_group.setter
    def qos_policy_group(self, val):
        if val != None:
            self.validate('qos_policy_group', val)
        self._qos_policy_group = val
    
    _device_binary_id = None
    @property
    def device_binary_id(self):
        """
        SCSI Peripheral Device Identifying Information returned
        in response to the SCSI command REPORT IDENTIFYING
        INFORMATION (INFORMATION TYPE 0000000b).
        Value is encoded as a hexadecimal string, representing
        1 to 64 bytes. Only present if a Peripheral Device
        Idendentifying Information value has been set on
        the LUN.
        """
        return self._device_binary_id
    @device_binary_id.setter
    def device_binary_id(self, val):
        if val != None:
            self.validate('device_binary_id', val)
        self._device_binary_id = val
    
    _qtree = None
    @property
    def qtree(self):
        """
        Name of the qtree containing the LUN.
        """
        return self._qtree
    @qtree.setter
    def qtree(self, val):
        if val != None:
            self.validate('qtree', val)
        self._qtree = val
    
    _mapped = None
    @property
    def mapped(self):
        """
        Whether or not the LUN is mapped to any initiators.
        "true" if mapped, "false" otherwise.
        This field is not applicable to LUNs where the class
        attribute is set to 'vvol'.
        """
        return self._mapped
    @mapped.setter
    def mapped(self, val):
        if val != None:
            self.validate('mapped', val)
        self._mapped = val
    
    _is_clone = None
    @property
    def is_clone(self):
        """
        "true" if the lun is a clone
        "false" otherwise.
        """
        return self._is_clone
    @is_clone.setter
    def is_clone(self, val):
        if val != None:
            self.validate('is_clone', val)
        self._is_clone = val
    
    _clone_backing_snapshot = None
    @property
    def clone_backing_snapshot(self):
        """
        Name of the backing snapshot of a LUN clone,
        if there is one.
        Only returned if the 'get-clone-backing-snapshot'
        option is specified and set to TRUE.
        The maximum string length is 256 characters.
        """
        return self._clone_backing_snapshot
    @clone_backing_snapshot.setter
    def clone_backing_snapshot(self, val):
        if val != None:
            self.validate('clone_backing_snapshot', val)
        self._clone_backing_snapshot = val
    
    @staticmethod
    def get_api_name():
          return "lun-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'is-restore-inaccessible',
            'serial-number',
            'is-clone-autodelete-enabled',
            'read-only',
            'size',
            'staging',
            'block-size',
            'suffix-size',
            'device-text-id',
            'backing-snapshot',
            'prefix-size',
            'vserver',
            'size-used',
            'alignment',
            'online',
            'is-space-alloc-enabled',
            'device-id',
            'volume',
            'multiprotocol-type',
            'share-state',
            'path',
            'is-space-reservation-enabled',
            'class',
            'uuid',
            'creation-timestamp',
            'qos-policy-group',
            'device-binary-id',
            'qtree',
            'mapped',
            'is-clone',
            'clone-backing-snapshot',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_restore_inaccessible': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_clone_autodelete_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'read_only': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'staging': { 'class': bool, 'is_list': False, 'required': 'required' },
            'block_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'suffix_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'device_text_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'backing_snapshot': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'prefix_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'size_used': { 'class': int, 'is_list': False, 'required': 'optional' },
            'alignment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'online': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_space_alloc_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'device_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'multiprotocol_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'share_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_space_reservation_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'class': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'creation_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'qos_policy_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'device_binary_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'qtree': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'mapped': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_clone': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'clone_backing_snapshot': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
