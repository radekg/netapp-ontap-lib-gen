from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class OutMethod2Info(NetAppObject):
    """
    Output typedef for method 2
    """
    
    _arg_4 = None
    @property
    def arg_4(self):
        """
        Argument 4 for method method2
        Attributes: non-creatable, modifiable
        """
        return self._arg_4
    @arg_4.setter
    def arg_4(self, val):
        if val != None:
            self.validate('arg_4', val)
        self._arg_4 = val
    
    _arg_3 = None
    @property
    def arg_3(self):
        """
        Argument 3 for method method2
        Attributes: non-creatable, modifiable
        """
        return self._arg_3
    @arg_3.setter
    def arg_3(self, val):
        if val != None:
            self.validate('arg_3', val)
        self._arg_3 = val
    
    @staticmethod
    def get_api_name():
          return "out-method-2-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'arg-4',
            'arg-3',
        ]
    
    def describe_properties(self):
        return {
            'arg_4': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'arg_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
