from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class OutputTypedef4(NetAppObject):
    """
    Output
    """
    
    _zfield8 = None
    @property
    def zfield8(self):
        """
        Generic/Dummy Field 4
        Attributes: non-creatable, non-modifiable
        """
        return self._zfield8
    @zfield8.setter
    def zfield8(self, val):
        if val != None:
            self.validate('zfield8', val)
        self._zfield8 = val
    
    @staticmethod
    def get_api_name():
          return "output-typedef-4"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield8',
        ]
    
    def describe_properties(self):
        return {
            'zfield8': { 'class': NtdtestInfo, 'is_list': False, 'required': 'optional' },
        }
