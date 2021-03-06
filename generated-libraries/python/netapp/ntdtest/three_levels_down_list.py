from netapp.netapp_object import NetAppObject

class ThreeLevelsDownList(NetAppObject):
    """
    Theree levels deep and of list type
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
    
    @staticmethod
    def get_api_name():
          return "three-levels-down-list"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield3',
        ]
    
    def describe_properties(self):
        return {
            'zfield3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
