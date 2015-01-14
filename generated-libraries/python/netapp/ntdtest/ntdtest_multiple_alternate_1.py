from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class NtdtestMultipleAlternate1(NetAppObject):
    """
    1st alternative typedef for table
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
    
    _zfield6 = None
    @property
    def zfield6(self):
        """
        Generic/Dummy Field 6
        Attributes: required-for-create, modifiable
        """
        return self._zfield6
    @zfield6.setter
    def zfield6(self, val):
        if val != None:
            self.validate('zfield6', val)
        self._zfield6 = val
    
    _zfield1 = None
    @property
    def zfield1(self):
        """
        Generic/Dummy Field 1
        Attributes: key, required-for-create, non-modifiable
        """
        return self._zfield1
    @zfield1.setter
    def zfield1(self, val):
        if val != None:
            self.validate('zfield1', val)
        self._zfield1 = val
    
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
          return "ntdtest-multiple-alternate-1"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield5',
            'zfield4',
            'zfield6',
            'zfield1',
            'zfield3',
            'zfield2',
        ]
    
    def describe_properties(self):
        return {
            'zfield5': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'zfield4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield6': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'zfield1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield2': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
