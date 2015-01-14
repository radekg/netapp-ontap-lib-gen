from netapp.coredump.coredump_config_info import CoredumpConfigInfo
from netapp.netapp_object import NetAppObject

class CoredumpConfigModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against coredump-config object.
    were not modified due to some error.
    due to some error.
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
    
    _coredump_config_key = None
    @property
    def coredump_config_key(self):
        """
        The keys for the coredump-config object to which the
        modify operation applies.
        """
        return self._coredump_config_key
    @coredump_config_key.setter
    def coredump_config_key(self, val):
        if val != None:
            self.validate('coredump_config_key', val)
        self._coredump_config_key = val
    
    @staticmethod
    def get_api_name():
          return "coredump-config-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'coredump-config-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'coredump_config_key': { 'class': CoredumpConfigInfo, 'is_list': False, 'required': 'required' },
        }
