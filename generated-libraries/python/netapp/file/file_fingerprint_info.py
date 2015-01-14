from netapp.netapp_object import NetAppObject

class FileFingerprintInfo(NetAppObject):
    """
    Fingerprint information about single file.
    """
    
    _is_changed_time_wraparound = None
    @property
    def is_changed_time_wraparound(self):
        """
        This  field is included for WORM files when
        changed-time is in wraparound format.
        This field is true if the date represented in
        changed-time is in wraparound format and
        false if changed-time is not is not in wraparound
        format.
        The wraparound format indicates that dates
        after 01/19/2038 are mapped from
        01/01/1970 - 12/31/2002 to
        01/19/2038 - 01/19/2071.
        This field is not included for regular files.
        """
        return self._is_changed_time_wraparound
    @is_changed_time_wraparound.setter
    def is_changed_time_wraparound(self, val):
        if val != None:
            self.validate('is_changed_time_wraparound', val)
        self._is_changed_time_wraparound = val
    
    _formatted_creation_time = None
    @property
    def formatted_creation_time(self):
        """
        Creation time of the file formatted in a
        human-readable format
        <day> <month> <day of month> <hour>:<min>:<sec>
        <year> in GMT timezone.
        """
        return self._formatted_creation_time
    @formatted_creation_time.setter
    def formatted_creation_time(self, val):
        if val != None:
            self.validate('formatted_creation_time', val)
        self._formatted_creation_time = val
    
    _changed_time = None
    @property
    def changed_time(self):
        """
        Last changed time of the file attributes in
        seconds in the standard UNIX format since
        January 1, 1970 00:00:00.
        For WORM files last change time for file
        attributes occurs when file is committed to
        WORM. Time is taken out of system clock for
        regular files and time is taken out of
        Compliance Clock when file is committed to worm.
        The changed-time can be in wraparound format for
        WORM files. The flag is-changed-time-wraparound
        indicates that changed time is in the
        wraparound format.
        The wraparound format indicates that dates
        after 01/19/2038 are mapped from
        01/01/1970 - 12/31/2002 to
        01/19/2038 - 01/19/2071
        Range : [0..2^64-1]
        """
        return self._changed_time
    @changed_time.setter
    def changed_time(self, val):
        if val != None:
            self.validate('changed_time', val)
        self._changed_time = val
    
    _data_fingerprint = None
    @property
    def data_fingerprint(self):
        """
        The digest value of data of the file.
        The fingerprint is base64 encoded.
        This field is not included if scope is
        'metadata_only'.
        """
        return self._data_fingerprint
    @data_fingerprint.setter
    def data_fingerprint(self, val):
        if val != None:
            self.validate('data_fingerprint', val)
        self._data_fingerprint = val
    
    _modified_time = None
    @property
    def modified_time(self):
        """
        Last modification time of the file in seconds
        in the standard UNIX format since
        January 1, 1970 00:00:00.
        Time is taken out of system clock.
        Range : [0..2^64-1]
        """
        return self._modified_time
    @modified_time.setter
    def modified_time(self, val):
        if val != None:
            self.validate('modified_time', val)
        self._modified_time = val
    
    _is_wraparound = None
    @property
    def is_wraparound(self):
        """
        True if the date represented in retention-time
        is in wraparound format.
        The wraparound format indicates that dates
        after 01/19/2038 are mapped from
        01/01/1970 - 12/31/2002 to
        01/19/2038 - 01/19/2071.
        This field is not included if retention-time
        is not included.
        """
        return self._is_wraparound
    @is_wraparound.setter
    def is_wraparound(self, val):
        if val != None:
            self.validate('is_wraparound', val)
        self._is_wraparound = val
    
    _metadata_fingerprint = None
    @property
    def metadata_fingerprint(self):
        """
        The digest value of metadata of the file
        The metadata fingerprint is calculated for
        file size, file ctime, file mtime, file
        crtime, file retention time, file uid, gid
        and file type.
        The fingerprint is base64 encoded.
        This field is not included if scope is
        'data_only'.
        """
        return self._metadata_fingerprint
    @metadata_fingerprint.setter
    def metadata_fingerprint(self, val):
        if val != None:
            self.validate('metadata_fingerprint', val)
        self._metadata_fingerprint = val
    
    _file_size = None
    @property
    def file_size(self):
        """
        The size of the file in bytes.
        Range : [0..2^64-1].
        """
        return self._file_size
    @file_size.setter
    def file_size(self, val):
        if val != None:
            self.validate('file_size', val)
        self._file_size = val
    
    _retention_time = None
    @property
    def retention_time(self):
        """
        Retention time of the file in seconds in the
        standard UNIX format since January 1, 1970
        00:00:00.
        This field is not included for regular files,
        files on Non-Snaplock volumes and files with
        infinite retention.
        The flag is-wraparound indicates that retention
        is in the wraparound format.
        The wraparound format indicates that dates
        after 01/19/2038 are mapped from
        01/01/1970 - 12/31/2002 to
        01/19/2038 - 01/19/2071
        The time is taken out of Compliance Clock.
        Range : [0..2^64-1]
        """
        return self._retention_time
    @retention_time.setter
    def retention_time(self, val):
        if val != None:
            self.validate('retention_time', val)
        self._retention_time = val
    
    _fileid = None
    @property
    def fileid(self):
        """
        A unique number within filesystem identifying
        the file for fingerprint.
        Range : [0..2^31-1]
        """
        return self._fileid
    @fileid.setter
    def fileid(self, val):
        if val != None:
            self.validate('fileid', val)
        self._fileid = val
    
    _creation_time = None
    @property
    def creation_time(self):
        """
        Creation time of the file in seconds in the
        standard UNIX format since January 1, 1970
        00:00:00.
        Time is taken out of system clock.
        Range : [0..2^64-1]
        """
        return self._creation_time
    @creation_time.setter
    def creation_time(self, val):
        if val != None:
            self.validate('creation_time', val)
        self._creation_time = val
    
    _access_time = None
    @property
    def access_time(self):
        """
        Last access time of the file attributes in
        seconds in the standard UNIX format since
        January 1, 1970 00:00:00.
        The field is included for regular files and
        files on Non-Snaplock volumes.
        Time is taken out of system clock.
        Range : [0..2^64-1]
        """
        return self._access_time
    @access_time.setter
    def access_time(self, val):
        if val != None:
            self.validate('access_time', val)
        self._access_time = val
    
    _formatted_modified_time = None
    @property
    def formatted_modified_time(self):
        """
        Last modification time of the file formatted
        in a human-readable format
        <day> <month> <day of month> <hour>:<min>:<sec>
        <year> in GMT timezone.
        """
        return self._formatted_modified_time
    @formatted_modified_time.setter
    def formatted_modified_time(self, val):
        if val != None:
            self.validate('formatted_modified_time', val)
        self._formatted_modified_time = val
    
    _owner_sid = None
    @property
    def owner_sid(self):
        """
        The owner SID of the file. This field is
        included in the case when file has NTFS
        security style.
        """
        return self._owner_sid
    @owner_sid.setter
    def owner_sid(self, val):
        if val != None:
            self.validate('owner_sid', val)
        self._owner_sid = val
    
    _path = None
    @property
    def path(self):
        """
        Full path of the file that is fingerprinted.
        The value begins with /vol/<volumename>.
        """
        return self._path
    @path.setter
    def path(self, val):
        if val != None:
            self.validate('path', val)
        self._path = val
    
    _formatted_access_time = None
    @property
    def formatted_access_time(self):
        """
        Last access time of the file formatted in a
        human-readable format
        <day> <month> <day of month> <hour>:<min>:<sec>
        <year> in GMT timezone.
        The field is included for regular files and
        files on Non-Snaplock volumes.
        """
        return self._formatted_access_time
    @formatted_access_time.setter
    def formatted_access_time(self, val):
        if val != None:
            self.validate('formatted_access_time', val)
        self._formatted_access_time = val
    
    _fsid = None
    @property
    def fsid(self):
        """
        Filesystem ID.
        Range : [0..2^31-1]
        """
        return self._fsid
    @fsid.setter
    def fsid(self, val):
        if val != None:
            self.validate('fsid', val)
        self._fsid = val
    
    _group_id = None
    @property
    def group_id(self):
        """
        The integer id of the group owner of the file.
        Range : [0..2^31-1]
        """
        return self._group_id
    @group_id.setter
    def group_id(self, val):
        if val != None:
            self.validate('group_id', val)
        self._group_id = val
    
    _formatted_retention_time = None
    @property
    def formatted_retention_time(self):
        """
        Expiry date of the worm file formatted in a
        human-readable format. This takes care of
        wraparound dates and prints the expiry date
        of the file in the format
        <day> <month> <day of month> <hour>:<min>:<sec>
        <year> in GMT timezone.
        A value of "infinite" indicates that this file
        has infinite retention time. This field is not
        included for regular files and files on
        Non-Snaplock volumes.
        """
        return self._formatted_retention_time
    @formatted_retention_time.setter
    def formatted_retention_time(self, val):
        if val != None:
            self.validate('formatted_retention_time', val)
        self._formatted_retention_time = val
    
    _formatted_changed_time = None
    @property
    def formatted_changed_time(self):
        """
        Last changed time of the file formatted in a
        human-readable format
        <day> <month> <day of month> <hour>:<min>:<sec>
        <year> in GMT timezone.
        """
        return self._formatted_changed_time
    @formatted_changed_time.setter
    def formatted_changed_time(self, val):
        if val != None:
            self.validate('formatted_changed_time', val)
        self._formatted_changed_time = val
    
    _owner_id = None
    @property
    def owner_id(self):
        """
        The integer id of the owner of the file.
        Range : [0..2^31-1]
        """
        return self._owner_id
    @owner_id.setter
    def owner_id(self, val):
        if val != None:
            self.validate('owner_id', val)
        self._owner_id = val
    
    _file_type = None
    @property
    def file_type(self):
        """
        Type of the file.
        Possible values: "worm", "worm_appendable",
        "worm_log"
        and "regular".
        """
        return self._file_type
    @file_type.setter
    def file_type(self, val):
        if val != None:
            self.validate('file_type', val)
        self._file_type = val
    
    @staticmethod
    def get_api_name():
          return "file-fingerprint-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-changed-time-wraparound',
            'formatted-creation-time',
            'changed-time',
            'data-fingerprint',
            'modified-time',
            'is-wraparound',
            'metadata-fingerprint',
            'file-size',
            'retention-time',
            'fileid',
            'creation-time',
            'access-time',
            'formatted-modified-time',
            'owner-sid',
            'path',
            'formatted-access-time',
            'fsid',
            'group-id',
            'formatted-retention-time',
            'formatted-changed-time',
            'owner-id',
            'file-type',
        ]
    
    def describe_properties(self):
        return {
            'is_changed_time_wraparound': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'formatted_creation_time': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'changed_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'data_fingerprint': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'modified_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_wraparound': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'metadata_fingerprint': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'retention_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fileid': { 'class': int, 'is_list': False, 'required': 'required' },
            'creation_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'access_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'formatted_modified_time': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'owner_sid': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'formatted_access_time': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'fsid': { 'class': int, 'is_list': False, 'required': 'required' },
            'group_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'formatted_retention_time': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'formatted_changed_time': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'owner_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'file_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
