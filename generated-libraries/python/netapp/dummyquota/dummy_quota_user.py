from netapp.netapp_object import NetAppObject

class DummyQuotaUser(NetAppObject):
    """
    Quota user info
    """
    
    _quota_user_name = None
    @property
    def quota_user_name(self):
        """
        Quota User Names
        Attributes: required-for-create, modifiable
        """
        return self._quota_user_name
    @quota_user_name.setter
    def quota_user_name(self, val):
        if val != None:
            self.validate('quota_user_name', val)
        self._quota_user_name = val
    
    _quota_user_type = None
    @property
    def quota_user_type(self):
        """
        Quota User Types
        Attributes: required-for-create, modifiable
        """
        return self._quota_user_type
    @quota_user_type.setter
    def quota_user_type(self, val):
        if val != None:
            self.validate('quota_user_type', val)
        self._quota_user_type = val
    
    _quota_user_id = None
    @property
    def quota_user_id(self):
        """
        Quota User IDs
        Attributes: required-for-create, modifiable
        """
        return self._quota_user_id
    @quota_user_id.setter
    def quota_user_id(self, val):
        if val != None:
            self.validate('quota_user_id', val)
        self._quota_user_id = val
    
    @staticmethod
    def get_api_name():
          return "dummy-quota-user"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'quota-user-name',
            'quota-user-type',
            'quota-user-id',
        ]
    
    def describe_properties(self):
        return {
            'quota_user_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quota_user_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quota_user_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
