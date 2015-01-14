from netapp.netapp_object import NetAppObject

class RpcDataInfo(NetAppObject):
    """
    structure containing statisticcs for RPC operations
    """
    
    _nullrecv_total = None
    @property
    def nullrecv_total(self):
        """
        total nullrecv RPC calls
        Range : [0..2^32-1].
        """
        return self._nullrecv_total
    @nullrecv_total.setter
    def nullrecv_total(self, val):
        if val != None:
            self.validate('nullrecv_total', val)
        self._nullrecv_total = val
    
    _calls_total = None
    @property
    def calls_total(self):
        """
        total RPC calls
        Range : [0..2^64-1].
        """
        return self._calls_total
    @calls_total.setter
    def calls_total(self, val):
        if val != None:
            self.validate('calls_total', val)
        self._calls_total = val
    
    _badcalls_total = None
    @property
    def badcalls_total(self):
        """
        total bad RPC calls
        Range : [0..2^32-1].
        """
        return self._badcalls_total
    @badcalls_total.setter
    def badcalls_total(self, val):
        if val != None:
            self.validate('badcalls_total', val)
        self._badcalls_total = val
    
    _badlen_total = None
    @property
    def badlen_total(self):
        """
        total badlen RPC calls
        Range : [0..2^32-1].
        """
        return self._badlen_total
    @badlen_total.setter
    def badlen_total(self, val):
        if val != None:
            self.validate('badlen_total', val)
        self._badlen_total = val
    
    _xdrcall_total = None
    @property
    def xdrcall_total(self):
        """
        total badhdr RPC calls
        Range : [0..2^32-1].
        """
        return self._xdrcall_total
    @xdrcall_total.setter
    def xdrcall_total(self, val):
        if val != None:
            self.validate('xdrcall_total', val)
        self._xdrcall_total = val
    
    @staticmethod
    def get_api_name():
          return "rpc-data-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'nullrecv-total',
            'calls-total',
            'badcalls-total',
            'badlen-total',
            'xdrcall-total',
        ]
    
    def describe_properties(self):
        return {
            'nullrecv_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'calls_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'badcalls_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'badlen_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'xdrcall_total': { 'class': int, 'is_list': False, 'required': 'required' },
        }
