from netapp.storage_disk.vmdisk_backing_info import VmdiskBackingInfo
from netapp.disk.storage_ssd_info import StorageSsdInfo
from netapp.netapp_object import NetAppObject

class DiskInventoryInfo(NetAppObject):
    """
    Disk inventory info.
    """
    
    _carrier_id = None
    @property
    def carrier_id(self):
        """
        Unique identifier of the disk carrier. Maximum length
        of 34 characters. It is not returned if
        is-multidisk-carrier is set to false.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._carrier_id
    @carrier_id.setter
    def carrier_id(self, val):
        if val != None:
            self.validate('carrier_id', val)
        self._carrier_id = val
    
    _import_in_progress = None
    @property
    def import_in_progress(self):
        """
        For array LUNs marked with container-type of foreign,
        this value indicates when data is actively being
        imported from this disk. Omitted if excluded
        by 'desired-attributes'.
        """
        return self._import_in_progress
    @import_in_progress.setter
    def import_in_progress(self, val):
        if val != None:
            self.validate('import_in_progress', val)
        self._import_in_progress = val
    
    _grown_defect_list_count = None
    @property
    def grown_defect_list_count(self):
        """
        Number of entries in the drive's grown defect list.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._grown_defect_list_count
    @grown_defect_list_count.setter
    def grown_defect_list_count(self, val):
        if val != None:
            self.validate('grown_defect_list_count', val)
        self._grown_defect_list_count = val
    
    _media_scrub_count = None
    @property
    def media_scrub_count(self):
        """
        Number of times media has been scrubbed since controller
        last powered on.  Omitted if not available.
        """
        return self._media_scrub_count
    @media_scrub_count.setter
    def media_scrub_count(self, val):
        if val != None:
            self.validate('media_scrub_count', val)
        self._media_scrub_count = val
    
    _is_multidisk_carrier = None
    @property
    def is_multidisk_carrier(self):
        """
        True if the disk is in a carrier which contains more than
        one disk.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._is_multidisk_carrier
    @is_multidisk_carrier.setter
    def is_multidisk_carrier(self, val):
        if val != None:
            self.validate('is_multidisk_carrier', val)
        self._is_multidisk_carrier = val
    
    _bytes_per_sector = None
    @property
    def bytes_per_sector(self):
        """
        Number of bytes per disk sector.  A sector
        count element, such as 'capacity-sectors' and
        'right-size-sectors', may be multiplied
        by this value to convert to a byte count.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._bytes_per_sector
    @bytes_per_sector.setter
    def bytes_per_sector(self, val):
        if val != None:
            self.validate('bytes_per_sector', val)
        self._bytes_per_sector = val
    
    _media_scrub_last_done_time_interval = None
    @property
    def media_scrub_last_done_time_interval(self):
        """
        Number of seconds since a media scrub last completed.
        Omitted if not available.
        """
        return self._media_scrub_last_done_time_interval
    @media_scrub_last_done_time_interval.setter
    def media_scrub_last_done_time_interval(self, val):
        if val != None:
            self.validate('media_scrub_last_done_time_interval', val)
        self._media_scrub_last_done_time_interval = val
    
    _serial_number = None
    @property
    def serial_number(self):
        """
        Disk serial number.  Maximum length of 129
        characters.  Omitted if excluded by 'desired-attributes'.
        """
        return self._serial_number
    @serial_number.setter
    def serial_number(self, val):
        if val != None:
            self.validate('serial_number', val)
        self._serial_number = val
    
    _right_size_sectors = None
    @property
    def right_size_sectors(self):
        """
        Number of usable disk sectors that remain after
        subtracting the right-size adjustment for this
        disk.  Given in units of 'bytes-per-sector'.
        Omitted if information is unavailable, or if
        excluded by 'desired-attributes'.
        """
        return self._right_size_sectors
    @right_size_sectors.setter
    def right_size_sectors(self, val):
        if val != None:
            self.validate('right_size_sectors', val)
        self._right_size_sectors = val
    
    _is_foreign = None
    @property
    def is_foreign(self):
        """
        Indicates an array LUN has been designated as a foreign LUN
        and cannot be assigned. Omitted if excluded
        by 'desired-attributes'.
        """
        return self._is_foreign
    @is_foreign.setter
    def is_foreign(self, val):
        if val != None:
            self.validate('is_foreign', val)
        self._is_foreign = val
    
    _firmware_revision = None
    @property
    def firmware_revision(self):
        """
        Firmware revision of disk.  The format of the
        firmware revision  will vary depending on the
        type of disk and its vendor.  Omitted if excluded
        by 'desired-attributes'.
        """
        return self._firmware_revision
    @firmware_revision.setter
    def firmware_revision(self, val):
        if val != None:
            self.validate('firmware_revision', val)
        self._firmware_revision = val
    
    _rpm = None
    @property
    def rpm(self):
        """
        Rotational speed in revolutions per minute.
        Possible values are: 5400, 7200, 10000, and 15000.
        Omitted if information is unavailable, if rpm does
        not apply to this 'disk-type', or if excluded by
        'desired-attributes'.
        """
        return self._rpm
    @rpm.setter
    def rpm(self, val):
        if val != None:
            self.validate('rpm', val)
        self._rpm = val
    
    _vmdisk_backing_info = None
    @property
    def vmdisk_backing_info(self):
        """
        Backing info block for virtual machine disks.
        """
        return self._vmdisk_backing_info
    @vmdisk_backing_info.setter
    def vmdisk_backing_info(self, val):
        if val != None:
            self.validate('vmdisk_backing_info', val)
        self._vmdisk_backing_info = val
    
    _shelf_bay = None
    @property
    def shelf_bay(self):
        """
        Disk shelf bay, if it can be determined.
        Omitted if Shelf Enclosure Service is not enabled for
        this device, information is unavailable, or
        excluded by 'desired-attributes'.
        """
        return self._shelf_bay
    @shelf_bay.setter
    def shelf_bay(self, val):
        if val != None:
            self.validate('shelf_bay', val)
        self._shelf_bay = val
    
    _is_dynamically_qualified = None
    @property
    def is_dynamically_qualified(self):
        """
        True if the drive was dynamically qualified.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._is_dynamically_qualified
    @is_dynamically_qualified.setter
    def is_dynamically_qualified(self, val):
        if val != None:
            self.validate('is_dynamically_qualified', val)
        self._is_dynamically_qualified = val
    
    _disk_type = None
    @property
    def disk_type(self):
        """
        Disk interface type.  Omitted if excluded by
        'desired-attributes'.
        <p>
        Possible values:
        <ul>
        <li> "ATA"
        <li> "BSAS"
        <li> "EATA"
        <li> "FCAL"
        <li> "LUN"
        <li> "MSATA"
        <li> "SAS"
        <li> "SATA"
        <li> "SCSI"
        <li> "SSD"
        <li> "XATA"
        <li> "XSAS"
        <li> "FSAS"
        <li> "unknown"
        </ul>
        """
        return self._disk_type
    @disk_type.setter
    def disk_type(self, val):
        if val != None:
            self.validate('disk_type', val)
        self._disk_type = val
    
    _vendor = None
    @property
    def vendor(self):
        """
        Vendor of this disk.
        Omitted if excluded by 	'desired-attributes'.
        """
        return self._vendor
    @vendor.setter
    def vendor(self, val):
        if val != None:
            self.validate('vendor', val)
        self._vendor = val
    
    _checksum_compatibility = None
    @property
    def checksum_compatibility(self):
        """
        An indication of the checksum types that this
        disk is capable of supporting.  Each possible
        return value represents one or more checksum
        types. Omitted if not available or if excluded
        by 'desired-attributes'.
        <p>
        Starting in Data ONTAP 8.1, "zoned/block" is
        no longer supported.
        <p>
        Possible values:
        <ul>
        <li> "advanced_zoned"           - Supports advanced zoned
        checksum.
        <li> "block"                    - Supports block checksum.
        <li> "none"                     - No checksum support.
        <li> "zoned/advanced_zoned" - Supports zoned and
        advanced zoned checksum.
        </ul>
        """
        return self._checksum_compatibility
    @checksum_compatibility.setter
    def checksum_compatibility(self, val):
        if val != None:
            self.validate('checksum_compatibility', val)
        self._checksum_compatibility = val
    
    _shelf = None
    @property
    def shelf(self):
        """
        Disk shelf, if it can be determined.
        Omitted if Shelf Enclosure Service is not enabled for
        this device, information is unavailable, or
        excluded by 'desired-attributes'.
        """
        return self._shelf
    @shelf.setter
    def shelf(self, val):
        if val != None:
            self.validate('shelf', val)
        self._shelf = val
    
    _capacity_sectors = None
    @property
    def capacity_sectors(self):
        """
        Total number of disk sectors on this disk,
        given in units of 'bytes-per-sector'.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._capacity_sectors
    @capacity_sectors.setter
    def capacity_sectors(self, val):
        if val != None:
            self.validate('capacity_sectors', val)
        self._capacity_sectors = val
    
    _health_monitor_time_interval = None
    @property
    def health_monitor_time_interval(self):
        """
        Number of seconds we have been keeping track of errors
        from storage health monitor (SHM).  Omitted if
        excluded by 'desired-attributes'.
        """
        return self._health_monitor_time_interval
    @health_monitor_time_interval.setter
    def health_monitor_time_interval(self, val):
        if val != None:
            self.validate('health_monitor_time_interval', val)
        self._health_monitor_time_interval = val
    
    _storage_ssd_info = None
    @property
    def storage_ssd_info(self):
        """
        solid state device specific lifecycle data
        Omitted if 'disk-type' is not "SSD", or if excluded
        by 'desired-attributes'.
        """
        return self._storage_ssd_info
    @storage_ssd_info.setter
    def storage_ssd_info(self, val):
        if val != None:
            self.validate('storage_ssd_info', val)
        self._storage_ssd_info = val
    
    _carrier_serialno = None
    @property
    def carrier_serialno(self):
        """
        Unique serial number of the disk carrier. Maximum length
        of 17 characters. It is not returned if
        is-multidisk-carrier is set to false.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._carrier_serialno
    @carrier_serialno.setter
    def carrier_serialno(self, val):
        if val != None:
            self.validate('carrier_serialno', val)
        self._carrier_serialno = val
    
    _model = None
    @property
    def model(self):
        """
        Disk model string.  Omitted if excluded by
        'desired-attributes'.
        """
        return self._model
    @model.setter
    def model(self, val):
        if val != None:
            self.validate('model', val)
        self._model = val
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        Disk unique identifier.  Maximum length of 90
        characters.  Omitted if excluded by
        desired-attributes'.
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    @staticmethod
    def get_api_name():
          return "disk-inventory-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'carrier-id',
            'import-in-progress',
            'grown-defect-list-count',
            'media-scrub-count',
            'is-multidisk-carrier',
            'bytes-per-sector',
            'media-scrub-last-done-time-interval',
            'serial-number',
            'right-size-sectors',
            'is-foreign',
            'firmware-revision',
            'rpm',
            'vmdisk-backing-info',
            'shelf-bay',
            'is-dynamically-qualified',
            'disk-type',
            'vendor',
            'checksum-compatibility',
            'shelf',
            'capacity-sectors',
            'health-monitor-time-interval',
            'storage-ssd-info',
            'carrier-serialno',
            'model',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'carrier_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'import_in_progress': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'grown_defect_list_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'media_scrub_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_multidisk_carrier': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'bytes_per_sector': { 'class': int, 'is_list': False, 'required': 'optional' },
            'media_scrub_last_done_time_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'right_size_sectors': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_foreign': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'firmware_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'rpm': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vmdisk_backing_info': { 'class': VmdiskBackingInfo, 'is_list': False, 'required': 'optional' },
            'shelf_bay': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_dynamically_qualified': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'disk_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vendor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'checksum_compatibility': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'shelf': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'capacity_sectors': { 'class': int, 'is_list': False, 'required': 'optional' },
            'health_monitor_time_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'storage_ssd_info': { 'class': StorageSsdInfo, 'is_list': False, 'required': 'optional' },
            'carrier_serialno': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'model': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
