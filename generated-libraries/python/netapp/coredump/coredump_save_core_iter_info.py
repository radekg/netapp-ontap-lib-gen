from netapp.coredump.coredump_info import CoredumpInfo
from netapp.netapp_object import NetAppObject

class CoredumpSaveCoreIterInfo(NetAppObject):
    """
    Information about the operation that was attempted/performed
    against coredump object.
    not operated on due some error.
    to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the operation caused an error.
        """
        return self._error_code
    @error_code.setter
    def error_code(self, val):
        if val != None:
            self.validate('error_code', val)
        self._error_code = val
    
    _coredump_key = None
    @property
    def coredump_key(self):
        """
        The keys for the coredump object to which the operation
        applies.
        """
        return self._coredump_key
    @coredump_key.setter
    def coredump_key(self, val):
        if val != None:
            self.validate('coredump_key', val)
        self._coredump_key = val
    
    _error_message = None
    @property
    def error_message(self):
        """
        Error description, if the operation caused an error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    @staticmethod
    def get_api_name():
          return "coredump-save-core-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'coredump-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'coredump_key': { 'class': CoredumpInfo, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
