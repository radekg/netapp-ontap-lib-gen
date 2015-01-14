from netapp.vserver.vserver_info import VserverInfo
from netapp.netapp_object import NetAppObject

class VserverModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against vserver object.
    modified due to some error.
    some error.
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
    
    _vserver_key = None
    @property
    def vserver_key(self):
        """
        The keys for the vserver object to which the modify
        operation applies.
        """
        return self._vserver_key
    @vserver_key.setter
    def vserver_key(self, val):
        if val != None:
            self.validate('vserver_key', val)
        self._vserver_key = val
    
    @staticmethod
    def get_api_name():
          return "vserver-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'vserver-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver_key': { 'class': VserverInfo, 'is_list': False, 'required': 'required' },
        }
