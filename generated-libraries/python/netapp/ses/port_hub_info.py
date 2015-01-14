from netapp.netapp_object import NetAppObject

class PortHubInfo(NetAppObject):
    """
    Hub information for an individual port.
    """
    
    _insert_count = None
    @property
    def insert_count(self):
        """
        Number of times this port has been inserted into the loop.
        """
        return self._insert_count
    @insert_count.setter
    def insert_count(self, val):
        if val != None:
            self.validate('insert_count', val)
        self._insert_count = val
    
    _port_state = None
    @property
    def port_state(self):
        """
        Current port state. Possible values are: "ok", "empty",
        "byp_init", "byp_gen",
        "byp_man", "byp_xmit", "byp_lipf8", "byp_dto", "byp_rlos",
        "byp_clos", "byp_tbi", "byp_rprt", "byp_stall", "byp_wrd",
        "byp_crc", "byp_lip", "byp_osc", "byp_clk", "byp_mir",
        "byp_lipf7", "byp_bzr", "byp_self", "byp_flt", "byp_pwr",
        "byp_pcycl",
        "warn_lip", "warn_wrdb", "warn_wrd", "warn_crc", "warn_clk",
        "unknown", "term-err", "term", "autoterm".
        """
        return self._port_state
    @port_state.setter
    def port_state(self, val):
        if val != None:
            self.validate('port_state', val)
        self._port_state = val
    
    _utilization_percentage = None
    @property
    def utilization_percentage(self):
        """
        Relative utilization of this port vs. other ports in the ESH.
        """
        return self._utilization_percentage
    @utilization_percentage.setter
    def utilization_percentage(self, val):
        if val != None:
            self.validate('utilization_percentage', val)
        self._utilization_percentage = val
    
    _invalid_word_count = None
    @property
    def invalid_word_count(self):
        """
        Number of times this port has seen invalid FC-AL words
        transmitted.
        """
        return self._invalid_word_count
    @invalid_word_count.setter
    def invalid_word_count(self, val):
        if val != None:
            self.validate('invalid_word_count', val)
        self._invalid_word_count = val
    
    _loop_up_count = None
    @property
    def loop_up_count(self):
        """
        Number of times this port has seen the loop come
        up/transition to up.
        """
        return self._loop_up_count
    @loop_up_count.setter
    def loop_up_count(self, val):
        if val != None:
            self.validate('loop_up_count', val)
        self._loop_up_count = val
    
    _clock_delta = None
    @property
    def clock_delta(self):
        """
        The clock delta between this port in respect to ESH clock
        and other ports in the ESH.
        """
        return self._clock_delta
    @clock_delta.setter
    def clock_delta(self, val):
        if val != None:
            self.validate('clock_delta', val)
        self._clock_delta = val
    
    _port_id = None
    @property
    def port_id(self):
        """
        Possible values are: port number in the range of 0 to 255
        or "in", "out", "aux1" or "aux2" representing input, output
        or one of auxiliary ports. This is the same as FCAL ALPA
        for the port.
        """
        return self._port_id
    @port_id.setter
    def port_id(self, val):
        if val != None:
            self.validate('port_id', val)
        self._port_id = val
    
    _disk_bay = None
    @property
    def disk_bay(self):
        """
        If port-id is "in", "out", "aux1" or "aux2" then this is
        not populated, otherwise, it represents the shelf bay
        that the disk resides in.
        """
        return self._disk_bay
    @disk_bay.setter
    def disk_bay(self, val):
        if val != None:
            self.validate('disk_bay', val)
        self._disk_bay = val
    
    _lip_count = None
    @property
    def lip_count(self):
        """
        Lip count, number of times loop initialization primitive
        has been generated. This field is not available on all shelf
        modules.
        """
        return self._lip_count
    @lip_count.setter
    def lip_count(self, val):
        if val != None:
            self.validate('lip_count', val)
        self._lip_count = val
    
    _invalid_crc_count = None
    @property
    def invalid_crc_count(self):
        """
        Number of times this port has seen a CRC error.
        """
        return self._invalid_crc_count
    @invalid_crc_count.setter
    def invalid_crc_count(self, val):
        if val != None:
            self.validate('invalid_crc_count', val)
        self._invalid_crc_count = val
    
    _stall_count = None
    @property
    def stall_count(self):
        """
        Number of times this port exceeded the OPN/CLS maximum
        threshold.
        """
        return self._stall_count
    @stall_count.setter
    def stall_count(self, val):
        if val != None:
            self.validate('stall_count', val)
        self._stall_count = val
    
    @staticmethod
    def get_api_name():
          return "port-hub-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'insert-count',
            'port-state',
            'utilization-percentage',
            'invalid-word-count',
            'loop-up-count',
            'clock-delta',
            'port-id',
            'disk-bay',
            'lip-count',
            'invalid-crc-count',
            'stall-count',
        ]
    
    def describe_properties(self):
        return {
            'insert_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'port_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'utilization_percentage': { 'class': int, 'is_list': False, 'required': 'required' },
            'invalid_word_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'loop_up_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'clock_delta': { 'class': int, 'is_list': False, 'required': 'required' },
            'port_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'disk_bay': { 'class': int, 'is_list': False, 'required': 'optional' },
            'lip_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'invalid_crc_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'stall_count': { 'class': int, 'is_list': False, 'required': 'required' },
        }
