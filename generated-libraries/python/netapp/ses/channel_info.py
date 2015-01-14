from netapp.netapp_object import NetAppObject

class ChannelInfo(NetAppObject):
    """
    A list of channel-names that can be used in other
    storage-shelf interface calls.
    """
    
    _channel_name = None
    @property
    def channel_name(self):
        """
        The adapter number or switch name and
        the port number (together, called the
        channel). Examples are 8a and switch:5
        """
        return self._channel_name
    @channel_name.setter
    def channel_name(self, val):
        if val != None:
            self.validate('channel_name', val)
        self._channel_name = val
    
    @staticmethod
    def get_api_name():
          return "channel-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'channel-name',
        ]
    
    def describe_properties(self):
        return {
            'channel_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
