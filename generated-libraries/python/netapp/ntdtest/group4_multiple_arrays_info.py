from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class Group4MultipleArraysInfo(NetAppObject):
    """
    4th nested typedef at level 1
    """
    
    _zfield8 = None
    @property
    def zfield8(self):
        """
        Generic/Dummy Field 6
        Attributes: required-for-create, modifiable
        """
        return self._zfield8
    @zfield8.setter
    def zfield8(self, val):
        if val != None:
            self.validate('zfield8', val)
        self._zfield8 = val
    
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
    
    _zfield7 = None
    @property
    def zfield7(self):
        """
        Generic/Dummy Field 5
        Attributes: required-for-create, modifiable
        """
        return self._zfield7
    @zfield7.setter
    def zfield7(self, val):
        if val != None:
            self.validate('zfield7', val)
        self._zfield7 = val
    
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
    
    _zfield3 = None
    @property
    def zfield3(self):
        """
        SOMEFIELD3
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
          return "group4-multiple-arrays-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield8',
            'zfield5',
            'zfield4',
            'zfield7',
            'zfield6',
            'zfield3',
        ]
    
    def describe_properties(self):
        return {
            'zfield8': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'zfield5': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield4': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield7': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'zfield6': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'zfield3': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
