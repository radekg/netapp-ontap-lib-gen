from netapp.netapp_object import NetAppObject

class AggrWaflironInfo(NetAppObject):
    """
    Information related to wafliron, the online WAFL
    file system check/repair tool.
    """
    
    _last_start_errno = None
    @property
    def last_start_errno(self):
        """
        The error code of the last attempt to
        start wafliron on the specific aggregate
        or the traditional volume. This field is
        present only if 'wafliron start' was
        previously attempted.
        """
        return self._last_start_errno
    @last_start_errno.setter
    def last_start_errno(self, val):
        if val != None:
            self.validate('last_start_errno', val)
        self._last_start_errno = val
    
    _state = None
    @property
    def state(self):
        """
        When wafliron is run, it goes through
        different stages/states. This field
        indicates the current state of wafliron
        on the specified aggregate.
        <p>
        Possible values are:
        <p>
        "waiting_for_commit"	- wafliron is finished
        on this volume but
        waiting for the
        changes to be
        committed or rejected.
        <p>
        "not_running"   - wafliron is not
        running on this
        aggregate.
        <p>
        "starting"      - wafliron is starting,
        allocating, and/or in
        the initial mounting
        phase.
        <p>
        "scanning"      - wafliron is scanning
        inodes, and/or fixing
        file system
        inconsistencies.
        <p>
        "checking_lost_blocks"  - wafliron is
        checking for lost
        blocks.
        <p>
        "checking_lost_inodes"  - wafliron is
        checking link counts.
        <p>
        "finishing"     - wafliron is cleaning
        up.
        <p>
        "aborting"      - wafliron is aborting.
        <p>
        "unknown"       - wafliron state could
        not be determined.
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _scan_percentage = None
    @property
    def scan_percentage(self):
        """
        When present, this field indicates the
        percentage of blocks that have been
        scanned in the specified aggregate. This
        field is present only when wafliron is
        running and its state is "starting" or "scanning".
        <p>
        Range: [0..100]
        """
        return self._scan_percentage
    @scan_percentage.setter
    def scan_percentage(self, val):
        if val != None:
            self.validate('scan_percentage', val)
        self._scan_percentage = val
    
    _summary_scan_percentage = None
    @property
    def summary_scan_percentage(self):
        """
        When present and the value is other than -1,
        this field indicates the percentage of summary
        blocks that have been scanned in the specified
        aggregate. This field is present only when
        wafliron is running and its state is "starting"
        or "scanning".
        <p>
        Range: [-1..100]
        """
        return self._summary_scan_percentage
    @summary_scan_percentage.setter
    def summary_scan_percentage(self, val):
        if val != None:
            self.validate('summary_scan_percentage', val)
        self._summary_scan_percentage = val
    
    _last_start_error_info = None
    @property
    def last_start_error_info(self):
        """
        The error information of the last
        attempt to start wafliron on the
        specific aggregate or the traditional
        volume. This field is present only if
        'wafliron start' was previously
        attempted.
        """
        return self._last_start_error_info
    @last_start_error_info.setter
    def last_start_error_info(self, val):
        if val != None:
            self.validate('last_start_error_info', val)
        self._last_start_error_info = val
    
    @staticmethod
    def get_api_name():
          return "aggr-wafliron-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'last-start-errno',
            'state',
            'scan-percentage',
            'summary-scan-percentage',
            'last-start-error-info',
        ]
    
    def describe_properties(self):
        return {
            'last_start_errno': { 'class': int, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'scan_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'summary_scan_percentage': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_start_error_info': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
