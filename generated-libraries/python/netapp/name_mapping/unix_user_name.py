from netapp.netapp_object import NetAppObject

class UnixUserName(NetAppObject):
    """
    Specifies user name information.
    """
    
    _user_name = None
    @property
    def user_name(self):
        """
        Specifies user's UNIX account name.
        Attributes: non-creatable, non-modifiable
        """
        return self._user_name
    @user_name.setter
    def user_name(self, val):
        if val != None:
            self.validate('user_name', val)
        self._user_name = val
    
    @staticmethod
    def get_api_name():
          return "unix-user-name"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'user-name',
        ]
    
    def describe_properties(self):
        return {
            'user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
