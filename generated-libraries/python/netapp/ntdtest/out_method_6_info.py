from netapp.netapp_object import NetAppObject

class OutMethod6Info(NetAppObject):
    """
    Output typedef for method 6
    """
    
    _arg4 = None
    @property
    def arg4(self):
        """
        Argument 4 for method method6
        Attributes: non-creatable, modifiable
        """
        return self._arg4
    @arg4.setter
    def arg4(self, val):
        if val != None:
            self.validate('arg4', val)
        self._arg4 = val
    
    _hidden5 = None
    @property
    def hidden5(self):
        """
        Argument 5 for method method6
        Attributes: non-creatable, modifiable
        """
        return self._hidden5
    @hidden5.setter
    def hidden5(self, val):
        if val != None:
            self.validate('hidden5', val)
        self._hidden5 = val
    
    @staticmethod
    def get_api_name():
          return "out-method-6-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'arg4',
            'hidden5',
        ]
    
    def describe_properties(self):
        return {
            'arg4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'hidden5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
