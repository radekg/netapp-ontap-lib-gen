from netapp.netapp_object import NetAppObject

class MailboxIoTimesInfo(NetAppObject):
    """
    Mailbox IO times
    """
    
    _transition = None
    @property
    def transition(self):
        """
        Maximum IO time in milliseconds, transition
        """
        return self._transition
    @transition.setter
    def transition(self, val):
        if val != None:
            self.validate('transition', val)
        self._transition = val
    
    _normal = None
    @property
    def normal(self):
        """
        Maximum IO time in milliseconds, normal
        """
        return self._normal
    @normal.setter
    def normal(self, val):
        if val != None:
            self.validate('normal', val)
        self._normal = val
    
    @staticmethod
    def get_api_name():
          return "mailbox-io-times-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'transition',
            'normal',
        ]
    
    def describe_properties(self):
        return {
            'transition': { 'class': int, 'is_list': False, 'required': 'required' },
            'normal': { 'class': int, 'is_list': False, 'required': 'required' },
        }
