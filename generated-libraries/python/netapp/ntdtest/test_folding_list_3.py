from netapp.netapp_object import NetAppObject

class TestFoldingList3(NetAppObject):
    """
    Test output typedef 3
    """
    
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
    
    _zfield2 = None
    @property
    def zfield2(self):
        """
        Generic/Dummy Field 2
        Attributes: key, required-for-create, non-modifiable
        """
        return self._zfield2
    @zfield2.setter
    def zfield2(self, val):
        if val != None:
            self.validate('zfield2', val)
        self._zfield2 = val
    
    @staticmethod
    def get_api_name():
          return "test-folding-list-3"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield3',
            'zfield2',
        ]
    
    def describe_properties(self):
        return {
            'zfield3': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'zfield2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
