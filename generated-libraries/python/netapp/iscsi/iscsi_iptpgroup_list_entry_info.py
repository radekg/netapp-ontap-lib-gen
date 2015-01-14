from netapp.iscsi.ipaddress_list_entry_info import IpaddressListEntryInfo
from netapp.netapp_object import NetAppObject

class IscsiIptpgroupListEntryInfo(NetAppObject):
    """
    Information about a single portal group
    """
    
    _tpgroup_tag = None
    @property
    def tpgroup_tag(self):
        """
        Portal group tag
        """
        return self._tpgroup_tag
    @tpgroup_tag.setter
    def tpgroup_tag(self, val):
        if val != None:
            self.validate('tpgroup_tag', val)
        self._tpgroup_tag = val
    
    _tpgroup_name = None
    @property
    def tpgroup_name(self):
        """
        Portal group name
        """
        return self._tpgroup_name
    @tpgroup_name.setter
    def tpgroup_name(self, val):
        if val != None:
            self.validate('tpgroup_name', val)
        self._tpgroup_name = val
    
    _ipaddress_list_entries = None
    @property
    def ipaddress_list_entries(self):
        """
        List of IP Addresses associated with this iptpgroup
        """
        return self._ipaddress_list_entries
    @ipaddress_list_entries.setter
    def ipaddress_list_entries(self, val):
        if val != None:
            self.validate('ipaddress_list_entries', val)
        self._ipaddress_list_entries = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-iptpgroup-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'tpgroup-tag',
            'tpgroup-name',
            'ipaddress-list-entries',
        ]
    
    def describe_properties(self):
        return {
            'tpgroup_tag': { 'class': int, 'is_list': False, 'required': 'required' },
            'tpgroup_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ipaddress_list_entries': { 'class': IpaddressListEntryInfo, 'is_list': True, 'required': 'required' },
        }
