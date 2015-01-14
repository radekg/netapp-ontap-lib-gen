from netapp.netapp_object import NetAppObject

class GivebackRelatedInfo(NetAppObject):
    """
    Giveback related Info
    """
    
    _giveback_state = None
    @property
    def giveback_state(self):
        """
        Giveback state of the node.
        Possible values are:
        <ul>
        <li>nothing_to_gb</li>
        <li>not_attempted_yet</li>
        <li>giveback_in_progress</li>
        <li>giveback_failed_autogiveback_disabled</li>
        <li>giveback_failed_autogiveback_scheduled</li>
        <li>previous_giveback_failed</li>
        <li>giveback_vetoed_no_di</li>
        <li>giveback_vetoed_missing_disks</li>
        <li>autogiveback_scheduled</li>
        <li>autogiveback_deferred</li>
        <li>node_upgrade_in_progress</li>
        <li>sfo_aggr_giveback_failed</li>
        <li>sfo_aggr_giveback_in_progress</li>
        <li>partial_giveback</li>
        <li>partner_spare_disks_giveback_pending</li></ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._giveback_state
    @giveback_state.setter
    def giveback_state(self, val):
        if val != None:
            self.validate('giveback_state', val)
        self._giveback_state = val
    
    _giveback_failure_reason = None
    @property
    def giveback_failure_reason(self):
        """
        This is the reason for the giveback failure.
        Possible values are:
        <ul>
        <li>aggr_relocation_in_progress	- aggregate relocation
        is in
        progress</li>
        <li>shutdown_in_progress        - shutdown is in
        progress</li>
        <li>testpoint		        - a giveback failure was
        simulated
        with a testpoint</li>
        <li>cannot_giveback_partner_subsystem
        - node failed to giveback one of
        partner's subsystems</li>
        <li>bck_mbx_update_error        - node could not update
        its
        backup mailbox</li>
        </ul>
        Attributes: non-creatable, non-modifiable
        """
        return self._giveback_failure_reason
    @giveback_failure_reason.setter
    def giveback_failure_reason(self, val):
        if val != None:
            self.validate('giveback_failure_reason', val)
        self._giveback_failure_reason = val
    
    _giveback_module = None
    @property
    def giveback_module(self):
        """
        The current module giveback process is in.
        e.g. WAFL
        Attributes: non-creatable, non-modifiable
        """
        return self._giveback_module
    @giveback_module.setter
    def giveback_module(self, val):
        if val != None:
            self.validate('giveback_module', val)
        self._giveback_module = val
    
    @staticmethod
    def get_api_name():
          return "giveback-related-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'giveback-state',
            'giveback-failure-reason',
            'giveback-module',
        ]
    
    def describe_properties(self):
        return {
            'giveback_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'giveback_failure_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'giveback_module': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
