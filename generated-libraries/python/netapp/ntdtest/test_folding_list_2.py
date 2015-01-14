from netapp.netapp_object import NetAppObject

class TestFoldingList2(NetAppObject):
    """
    Test output typedef 2
    """
    
    _zfield4 = None
    @property
    def zfield4(self):
        """
        Generic/Dummy Field 4
        Attributes: required-for-create, non-modifiable
        """
        return self._zfield4
    @zfield4.setter
    def zfield4(self, val):
        if val != None:
            self.validate('zfield4', val)
        self._zfield4 = val
    
    _zfield3 = None
    @property
    def zfield3(self):
        """
        Generic/Dummy Field 3
        Attributes: key, required-for-create, non-modifiable
        """
        return self._zfield3
    @zfield3.setter
    def zfield3(self, val):
        if val != None:
            self.validate('zfield3', val)
        self._zfield3 = val
    
    @staticmethod
    def get_api_name():
          return "test-folding-list-2"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield4',
            'zfield3',
        ]
    
    def describe_properties(self):
        return {
            'zfield4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
