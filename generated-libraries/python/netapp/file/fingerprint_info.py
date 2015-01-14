from netapp.file.file_fingerprint_info import FileFingerprintInfo
from netapp.netapp_object import NetAppObject

class FingerprintInfo(NetAppObject):
    """
    Fingerprint information.
    """
    
    _fingerprint_scope = None
    @property
    def fingerprint_scope(self):
        """
        """
        return self._fingerprint_scope
    @fingerprint_scope.setter
    def fingerprint_scope(self, val):
        if val != None:
            self.validate('fingerprint_scope', val)
        self._fingerprint_scope = val
    
    _formatted_fingerprint_end_time = None
    @property
    def formatted_fingerprint_end_time(self):
        """
        End time of fingerprint computation in a human
        readable format
        <day> <month> <day of month> <hour>:<min>:<sec> <year>
        in GMT timezone.
        Time is taken out of system clock.
        """
        return self._formatted_fingerprint_end_time
    @formatted_fingerprint_end_time.setter
    def formatted_fingerprint_end_time(self, val):
        if val != None:
            self.validate('formatted_fingerprint_end_time', val)
        self._formatted_fingerprint_end_time = val
    
    _formatted_volume_expiry_date = None
    @property
    def formatted_volume_expiry_date(self):
        """
        Expiry date of the SnapLock volume in a
        human-readable format <day> <month> <day of month>
        <hour>:<min>:<sec> <year> in GMT timezone.
        A value of "infinite" indicates that the volume has
        an infinite expiry date.
        A value of "scan_in_progress" indicates that expiry
        date is not displayed since worm scan on the volume is
        in progress.
        A value of "no_expiry_date" indicates that expiry
        date is not displayed since the SnapLock volume has
        no WORM files and WORM snapshots.
        This field is not included if the volume is offline or
        the volume is regular volume.
        """
        return self._formatted_volume_expiry_date
    @formatted_volume_expiry_date.setter
    def formatted_volume_expiry_date(self, val):
        if val != None:
            self.validate('formatted_volume_expiry_date', val)
        self._formatted_volume_expiry_date = val
    
    _fingerprint_version = None
    @property
    def fingerprint_version(self):
        """
        Version of the fingerprint output format.
        """
        return self._fingerprint_version
    @fingerprint_version.setter
    def fingerprint_version(self, val):
        if val != None:
            self.validate('fingerprint_version', val)
        self._fingerprint_version = val
    
    _snaplock_system_compliance_clock = None
    @property
    def snaplock_system_compliance_clock(self):
        """
        If System Compliance Clock is initialized then time in
        seconds in the standard UNIX format (since 01/01/1970
        00:00:00) in GMT timezone.
        Range:[0..2^64-1].
        """
        return self._snaplock_system_compliance_clock
    @snaplock_system_compliance_clock.setter
    def snaplock_system_compliance_clock(self, val):
        if val != None:
            self.validate('snaplock_system_compliance_clock', val)
        self._snaplock_system_compliance_clock = val
    
    _fingerprint_end_time = None
    @property
    def fingerprint_end_time(self):
        """
        End time of fingerprint computation in seconds
        since January 1, 1970.
        Time is taken out of system clock.
        Range : [0..2^64-1].
        """
        return self._fingerprint_end_time
    @fingerprint_end_time.setter
    def fingerprint_end_time(self, val):
        if val != None:
            self.validate('fingerprint_end_time', val)
        self._fingerprint_end_time = val
    
    _volume_name = None
    @property
    def volume_name(self):
        """
        Name of the volume.
        """
        return self._volume_name
    @volume_name.setter
    def volume_name(self, val):
        if val != None:
            self.validate('volume_name', val)
        self._volume_name = val
    
    _volume_containing_aggregate = None
    @property
    def volume_containing_aggregate(self):
        """
        <b>Flexible</b> volumes only.
        The name of the aggregate in which the given
        flexible volume resides.
        """
        return self._volume_containing_aggregate
    @volume_containing_aggregate.setter
    def volume_containing_aggregate(self, val):
        if val != None:
            self.validate('volume_containing_aggregate', val)
        self._volume_containing_aggregate = val
    
    _metadata_files = None
    @property
    def metadata_files(self):
        """
        List of files and their fingerprint related information.
        """
        return self._metadata_files
    @metadata_files.setter
    def metadata_files(self, val):
        if val != None:
            self.validate('metadata_files', val)
        self._metadata_files = val
    
    _volume_type = None
    @property
    def volume_type(self):
        """
        The type of volume.
        Possible values: "flexible" for flexible volumes, and
        "traditional" for traditional volumes.
        """
        return self._volume_type
    @volume_type.setter
    def volume_type(self, val):
        if val != None:
            self.validate('volume_type', val)
        self._volume_type = val
    
    _volume_expiry_date = None
    @property
    def volume_expiry_date(self):
        """
        Expiry date of the SnapLock volume in
        seconds in the standard UNIX format
        (since 01/01/1970 00:00:00).
        Range:[0..2^64-1].
        This field is not included if
        1. Volume is non Snaplock volume, or
        2. Snaplock volume has an infinite expiry date, or
        3. Snaplock volume has no worm files or snapshots, or
        4. Snaplock volume has worm scanner in progress
        The volume expiry date can be in wraparound format.
        The wraparound format indicates that dates after
        01/19/2038 are mapped from 01/01/1970 - 12/31/2002 to
        01/19/2038 - 01/19/2071.
        """
        return self._volume_expiry_date
    @volume_expiry_date.setter
    def volume_expiry_date(self, val):
        if val != None:
            self.validate('volume_expiry_date', val)
        self._volume_expiry_date = val
    
    _formatted_snaplock_system_compliance_clock = None
    @property
    def formatted_snaplock_system_compliance_clock(self):
        """
        If System Compliance Clock is initialized then
        human readable time
        <day> <month> <day of month> <hour>:<min>:<sec> <year>
        in GMT timezone.
        A value of "not_initalized" indicates that System
        Compliance Clock has not been initialized.
        """
        return self._formatted_snaplock_system_compliance_clock
    @formatted_snaplock_system_compliance_clock.setter
    def formatted_snaplock_system_compliance_clock(self, val):
        if val != None:
            self.validate('formatted_snaplock_system_compliance_clock', val)
        self._formatted_snaplock_system_compliance_clock = val
    
    _fingerprint_start_time = None
    @property
    def fingerprint_start_time(self):
        """
        Start time of fingerprint computation in seconds
        since January 1, 1970.
        Time is taken out of system clock.
        Range : [0..2^64-1].
        """
        return self._fingerprint_start_time
    @fingerprint_start_time.setter
    def fingerprint_start_time(self, val):
        if val != None:
            self.validate('fingerprint_start_time', val)
        self._fingerprint_start_time = val
    
    _fingerprint_algorithm = None
    @property
    def fingerprint_algorithm(self):
        """
        """
        return self._fingerprint_algorithm
    @fingerprint_algorithm.setter
    def fingerprint_algorithm(self, val):
        if val != None:
            self.validate('fingerprint_algorithm', val)
        self._fingerprint_algorithm = val
    
    _filer_name = None
    @property
    def filer_name(self):
        """
        Name of the filer. If the filer name has not
        been written to the disks, this will not be returned.
        """
        return self._filer_name
    @filer_name.setter
    def filer_name(self, val):
        if val != None:
            self.validate('filer_name', val)
        self._filer_name = val
    
    _volume_uuid = None
    @property
    def volume_uuid(self):
        """
        Universal unique identifier (UUID) for the volume.
        """
        return self._volume_uuid
    @volume_uuid.setter
    def volume_uuid(self, val):
        if val != None:
            self.validate('volume_uuid', val)
        self._volume_uuid = val
    
    _formatted_fingerprint_start_time = None
    @property
    def formatted_fingerprint_start_time(self):
        """
        Start time of fingerprint computation in a human
        readable format
        <day> <month> <day of month> <hour>:<min>:<sec> <year>
        in GMT timezone.
        Time is taken out of system clock.
        """
        return self._formatted_fingerprint_start_time
    @formatted_fingerprint_start_time.setter
    def formatted_fingerprint_start_time(self, val):
        if val != None:
            self.validate('formatted_fingerprint_start_time', val)
        self._formatted_fingerprint_start_time = val
    
    _snaplock_volume_compliance_clock = None
    @property
    def snaplock_volume_compliance_clock(self):
        """
        Volume Compliance Clock time in seconds for the
        SnapLock volumes.
        The time is in the standard UNIX format (since 01/01/1970
        00:00:00) in GMT timezone.
        This field is not included for Non-SnapLock volumes.
        Range:[0..2^64-1].
        """
        return self._snaplock_volume_compliance_clock
    @snaplock_volume_compliance_clock.setter
    def snaplock_volume_compliance_clock(self, val):
        if val != None:
            self.validate('snaplock_volume_compliance_clock', val)
        self._snaplock_volume_compliance_clock = val
    
    _is_volume_expiry_date_wraparound = None
    @property
    def is_volume_expiry_date_wraparound(self):
        """
        True if the date represented in the field
        volume-expiry-date is a wraparound format.
        The wraparound format indicates that dates after
        01/19/2038 are mapped from 01/01/1970 - 12/31/2002 to
        01/19/2038 - 01/19/2071.
        The field is not included if volume-expiry-date is not
        included.
        """
        return self._is_volume_expiry_date_wraparound
    @is_volume_expiry_date_wraparound.setter
    def is_volume_expiry_date_wraparound(self, val):
        if val != None:
            self.validate('is_volume_expiry_date_wraparound', val)
        self._is_volume_expiry_date_wraparound = val
    
    _aggregate_uuid = None
    @property
    def aggregate_uuid(self):
        """
        Universal unique identifier (UUID) for the aggregate
        containing volume. The field is included for flexible
        volumes only.
        """
        return self._aggregate_uuid
    @aggregate_uuid.setter
    def aggregate_uuid(self, val):
        if val != None:
            self.validate('aggregate_uuid', val)
        self._aggregate_uuid = val
    
    _fingerprint_input_path = None
    @property
    def fingerprint_input_path(self):
        """
        Full path of the file to be fingerprinted.
        The value begins with /vol/<volumename>.
        """
        return self._fingerprint_input_path
    @fingerprint_input_path.setter
    def fingerprint_input_path(self, val):
        if val != None:
            self.validate('fingerprint_input_path', val)
        self._fingerprint_input_path = val
    
    _filer_id = None
    @property
    def filer_id(self):
        """
        ID (NVRAM ID) of owner.
        """
        return self._filer_id
    @filer_id.setter
    def filer_id(self, val):
        if val != None:
            self.validate('filer_id', val)
        self._filer_id = val
    
    _volume_snaplock_type = None
    @property
    def volume_snaplock_type(self):
        """
        The type of the Snaplock volume.
        It is present for Snaplock volumes only.
        Possible values: "compliance" or "enterprise"
        """
        return self._volume_snaplock_type
    @volume_snaplock_type.setter
    def volume_snaplock_type(self, val):
        if val != None:
            self.validate('volume_snaplock_type', val)
        self._volume_snaplock_type = val
    
    _formatted_snaplock_volume_compliance_clock = None
    @property
    def formatted_snaplock_volume_compliance_clock(self):
        """
        Volume Compliance Clock time for SnapLock volumes in
        human readable format
        <day> <month> <day of month> <hour>:<min>:<sec> <year>
        in GMT timezone.
        This field is not included for Non-SnapLock volumes.
        """
        return self._formatted_snaplock_volume_compliance_clock
    @formatted_snaplock_volume_compliance_clock.setter
    def formatted_snaplock_volume_compliance_clock(self, val):
        if val != None:
            self.validate('formatted_snaplock_volume_compliance_clock', val)
        self._formatted_snaplock_volume_compliance_clock = val
    
    _snaplock_license = None
    @property
    def snaplock_license(self):
        """
        Type of SnapLock license installed.
        Possible values: "compliance" that applies to SnapLock
        compliance restrictions and "enterprise" that applies
        to SnapLock enterprise restrictions and value
        "compliance and enterprise" if there are both licenses
        installed. This field is not included if SnapLock
        license is not installed.
        """
        return self._snaplock_license
    @snaplock_license.setter
    def snaplock_license(self, val):
        if val != None:
            self.validate('snaplock_license', val)
        self._snaplock_license = val
    
    @staticmethod
    def get_api_name():
          return "fingerprint-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'fingerprint-scope',
            'formatted-fingerprint-end-time',
            'formatted-volume-expiry-date',
            'fingerprint-version',
            'snaplock-system-compliance-clock',
            'fingerprint-end-time',
            'volume-name',
            'volume-containing-aggregate',
            'metadata-files',
            'volume-type',
            'volume-expiry-date',
            'formatted-snaplock-system-compliance-clock',
            'fingerprint-start-time',
            'fingerprint-algorithm',
            'filer-name',
            'volume-uuid',
            'formatted-fingerprint-start-time',
            'snaplock-volume-compliance-clock',
            'is-volume-expiry-date-wraparound',
            'aggregate-uuid',
            'fingerprint-input-path',
            'filer-id',
            'volume-snaplock-type',
            'formatted-snaplock-volume-compliance-clock',
            'snaplock-license',
        ]
    
    def describe_properties(self):
        return {
            'fingerprint_scope': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'formatted_fingerprint_end_time': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'formatted_volume_expiry_date': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fingerprint_version': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'snaplock_system_compliance_clock': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fingerprint_end_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'volume_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume_containing_aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'metadata_files': { 'class': FileFingerprintInfo, 'is_list': True, 'required': 'required' },
            'volume_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume_expiry_date': { 'class': int, 'is_list': False, 'required': 'optional' },
            'formatted_snaplock_system_compliance_clock': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fingerprint_start_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'fingerprint_algorithm': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'filer_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume_uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'formatted_fingerprint_start_time': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'snaplock_volume_compliance_clock': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_volume_expiry_date_wraparound': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'aggregate_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'fingerprint_input_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'filer_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume_snaplock_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'formatted_snaplock_volume_compliance_clock': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snaplock_license': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
