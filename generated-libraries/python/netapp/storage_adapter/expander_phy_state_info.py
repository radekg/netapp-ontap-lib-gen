from netapp.netapp_object import NetAppObject

class ExpanderPhyStateInfo(NetAppObject):
    """
    Expander PHY state information.
    """
    
    _expander_phy_wwn = None
    @property
    def expander_phy_wwn(self):
        """
        Expander PHY's world-wide name.
        """
        return self._expander_phy_wwn
    @expander_phy_wwn.setter
    def expander_phy_wwn(self, val):
        if val != None:
            self.validate('expander_phy_wwn', val)
        self._expander_phy_wwn = val
    
    _expander_phy = None
    @property
    def expander_phy(self):
        """
        A PHY is a transceiver;
        it is the object in a device that
        electrically interfaces to a
        physical link.
        """
        return self._expander_phy
    @expander_phy.setter
    def expander_phy(self, val):
        if val != None:
            self.validate('expander_phy', val)
        self._expander_phy = val
    
    _expander_phy_attached_device_type = None
    @property
    def expander_phy_attached_device_type(self):
        """
        Device type attached to an adapter PHY.
        Possible values:
        <ul>
        <li> "initiator" - A device type that can initiate a SAS communication,
        <li> "expander" - A device type that facilitates communication between multiple SAS devices,
        <li> "sas_end_device" - A SAS device that is not contained within an expander device,
        <li> "sata_end_device" - A SATA end device,
        <li> "unknown" - An unknown device type.
        </ul>
        """
        return self._expander_phy_attached_device_type
    @expander_phy_attached_device_type.setter
    def expander_phy_attached_device_type(self, val):
        if val != None:
            self.validate('expander_phy_attached_device_type', val)
        self._expander_phy_attached_device_type = val
    
    _expander_phy_state = None
    @property
    def expander_phy_state(self):
        """
        Expander PHY state info.
        Possible values:
        <ul>
        <li> "sas_phy_state_enabled_rate_unknown" - PHY is enabled but data transfer rate is unknown,
        <li> "sas_phy_state_disabled"  - PHY is disabled,
        <li> "sas_phy_state_speed_neg_failed" - Data tranfer rate negotiation failed,
        <li> "sas_phy_state_sata_oob_failed" - SATA OOB(Out Of Band) signaling failed,
        <li> "sas_phy_state_enabled_15gbs" - 1.5 Gb/s data transfer rate,
        <li> "sas_phy_state_enabled_30gbs" - 3.0 Gb/s data transfer rate,
        <li> "sas_phy_state_enabled_60gbs" - 6.0 Gb/s data transfer rate,
        <li> "unknown" - Unknown PHY state.
        </ul>
        """
        return self._expander_phy_state
    @expander_phy_state.setter
    def expander_phy_state(self, val):
        if val != None:
            self.validate('expander_phy_state', val)
        self._expander_phy_state = val
    
    @staticmethod
    def get_api_name():
          return "expander-phy-state-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'expander-phy-wwn',
            'expander-phy',
            'expander-phy-attached-device-type',
            'expander-phy-state',
        ]
    
    def describe_properties(self):
        return {
            'expander_phy_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'expander_phy': { 'class': int, 'is_list': False, 'required': 'required' },
            'expander_phy_attached_device_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'expander_phy_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
