from netapp.netapp_object import NetAppObject

class IscsiTransmittedStatsInfo(NetAppObject):
    """
    Counts for PDUs transmitted.
    """
    
    _nop_in = None
    @property
    def nop_in(self):
        """
        Count of NOP In.
        """
        return self._nop_in
    @nop_in.setter
    def nop_in(self, val):
        if val != None:
            self.validate('nop_in', val)
        self._nop_in = val
    
    _login_rsp = None
    @property
    def login_rsp(self):
        """
        Count of login responses.
        """
        return self._login_rsp
    @login_rsp.setter
    def login_rsp(self, val):
        if val != None:
            self.validate('login_rsp', val)
        self._login_rsp = val
    
    _scsi_task_mgt_rsp = None
    @property
    def scsi_task_mgt_rsp(self):
        """
        Count of scsi task management responses.
        """
        return self._scsi_task_mgt_rsp
    @scsi_task_mgt_rsp.setter
    def scsi_task_mgt_rsp(self, val):
        if val != None:
            self.validate('scsi_task_mgt_rsp', val)
        self._scsi_task_mgt_rsp = val
    
    _async_msg = None
    @property
    def async_msg(self):
        """
        Count of asynchronous iSCSI messages.
        """
        return self._async_msg
    @async_msg.setter
    def async_msg(self, val):
        if val != None:
            self.validate('async_msg', val)
        self._async_msg = val
    
    _ready_to_transmit = None
    @property
    def ready_to_transmit(self):
        """
        Count of ready to transmit PDUs
        """
        return self._ready_to_transmit
    @ready_to_transmit.setter
    def ready_to_transmit(self, val):
        if val != None:
            self.validate('ready_to_transmit', val)
        self._ready_to_transmit = val
    
    _logout_rsp = None
    @property
    def logout_rsp(self):
        """
        Count of logout responses.
        """
        return self._logout_rsp
    @logout_rsp.setter
    def logout_rsp(self, val):
        if val != None:
            self.validate('logout_rsp', val)
        self._logout_rsp = val
    
    _reject = None
    @property
    def reject(self):
        """
        Count of reject PDUs.
        """
        return self._reject
    @reject.setter
    def reject(self, val):
        if val != None:
            self.validate('reject', val)
        self._reject = val
    
    _total = None
    @property
    def total(self):
        """
        Total PDUs transmitted.
        """
        return self._total
    @total.setter
    def total(self, val):
        if val != None:
            self.validate('total', val)
        self._total = val
    
    _scsi_rsp = None
    @property
    def scsi_rsp(self):
        """
        Count of scsi responses.
        """
        return self._scsi_rsp
    @scsi_rsp.setter
    def scsi_rsp(self, val):
        if val != None:
            self.validate('scsi_rsp', val)
        self._scsi_rsp = val
    
    _data_in = None
    @property
    def data_in(self):
        """
        Count of data in PDUs.
        """
        return self._data_in
    @data_in.setter
    def data_in(self, val):
        if val != None:
            self.validate('data_in', val)
        self._data_in = val
    
    _text_rsp = None
    @property
    def text_rsp(self):
        """
        Count of text responses.
        """
        return self._text_rsp
    @text_rsp.setter
    def text_rsp(self, val):
        if val != None:
            self.validate('text_rsp', val)
        self._text_rsp = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-transmitted-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'nop-in',
            'login-rsp',
            'scsi-task-mgt-rsp',
            'async-msg',
            'ready-to-transmit',
            'logout-rsp',
            'reject',
            'total',
            'scsi-rsp',
            'data-in',
            'text-rsp',
        ]
    
    def describe_properties(self):
        return {
            'nop_in': { 'class': int, 'is_list': False, 'required': 'required' },
            'login_rsp': { 'class': int, 'is_list': False, 'required': 'required' },
            'scsi_task_mgt_rsp': { 'class': int, 'is_list': False, 'required': 'required' },
            'async_msg': { 'class': int, 'is_list': False, 'required': 'required' },
            'ready_to_transmit': { 'class': int, 'is_list': False, 'required': 'required' },
            'logout_rsp': { 'class': int, 'is_list': False, 'required': 'required' },
            'reject': { 'class': int, 'is_list': False, 'required': 'required' },
            'total': { 'class': int, 'is_list': False, 'required': 'required' },
            'scsi_rsp': { 'class': int, 'is_list': False, 'required': 'required' },
            'data_in': { 'class': int, 'is_list': False, 'required': 'required' },
            'text_rsp': { 'class': int, 'is_list': False, 'required': 'required' },
        }
