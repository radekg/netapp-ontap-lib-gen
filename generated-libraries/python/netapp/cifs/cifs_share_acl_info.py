from netapp.cifs.access_rights_info import AccessRightsInfo
from netapp.netapp_object import NetAppObject

class CifsShareAclInfo(NetAppObject):
    """
    Information about single share.
    """
    
    _share_name = None
    @property
    def share_name(self):
        """
        Name of the share.
        """
        return self._share_name
    @share_name.setter
    def share_name(self, val):
        if val != None:
            self.validate('share_name', val)
        self._share_name = val
    
    _user_acl_info = None
    @property
    def user_acl_info(self):
        """
        List of users or Unix groups that have access to
        this share.
        """
        return self._user_acl_info
    @user_acl_info.setter
    def user_acl_info(self, val):
        if val != None:
            self.validate('user_acl_info', val)
        self._user_acl_info = val
    
    @staticmethod
    def get_api_name():
          return "cifs-share-acl-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'share-name',
            'user-acl-info',
        ]
    
    def describe_properties(self):
        return {
            'share_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'user_acl_info': { 'class': AccessRightsInfo, 'is_list': True, 'required': 'required' },
        }
