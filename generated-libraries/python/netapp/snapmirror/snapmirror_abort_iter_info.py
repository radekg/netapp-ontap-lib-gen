from netapp.snapmirror.snapmirror_info import SnapmirrorInfo
from netapp.netapp_object import NetAppObject

class SnapmirrorAbortIterInfo(NetAppObject):
    """
    Information about the operation that was attempted/performed
    against snapmirror object.
    not operated on due some error.
    due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _snapmirror_key = None
    @property
    def snapmirror_key(self):
        """
        The keys for the snapmirror object to which the operation
        applies.
        """
        return self._snapmirror_key
    @snapmirror_key.setter
    def snapmirror_key(self, val):
        if val != None:
            self.validate('snapmirror_key', val)
        self._snapmirror_key = val
    
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
          return "snapmirror-abort-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'snapmirror-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'snapmirror_key': { 'class': SnapmirrorInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
