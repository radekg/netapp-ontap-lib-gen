from netapp.ses.dongle_info import DongleInfo
from netapp.netapp_object import NetAppObject

class PhyExpanderInfo(NetAppObject):
    """
    Expander PHY (physical layer) information of an individual port.
    """
    
    _phy_change_count = None
    @property
    def phy_change_count(self):
        """
        This field the number of times this logical phy has changed state.
        This count increments when the logical phy transitions from disabled to
        enabled.  This count also increments when the logical phys transitions
        from enabled to disabled.  The value will be the count kept by the
        expander since either power-on or since the counts have been reset.
        """
        return self._phy_change_count
    @phy_change_count.setter
    def phy_change_count(self, val):
        if val != None:
            self.validate('phy_change_count', val)
        self._phy_change_count = val
    
    _crc_error_count = None
    @property
    def crc_error_count(self):
        """
        This field presents the number of CRC errors that have been seen in any
        address or data frames.  The value will be the count kept by the
        expander since either power-on or since the counts have been reset.
        """
        return self._crc_error_count
    @crc_error_count.setter
    def crc_error_count(self, val):
        if val != None:
            self.validate('crc_error_count', val)
        self._crc_error_count = val
    
    _bay_number = None
    @property
    def bay_number(self):
        """
        Bay port number. Unique bay-number for each type of phy-type.
        Present when multiple phy's for a phy-type exist in the
        shelf, such as phy-type "disk", "P0", "P1".
        """
        return self._bay_number
    @bay_number.setter
    def bay_number(self, val):
        if val != None:
            self.validate('bay_number', val)
        self._bay_number = val
    
    _link_rate = None
    @property
    def link_rate(self):
        """
        If port-state is "ok", then this is a floating number, representing
        SAS-1.1 defined negotiated link rate value for the phy in Gb/s.
        Example: 3.0. For all other port states, this field will not be
        available.
        """
        return self._link_rate
    @link_rate.setter
    def link_rate(self, val):
        if val != None:
            self.validate('link_rate', val)
        self._link_rate = val
    
    _dongle_data = None
    @property
    def dongle_data(self):
        """
        dongle information, if there's a dongle installed.
        Will be missing if not supported or not available.
        Present for drive phy only.
        """
        return self._dongle_data
    @dongle_data.setter
    def dongle_data(self, val):
        if val != None:
            self.validate('dongle_data', val)
        self._dongle_data = val
    
    _port_state = None
    @property
    def port_state(self):
        """
        Current port state. Possible values are: "ok", "unkwn_lnk",
        "unused", "unkwn", "empty", "dis_man", "dis_smp", "dis_loswd",
        "dis_dispa", "dis_invwd", "dis_reset", "dis_phchg",
        "dis_mir", "dis_crc", "dis_clk", "dis_resv", "dis_unusd",
        "unknown", "no_signal",
        """
        return self._port_state
    @port_state.setter
    def port_state(self, val):
        if val != None:
            self.validate('port_state', val)
        self._port_state = val
    
    _running_disparity_count = None
    @property
    def running_disparity_count(self):
        """
        The number of Dwords with a running disparity error seen outside
        the phy reset sequence. The value will be the count kept by the
        expander since either power-on or since the counts have been reset.
        """
        return self._running_disparity_count
    @running_disparity_count.setter
    def running_disparity_count(self, val):
        if val != None:
            self.validate('running_disparity_count', val)
        self._running_disparity_count = val
    
    _phy_reset_problem = None
    @property
    def phy_reset_problem(self):
        """
        This field presents the number of times the phy reset sequence has
        failed.  The value will be the count kept by the expander since either
        power-on or since the counts have been reset.
        """
        return self._phy_reset_problem
    @phy_reset_problem.setter
    def phy_reset_problem(self, val):
        if val != None:
            self.validate('phy_reset_problem', val)
        self._phy_reset_problem = val
    
    _reserve_count = None
    @property
    def reserve_count(self):
        """
        This field presents the number of times the driver has been
        reserved via this phy.
        Will be missing if not supported or not available.
        Present for drive phy only.
        """
        return self._reserve_count
    @reserve_count.setter
    def reserve_count(self, val):
        if val != None:
            self.validate('reserve_count', val)
        self._reserve_count = val
    
    _release_count = None
    @property
    def release_count(self):
        """
        This field presents the number of times the driver has been
        released (unreserved) via this phy.
        Will be missing if not supported or not available.
        Present for drive phy only.
        """
        return self._release_count
    @release_count.setter
    def release_count(self, val):
        if val != None:
            self.validate('release_count', val)
        self._release_count = val
    
    _port_id = None
    @property
    def port_id(self):
        """
        Possible values are: port id in range [0..19] or "in0", "in1",
        "in2", "in3", "out0", "out1", "out2", "out3", representing
        one of the input or output ports.
        """
        return self._port_id
    @port_id.setter
    def port_id(self, val):
        if val != None:
            self.validate('port_id', val)
        self._port_id = val
    
    _pathway_timeout = None
    @property
    def pathway_timeout(self):
        """
        This field the partial pathway timeout value, in microseconds,
        being used for the phy.
        """
        return self._pathway_timeout
    @pathway_timeout.setter
    def pathway_timeout(self, val):
        if val != None:
            self.validate('pathway_timeout', val)
        self._pathway_timeout = val
    
    _phy_type = None
    @property
    def phy_type(self):
        """
        PHY type. Possible values:
        "disk", "p0", "p1", "v255", "v99".
        """
        return self._phy_type
    @phy_type.setter
    def phy_type(self, val):
        if val != None:
            self.validate('phy_type', val)
        self._phy_type = val
    
    _phy_number = None
    @property
    def phy_number(self):
        """
        PHY number. Unique phy-number in the shelf, regardless of phy-type.
        """
        return self._phy_number
    @phy_number.setter
    def phy_number(self, val):
        if val != None:
            self.validate('phy_number', val)
        self._phy_number = val
    
    _phy_power_status = None
    @property
    def phy_power_status(self):
        """
        Current power status. Possible values:
        "on", "off".
        Will be missing if not supported or not available.
        Present for drive phy only.
        """
        return self._phy_power_status
    @phy_power_status.setter
    def phy_power_status(self, val):
        if val != None:
            self.validate('phy_power_status', val)
        self._phy_power_status = val
    
    _loss_dword_count = None
    @property
    def loss_dword_count(self):
        """
        This field presents the number of times the phy has lost double-word
        synchronization and restarted the link reset sequence of the phy reset
        sequence.  The value will be the count kept by the expander since
        either power-on or since the counts have been reset.
        """
        return self._loss_dword_count
    @loss_dword_count.setter
    def loss_dword_count(self, val):
        if val != None:
            self.validate('loss_dword_count', val)
        self._loss_dword_count = val
    
    _invalid_dword_count = None
    @property
    def invalid_dword_count(self):
        """
        The number of invalid double words seen outside of the phy reset
        sequence. The value will be the count kept by the expander
        since either power-on or since the counts have been reset.
        """
        return self._invalid_dword_count
    @invalid_dword_count.setter
    def invalid_dword_count(self, val):
        if val != None:
            self.validate('invalid_dword_count', val)
        self._invalid_dword_count = val
    
    _phy_state = None
    @property
    def phy_state(self):
        """
        State of the phy. Possible values:
        "rate_unknown", "disabled", "speed_negotiation_failed",
        "sata_oob_failed", "1.5_gbps", "3.0_gbps", "6.0_gbps",
        "state_unknown",
        """
        return self._phy_state
    @phy_state.setter
    def phy_state(self, val):
        if val != None:
            self.validate('phy_state', val)
        self._phy_state = val
    
    _power_cycle_count = None
    @property
    def power_cycle_count(self):
        """
        This field presents the number of times the driver has been
        power cycled via this phy.
        Will be missing if not supported or not available.
        Present for drive phy only.
        """
        return self._power_cycle_count
    @power_cycle_count.setter
    def power_cycle_count(self, val):
        if val != None:
            self.validate('power_cycle_count', val)
        self._power_cycle_count = val
    
    @staticmethod
    def get_api_name():
          return "phy-expander-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'phy-change-count',
            'crc-error-count',
            'bay-number',
            'link-rate',
            'dongle-data',
            'port-state',
            'running-disparity-count',
            'phy-reset-problem',
            'reserve-count',
            'release-count',
            'port-id',
            'pathway-timeout',
            'phy-type',
            'phy-number',
            'phy-power-status',
            'loss-dword-count',
            'invalid-dword-count',
            'phy-state',
            'power-cycle-count',
        ]
    
    def describe_properties(self):
        return {
            'phy_change_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'crc_error_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'bay_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'link_rate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'dongle_data': { 'class': DongleInfo, 'is_list': False, 'required': 'optional' },
            'port_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'running_disparity_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'phy_reset_problem': { 'class': int, 'is_list': False, 'required': 'required' },
            'reserve_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'release_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'port_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'pathway_timeout': { 'class': int, 'is_list': False, 'required': 'required' },
            'phy_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'phy_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'phy_power_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'loss_dword_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'invalid_dword_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'phy_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'power_cycle_count': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
