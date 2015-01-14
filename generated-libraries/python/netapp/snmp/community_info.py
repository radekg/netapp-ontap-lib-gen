from netapp.netapp_object import NetAppObject

class CommunityInfo(NetAppObject):
    """
    Information about a single community.
    """
    
    _access_control = None
    @property
    def access_control(self):
        """
        Access control of the community.  Possible
        values are "ro" (read-only), and "rw" (read-write).
        """
        return self._access_control
    @access_control.setter
    def access_control(self, val):
        if val != None:
            self.validate('access_control', val)
        self._access_control = val
    
    _community = None
    @property
    def community(self):
        """
        Community name.
        """
        return self._community
    @community.setter
    def community(self, val):
        if val != None:
            self.validate('community', val)
        self._community = val
    
    @staticmethod
    def get_api_name():
          return "community-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'access-control',
            'community',
        ]
    
    def describe_properties(self):
        return {
            'access_control': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'community': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
