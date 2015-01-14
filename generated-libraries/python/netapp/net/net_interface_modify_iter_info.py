from netapp.net.net_interface_info import NetInterfaceInfo
from netapp.netapp_object import NetAppObject

class NetInterfaceModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against given network interface object.
    but were not modified due to some error.
    modified due to some error.
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
    
    _net_key = None
    @property
    def net_key(self):
        """
        The keys for the given network interface object to which
        the modify operation applies.
        """
        return self._net_key
    @net_key.setter
    def net_key(self, val):
        if val != None:
            self.validate('net_key', val)
        self._net_key = val
    
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
          return "net-interface-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'net-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'net_key': { 'class': NetInterfaceInfo, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
