from netapp.storage_adapter.phy_state_info import PhyStateInfo
from netapp.storage_adapter.sas_adapter_expander_phy_state_info import SasAdapterExpanderPhyStateInfo
from netapp.storage_adapter.sas_qsfp_cable_info import SasQsfpCableInfo
from netapp.netapp_object import NetAppObject

class AdapterSasInfo(NetAppObject):
    """
    Detailed information for sas (Serial Attached SCSI)
    adapter.
    """
    
    _adapter_manufacturer = None
    @property
    def adapter_manufacturer(self):
        """
        Manufacturing facility where adapter was built.
        Will be missing if data not available or not supported.
        """
        return self._adapter_manufacturer
    @adapter_manufacturer.setter
    def adapter_manufacturer(self, val):
        if val != None:
            self.validate('adapter_manufacturer', val)
        self._adapter_manufacturer = val
    
    _is_in_use = None
    @property
    def is_in_use(self):
        """
        Is adapter in use? true or false.
        """
        return self._is_in_use
    @is_in_use.setter
    def is_in_use(self, val):
        if val != None:
            self.validate('is_in_use', val)
        self._is_in_use = val
    
    _sas_phy = None
    @property
    def sas_phy(self):
        """
        List of adapter PHY state info.
        """
        return self._sas_phy
    @sas_phy.setter
    def sas_phy(self, val):
        if val != None:
            self.validate('sas_phy', val)
        self._sas_phy = val
    
    _adapter_vendor = None
    @property
    def adapter_vendor(self):
        """
        Represents the adapter vendor. Example: Qlogic.
        Will be missing if data not available or not supported.
        """
        return self._adapter_vendor
    @adapter_vendor.setter
    def adapter_vendor(self, val):
        if val != None:
            self.validate('adapter_vendor', val)
        self._adapter_vendor = val
    
    _adapter_serial_number = None
    @property
    def adapter_serial_number(self):
        """
        Adapter serial number.
        Will be missing if data not available or not supported.
        """
        return self._adapter_serial_number
    @adapter_serial_number.setter
    def adapter_serial_number(self, val):
        if val != None:
            self.validate('adapter_serial_number', val)
        self._adapter_serial_number = val
    
    _is_redundant = None
    @property
    def is_redundant(self):
        """
        Is adapter dual-attached? true or false.
        """
        return self._is_redundant
    @is_redundant.setter
    def is_redundant(self, val):
        if val != None:
            self.validate('is_redundant', val)
        self._is_redundant = val
    
    _hardware_rev = None
    @property
    def hardware_rev(self):
        """
        This is the hardware chip revision of adapter.
        """
        return self._hardware_rev
    @hardware_rev.setter
    def hardware_rev(self, val):
        if val != None:
            self.validate('hardware_rev', val)
        self._hardware_rev = val
    
    _adapter_part_number = None
    @property
    def adapter_part_number(self):
        """
        Adapter part number assigned by the vendor.
        Will be missing if data not available or not supported.
        """
        return self._adapter_part_number
    @adapter_part_number.setter
    def adapter_part_number(self, val):
        if val != None:
            self.validate('adapter_part_number', val)
        self._adapter_part_number = val
    
    _sas_adapter_disabled_phy_count = None
    @property
    def sas_adapter_disabled_phy_count(self):
        """
        Number of disabled PHYs on the host adapter.
        """
        return self._sas_adapter_disabled_phy_count
    @sas_adapter_disabled_phy_count.setter
    def sas_adapter_disabled_phy_count(self, val):
        if val != None:
            self.validate('sas_adapter_disabled_phy_count', val)
        self._sas_adapter_disabled_phy_count = val
    
    _adapter_manufacturer_part_number = None
    @property
    def adapter_manufacturer_part_number(self):
        """
        Adapter part number assigned by the manufacturer.
        Will be missing if data not available or not supported.
        """
        return self._adapter_manufacturer_part_number
    @adapter_manufacturer_part_number.setter
    def adapter_manufacturer_part_number(self, val):
        if val != None:
            self.validate('adapter_manufacturer_part_number', val)
        self._adapter_manufacturer_part_number = val
    
    _sas_adapter_expander_phy_states = None
    @property
    def sas_adapter_expander_phy_states(self):
        """
        List of expander PHYs, a SAS adapter transceivers, state info.
        It will be missing if data is not available or if no expander
        is connected to the adapter.
        """
        return self._sas_adapter_expander_phy_states
    @sas_adapter_expander_phy_states.setter
    def sas_adapter_expander_phy_states(self, val):
        if val != None:
            self.validate('sas_adapter_expander_phy_states', val)
        self._sas_adapter_expander_phy_states = val
    
    _adapter_slot = None
    @property
    def adapter_slot(self):
        """
        Slot number for the adapter port.
        """
        return self._adapter_slot
    @adapter_slot.setter
    def adapter_slot(self, val):
        if val != None:
            self.validate('adapter_slot', val)
        self._adapter_slot = val
    
    _sas_qsfp_cable = None
    @property
    def sas_qsfp_cable(self):
        """
        QSFP information of the cable.
        QSFP is acronym for Quad Small Form-factor Pluggable..
        Will be missing if data not available or not
        or cable not present supported.
        """
        return self._sas_qsfp_cable
    @sas_qsfp_cable.setter
    def sas_qsfp_cable(self, val):
        if val != None:
            self.validate('sas_qsfp_cable', val)
        self._sas_qsfp_cable = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        Is the adapter enabled?
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _adapter_state = None
    @property
    def adapter_state(self):
        """
        Current state of the adapter. Possible values:
        "up", "down", "offline_soft", "offline_hard", "offline_loopback".
        """
        return self._adapter_state
    @adapter_state.setter
    def adapter_state(self, val):
        if val != None:
            self.validate('adapter_state', val)
        self._adapter_state = val
    
    _sas_adapter_enabled_phy_count = None
    @property
    def sas_adapter_enabled_phy_count(self):
        """
        Number of enabled PHYs on the host adapter.
        """
        return self._sas_adapter_enabled_phy_count
    @sas_adapter_enabled_phy_count.setter
    def sas_adapter_enabled_phy_count(self, val):
        if val != None:
            self.validate('sas_adapter_enabled_phy_count', val)
        self._sas_adapter_enabled_phy_count = val
    
    _adapter_model = None
    @property
    def adapter_model(self):
        """
        Model of the adapter.
        This is the same as adapter-vendor followed
        with adapter-family. Example: "Qlogic 2432"
        """
        return self._adapter_model
    @adapter_model.setter
    def adapter_model(self, val):
        if val != None:
            self.validate('adapter_model', val)
        self._adapter_model = val
    
    _firmware_rev = None
    @property
    def firmware_rev(self):
        """
        Firmware revision of adapter
        """
        return self._firmware_rev
    @firmware_rev.setter
    def firmware_rev(self, val):
        if val != None:
            self.validate('firmware_rev', val)
        self._firmware_rev = val
    
    _base_wwn = None
    @property
    def base_wwn(self):
        """
        Physical base node world-wide name
        """
        return self._base_wwn
    @base_wwn.setter
    def base_wwn(self, val):
        if val != None:
            self.validate('base_wwn', val)
        self._base_wwn = val
    
    _adapter_family = None
    @property
    def adapter_family(self):
        """
        Adapter family as assigned by the vendor. Example: 2432.
        Will be missing if data not available or not supported.
        """
        return self._adapter_family
    @adapter_family.setter
    def adapter_family(self, val):
        if val != None:
            self.validate('adapter_family', val)
        self._adapter_family = val
    
    _adapter_board_revision = None
    @property
    def adapter_board_revision(self):
        """
        Adapter board revision as assigned by the manufacturer.
        Will be missing if data not available or not supported.
        """
        return self._adapter_board_revision
    @adapter_board_revision.setter
    def adapter_board_revision(self, val):
        if val != None:
            self.validate('adapter_board_revision', val)
        self._adapter_board_revision = val
    
    _adapter_date_code = None
    @property
    def adapter_date_code(self):
        """
        Adapter data code assigned by the manufacturer.
        Will be missing if data not available or not supported.
        """
        return self._adapter_date_code
    @adapter_date_code.setter
    def adapter_date_code(self, val):
        if val != None:
            self.validate('adapter_date_code', val)
        self._adapter_date_code = val
    
    @staticmethod
    def get_api_name():
          return "adapter-sas-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'adapter-manufacturer',
            'is-in-use',
            'sas-phy',
            'adapter-vendor',
            'adapter-serial-number',
            'is-redundant',
            'hardware-rev',
            'adapter-part-number',
            'sas-adapter-disabled-phy-count',
            'adapter-manufacturer-part-number',
            'sas-adapter-expander-phy-states',
            'adapter-slot',
            'sas-qsfp-cable',
            'is-enabled',
            'adapter-state',
            'sas-adapter-enabled-phy-count',
            'adapter-model',
            'firmware-rev',
            'base-wwn',
            'adapter-family',
            'adapter-board-revision',
            'adapter-date-code',
        ]
    
    def describe_properties(self):
        return {
            'adapter_manufacturer': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_in_use': { 'class': bool, 'is_list': False, 'required': 'required' },
            'sas_phy': { 'class': PhyStateInfo, 'is_list': True, 'required': 'optional' },
            'adapter_vendor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_redundant': { 'class': bool, 'is_list': False, 'required': 'required' },
            'hardware_rev': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sas_adapter_disabled_phy_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'adapter_manufacturer_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sas_adapter_expander_phy_states': { 'class': SasAdapterExpanderPhyStateInfo, 'is_list': True, 'required': 'optional' },
            'adapter_slot': { 'class': int, 'is_list': False, 'required': 'required' },
            'sas_qsfp_cable': { 'class': SasQsfpCableInfo, 'is_list': False, 'required': 'optional' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'adapter_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'sas_adapter_enabled_phy_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'adapter_model': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'firmware_rev': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'base_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_family': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_board_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_date_code': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
