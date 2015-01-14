from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class OutMethod1Info(NetAppObject):
    """
    Output typedef for method 1
    """
    
    _arg_4 = None
    @property
    def arg_4(self):
        """
        Argument 4 for method method1
        Attributes: optional-for-create, non-modifiable
        """
        return self._arg_4
    @arg_4.setter
    def arg_4(self, val):
        if val != None:
            self.validate('arg_4', val)
        self._arg_4 = val
    
    @staticmethod
    def get_api_name():
          return "out-method-1-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'arg-4',
        ]
    
    def describe_properties(self):
        return {
            'arg_4': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
        }
