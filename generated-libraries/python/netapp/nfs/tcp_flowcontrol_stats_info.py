from netapp.netapp_object import NetAppObject

class TcpFlowcontrolStatsInfo(NetAppObject):
    """
    structure containing statistics for tcp flowcontrol
    """
    
    _receive_out_total = None
    @property
    def receive_out_total(self):
        """
        total number of times output was flow controlled on
        receive
        Range : [0..2^32-1].
        """
        return self._receive_out_total
    @receive_out_total.setter
    def receive_out_total(self, val):
        if val != None:
            self.validate('receive_out_total', val)
        self._receive_out_total = val
    
    _transmit_out_total = None
    @property
    def transmit_out_total(self):
        """
        total number of times output was flow controlled on
        transmit
        Range : [0..2^32-1].
        """
        return self._transmit_out_total
    @transmit_out_total.setter
    def transmit_out_total(self, val):
        if val != None:
            self.validate('transmit_out_total', val)
        self._transmit_out_total = val
    
    _receive_total = None
    @property
    def receive_total(self):
        """
        total number of times input was flow controlled on
        receive
        Range : [0..2^32-1].
        """
        return self._receive_total
    @receive_total.setter
    def receive_total(self, val):
        if val != None:
            self.validate('receive_total', val)
        self._receive_total = val
    
    _transmit_total = None
    @property
    def transmit_total(self):
        """
        total number of times input was flow controlled on
        transmit
        Range : [0..2^32-1].
        """
        return self._transmit_total
    @transmit_total.setter
    def transmit_total(self, val):
        if val != None:
            self.validate('transmit_total', val)
        self._transmit_total = val
    
    @staticmethod
    def get_api_name():
          return "tcp-flowcontrol-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'receive-out-total',
            'transmit-out-total',
            'receive-total',
            'transmit-total',
        ]
    
    def describe_properties(self):
        return {
            'receive_out_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'transmit_out_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'receive_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'transmit_total': { 'class': int, 'is_list': False, 'required': 'required' },
        }
