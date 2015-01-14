from netapp.netapp_object import NetAppObject

class SasSpecificInfo(NetAppObject):
    """
    Vendor specific enclosure system information for
    SAS shelf.
    """
    
    _serial_no = None
    @property
    def serial_no(self):
        """
        Shelf backplane serial number.
        """
        return self._serial_no
    @serial_no.setter
    def serial_no(self, val):
        if val != None:
            self.validate('serial_no', val)
        self._serial_no = val
    
    @staticmethod
    def get_api_name():
          return "sas-specific-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'serial-no',
        ]
    
    def describe_properties(self):
        return {
            'serial_no': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
