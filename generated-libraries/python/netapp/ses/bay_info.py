from netapp.netapp_object import NetAppObject

class BayInfo(NetAppObject):
    """
    A list of shelf bay numbers which have disks.
    """
    
    _lun = None
    @property
    def lun(self):
        """
        The logical unit number within the target.
        This field will be present in some storage
        configurations.  In some cases, devices
        with a logical unit number will have LEDs
        that can be affected.
        Range : [0..255]
        """
        return self._lun
    @lun.setter
    def lun(self, val):
        if val != None:
            self.validate('lun', val)
        self._lun = val
    
    _shelf_bay = None
    @property
    def shelf_bay(self):
        """
        A shelf-bay number indicates the presence
        of a drive in that bay.  Shelf bays are
        numbered starting at 0 which is the
        right most drive bay in the shelf when
        viewing the shelf from the front.
        Range: [0..255]
        """
        return self._shelf_bay
    @shelf_bay.setter
    def shelf_bay(self, val):
        if val != None:
            self.validate('shelf_bay', val)
        self._shelf_bay = val
    
    @staticmethod
    def get_api_name():
          return "bay-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'lun',
            'shelf-bay',
        ]
    
    def describe_properties(self):
        return {
            'lun': { 'class': int, 'is_list': False, 'required': 'optional' },
            'shelf_bay': { 'class': int, 'is_list': False, 'required': 'required' },
        }
