from netapp.netapp_object import NetAppObject

class OutputTypedef2(NetAppObject):
    """
    Output
    """
    
    _zfield5 = None
    @property
    def zfield5(self):
        """
        Generic/Dummy Field 5
        Attributes: required-for-create, modifiable
        """
        return self._zfield5
    @zfield5.setter
    def zfield5(self, val):
        if val != None:
            self.validate('zfield5', val)
        self._zfield5 = val
    
    _zfield3 = None
    @property
    def zfield3(self):
        """
        Generic/Dummy Field 3
        Attributes: required-for-create, non-modifiable
        """
        return self._zfield3
    @zfield3.setter
    def zfield3(self, val):
        if val != None:
            self.validate('zfield3', val)
        self._zfield3 = val
    
    @staticmethod
    def get_api_name():
          return "output-typedef-2"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield5',
            'zfield3',
        ]
    
    def describe_properties(self):
        return {
            'zfield5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
