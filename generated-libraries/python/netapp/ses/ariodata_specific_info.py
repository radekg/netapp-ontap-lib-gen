from netapp.netapp_object import NetAppObject

class AriodataSpecificInfo(NetAppObject):
    """
    Vendor specific enclosure system information for
    Ariodata shelf.
    """
    
    _ariodata_serial_no = None
    @property
    def ariodata_serial_no(self):
        """
        Serial number for Ariodata shelf.
        """
        return self._ariodata_serial_no
    @ariodata_serial_no.setter
    def ariodata_serial_no(self, val):
        if val != None:
            self.validate('ariodata_serial_no', val)
        self._ariodata_serial_no = val
    
    @staticmethod
    def get_api_name():
          return "ariodata-specific-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ariodata-serial-no',
        ]
    
    def describe_properties(self):
        return {
            'ariodata_serial_no': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
