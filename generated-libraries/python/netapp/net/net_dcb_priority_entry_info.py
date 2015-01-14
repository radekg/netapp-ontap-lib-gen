from netapp.net.interface_dcb_priority_entry_info import InterfaceDcbPriorityEntryInfo
from netapp.netapp_object import NetAppObject

class NetDcbPriorityEntryInfo(NetAppObject):
    """
    DCB configuration information indexed by the priority about
    a single network interface.
    """
    
    _interface_dcb_priority_entries = None
    @property
    def interface_dcb_priority_entries(self):
        """
        A list of DCB configuration parameters indexed by the priority.
        """
        return self._interface_dcb_priority_entries
    @interface_dcb_priority_entries.setter
    def interface_dcb_priority_entries(self, val):
        if val != None:
            self.validate('interface_dcb_priority_entries', val)
        self._interface_dcb_priority_entries = val
    
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
          return "net-dcb-priority-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'interface-dcb-priority-entries',
            'interface-name',
        ]
    
    def describe_properties(self):
        return {
            'interface_dcb_priority_entries': { 'class': InterfaceDcbPriorityEntryInfo, 'is_list': True, 'required': 'required' },
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
