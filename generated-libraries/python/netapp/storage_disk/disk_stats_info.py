from netapp.netapp_object import NetAppObject

class DiskStatsInfo(NetAppObject):
    """
    Contains disk statistics.
    """
    
    _average_latency = None
    @property
    def average_latency(self):
        """
        Access time to disk in milliseconds.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._average_latency
    @average_latency.setter
    def average_latency(self, val):
        if val != None:
            self.validate('average_latency', val)
        self._average_latency = val
    
    _sectors_written = None
    @property
    def sectors_written(self):
        """
        Number of disk sectors written since system last
        booted, given in units of 'bytes-per-sector'.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._sectors_written
    @sectors_written.setter
    def sectors_written(self, val):
        if val != None:
            self.validate('sectors_written', val)
        self._sectors_written = val
    
    _disk_io_kbps = None
    @property
    def disk_io_kbps(self):
        """
        Rolling average of kilobytes per second read and written
        to this disk.  Omitted if excluded by
        'desired-attributes'.
        """
        return self._disk_io_kbps
    @disk_io_kbps.setter
    def disk_io_kbps(self, val):
        if val != None:
            self.validate('disk_io_kbps', val)
        self._disk_io_kbps = val
    
    _bytes_per_sector = None
    @property
    def bytes_per_sector(self):
        """
        Number of bytes per disk sector.  A sector
        count element, such as 'sectors-read' and
        'sectors-written', may be multipled by this
        value to convert to a byte count.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._bytes_per_sector
    @bytes_per_sector.setter
    def bytes_per_sector(self, val):
        if val != None:
            self.validate('bytes_per_sector', val)
        self._bytes_per_sector = val
    
    _disk_iops = None
    @property
    def disk_iops(self):
        """
        Rolling average of I/O operations per second read and
        written to this disk. 	Omitted if excluded by
        'desired-attributes'.
        """
        return self._disk_iops
    @disk_iops.setter
    def disk_iops(self, val):
        if val != None:
            self.validate('disk_iops', val)
        self._disk_iops = val
    
    _power_on_time_interval = None
    @property
    def power_on_time_interval(self):
        """
        Number of seconds the drive has been powered on.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._power_on_time_interval
    @power_on_time_interval.setter
    def power_on_time_interval(self, val):
        if val != None:
            self.validate('power_on_time_interval', val)
        self._power_on_time_interval = val
    
    _path_error_count = None
    @property
    def path_error_count(self):
        """
        The number of errors on this disk.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._path_error_count
    @path_error_count.setter
    def path_error_count(self, val):
        if val != None:
            self.validate('path_error_count', val)
        self._path_error_count = val
    
    _sectors_read = None
    @property
    def sectors_read(self):
        """
        Number of disk sectors read since system
        last booted, given in units of 'bytes-per-sector'.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._sectors_read
    @sectors_read.setter
    def sectors_read(self, val):
        if val != None:
            self.validate('sectors_read', val)
        self._sectors_read = val
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        Unique identifier of disk for this disk.
        Maximum length of 90 characters.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    @staticmethod
    def get_api_name():
          return "disk-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'average-latency',
            'sectors-written',
            'disk-io-kbps',
            'bytes-per-sector',
            'disk-iops',
            'power-on-time-interval',
            'path-error-count',
            'sectors-read',
            'disk-uid',
        ]
    
    def describe_properties(self):
        return {
            'average_latency': { 'class': int, 'is_list': False, 'required': 'optional' },
            'sectors_written': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_io_kbps': { 'class': int, 'is_list': False, 'required': 'optional' },
            'bytes_per_sector': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_iops': { 'class': int, 'is_list': False, 'required': 'optional' },
            'power_on_time_interval': { 'class': int, 'is_list': False, 'required': 'optional' },
            'path_error_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'sectors_read': { 'class': int, 'is_list': False, 'required': 'optional' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
