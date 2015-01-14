from netapp.ems.ems_routing_info import EmsRoutingInfo
from netapp.netapp_object import NetAppObject

class EmsRoutingModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against ems-routing object.
    not modified due to some error.
    to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the modify operation caused an error.
        """
        return self._error_code
    @error_code.setter
    def error_code(self, val):
        if val != None:
            self.validate('error_code', val)
        self._error_code = val
    
    _ems_routing_key = None
    @property
    def ems_routing_key(self):
        """
        The keys for the ems-routing object to which the modify
        operation applies.
        """
        return self._ems_routing_key
    @ems_routing_key.setter
    def ems_routing_key(self, val):
        if val != None:
            self.validate('ems_routing_key', val)
        self._ems_routing_key = val
    
    _error_message = None
    @property
    def error_message(self):
        """
        Error description, if the modify operation caused an
        error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    @staticmethod
    def get_api_name():
          return "ems-routing-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'ems-routing-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ems_routing_key': { 'class': EmsRoutingInfo, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
