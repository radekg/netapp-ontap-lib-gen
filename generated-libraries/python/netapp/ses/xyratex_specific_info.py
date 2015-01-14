from netapp.netapp_object import NetAppObject

class XyratexSpecificInfo(NetAppObject):
    """
    Vendor specific enclosure system information for
    Xyratex shelf.
    """
    
    _xyratex_option_setting = None
    @property
    def xyratex_option_setting(self):
        """
        Option setting for the Xyratex shelf.
        """
        return self._xyratex_option_setting
    @xyratex_option_setting.setter
    def xyratex_option_setting(self, val):
        if val != None:
            self.validate('xyratex_option_setting', val)
        self._xyratex_option_setting = val
    
    _xyratex_serial_no = None
    @property
    def xyratex_serial_no(self):
        """
        serial number for Xyratex shelf.
        """
        return self._xyratex_serial_no
    @xyratex_serial_no.setter
    def xyratex_serial_no(self, val):
        if val != None:
            self.validate('xyratex_serial_no', val)
        self._xyratex_serial_no = val
    
    @staticmethod
    def get_api_name():
          return "xyratex-specific-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'xyratex-option-setting',
            'xyratex-serial-no',
        ]
    
    def describe_properties(self):
        return {
            'xyratex_option_setting': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'xyratex_serial_no': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
