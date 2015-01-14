from netapp.netapp_object import NetAppObject

class SnapvaultSnapcreateOptions(NetAppObject):
    """
    Snap create options.
    """
    
    _tries_count = None
    @property
    def tries_count(self):
        """
        This option is similar to one in snapvault-schedule-options.
        Range:[-1..120]
        """
        return self._tries_count
    @tries_count.setter
    def tries_count(self, val):
        if val != None:
            self.validate('tries_count', val)
        self._tries_count = val
    
    @staticmethod
    def get_api_name():
          return "snapvault-snapcreate-options"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'tries-count',
        ]
    
    def describe_properties(self):
        return {
            'tries_count': { 'class': int, 'is_list': False, 'required': 'required' },
        }
