from netapp.cf.options_related_info_modify import OptionsRelatedInfoModify
from netapp.netapp_object import NetAppObject

class CfModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against cf object.
    modified due to some error.
    error.
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
    
    _cf_key = None
    @property
    def cf_key(self):
        """
        The keys for the cf object to which the modify operation
        applies.
        """
        return self._cf_key
    @cf_key.setter
    def cf_key(self, val):
        if val != None:
            self.validate('cf_key', val)
        self._cf_key = val
    
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
          return "cf-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'cf-key',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cf_key': { 'class': OptionsRelatedInfoModify, 'is_list': False, 'required': 'required' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
