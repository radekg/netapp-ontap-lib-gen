from netapp.netapp_object import NetAppObject

class QuotaReportIterKeyTd(NetAppObject):
    """
    Key typedef for table quota_report_common
    """
    
    _key_1 = None
    @property
    def key_1(self):
        """
        Field index
        """
        return self._key_1
    @key_1.setter
    def key_1(self, val):
        if val != None:
            self.validate('key_1', val)
        self._key_1 = val
    
    _key_0 = None
    @property
    def key_0(self):
        """
        Field volume_index
        """
        return self._key_0
    @key_0.setter
    def key_0(self, val):
        if val != None:
            self.validate('key_0', val)
        self._key_0 = val
    
    @staticmethod
    def get_api_name():
          return "quota-report-iter-key-td"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'key-1',
            'key-0',
        ]
    
    def describe_properties(self):
        return {
            'key_1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'key_0': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
