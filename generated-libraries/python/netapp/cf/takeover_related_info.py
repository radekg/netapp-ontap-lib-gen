from netapp.netapp_object import NetAppObject

class TakeoverRelatedInfo(NetAppObject):
    """
    Takeover related Info
    """
    
    _takeover_module = None
    @property
    def takeover_module(self):
        """
        The current module takeover process is in.
        e.g. WAFL
        Attributes: non-creatable, non-modifiable
        """
        return self._takeover_module
    @takeover_module.setter
    def takeover_module(self, val):
        if val != None:
            self.validate('takeover_module', val)
        self._takeover_module = val
    
    _takeover_of_partner_possible = None
    @property
    def takeover_of_partner_possible(self):
        """
        True, if storage failover takeover is currently
        possible,
        false otherwise.
        Attributes: non-creatable, non-modifiable
        """
        return self._takeover_of_partner_possible
    @takeover_of_partner_possible.setter
    def takeover_of_partner_possible(self, val):
        if val != None:
            self.validate('takeover_of_partner_possible', val)
        self._takeover_of_partner_possible = val
    
    _takeover_reason = None
    @property
    def takeover_reason(self):
        """
        List of reasons why a takeover can happen.
        Possible values are:
        <ul>
        <li>none 			- Not in takeover </li>
        <li>takeover_normal 		- Operator initiated takeover
        <li>takeover_immediate 		- Operator initiated forced
        takeover</li>
        <li>takeover_ndu 		- Takeover initiated as part of NDU
        </li>
        <li>takeover_forced 		- Operator initiated forced
        takeover, possible data loss</li>
        <li>takeover_early 		- Takeover occuring during bootup of
        a filer </li>
        <li>takeover_operator_exp 	- Takeover occuring after
        operator timeout expired </li>
        <li>takeover_post_failed 	- Takeover occuring on POST
        failure </li>
        <li>takeover_panic 		- Takeover on panic </li>
        <li>takeover_shortuptime 	- Takeover after quick toggling
        between up & down states <li>
        <li>takeover_sparecore_exp 	- Takeover on panic timeout
        expiry </li>
        <li>takeover_reboot_exp 	- Takeover on reboot timer
        expiry </li>
        <li>takeover_booting_exp 	- Takeover on booting timer
        expiry </li>
        <li>takeover_nfo_shutdown 	- Takeover on negotiated
        failover shutdown </li>
        <li>takeover_nfo_timer 		- Takeover on negotiated
        failover timer expiry </li>
        <li>takeover_mdp 		- Takeover on multi-disk panic </li>
        <li>takeover_reboot 		- Takeover on reboot </li>
        <li>takeover_halt 		- Takeover on halt</li>
        <li>takeover_clam 		- CLAM triggered takeover </li>
        <li>takeover_hwassist 		- H/w assisted takeover </li>
        </ul>
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "takeover_none"            - None,
        <li> "takeover_immediate"       - Immediate takeover,
        <li> "takeover_ndu"             - NDU Takeover,
        <li> "takeover_forced"          - Forced Takeover,
        <li> "takeover_disaster"        - Disaster Takeover,
        <li> "takeover_early"           - Early Takeover,
        <li> "takeover_operator_exp"    - Takeover Operator
        Timeout,
        <li> "takeover_post_failed"     - Takeover POST
        Failed,
        <li> "takeover_panic"           - Takeover On Panic,
        <li> "takeover_shortuptime"     - Takeover On Short
        Uptime,
        <li> "takeover_sparecore_exp"   - Takeover On Sparecore
        Timeout,
        <li> "takeover_reboot_exp"      - Takeover On Reboot
        Timeout,
        <li> "takeover_booting_exp"     - Takeover On Booting
        Timeout,
        <li> "takeover_firmware_exp"    - Takeover On Firmware
        Timeout,
        <li> "takeover_nfo_shutdown"    - Takeover On
        Negotiated Failover,
        <li> "takeover_nfo_timer"       - Takeover On
        Negotiated Failover Timeout,
        <li> "takeover_mdp"             - Takeover On MDP,
        <li> "takeover_reboot"          - Takeover On Reboot,
        <li> "takeover_halt"            - Takeover On Halt,
        <li> "takeover_clam"            - CLAM Initiated
        Takeover,
        <li> "takeover_hwassist"        - H/w assisted
        Takeover,
        <li> "takeover_normal"          - Operator initiated
        takeover
        </ul>
        """
        return self._takeover_reason
    @takeover_reason.setter
    def takeover_reason(self, val):
        if val != None:
            self.validate('takeover_reason', val)
        self._takeover_reason = val
    
    _time_since_takeover = None
    @property
    def time_since_takeover(self):
        """
        Time in milliseconds since the local node has taken over
        partner.
        Attributes: non-creatable, non-modifiable
        """
        return self._time_since_takeover
    @time_since_takeover.setter
    def time_since_takeover(self, val):
        if val != None:
            self.validate('time_since_takeover', val)
        self._time_since_takeover = val
    
    _takeover_by_partner_possible = None
    @property
    def takeover_by_partner_possible(self):
        """
        True, if storage failover takeover is currently
        possible.
        by the partner, false otherwise.
        Note that this is the local node's view of partner.
        Attributes: non-creatable, non-modifiable
        """
        return self._takeover_by_partner_possible
    @takeover_by_partner_possible.setter
    def takeover_by_partner_possible(self, val):
        if val != None:
            self.validate('takeover_by_partner_possible', val)
        self._takeover_by_partner_possible = val
    
    _takeover_state = None
    @property
    def takeover_state(self):
        """
        Takeover state of the node.
        Possible values are:
        <ul>
        <li>takeover_failed                     - Takeover
        Failed</li>
        <li>sfo_takeover_in_progress            - SFO phase of
        takeover of partner is in progress</li>
        <li>relocating_aggrs_before_takeover    - Relocating
        aggregates to partner
        as a takeover
        was initiated by partner</li>
        <li>cfo_takeover_scheduled              - CFO phase of
        takeover is scheduled</li>
        <li>relocated_aggrs_before_takeover     - Relocated
        aggregates to partner
        after a
        takeover was initiated by partner</li>
        <li>takeover_by_partner_failed          - A takeover
        attempt by partner failed.
        Refer to
        takeover-failure-reason field
        to check the
        reason for takeover failure.</li>
        <li>in_takeover                         - Node is in
        takeover</li>
        <li>takeover_started                    - A takeover is
        in progress</li>
        <li>takeover_scheduled                  - A takeover of
        partner is scheduled</li>
        Refer to
        time-until-takeover field to check
        time remaining
        till takeover.</li>
        <li>not_in_takeover                     - Local node is
        not in takeover</li></ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._takeover_state
    @takeover_state.setter
    def takeover_state(self, val):
        if val != None:
            self.validate('takeover_state', val)
        self._takeover_state = val
    
    _takeover_failure_reason = None
    @property
    def takeover_failure_reason(self):
        """
        This is the reason for the takeover failure.
        Possible values are:
        <ul>
        <li>shutdown_in_progress	- shutdown is in
        progress</li>
        <li>aggr_relocation_in_progress	- aggregate relocation
        is in
        progress</li>
        <li>giveback_in_progress	- giveback is in
        progress</li>
        <li>takeover_in_progress	- takeover is in progress
        </li>
        <li>unknown_partner_id		- node could not detect its
        partner's system ID</li>
        <li>conflicting_sysid		- node has the same system ID
        as its partner</li>
        <li>pri_mbx_update_error	- node could not update its
        primary mailbox</li>
        <li>takeover_disabled_by_partner
        - partner has disabled takeover</li>
        <li>cannot_takeover_partner_subsystem
        - node failed to takeover one of
        partner's subsystems</li>
        <li>non_etc_or_rc_boot		- it is not possible to
        takeover
        in a non-etc/rc boot</li>
        <li>bck_mbx_update_error	- node could not update its
        backup mailbox</li>
        <li>partner_taking_over		- partner is taking over
        local
        node </li>
        <li>revert_in_progress		- revert is in progress </li>
        <li>disaster_recovery_in_progress
        - disaster recovery operation is
        in progress</li>
        <li>headswap_in_progress	- headswap is in progress
        </li>
        <li>destination_check_failed	- destination check failed
        </li>
        <li>communication_failed	- communication with
        destination
        failed</li>
        <li>operation_aborted		- operation was aborted </li>
        <li>aggr_not_online		- destination node did not
        online the aggregate being
        relocated in time </li>
        <li>sfo_disabled		- storage failover service is
        not enabled </li>
        <li>partner_taking_over		- partner is taking over
        local
        node </li>
        <li>bdfu_not_disabled_source	- failed to disable
        background
        disk firmware update (BDFU)
        on local node </li>
        <li>bdfu_not_disabled_dest	- failed to disable
        background
        disk firmware update (BDFU)
        on partner node </li>
        <li>partner_shutting_down	- shutdown is in progress on
        the
        partner node</li>
        <li>partner_aggr_relocation_in_progress
        - aggregate relocation is in
        progress on the partner node</li>
        <li>partner_giveback_in_progress
        - giveback is in progress on the
        partner node</li>
        <li>partner_revert_in_progress  - revert is in progress
        on the
        partner node </li>
        <li>partner_disaster_recovery_in_progress
        - disaster recovery operation
        is in progress on the partner
        node</li>
        <li>partner_in_headswap		- headswap is in progress on
        the
        partner node</li>
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._takeover_failure_reason
    @takeover_failure_reason.setter
    def takeover_failure_reason(self, val):
        if val != None:
            self.validate('takeover_failure_reason', val)
        self._takeover_failure_reason = val
    
    _takeover_enabled = None
    @property
    def takeover_enabled(self):
        """
        True, if the storage failover facility is enabled, false
        otherwise.  Note that the facility can be enabled but
        takeover may not be possible due to various reasons.
        Attributes: non-creatable, modifiable
        """
        return self._takeover_enabled
    @takeover_enabled.setter
    def takeover_enabled(self, val):
        if val != None:
            self.validate('takeover_enabled', val)
        self._takeover_enabled = val
    
    _takeover_by_partner_not_possible_reason = None
    @property
    def takeover_by_partner_not_possible_reason(self):
        """
        It list of one or more reasons why takeover by partner is
        not
        possible.
        Attributes: non-creatable, non-modifiable
        """
        return self._takeover_by_partner_not_possible_reason
    @takeover_by_partner_not_possible_reason.setter
    def takeover_by_partner_not_possible_reason(self, val):
        if val != None:
            self.validate('takeover_by_partner_not_possible_reason', val)
        self._takeover_by_partner_not_possible_reason = val
    
    _takeover_of_partner_not_possible_reason = None
    @property
    def takeover_of_partner_not_possible_reason(self):
        """
        If takeover-possible field is false, it lists of one or
        more
        reasons why takeover of partner is not possible.
        Attributes: non-creatable, non-modifiable
        """
        return self._takeover_of_partner_not_possible_reason
    @takeover_of_partner_not_possible_reason.setter
    def takeover_of_partner_not_possible_reason(self, val):
        if val != None:
            self.validate('takeover_of_partner_not_possible_reason', val)
        self._takeover_of_partner_not_possible_reason = val
    
    _time_until_takeover = None
    @property
    def time_until_takeover(self):
        """
        This is the countdown time in seconds until takeover is
        started.
        Attributes: non-creatable, non-modifiable
        """
        return self._time_until_takeover
    @time_until_takeover.setter
    def time_until_takeover(self, val):
        if val != None:
            self.validate('time_until_takeover', val)
        self._time_until_takeover = val
    
    @staticmethod
    def get_api_name():
          return "takeover-related-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'takeover-module',
            'takeover-of-partner-possible',
            'takeover-reason',
            'time-since-takeover',
            'takeover-by-partner-possible',
            'takeover-state',
            'takeover-failure-reason',
            'takeover-enabled',
            'takeover-by-partner-not-possible-reason',
            'takeover-of-partner-not-possible-reason',
            'time-until-takeover',
        ]
    
    def describe_properties(self):
        return {
            'takeover_module': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'takeover_of_partner_possible': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'takeover_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'time_since_takeover': { 'class': int, 'is_list': False, 'required': 'optional' },
            'takeover_by_partner_possible': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'takeover_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'takeover_failure_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'takeover_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'takeover_by_partner_not_possible_reason': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'takeover_of_partner_not_possible_reason': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'time_until_takeover': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
