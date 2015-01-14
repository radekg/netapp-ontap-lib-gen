from netapp.netapp_object import NetAppObject

class DiskSpareInfo(NetAppObject):
    """
    Details giving disk's basic disposition within its overlying
    spare pool.  Information that is specific to a disk that is
    contained within a spare pool belongs here.
    """
    
    _is_media_scrubbing = None
    @property
    def is_media_scrubbing(self):
        """
        True if media scrub is currently active for this disk.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._is_media_scrubbing
    @is_media_scrubbing.setter
    def is_media_scrubbing(self, val):
        if val != None:
            self.validate('is_media_scrubbing', val)
        self._is_media_scrubbing = val
    
    _zeroing_percent_complete = None
    @property
    def zeroing_percent_complete(self):
        """
        Percent completion of disk zeroing.
        Omitted if is-zeroing' is not true,
        or if excluded by 'desired-attributes'.
        """
        return self._zeroing_percent_complete
    @zeroing_percent_complete.setter
    def zeroing_percent_complete(self, val):
        if val != None:
            self.validate('zeroing_percent_complete', val)
        self._zeroing_percent_complete = val
    
    _is_zeroed = None
    @property
    def is_zeroed(self):
        """
        True if disk has been pre-zeroed.  Omitted if
        excluded by 'desired-attributes'.
        """
        return self._is_zeroed
    @is_zeroed.setter
    def is_zeroed(self, val):
        if val != None:
            self.validate('is_zeroed', val)
        self._is_zeroed = val
    
    _is_sparecore = None
    @property
    def is_sparecore(self):
        """
        True if disk is sparecore disk.  Omitted if
        excluded by 'desired-attributes'.
        """
        return self._is_sparecore
    @is_sparecore.setter
    def is_sparecore(self, val):
        if val != None:
            self.validate('is_sparecore', val)
        self._is_sparecore = val
    
    _is_zeroing = None
    @property
    def is_zeroing(self):
        """
        True if disk is in process of being zeroed.
        Omitted if excluded by 'desired-attributes'.
        """
        return self._is_zeroing
    @is_zeroing.setter
    def is_zeroing(self, val):
        if val != None:
            self.validate('is_zeroing', val)
        self._is_zeroing = val
    
    _is_offline = None
    @property
    def is_offline(self):
        """
        True if disk is offline.  Omitted if excluded
        by 'desired-attributes'.
        """
        return self._is_offline
    @is_offline.setter
    def is_offline(self, val):
        if val != None:
            self.validate('is_offline', val)
        self._is_offline = val
    
    @staticmethod
    def get_api_name():
          return "disk-spare-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-media-scrubbing',
            'zeroing-percent-complete',
            'is-zeroed',
            'is-sparecore',
            'is-zeroing',
            'is-offline',
        ]
    
    def describe_properties(self):
        return {
            'is_media_scrubbing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'zeroing_percent_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_zeroed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_sparecore': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_zeroing': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_offline': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
