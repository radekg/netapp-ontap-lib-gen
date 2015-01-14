from netapp.netapp_object import NetAppObject

class MediascrubDetailInfo(NetAppObject):
    """
    Information about media scrubbing.
    """
    
    _raid_group = None
    @property
    def raid_group(self):
        """
        Name of the RAID group.
        """
        return self._raid_group
    @raid_group.setter
    def raid_group(self, val):
        if val != None:
            self.validate('raid_group', val)
        self._raid_group = val
    
    _mediascrub_status = None
    @property
    def mediascrub_status(self):
        """
        Possible values are "suspended", "disabled" and "enabled"
        "suspended": Media scrub is enabled but temporarily paused
        because another task is running or it is in the idle cycle of
        its periodic run. It will resume automatically when the task is done
        or the idle cycle ends.
        "disabled": Media scrub feature is turned off.
        "enabled": Media scrub feature is active.
        """
        return self._mediascrub_status
    @mediascrub_status.setter
    def mediascrub_status(self, val):
        if val != None:
            self.validate('mediascrub_status', val)
        self._mediascrub_status = val
    
    _percentage_complete = None
    @property
    def percentage_complete(self):
        """
        Media scrubbing percentage complete.
        Range: [0..100].
        """
        return self._percentage_complete
    @percentage_complete.setter
    def percentage_complete(self, val):
        if val != None:
            self.validate('percentage_complete', val)
        self._percentage_complete = val
    
    @staticmethod
    def get_api_name():
          return "mediascrub-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'raid-group',
            'mediascrub-status',
            'percentage-complete',
        ]
    
    def describe_properties(self):
        return {
            'raid_group': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'mediascrub_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'percentage_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
