from netapp.fcp.fcp_adapter_zone_member_info import FcpAdapterZoneMemberInfo
from netapp.netapp_object import NetAppObject

class FcpAdapterZoneInfo(NetAppObject):
    """
    Information about a zone.
    """
    
    _adapter = None
    @property
    def adapter(self):
        """
        The adapter this zone is visible through.
        """
        return self._adapter
    @adapter.setter
    def adapter(self, val):
        if val != None:
            self.validate('adapter', val)
        self._adapter = val
    
    _zone_set_name = None
    @property
    def zone_set_name(self):
        """
        The name of the zone set containing this zone. The
        maximum length is 64.
        """
        return self._zone_set_name
    @zone_set_name.setter
    def zone_set_name(self, val):
        if val != None:
            self.validate('zone_set_name', val)
        self._zone_set_name = val
    
    _fcp_adapter_zone_members = None
    @property
    def fcp_adapter_zone_members(self):
        """
        List of zone members.
        """
        return self._fcp_adapter_zone_members
    @fcp_adapter_zone_members.setter
    def fcp_adapter_zone_members(self, val):
        if val != None:
            self.validate('fcp_adapter_zone_members', val)
        self._fcp_adapter_zone_members = val
    
    _zone_name = None
    @property
    def zone_name(self):
        """
        The name of the zone. The maximum length is 64.
        """
        return self._zone_name
    @zone_name.setter
    def zone_name(self, val):
        if val != None:
            self.validate('zone_name', val)
        self._zone_name = val
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-zone-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'adapter',
            'zone-set-name',
            'fcp-adapter-zone-members',
            'zone-name',
        ]
    
    def describe_properties(self):
        return {
            'adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'zone_set_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'fcp_adapter_zone_members': { 'class': FcpAdapterZoneMemberInfo, 'is_list': False, 'required': 'required' },
            'zone_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
