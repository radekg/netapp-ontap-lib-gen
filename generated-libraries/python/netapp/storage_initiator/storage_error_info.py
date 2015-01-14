from netapp.netapp_object import NetAppObject

class StorageErrorInfo(NetAppObject):
    """
    Contains error messages associated with back end array/shelf/LUNs.
    """
    
    _node = None
    @property
    def node(self):
        """
        The nodename reporting the disk or array lun with the error.
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _error_id = None
    @property
    def error_id(self):
        """
        A unique ID for each error returned.  ID is unique
        on a per API call basis only.
        Range: [0..2^32-1]
        """
        return self._error_id
    @error_id.setter
    def error_id(self, val):
        if val != None:
            self.validate('error_id', val)
        self._error_id = val
    
    _lun_serial_number = None
    @property
    def lun_serial_number(self):
        """
        The serial number of the lun the error occurs on, blank if the error is not lun related.
        """
        return self._lun_serial_number
    @lun_serial_number.setter
    def lun_serial_number(self, val):
        if val != None:
            self.validate('lun_serial_number', val)
        self._lun_serial_number = val
    
    _error_text = None
    @property
    def error_text(self):
        """
        A description of the error being reported.
        """
        return self._error_text
    @error_text.setter
    def error_text(self, val):
        if val != None:
            self.validate('error_text', val)
        self._error_text = val
    
    _disk_name = None
    @property
    def disk_name(self):
        """
        The name of the disk or array lun this error information is for.
        """
        return self._disk_name
    @disk_name.setter
    def disk_name(self, val):
        if val != None:
            self.validate('disk_name', val)
        self._disk_name = val
    
    _error_type = None
    @property
    def error_type(self):
        """
        Enum describing type of error.
        Range: [0..2^32-1]
        1. Redundancy error, less than two paths to a disk.
        2. Redundancy error, device is only accessible
        via a single fault domain, all paths go into
        the same target port group.
        3. Device is a control LUN.
        4. This LUN has non WAFL data on it, and
        is write protected.
        5. LUN too large, A LUN has been detected that
        is larger than the maximum size supported.
        6. LUN too small, A LUN has been detected that
        is smaller than the minimum size supported.
        7. Invalid Block Size, A LUN has been detected
        that has an unsupported block size.
        8. A target port is accessable via multiple
        HBAs but the device to LUN id mappings aren't
        the same.
        9. A device is presented at different LUN ids on
        different ports.
        10. Multiple failover mode policies detected
        11. Unknown array LUN
        12. Data ONTAP(R) LUN
        """
        return self._error_type
    @error_type.setter
    def error_type(self, val):
        if val != None:
            self.validate('error_type', val)
        self._error_type = val
    
    _array_name = None
    @property
    def array_name(self):
        """
        Name of the array/shelf with the configuration error.
        """
        return self._array_name
    @array_name.setter
    def array_name(self, val):
        if val != None:
            self.validate('array_name', val)
        self._array_name = val
    
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
          return "storage-error-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'error-id',
            'lun-serial-number',
            'error-text',
            'disk-name',
            'error-type',
            'array-name',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'error_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'lun_serial_number': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'error_text': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'error_type': { 'class': int, 'is_list': False, 'required': 'required' },
            'array_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
