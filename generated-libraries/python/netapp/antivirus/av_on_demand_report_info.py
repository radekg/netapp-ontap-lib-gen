from netapp.netapp_object import NetAppObject

class AvOnDemandReportInfo(NetAppObject):
    """
    on demand report
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
    
    _file_scanned = None
    @property
    def file_scanned(self):
        """
        This parameter specifies the specified number of files
        were scanned.
        Attributes: non-creatable, non-modifiable
        """
        return self._file_scanned
    @file_scanned.setter
    def file_scanned(self, val):
        if val != None:
            self.validate('file_scanned', val)
        self._file_scanned = val
    
    _scan_failed = None
    @property
    def scan_failed(self):
        """
        This parameter specifies the number of files failed to be
        successfully scanned.
        Attributes: non-creatable, non-modifiable
        """
        return self._scan_failed
    @scan_failed.setter
    def scan_failed(self, val):
        if val != None:
            self.validate('scan_failed', val)
        self._scan_failed = val
    
    _scan_success = None
    @property
    def scan_success(self):
        """
        This parameter specifies the specified number of files
        were successfully scanned
        Attributes: non-creatable, non-modifiable
        """
        return self._scan_success
    @scan_success.setter
    def scan_success(self, val):
        if val != None:
            self.validate('scan_success', val)
        self._scan_success = val
    
    _scan_retry = None
    @property
    def scan_retry(self):
        """
        This parameter specifies the number of files were re
        scanned.
        Attributes: non-creatable, non-modifiable
        """
        return self._scan_retry
    @scan_retry.setter
    def scan_retry(self, val):
        if val != None:
            self.validate('scan_retry', val)
        self._scan_retry = val
    
    _file_infected = None
    @property
    def file_infected(self):
        """
        This parameter specifies the number of files were found
        to be infected by a virus.
        Attributes: non-creatable, non-modifiable
        """
        return self._file_infected
    @file_infected.setter
    def file_infected(self, val):
        if val != None:
            self.validate('file_infected', val)
        self._file_infected = val
    
    _remedy_failed = None
    @property
    def remedy_failed(self):
        """
        This specifies the remedy failed for the specified number
        of files.
        Attributes: non-creatable, non-modifiable
        """
        return self._remedy_failed
    @remedy_failed.setter
    def remedy_failed(self, val):
        if val != None:
            self.validate('remedy_failed', val)
        self._remedy_failed = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver which owns this report.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _file_quarantined = None
    @property
    def file_quarantined(self):
        """
        This parameter specifies the number of files were
        quarantined because of a virus infection.
        Attributes: non-creatable, non-modifiable
        """
        return self._file_quarantined
    @file_quarantined.setter
    def file_quarantined(self, val):
        if val != None:
            self.validate('file_quarantined', val)
        self._file_quarantined = val
    
    _command = None
    @property
    def command(self):
        """
        This specifies the command used for scanning and that
        scan produced the report.
        Attributes: non-creatable, non-modifiable
        """
        return self._command
    @command.setter
    def command(self, val):
        if val != None:
            self.validate('command', val)
        self._command = val
    
    _file_deleted = None
    @property
    def file_deleted(self):
        """
        This parameter specifies the number of files were deleted
        because of a virus infection.
        Attributes: non-creatable, non-modifiable
        """
        return self._file_deleted
    @file_deleted.setter
    def file_deleted(self, val):
        if val != None:
            self.validate('file_deleted', val)
        self._file_deleted = val
    
    _scan_duration = None
    @property
    def scan_duration(self):
        """
        This displays reports in which scan proceeded for the
        specified length of time before completing successfully
        or failing.
        Attributes: non-creatable, non-modifiable
        """
        return self._scan_duration
    @scan_duration.setter
    def scan_duration(self, val):
        if val != None:
            self.validate('scan_duration', val)
        self._scan_duration = val
    
    _job_id = None
    @property
    def job_id(self):
        """
        This specifies the job id of the scan which has done the
        scanning.
        Attributes: non-creatable, non-modifiable
        """
        return self._job_id
    @job_id.setter
    def job_id(self, val):
        if val != None:
            self.validate('job_id', val)
        self._job_id = val
    
    _id = None
    @property
    def id(self):
        """
        This specifies the report identification number.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    _file_repaired = None
    @property
    def file_repaired(self):
        """
        This parameter specifies the number of files were
        successfully repaired from a virus infection.
        Attributes: non-creatable, non-modifiable
        """
        return self._file_repaired
    @file_repaired.setter
    def file_repaired(self, val):
        if val != None:
            self.validate('file_repaired', val)
        self._file_repaired = val
    
    @staticmethod
    def get_api_name():
          return "av-on-demand-report-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'file-scanned',
            'scan-failed',
            'scan-success',
            'scan-retry',
            'file-infected',
            'remedy-failed',
            'vserver',
            'file-quarantined',
            'command',
            'file-deleted',
            'scan-duration',
            'job-id',
            'id',
            'file-repaired',
        ]
    
    def describe_properties(self):
        return {
            'file_scanned': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scan_failed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scan_success': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scan_retry': { 'class': int, 'is_list': False, 'required': 'optional' },
            'file_infected': { 'class': int, 'is_list': False, 'required': 'optional' },
            'remedy_failed': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_quarantined': { 'class': int, 'is_list': False, 'required': 'optional' },
            'command': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'file_deleted': { 'class': int, 'is_list': False, 'required': 'optional' },
            'scan_duration': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'file_repaired': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
