from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class InMethod1Info(NetAppObject):
    """
    Input typedef for method 1
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
    
    _arg_2 = None
    @property
    def arg_2(self):
        """
        Argument 2 for method method1
        Attributes: required-for-create, non-modifiable
        """
        return self._arg_2
    @arg_2.setter
    def arg_2(self, val):
        if val != None:
            self.validate('arg_2', val)
        self._arg_2 = val
    
    _arg_3 = None
    @property
    def arg_3(self):
        """
        Argument 3 for method method1
        Attributes: optional-for-create, non-modifiable
        """
        return self._arg_3
    @arg_3.setter
    def arg_3(self, val):
        if val != None:
            self.validate('arg_3', val)
        self._arg_3 = val
    
    _arg_1 = None
    @property
    def arg_1(self):
        """
        Argument 1 for method method1
        Attributes: required-for-create, non-modifiable
        """
        return self._arg_1
    @arg_1.setter
    def arg_1(self, val):
        if val != None:
            self.validate('arg_1', val)
        self._arg_1 = val
    
    @staticmethod
    def get_api_name():
          return "in-method-1-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'arg-4',
            'arg-2',
            'arg-3',
            'arg-1',
        ]
    
    def describe_properties(self):
        return {
            'arg_4': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'arg_2': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'arg_3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'arg_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
