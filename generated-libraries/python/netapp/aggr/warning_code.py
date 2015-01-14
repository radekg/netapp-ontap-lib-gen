from netapp.netapp_object import NetAppObject

class WarningCode(NetAppObject):
    """
    Warning codes for pre-check mode.
    """
    
    _code = None
    @property
    def code(self):
        """
        Warning code.
        """
        return self._code
    @code.setter
    def code(self, val):
        if val != None:
            self.validate('code', val)
        self._code = val
    
    @staticmethod
    def get_api_name():
          return "warning-code"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'code',
        ]
    
    def describe_properties(self):
        return {
            'code': { 'class': int, 'is_list': False, 'required': 'required' },
        }
