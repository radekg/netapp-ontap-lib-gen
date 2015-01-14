from netapp.volume.volume_attributes import VolumeAttributes
from netapp.netapp_object import NetAppObject

class VolumeModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against volume object.
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
    
    _volume_key = None
    @property
    def volume_key(self):
        """
        The keys for the volume object to which the modify
        operation applies.
        """
        return self._volume_key
    @volume_key.setter
    def volume_key(self, val):
        if val != None:
            self.validate('volume_key', val)
        self._volume_key = val
    
    @staticmethod
    def get_api_name():
          return "volume-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'volume-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'volume_key': { 'class': VolumeAttributes, 'is_list': False, 'required': 'required' },
        }
