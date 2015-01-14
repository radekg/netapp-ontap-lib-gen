from netapp.ntdtest.dummy_vserver import DummyVserver
from netapp.netapp_object import NetAppObject

class DummyVserverDestroyIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against dummy-vserver object.
    not deleted due to some error.
    to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the deletion operation caused an error.
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
        Error description, if the operation caused an error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    _dummy_vserver_key = None
    @property
    def dummy_vserver_key(self):
        """
        The keys for the dummy-vserver object to which the
        deletion applies.
        """
        return self._dummy_vserver_key
    @dummy_vserver_key.setter
    def dummy_vserver_key(self, val):
        if val != None:
            self.validate('dummy_vserver_key', val)
        self._dummy_vserver_key = val
    
    @staticmethod
    def get_api_name():
          return "dummy-vserver-destroy-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'dummy-vserver-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dummy_vserver_key': { 'class': DummyVserver, 'is_list': False, 'required': 'required' },
        }
