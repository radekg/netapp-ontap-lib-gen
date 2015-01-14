from netapp.netapp_object import NetAppObject

class IscsiCdbStatsInfo(NetAppObject):
    """
    Counts for Command Descriptor Blocks processed
    """
    
    _data_in_blocks = None
    @property
    def data_in_blocks(self):
        """
        Count of data in blocks.
        """
        return self._data_in_blocks
    @data_in_blocks.setter
    def data_in_blocks(self, val):
        if val != None:
            self.validate('data_in_blocks', val)
        self._data_in_blocks = val
    
    _success_status = None
    @property
    def success_status(self):
        """
        Count of successes.
        """
        return self._success_status
    @success_status.setter
    def success_status(self, val):
        if val != None:
            self.validate('success_status', val)
        self._success_status = val
    
    _total = None
    @property
    def total(self):
        """
        Total Command Descriptor Blocks processed.
        """
        return self._total
    @total.setter
    def total(self, val):
        if val != None:
            self.validate('total', val)
        self._total = val
    
    _error_status = None
    @property
    def error_status(self):
        """
        Count of errors.
        """
        return self._error_status
    @error_status.setter
    def error_status(self, val):
        if val != None:
            self.validate('error_status', val)
        self._error_status = val
    
    _data_out_blocks = None
    @property
    def data_out_blocks(self):
        """
        Count of data out blocks.
        """
        return self._data_out_blocks
    @data_out_blocks.setter
    def data_out_blocks(self, val):
        if val != None:
            self.validate('data_out_blocks', val)
        self._data_out_blocks = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-cdb-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'data-in-blocks',
            'success-status',
            'total',
            'error-status',
            'data-out-blocks',
        ]
    
    def describe_properties(self):
        return {
            'data_in_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
            'success_status': { 'class': int, 'is_list': False, 'required': 'required' },
            'total': { 'class': int, 'is_list': False, 'required': 'required' },
            'error_status': { 'class': int, 'is_list': False, 'required': 'required' },
            'data_out_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
        }
