from netapp.netapp_object import NetAppObject

class WinsEntryInfo(NetAppObject):
    """
    Windows Internet Name Server (WINS) information
    """
    
    _wins_state = None
    @property
    def wins_state(self):
        """
        WINS Server State. Possible values: 'active', 'inactive'.
        Attributes: non-creatable, non-modifiable
        """
        return self._wins_state
    @wins_state.setter
    def wins_state(self, val):
        if val != None:
            self.validate('wins_state', val)
        self._wins_state = val
    
    _wins_address = None
    @property
    def wins_address(self):
        """
        Windows Internet Name Service (WINS) Server address.
        Attributes: non-creatable, non-modifiable
        """
        return self._wins_address
    @wins_address.setter
    def wins_address(self, val):
        if val != None:
            self.validate('wins_address', val)
        self._wins_address = val
    
    @staticmethod
    def get_api_name():
          return "wins-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'wins-state',
            'wins-address',
        ]
    
    def describe_properties(self):
        return {
            'wins_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'wins_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
