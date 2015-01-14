from netapp.net.priority_entry_info import PriorityEntryInfo
from netapp.netapp_object import NetAppObject

class InterfaceDcbEntryInfo(NetAppObject):
    """
    DCB configuration information about a priority group.
    """
    
    _bandwidth_percentage = None
    @property
    def bandwidth_percentage(self):
        """
        Bandwidth assigned to the specified priority group.
        Range: [0..100]
        """
        return self._bandwidth_percentage
    @bandwidth_percentage.setter
    def bandwidth_percentage(self, val):
        if val != None:
            self.validate('bandwidth_percentage', val)
        self._bandwidth_percentage = val
    
    _application = None
    @property
    def application(self):
        """
        Application assigned to the specified priority group.
        """
        return self._application
    @application.setter
    def application(self, val):
        if val != None:
            self.validate('application', val)
        self._application = val
    
    _priority_group_id = None
    @property
    def priority_group_id(self):
        """
        The Priority Group ID. A priority group is a group of
        priorities bound together by management for the purpose of
        bandwidth allocation. All priorities in a single group are
        expected to have similar traffic handling requirements
        (e.g. latency or frame loss).
        Range: [0..15]
        """
        return self._priority_group_id
    @priority_group_id.setter
    def priority_group_id(self, val):
        if val != None:
            self.validate('priority_group_id', val)
        self._priority_group_id = val
    
    _priority_entries = None
    @property
    def priority_entries(self):
        """
        A list of DCB priorities associated to the specified priority group.
        """
        return self._priority_entries
    @priority_entries.setter
    def priority_entries(self, val):
        if val != None:
            self.validate('priority_entries', val)
        self._priority_entries = val
    
    @staticmethod
    def get_api_name():
          return "interface-dcb-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'bandwidth-percentage',
            'application',
            'priority-group-id',
            'priority-entries',
        ]
    
    def describe_properties(self):
        return {
            'bandwidth_percentage': { 'class': int, 'is_list': False, 'required': 'required' },
            'application': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'priority_group_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'priority_entries': { 'class': PriorityEntryInfo, 'is_list': True, 'required': 'required' },
        }
