from netapp.netapp_object import NetAppObject

class NtdtestInfo(NetAppObject):
    """
    list for ntdtest
    """
    
    _ntdtest_name = None
    @property
    def ntdtest_name(self):
        """
        """
        return self._ntdtest_name
    @ntdtest_name.setter
    def ntdtest_name(self, val):
        if val != None:
            self.validate('ntdtest_name', val)
        self._ntdtest_name = val
    
    @staticmethod
    def get_api_name():
          return "ntdtest-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ntdtest-name',
        ]
    
    def describe_properties(self):
        return {
            'ntdtest_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
