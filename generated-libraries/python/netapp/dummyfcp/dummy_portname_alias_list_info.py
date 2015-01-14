from netapp.ntdtest.ntdtest_info import NtdtestInfo
from netapp.netapp_object import NetAppObject

class DummyPortnameAliasListInfo(NetAppObject):
    """
    List of aliases for the portname
    """
    
    _initiator_group_list = None
    @property
    def initiator_group_list(self):
        """
        Igroup Name
        Attributes: required-for-create, modifiable
        """
        return self._initiator_group_list
    @initiator_group_list.setter
    def initiator_group_list(self, val):
        if val != None:
            self.validate('initiator_group_list', val)
        self._initiator_group_list = val
    
    _portname_alias_name = None
    @property
    def portname_alias_name(self):
        """
        WWPN Alias
        Attributes: required-for-create, modifiable
        """
        return self._portname_alias_name
    @portname_alias_name.setter
    def portname_alias_name(self, val):
        if val != None:
            self.validate('portname_alias_name', val)
        self._portname_alias_name = val
    
    @staticmethod
    def get_api_name():
          return "dummy-portname-alias-list-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'initiator-group-list',
            'portname-alias-name',
        ]
    
    def describe_properties(self):
        return {
            'initiator_group_list': { 'class': NtdtestInfo, 'is_list': True, 'required': 'optional' },
            'portname_alias_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
