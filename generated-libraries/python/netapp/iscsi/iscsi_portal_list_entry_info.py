from netapp.netapp_object import NetAppObject

class IscsiPortalListEntryInfo(NetAppObject):
    """
    information about a single portal
    """
    
    _tpgroup_tag = None
    @property
    def tpgroup_tag(self):
        """
        tag of portal group this portal is associated with
        """
        return self._tpgroup_tag
    @tpgroup_tag.setter
    def tpgroup_tag(self, val):
        if val != None:
            self.validate('tpgroup_tag', val)
        self._tpgroup_tag = val
    
    _ip_port = None
    @property
    def ip_port(self):
        """
        portal listening port
        """
        return self._ip_port
    @ip_port.setter
    def ip_port(self, val):
        if val != None:
            self.validate('ip_port', val)
        self._ip_port = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Name of network interface exporting this portal
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    _ip_address = None
    @property
    def ip_address(self):
        """
        portal IP address
        """
        return self._ip_address
    @ip_address.setter
    def ip_address(self, val):
        if val != None:
            self.validate('ip_address', val)
        self._ip_address = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-portal-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'tpgroup-tag',
            'ip-port',
            'interface-name',
            'ip-address',
        ]
    
    def describe_properties(self):
        return {
            'tpgroup_tag': { 'class': int, 'is_list': False, 'required': 'required' },
            'ip_port': { 'class': int, 'is_list': False, 'required': 'required' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ip_address': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
