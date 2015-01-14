from netapp.storage_adapter.expander_phy_state_info import ExpanderPhyStateInfo
from netapp.netapp_object import NetAppObject

class SasAdapterExpanderPhyStateInfo(NetAppObject):
    """
    Adapter PHY and list of connected expander PHYs.
    """
    
    _adapter_phy = None
    @property
    def adapter_phy(self):
        """
        Adapter PHY connected to a list of expander PHYs.
        """
        return self._adapter_phy
    @adapter_phy.setter
    def adapter_phy(self, val):
        if val != None:
            self.validate('adapter_phy', val)
        self._adapter_phy = val
    
    _expander_phy_states = None
    @property
    def expander_phy_states(self):
        """
        List of all expanders connected to an adapter's
        PHY.
        """
        return self._expander_phy_states
    @expander_phy_states.setter
    def expander_phy_states(self, val):
        if val != None:
            self.validate('expander_phy_states', val)
        self._expander_phy_states = val
    
    @staticmethod
    def get_api_name():
          return "sas-adapter-expander-phy-state-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'adapter-phy',
            'expander-phy-states',
        ]
    
    def describe_properties(self):
        return {
            'adapter_phy': { 'class': int, 'is_list': False, 'required': 'required' },
            'expander_phy_states': { 'class': ExpanderPhyStateInfo, 'is_list': True, 'required': 'required' },
        }
