from netapp.netapp_object import NetAppObject

class ShelfBayPortInfo(NetAppObject):
    """
    Shelf bay port specific information.
    """
    
    _disk_name = None
    @property
    def disk_name(self):
        """
        if port-designator is "disk_bay" and there is a disk installed
        in the bay, then this will be the disk name. Otherwise the
        field will be missing.
        """
        return self._disk_name
    @disk_name.setter
    def disk_name(self, val):
        if val != None:
            self.validate('disk_name', val)
        self._disk_name = val
    
    _port_state = None
    @property
    def port_state(self):
        """
        Current port state. Possible values are: "ok", "empty",
        "unkwn_lnk", "no_signal", "unused", "unkwn", "unknown",
        "dis_man", "dis_unusd", "dis_smp", "dis_loswd", "dis_dispa",
        "dis_invwd", "dis_reset", "dis_phchg", "dis_mir", "dis_crc",
        "dis_clk",
        "byp_init", "byp_gen", "byp_man", "byp_xmit", "byp_lipf8",
        "byp_dto", "byp_rlos", "byp_clos", "byp_tbi", "byp_rprt",
        "byp_stall", "byp_wrd", "byp_crc", "byp_lip", "byp_osc",
        "byp_clk", "byp_mir", "byp_lipf7", "byp_bzr", "byp_self",
        "byp_flt", "byp_pwr", "byp_pcycl",
        "warn_lip", "warn_wrdb", "warn_wrd", "warn_crc", "warn_clk",
        "term-err", "term", "autoterm".
        """
        return self._port_state
    @port_state.setter
    def port_state(self, val):
        if val != None:
            self.validate('port_state', val)
        self._port_state = val
    
    _disk_uid = None
    @property
    def disk_uid(self):
        """
        if port-designator is "disk_bay" and there is a disk installed
        in the bay, then this will be UID of the disk. Otherwise the
        field will be missing.
        """
        return self._disk_uid
    @disk_uid.setter
    def disk_uid(self, val):
        if val != None:
            self.validate('disk_uid', val)
        self._disk_uid = val
    
    _bay_no = None
    @property
    def bay_no(self):
        """
        Disk bay number or port number, if applicable. In some
        instances bay numbers do apply and will not be present. An
        example is an ESH shelf with a single "in" and a single "out"
        port.
        """
        return self._bay_no
    @bay_no.setter
    def bay_no(self, val):
        if val != None:
            self.validate('bay_no', val)
        self._bay_no = val
    
    _port_designator = None
    @property
    def port_designator(self):
        """
        Shelf bay port designator. Possible values:
        "in", "out", "aux", "sqr", "cir", "sil", "hi_ho",
        "a_to_b", "b_to_a", "disk_bay".
        """
        return self._port_designator
    @port_designator.setter
    def port_designator(self, val):
        if val != None:
            self.validate('port_designator', val)
        self._port_designator = val
    
    @staticmethod
    def get_api_name():
          return "shelf-bay-port-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'disk-name',
            'port-state',
            'disk-uid',
            'bay-no',
            'port-designator',
        ]
    
    def describe_properties(self):
        return {
            'disk_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'port_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disk_uid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'bay_no': { 'class': int, 'is_list': False, 'required': 'optional' },
            'port_designator': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
