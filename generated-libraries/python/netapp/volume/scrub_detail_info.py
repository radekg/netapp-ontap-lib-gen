from netapp.netapp_object import NetAppObject

class ScrubDetailInfo(NetAppObject):
    """
    Scrubbing information.
    """
    
    _raid_group = None
    @property
    def raid_group(self):
        """
        Name of the RAID group involved in the scrub.
        """
        return self._raid_group
    @raid_group.setter
    def raid_group(self, val):
        if val != None:
            self.validate('raid_group', val)
        self._raid_group = val
    
    _is_suspended = None
    @property
    def is_suspended(self):
        """
        Suspended state of the scrub on that RAID
        group.
        """
        return self._is_suspended
    @is_suspended.setter
    def is_suspended(self, val):
        if val != None:
            self.validate('is_suspended', val)
        self._is_suspended = val
    
    _last_scrub_timestamp = None
    @property
    def last_scrub_timestamp(self):
        """
        Time at which the last full scrub completed.
        If a scrub has never been performed, this
        value will not be returned.  The time value
        is in seconds since January 1, 1970.
        Range : [0..2^31-1].
        """
        return self._last_scrub_timestamp
    @last_scrub_timestamp.setter
    def last_scrub_timestamp(self, val):
        if val != None:
            self.validate('last_scrub_timestamp', val)
        self._last_scrub_timestamp = val
    
    _percentage_complete = None
    @property
    def percentage_complete(self):
        """
        Scrubbing percentage complete.  I scrubbing
        is not active, this value will not be returned.
        Range : [0..100].
        """
        return self._percentage_complete
    @percentage_complete.setter
    def percentage_complete(self, val):
        if val != None:
            self.validate('percentage_complete', val)
        self._percentage_complete = val
    
    @staticmethod
    def get_api_name():
          return "scrub-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'raid-group',
            'is-suspended',
            'last-scrub-timestamp',
            'percentage-complete',
        ]
    
    def describe_properties(self):
        return {
            'raid_group': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_suspended': { 'class': bool, 'is_list': False, 'required': 'required' },
            'last_scrub_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percentage_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
