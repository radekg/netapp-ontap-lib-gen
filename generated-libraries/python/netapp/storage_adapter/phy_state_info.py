from netapp.netapp_object import NetAppObject

class PhyStateInfo(NetAppObject):
    """
    Adapter PHY state information.
    """
    
    _phy_wwn = None
    @property
    def phy_wwn(self):
        """
        Adapter PHY's world-wide name.
        """
        return self._phy_wwn
    @phy_wwn.setter
    def phy_wwn(self, val):
        if val != None:
            self.validate('phy_wwn', val)
        self._phy_wwn = val
    
    _phy = None
    @property
    def phy(self):
        """
        A PHY is a transceiver;
        it is the object in a device that
        electrically interfaces to a
        physical link.
        """
        return self._phy
    @phy.setter
    def phy(self, val):
        if val != None:
            self.validate('phy', val)
        self._phy = val
    
    _phy_state = None
    @property
    def phy_state(self):
        """
        Adapter PHY state info.
        Possible values:
        "sas_phy_state_enabled_rate_unknown",
        "sas_phy_state_disabled",
        "sas_phy_state_speed_neg_failed",
        "sas_phy_state_SATA_OOB_failed",
        "sas_phy_state_enabled_15gbs",
        "sas_phy_state_enabled_30gbs",
        "sas_phy_state_enabled_60gbs",
        "unknown".
        """
        return self._phy_state
    @phy_state.setter
    def phy_state(self, val):
        if val != None:
            self.validate('phy_state', val)
        self._phy_state = val
    
    @staticmethod
    def get_api_name():
          return "phy-state-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'phy-wwn',
            'phy',
            'phy-state',
        ]
    
    def describe_properties(self):
        return {
            'phy_wwn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'phy': { 'class': int, 'is_list': False, 'required': 'required' },
            'phy_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
