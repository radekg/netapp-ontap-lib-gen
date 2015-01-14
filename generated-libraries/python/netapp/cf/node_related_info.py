from netapp.netapp_object import NetAppObject

class NodeRelatedInfo(NetAppObject):
    """
    Node Info
    """
    
    _node = None
    @property
    def node(self):
        """
        Node name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _local_firmware_state = None
    @property
    def local_firmware_state(self):
        """
        Local firmware state that will be communicated through
        interconnect to the partner.
        Possible values are:
        <ul>
        <li>SF_OPERATOR_EXIT       - operator completed</li>
        <li>SF_DEBUG_EXIT          - debugger completed</li>
        <li>SF_PROGRESS            - progress counter</li>
        <li>SF_IOERROR             - I/O error</li>
        <li>SF_BADCKSUM            - bad checksum</li>
        <li>SF_RESERVED            - reserved</li>
        <li>SF_UNKNOWN             - unknown</li>
        <li>SF_OPEN                - initializing</li>
        <li>SF_POST                - in power-on self test</li>
        <li>SF_BOOTING             - booting</li>
        <li>SF_FAIL                - boot failed</li>
        <li>SF_WAITING             - waiting</li>
        <li>SF_OS_BOOTED           - kernel loaded</li>
        <li>SF_UP                  - up</li>
        <li>SF_DEBUG               - in debugger</li>
        <li>SF_OPERATOR            - waiting for operator
        input</li>
        <li>SF_DUMPCORE            - dumping core</li>
        <li>SF_HALT                - halted</li>
        <li>SF_REBOOT              - rebooting</li>
        <li>SF_GIVEWAIT            - waiting for giveback</li>
        <li>SF_MBWAIT              - waiting for cluster mailbox
        release</li>
        <li>SF_SPARECORE           - dumping sparecore and ready
        to be taken-over</li>
        <li>SF_MDP                 - multi-disk panic</li>
        <li>SF_TO                  - in takeover</li>
        <li>SF_NOTO		   - takeover disabled</li>
        <li>SF_CLUSTERWAIT	   - waiting for cluster
        apps</li></ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._local_firmware_state
    @local_firmware_state.setter
    def local_firmware_state(self, val):
        if val != None:
            self.validate('local_firmware_state', val)
        self._local_firmware_state = val
    
    _nvram_id = None
    @property
    def nvram_id(self):
        """
        NVRAM identifier
        Attributes: non-creatable, non-modifiable
        """
        return self._nvram_id
    @nvram_id.setter
    def nvram_id(self, val):
        if val != None:
            self.validate('nvram_id', val)
        self._nvram_id = val
    
    _partner_firmware_state = None
    @property
    def partner_firmware_state(self):
        """
        Partner firmware state as communicated by the partner
        through interconnect.
        Possible values are:
        <ul>
        <li>SF_OPERATOR_EXIT       - operator completed</li>
        <li>SF_DEBUG_EXIT          - debugger completed</li>
        <li>SF_PROGRESS            - progress counter</li>
        <li>SF_IOERROR             - I/O error</li>
        <li>SF_BADCKSUM            - bad checksum</li>
        <li>SF_RESERVED            - reserved</li>
        <li>SF_UNKNOWN             - unknown</li>
        <li>SF_OPEN                - initializing</li>
        <li>SF_POST                - in power-on self test</li>
        <li>SF_BOOTING             - booting</li>
        <li>SF_FAIL                - boot failed</li>
        <li>SF_WAITING             - waiting</li>
        <li>SF_OS_BOOTED           - kernel loaded</li>
        <li>SF_UP                  - up</li>
        <li>SF_DEBUG               - in debugger</li>
        <li>SF_OPERATOR            - waiting for operator
        input</li>
        <li>SF_DUMPCORE            - dumping core</li>
        <li>SF_HALT                - halted</li>
        <li>SF_REBOOT              - rebooting</li>
        <li>SF_GIVEWAIT            - waiting for giveback</li>
        <li>SF_MBWAIT              - waiting for cluster mailbox
        release</li>
        <li>SF_SPARECORE           - dumping sparecore and ready
        to be taken-over</li>
        <li>SF_MDP                 - multi-disk panic</li>
        <li>SF_TO                  - in takeover</li>
        <li>SF_NOTO		   - takeover disabled</li>
        <li>SF_CLUSTERWAIT	   - waiting for cluster
        apps</li></ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._partner_firmware_state
    @partner_firmware_state.setter
    def partner_firmware_state(self, val):
        if val != None:
            self.validate('partner_firmware_state', val)
        self._partner_firmware_state = val
    
    _partner_name = None
    @property
    def partner_name(self):
        """
        Storage failover partner node name
        Attributes: non-creatable, non-modifiable
        """
        return self._partner_name
    @partner_name.setter
    def partner_name(self, val):
        if val != None:
            self.validate('partner_name', val)
        self._partner_name = val
    
    _partner_firmware_progress = None
    @property
    def partner_firmware_progress(self):
        """
        A counter to indicate that the partner node is
        progressing in the current firmware state.
        If the counter is not progressing the partner node may be
        unresponsive or down.
        Attributes: non-creatable, non-modifiable
        """
        return self._partner_firmware_progress
    @partner_firmware_progress.setter
    def partner_firmware_progress(self, val):
        if val != None:
            self.validate('partner_firmware_progress', val)
        self._partner_firmware_progress = val
    
    _local_firmware_progress = None
    @property
    def local_firmware_progress(self):
        """
        A counter to indicate that the local node is progressing
        in the current firmware state.
        If the counter is not progressing the node may be
        unresponsive or down.
        Attributes: non-creatable, non-modifiable
        """
        return self._local_firmware_progress
    @local_firmware_progress.setter
    def local_firmware_progress(self, val):
        if val != None:
            self.validate('local_firmware_progress', val)
        self._local_firmware_progress = val
    
    _node_state = None
    @property
    def node_state(self):
        """
        Storage failover status of the node.
        Possible values are:
        <ul>
        <li>connected</li>
        <li>takeover_scheduled</li>
        <li>takeover_started</li>
        <li>takeover</li>
        <li>takeover_failed</li>
        <li>giveback_partial_waiting</li>
        <li>giveback_partial_connected</li>
        <li>waiting_for_root_aggr</li>
        <li>waiting</li>
        <li>in_maintenance_mode</li>
        <li>pending_shutdown</li>
        <li>relocating_aggrs_before_takeover</li>
        <li>sfo_takeover_phase_done</li>
        <li>sfo_takenover_phase_done</li>
        <li>sfo_takeover_phase_aborted</li>
        <li>sfo_takenover_phase_aborted</li>
        <li>in_non_HA_mode</li>
        <li>cfo_takeover_failed</li>
        <li>sfo_takeover_in_progress</li>
        <li>relocated_aggrs_before_takeover</li>
        <li>giveback_in_progress</li>
        <li>giveback_failed_autogiveback_disabled</li>
        <li>giveback_failed_autogiveback_scheduled</li>
        <li>previous_giveback_failed</li>
        <li>takeover_no_di</li>
        <li>takeover_partner_missing_disks</li>
        <li>takeover_autogiveback_scheduled</li>
        <li>takeover_network_failure</li>
        <li>takeover_autogiveback_deferred</li>
        <li>automatic_takeover_disabled_connected</li>
        <li>automatic_takeover_disabled_waiting</li>
        <li>ndo_upgrade_in_progress</li>
        <li>own_aggr_non_local_connected</li>
        <li>own_aggr_non_local_waiting</li>
        <li>clusterwait_connected</li>
        <li>clusterwait_waiting</li>
        <li>error</li></ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._node_state
    @node_state.setter
    def node_state(self, val):
        if val != None:
            self.validate('node_state', val)
        self._node_state = val
    
    _state_description = None
    @property
    def state_description(self):
        """
        A detailed description of the storage failover state of
        the node.
        Attributes: non-creatable, non-modifiable
        """
        return self._state_description
    @state_description.setter
    def state_description(self, val):
        if val != None:
            self.validate('state_description', val)
        self._state_description = val
    
    _partner_nvram_id = None
    @property
    def partner_nvram_id(self):
        """
        Partner NVRAM identifier
        Attributes: non-creatable, non-modifiable
        """
        return self._partner_nvram_id
    @partner_nvram_id.setter
    def partner_nvram_id(self, val):
        if val != None:
            self.validate('partner_nvram_id', val)
        self._partner_nvram_id = val
    
    @staticmethod
    def get_api_name():
          return "node-related-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'local-firmware-state',
            'nvram-id',
            'partner-firmware-state',
            'partner-name',
            'partner-firmware-progress',
            'local-firmware-progress',
            'node-state',
            'state-description',
            'partner-nvram-id',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'local_firmware_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nvram_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'partner_firmware_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'partner_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'partner_firmware_progress': { 'class': int, 'is_list': False, 'required': 'optional' },
            'local_firmware_progress': { 'class': int, 'is_list': False, 'required': 'optional' },
            'node_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state_description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'partner_nvram_id': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
