from netapp.net.interface_dcb_entry_info import InterfaceDcbEntryInfo
from netapp.netapp_object import NetAppObject

class NetDcbEntryInfo(NetAppObject):
    """
    DCB configuration information about a single network interface.
    """
    
    _interface_dcb_entries = None
    @property
    def interface_dcb_entries(self):
        """
        A list of priority group associated DCB configuration parameters
        for a single network interface.
        """
        return self._interface_dcb_entries
    @interface_dcb_entries.setter
    def interface_dcb_entries(self, val):
        if val != None:
            self.validate('interface_dcb_entries', val)
        self._interface_dcb_entries = val
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        The network interface name.
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    @staticmethod
    def get_api_name():
          return "net-dcb-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'interface-dcb-entries',
            'interface-name',
        ]
    
    def describe_properties(self):
        return {
            'interface_dcb_entries': { 'class': InterfaceDcbEntryInfo, 'is_list': True, 'required': 'required' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
