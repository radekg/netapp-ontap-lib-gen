from netapp.qos.qos_settings_read_ahead_info import QosSettingsReadAheadInfo
from netapp.netapp_object import NetAppObject

class QosSettingsReadAheadModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against qos-settings-read-ahead object.
    but were not modified due to some error.
    modified due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _qos_settings_read_ahead_key = None
    @property
    def qos_settings_read_ahead_key(self):
        """
        The keys for the qos-settings-read-ahead object to which
        the modify operation applies.
        """
        return self._qos_settings_read_ahead_key
    @qos_settings_read_ahead_key.setter
    def qos_settings_read_ahead_key(self, val):
        if val != None:
            self.validate('qos_settings_read_ahead_key', val)
        self._qos_settings_read_ahead_key = val
    
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
    
    @staticmethod
    def get_api_name():
          return "qos-settings-read-ahead-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'qos-settings-read-ahead-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'qos_settings_read_ahead_key': { 'class': QosSettingsReadAheadInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
