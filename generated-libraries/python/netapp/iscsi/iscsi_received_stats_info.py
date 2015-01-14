from netapp.netapp_object import NetAppObject

class IscsiReceivedStatsInfo(NetAppObject):
    """
    Counts for PDUs received.
    """
    
    _data_out = None
    @property
    def data_out(self):
        """
        Count of data out requests.
        """
        return self._data_out
    @data_out.setter
    def data_out(self, val):
        if val != None:
            self.validate('data_out', val)
        self._data_out = val
    
    _scsi_task_mgt_cmd = None
    @property
    def scsi_task_mgt_cmd(self):
        """
        Count of SCSI task management commands.
        """
        return self._scsi_task_mgt_cmd
    @scsi_task_mgt_cmd.setter
    def scsi_task_mgt_cmd(self, val):
        if val != None:
            self.validate('scsi_task_mgt_cmd', val)
        self._scsi_task_mgt_cmd = val
    
    _login_req = None
    @property
    def login_req(self):
        """
        Count of login requests.
        """
        return self._login_req
    @login_req.setter
    def login_req(self, val):
        if val != None:
            self.validate('login_req', val)
        self._login_req = val
    
    _unknown = None
    @property
    def unknown(self):
        """
        Count of unknown PDUs.
        """
        return self._unknown
    @unknown.setter
    def unknown(self, val):
        if val != None:
            self.validate('unknown', val)
        self._unknown = val
    
    _nop_out = None
    @property
    def nop_out(self):
        """
        Count of NOP Out.
        """
        return self._nop_out
    @nop_out.setter
    def nop_out(self, val):
        if val != None:
            self.validate('nop_out', val)
        self._nop_out = val
    
    _scsi_cmd = None
    @property
    def scsi_cmd(self):
        """
        Count of SCSI commands.
        """
        return self._scsi_cmd
    @scsi_cmd.setter
    def scsi_cmd(self, val):
        if val != None:
            self.validate('scsi_cmd', val)
        self._scsi_cmd = val
    
    _snack = None
    @property
    def snack(self):
        """
        Count of SNACK requests.
        """
        return self._snack
    @snack.setter
    def snack(self, val):
        if val != None:
            self.validate('snack', val)
        self._snack = val
    
    _text_req = None
    @property
    def text_req(self):
        """
        Count of text requests.
        """
        return self._text_req
    @text_req.setter
    def text_req(self, val):
        if val != None:
            self.validate('text_req', val)
        self._text_req = val
    
    _total = None
    @property
    def total(self):
        """
        Total PDUs received.
        """
        return self._total
    @total.setter
    def total(self, val):
        if val != None:
            self.validate('total', val)
        self._total = val
    
    _logout_req = None
    @property
    def logout_req(self):
        """
        Count of logout requests.
        """
        return self._logout_req
    @logout_req.setter
    def logout_req(self, val):
        if val != None:
            self.validate('logout_req', val)
        self._logout_req = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-received-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'data-out',
            'scsi-task-mgt-cmd',
            'login-req',
            'unknown',
            'nop-out',
            'scsi-cmd',
            'snack',
            'text-req',
            'total',
            'logout-req',
        ]
    
    def describe_properties(self):
        return {
            'data_out': { 'class': int, 'is_list': False, 'required': 'required' },
            'scsi_task_mgt_cmd': { 'class': int, 'is_list': False, 'required': 'required' },
            'login_req': { 'class': int, 'is_list': False, 'required': 'required' },
            'unknown': { 'class': int, 'is_list': False, 'required': 'required' },
            'nop_out': { 'class': int, 'is_list': False, 'required': 'required' },
            'scsi_cmd': { 'class': int, 'is_list': False, 'required': 'required' },
            'snack': { 'class': int, 'is_list': False, 'required': 'required' },
            'text_req': { 'class': int, 'is_list': False, 'required': 'required' },
            'total': { 'class': int, 'is_list': False, 'required': 'required' },
            'logout_req': { 'class': int, 'is_list': False, 'required': 'required' },
        }
