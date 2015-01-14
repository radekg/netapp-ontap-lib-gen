from netapp.netapp_object import NetAppObject

class FcpAdapterStatsInfo(NetAppObject):
    """
    Statistics for one FC adapter.
    """
    
    _sfp_wavelength = None
    @property
    def sfp_wavelength(self):
        """
        Wavelength for the optical transceiver. Measured
        in nanometers.
        Range [830..860]
        """
        return self._sfp_wavelength
    @sfp_wavelength.setter
    def sfp_wavelength(self, val):
        if val != None:
            self.validate('sfp_wavelength', val)
        self._sfp_wavelength = val
    
    _sfp_part_number = None
    @property
    def sfp_part_number(self):
        """
        Part number for the optical transceiver.
        """
        return self._sfp_part_number
    @sfp_part_number.setter
    def sfp_part_number(self, val):
        if val != None:
            self.validate('sfp_part_number', val)
        self._sfp_part_number = val
    
    _scsi_requests_dropped = None
    @property
    def scsi_requests_dropped(self):
        """
        Number of SCSI requests being dropped.
        """
        return self._scsi_requests_dropped
    @scsi_requests_dropped.setter
    def scsi_requests_dropped(self, val):
        if val != None:
            self.validate('scsi_requests_dropped', val)
        self._scsi_requests_dropped = val
    
    _lr_sent = None
    @property
    def lr_sent(self):
        """
        Number of LRs (Link Reset) sent from the
        target HBA.
        Range [0..2^31-1]
        """
        return self._lr_sent
    @lr_sent.setter
    def lr_sent(self, val):
        if val != None:
            self.validate('lr_sent', val)
        self._lr_sent = val
    
    _total_logins = None
    @property
    def total_logins(self):
        """
        Counts the times of initiators added.
        Each time a new initiator is added, the total
        logins is incremented by 1. Each time an
        initiator is removed, the total logouts is
        incremented by 1.
        """
        return self._total_logins
    @total_logins.setter
    def total_logins(self, val):
        if val != None:
            self.validate('total_logins', val)
        self._total_logins = val
    
    _frame_underruns = None
    @property
    def frame_underruns(self):
        """
        Number of frame underruns detected by the
        adapter during read requests.
        """
        return self._frame_underruns
    @frame_underruns.setter
    def frame_underruns(self, val):
        if val != None:
            self.validate('frame_underruns', val)
        self._frame_underruns = val
    
    _total_logouts = None
    @property
    def total_logouts(self):
        """
        Counts the times of initiators removed.
        Each time a new initiator is added, the total
        logins is incremented by 1. Each time an
        initiator is removed, the total logouts is
        incremented by 1.
        """
        return self._total_logouts
    @total_logouts.setter
    def total_logouts(self, val):
        if val != None:
            self.validate('total_logouts', val)
        self._total_logouts = val
    
    _sfp_tx_power = None
    @property
    def sfp_tx_power(self):
        """
        SFP transmitted optical power, reported to tenth decimal
        in uWatts.
        """
        return self._sfp_tx_power
    @sfp_tx_power.setter
    def sfp_tx_power(self, val):
        if val != None:
            self.validate('sfp_tx_power', val)
        self._sfp_tx_power = val
    
    _sfp_vendor_oui = None
    @property
    def sfp_vendor_oui(self):
        """
        Vendor OUI (The IEEE Organizationally Unique
        Identifier) for the optical transceiver.
        """
        return self._sfp_vendor_oui
    @sfp_vendor_oui.setter
    def sfp_vendor_oui(self, val):
        if val != None:
            self.validate('sfp_vendor_oui', val)
        self._sfp_vendor_oui = val
    
    _lr_received = None
    @property
    def lr_received(self):
        """
        Number of LRs (Link Reset) received by the
        target HBA.
        Range [0..2^31-1]
        """
        return self._lr_received
    @lr_received.setter
    def lr_received(self, val):
        if val != None:
            self.validate('lr_received', val)
        self._lr_received = val
    
    _crc_errors = None
    @property
    def crc_errors(self):
        """
        Total CRC errors occurred.
        """
        return self._crc_errors
    @crc_errors.setter
    def crc_errors(self, val):
        if val != None:
            self.validate('crc_errors', val)
        self._crc_errors = val
    
    _is_sfp_tx_power_in_range = None
    @property
    def is_sfp_tx_power_in_range(self):
        """
        Flag to indicate transmitted optical power is in range.
        """
        return self._is_sfp_tx_power_in_range
    @is_sfp_tx_power_in_range.setter
    def is_sfp_tx_power_in_range(self, val):
        if val != None:
            self.validate('is_sfp_tx_power_in_range', val)
        self._is_sfp_tx_power_in_range = val
    
    _spurious_interrupts = None
    @property
    def spurious_interrupts(self):
        """
        Count of spurious interrupts.
        """
        return self._spurious_interrupts
    @spurious_interrupts.setter
    def spurious_interrupts(self, val):
        if val != None:
            self.validate('spurious_interrupts', val)
        self._spurious_interrupts = val
    
    _sfp_connector = None
    @property
    def sfp_connector(self):
        """
        Connector used with the optical transceiver.
        """
        return self._sfp_connector
    @sfp_connector.setter
    def sfp_connector(self, val):
        if val != None:
            self.validate('sfp_connector', val)
        self._sfp_connector = val
    
    _sfp_formfactor = None
    @property
    def sfp_formfactor(self):
        """
        Form factor of the optical transceiver.
        Possible values: "SFP" (for Small FormFactor).
        """
        return self._sfp_formfactor
    @sfp_formfactor.setter
    def sfp_formfactor(self, val):
        if val != None:
            self.validate('sfp_formfactor', val)
        self._sfp_formfactor = val
    
    _sfp_encoding = None
    @property
    def sfp_encoding(self):
        """
        Encoding used with the optical transceiver.
        Possible values ["8B10B", "?????"]
        """
        return self._sfp_encoding
    @sfp_encoding.setter
    def sfp_encoding(self, val):
        if val != None:
            self.validate('sfp_encoding', val)
        self._sfp_encoding = val
    
    _adapter_resets = None
    @property
    def adapter_resets(self):
        """
        Number of adapter resets occurred.
        """
        return self._adapter_resets
    @adapter_resets.setter
    def adapter_resets(self, val):
        if val != None:
            self.validate('adapter_resets', val)
        self._adapter_resets = val
    
    _invalid_xmit_words = None
    @property
    def invalid_xmit_words(self):
        """
        Number of invalid words transmitted.
        Range [0..2^31-1]
        """
        return self._invalid_xmit_words
    @invalid_xmit_words.setter
    def invalid_xmit_words(self, val):
        if val != None:
            self.validate('invalid_xmit_words', val)
        self._invalid_xmit_words = val
    
    _protocol_errors = None
    @property
    def protocol_errors(self):
        """
        Number of protocol errors occured.
        Range [0..2^31-1]
        """
        return self._protocol_errors
    @protocol_errors.setter
    def protocol_errors(self, val):
        if val != None:
            self.validate('protocol_errors', val)
        self._protocol_errors = val
    
    _discarded_frames = None
    @property
    def discarded_frames(self):
        """
        Number of frames discarded by the target HBA.
        Range [0..2^31-1]
        """
        return self._discarded_frames
    @discarded_frames.setter
    def discarded_frames(self, val):
        if val != None:
            self.validate('discarded_frames', val)
        self._discarded_frames = val
    
    _sfp_date_code = None
    @property
    def sfp_date_code(self):
        """
        Date code for the optical transceiver.
        """
        return self._sfp_date_code
    @sfp_date_code.setter
    def sfp_date_code(self, val):
        if val != None:
            self.validate('sfp_date_code', val)
        self._sfp_date_code = val
    
    _link_breaks = None
    @property
    def link_breaks(self):
        """
        Number of times that the link breaks.
        """
        return self._link_breaks
    @link_breaks.setter
    def link_breaks(self, val):
        if val != None:
            self.validate('link_breaks', val)
        self._link_breaks = val
    
    _ols_received = None
    @property
    def ols_received(self):
        """
        Number of OLSs (Offline Primitive Sequence)
        received by the target HBA.
        Range [0..2^31-1]
        """
        return self._ols_received
    @ols_received.setter
    def ols_received(self, val):
        if val != None:
            self.validate('ols_received', val)
        self._ols_received = val
    
    _is_sfp_rx_power_in_range = None
    @property
    def is_sfp_rx_power_in_range(self):
        """
        Flag to indicate received optical power is in range.
        """
        return self._is_sfp_rx_power_in_range
    @is_sfp_rx_power_in_range.setter
    def is_sfp_rx_power_in_range(self, val):
        if val != None:
            self.validate('is_sfp_rx_power_in_range', val)
        self._is_sfp_rx_power_in_range = val
    
    _queue_depth = None
    @property
    def queue_depth(self):
        """
        Counts the queue depth on the target HBA.
        """
        return self._queue_depth
    @queue_depth.setter
    def queue_depth(self, val):
        if val != None:
            self.validate('queue_depth', val)
        self._queue_depth = val
    
    _nos_received = None
    @property
    def nos_received(self):
        """
        Number of NOSs (Not_Operational Primitive
        Sequence)received by the target HBA.
        Range [0..2^31-1]
        """
        return self._nos_received
    @nos_received.setter
    def nos_received(self, val):
        if val != None:
            self.validate('nos_received', val)
        self._nos_received = val
    
    _sfp_rev = None
    @property
    def sfp_rev(self):
        """
        Revision for the optical transceiver.
        """
        return self._sfp_rev
    @sfp_rev.setter
    def sfp_rev(self, val):
        if val != None:
            self.validate('sfp_rev', val)
        self._sfp_rev = val
    
    _lip_resets = None
    @property
    def lip_resets(self):
        """
        Number of times that a selective Reset
        LIP (Loop Initialization Primitive) occurred.
        LIP reset is used to preform a verndorspecific
        reset at the loop port specified by the AL-PA
        value.
        """
        return self._lip_resets
    @lip_resets.setter
    def lip_resets(self, val):
        if val != None:
            self.validate('lip_resets', val)
        self._lip_resets = val
    
    _sfp_rx_power = None
    @property
    def sfp_rx_power(self):
        """
        SFP received optical power, reported to tenth decimal
        in uWatts.
        """
        return self._sfp_rx_power
    @sfp_rx_power.setter
    def sfp_rx_power(self, val):
        if val != None:
            self.validate('sfp_rx_power', val)
        self._sfp_rx_power = val
    
    _initiators_connected = None
    @property
    def initiators_connected(self):
        """
        Total number of initiators connected to
        this target adapter.
        """
        return self._initiators_connected
    @initiators_connected.setter
    def initiators_connected(self, val):
        if val != None:
            self.validate('initiators_connected', val)
        self._initiators_connected = val
    
    _sfp_vendor_name = None
    @property
    def sfp_vendor_name(self):
        """
        Vendor name for the optical transceiver.
        """
        return self._sfp_vendor_name
    @sfp_vendor_name.setter
    def sfp_vendor_name(self, val):
        if val != None:
            self.validate('sfp_vendor_name', val)
        self._sfp_vendor_name = val
    
    _adapter = None
    @property
    def adapter(self):
        """
        Which FC adapter.
        """
        return self._adapter
    @adapter.setter
    def adapter(self, val):
        if val != None:
            self.validate('adapter', val)
        self._adapter = val
    
    _is_sfp_optical_transceiver_valid = None
    @property
    def is_sfp_optical_transceiver_valid(self):
        """
        Validity of the optical transceiver. Until Data
        ONTAP 8.0.0, this field was incorrectly named
        "is-spf-optical-transceiver-valid". While that
        field is also returned for backward compatibility,
        all new applications must use the current version.
        """
        return self._is_sfp_optical_transceiver_valid
    @is_sfp_optical_transceiver_valid.setter
    def is_sfp_optical_transceiver_valid(self, val):
        if val != None:
            self.validate('is_sfp_optical_transceiver_valid', val)
        self._is_sfp_optical_transceiver_valid = val
    
    _frame_overruns = None
    @property
    def frame_overruns(self):
        """
        Number of frame overruns detected by the
        adapter during write requests.
        """
        return self._frame_overruns
    @frame_overruns.setter
    def frame_overruns(self, val):
        if val != None:
            self.validate('frame_overruns', val)
        self._frame_overruns = val
    
    _sfp_serial_number = None
    @property
    def sfp_serial_number(self):
        """
        Serial number for the optical transceiver.
        """
        return self._sfp_serial_number
    @sfp_serial_number.setter
    def sfp_serial_number(self, val):
        if val != None:
            self.validate('sfp_serial_number', val)
        self._sfp_serial_number = val
    
    _sfp_fc_speedcapabilities = None
    @property
    def sfp_fc_speedcapabilities(self):
        """
        FC speed capabilities for the optical
        transceiver.
        Possible values [1, 2, 4, 8 in Gbps]
        """
        return self._sfp_fc_speedcapabilities
    @sfp_fc_speedcapabilities.setter
    def sfp_fc_speedcapabilities(self, val):
        if val != None:
            self.validate('sfp_fc_speedcapabilities', val)
        self._sfp_fc_speedcapabilities = val
    
    _is_sfp_diagnostics_internally_calibrated = None
    @property
    def is_sfp_diagnostics_internally_calibrated(self):
        """
        Indicates if the SFP diagnostics are internally
        calibrated or not. The optional SFP rx/tx fields
        are invalid (and therefore not provided) if the
        SFP diagnostics are not internally calibrated.
        """
        return self._is_sfp_diagnostics_internally_calibrated
    @is_sfp_diagnostics_internally_calibrated.setter
    def is_sfp_diagnostics_internally_calibrated(self, val):
        if val != None:
            self.validate('is_sfp_diagnostics_internally_calibrated', val)
        self._is_sfp_diagnostics_internally_calibrated = val
    
    @staticmethod
    def get_api_name():
          return "fcp-adapter-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'sfp-wavelength',
            'sfp-part-number',
            'scsi-requests-dropped',
            'lr-sent',
            'total-logins',
            'frame-underruns',
            'total-logouts',
            'sfp-tx-power',
            'sfp-vendor-oui',
            'lr-received',
            'crc-errors',
            'is-sfp-tx-power-in-range',
            'spurious-interrupts',
            'sfp-connector',
            'sfp-formfactor',
            'sfp-encoding',
            'adapter-resets',
            'invalid-xmit-words',
            'protocol-errors',
            'discarded-frames',
            'sfp-date-code',
            'link-breaks',
            'ols-received',
            'is-sfp-rx-power-in-range',
            'queue-depth',
            'nos-received',
            'sfp-rev',
            'lip-resets',
            'sfp-rx-power',
            'initiators-connected',
            'sfp-vendor-name',
            'adapter',
            'is-sfp-optical-transceiver-valid',
            'frame-overruns',
            'sfp-serial-number',
            'sfp-fc-speedcapabilities',
            'is-sfp-diagnostics-internally-calibrated',
        ]
    
    def describe_properties(self):
        return {
            'sfp_wavelength': { 'class': int, 'is_list': False, 'required': 'optional' },
            'sfp_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'scsi_requests_dropped': { 'class': int, 'is_list': False, 'required': 'required' },
            'lr_sent': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_logins': { 'class': int, 'is_list': False, 'required': 'required' },
            'frame_underruns': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_logouts': { 'class': int, 'is_list': False, 'required': 'required' },
            'sfp_tx_power': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sfp_vendor_oui': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lr_received': { 'class': int, 'is_list': False, 'required': 'required' },
            'crc_errors': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_sfp_tx_power_in_range': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'spurious_interrupts': { 'class': int, 'is_list': False, 'required': 'required' },
            'sfp_connector': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sfp_formfactor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sfp_encoding': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_resets': { 'class': int, 'is_list': False, 'required': 'required' },
            'invalid_xmit_words': { 'class': int, 'is_list': False, 'required': 'required' },
            'protocol_errors': { 'class': int, 'is_list': False, 'required': 'required' },
            'discarded_frames': { 'class': int, 'is_list': False, 'required': 'required' },
            'sfp_date_code': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'link_breaks': { 'class': int, 'is_list': False, 'required': 'required' },
            'ols_received': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_sfp_rx_power_in_range': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'queue_depth': { 'class': int, 'is_list': False, 'required': 'required' },
            'nos_received': { 'class': int, 'is_list': False, 'required': 'required' },
            'sfp_rev': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'lip_resets': { 'class': int, 'is_list': False, 'required': 'required' },
            'sfp_rx_power': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'initiators_connected': { 'class': int, 'is_list': False, 'required': 'required' },
            'sfp_vendor_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'is_sfp_optical_transceiver_valid': { 'class': bool, 'is_list': False, 'required': 'required' },
            'frame_overruns': { 'class': int, 'is_list': False, 'required': 'required' },
            'sfp_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'sfp_fc_speedcapabilities': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_sfp_diagnostics_internally_calibrated': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
