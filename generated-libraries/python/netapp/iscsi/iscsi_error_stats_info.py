from netapp.netapp_object import NetAppObject

class IscsiErrorStatsInfo(NetAppObject):
    """
    Counts for iSCSI errors.
    """
    
    _outside_cmd_sn_window = None
    @property
    def outside_cmd_sn_window(self):
        """
        Count of PDU discards due to PDU being
        outside of command sequence number window.
        """
        return self._outside_cmd_sn_window
    @outside_cmd_sn_window.setter
    def outside_cmd_sn_window(self, val):
        if val != None:
            self.validate('outside_cmd_sn_window', val)
        self._outside_cmd_sn_window = val
    
    _failed_logouts = None
    @property
    def failed_logouts(self):
        """
        Count of failed logouts.
        """
        return self._failed_logouts
    @failed_logouts.setter
    def failed_logouts(self, val):
        if val != None:
            self.validate('failed_logouts', val)
        self._failed_logouts = val
    
    _protocol = None
    @property
    def protocol(self):
        """
        Count of protocol errors.
        """
        return self._protocol
    @protocol.setter
    def protocol(self, val):
        if val != None:
            self.validate('protocol', val)
        self._protocol = val
    
    _failed_task_mgt = None
    @property
    def failed_task_mgt(self):
        """
        Count of failed management tasks.
        """
        return self._failed_task_mgt
    @failed_task_mgt.setter
    def failed_task_mgt(self, val):
        if val != None:
            self.validate('failed_task_mgt', val)
        self._failed_task_mgt = val
    
    _failed_text_cmd = None
    @property
    def failed_text_cmd(self):
        """
        Count of failed text commands.
        """
        return self._failed_text_cmd
    @failed_text_cmd.setter
    def failed_text_cmd(self, val):
        if val != None:
            self.validate('failed_text_cmd', val)
        self._failed_text_cmd = val
    
    _data_digest = None
    @property
    def data_digest(self):
        """
        Count of digest errors.
        """
        return self._data_digest
    @data_digest.setter
    def data_digest(self, val):
        if val != None:
            self.validate('data_digest', val)
        self._data_digest = val
    
    _invalid_header = None
    @property
    def invalid_header(self):
        """
        Count of PDU discards due to invalid PDU header.
        """
        return self._invalid_header
    @invalid_header.setter
    def invalid_header(self, val):
        if val != None:
            self.validate('invalid_header', val)
        self._invalid_header = val
    
    _total = None
    @property
    def total(self):
        """
        Total errors.
        """
        return self._total
    @total.setter
    def total(self, val):
        if val != None:
            self.validate('total', val)
        self._total = val
    
    _failed_logins = None
    @property
    def failed_logins(self):
        """
        Count of failed logins.
        """
        return self._failed_logins
    @failed_logins.setter
    def failed_logins(self, val):
        if val != None:
            self.validate('failed_logins', val)
        self._failed_logins = val
    
    _hdr_digest = None
    @property
    def hdr_digest(self):
        """
        Count of digest errors.
        """
        return self._hdr_digest
    @hdr_digest.setter
    def hdr_digest(self, val):
        if val != None:
            self.validate('hdr_digest', val)
        self._hdr_digest = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-error-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'outside-cmd-sn-window',
            'failed-logouts',
            'protocol',
            'failed-task-mgt',
            'failed-text-cmd',
            'data-digest',
            'invalid-header',
            'total',
            'failed-logins',
            'hdr-digest',
        ]
    
    def describe_properties(self):
        return {
            'outside_cmd_sn_window': { 'class': int, 'is_list': False, 'required': 'required' },
            'failed_logouts': { 'class': int, 'is_list': False, 'required': 'required' },
            'protocol': { 'class': int, 'is_list': False, 'required': 'required' },
            'failed_task_mgt': { 'class': int, 'is_list': False, 'required': 'required' },
            'failed_text_cmd': { 'class': int, 'is_list': False, 'required': 'required' },
            'data_digest': { 'class': int, 'is_list': False, 'required': 'required' },
            'invalid_header': { 'class': int, 'is_list': False, 'required': 'required' },
            'total': { 'class': int, 'is_list': False, 'required': 'required' },
            'failed_logins': { 'class': int, 'is_list': False, 'required': 'required' },
            'hdr_digest': { 'class': int, 'is_list': False, 'required': 'required' },
        }
