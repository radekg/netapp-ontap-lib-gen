from netapp.netapp_object import NetAppObject

class PriorityEntryInfo(NetAppObject):
    """
    A priority associated to the specified priority group.
    """
    
    _priority = None
    @property
    def priority(self):
        """
        The priority associated with the specified priority group.
        Range: [0..7]
        """
        return self._priority
    @priority.setter
    def priority(self, val):
        if val != None:
            self.validate('priority', val)
        self._priority = val
    
    @staticmethod
    def get_api_name():
          return "priority-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'priority',
        ]
    
    def describe_properties(self):
        return {
            'priority': { 'class': int, 'is_list': False, 'required': 'required' },
        }
