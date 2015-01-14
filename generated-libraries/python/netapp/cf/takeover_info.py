from netapp.netapp_object import NetAppObject

class TakeoverInfo(NetAppObject):
    """
    Takeover info.
    """
    
    _reason = None
    @property
    def reason(self):
        """
        reason we can't takeover:
        <ul>
        <li>not_initialized                     - Controller Failover not initialized</li>
        <li>non_ha_mode                         - Controller is in non-HA mode</li>
        <li>disabled                            - Controller Failover takeover disabled</li>
        <li>mailbox_invalid                     - Partner mailbox disks not accessible or invalid</li>
        <li>mailbox_uninit                      - Partner mailbox status uninitialized</li>
        <li>fm_version_mismatch                 - Failover monitor version mismatch</li>
        <li>partner_disabled                    - Takeover disabled by partner</li>
        <li>operator_deny                       - Takeover disabled by operator</li>
        <li>nvram_mismatch                      - NVRAM size mismatch</li>
        <li>version                             - Version mismatch</li>
        <li>ic_error                            - Interconnect error</li>
        <li>booting                             - Partner booting</li>
        <li>shelf_hot                           - Disk shelf is too hot</li>
        <li>partner_revert_in_progress          - Partner is performing revert</li>
        <li>local_revert_in_progress            - Revert is in progress</li>
        <li>partner_takeover                    - Partner is attempting takeover</li>
        <li>local_takeover                      - Already in takeover mode</li>
        <li>halt_no_takeover                    - Partner halted in notakeover mode</li>
        <li>log_unsync                          - NVRAM log unsynchronized</li>
        <li>unknown                             - No takeover due to unknown reason</li>
        <li>waiting_for_partner                 - Waiting for partner to recover</li>
        <li>low_memory                          - Low memory condition</li>
        <li>halting                             - Local halt in progress</li>
        <li>mailbox_uncertain                   - Status of partner mailbox is uncertain</li>
        <li>no_auto_takeover                    - Automatic takeover is disabled</li>
        <li>disk_inventory_not_exchanged        - Disk inventory information not received
        from partner</li>
        <li>disk_inventory_mismatch_local       - Local node missing some of partner node's
        file system disks</li>
        <li>pending_shutdown                    - Local node is shutting down</li>
        </ul>
        """
        return self._reason
    @reason.setter
    def reason(self, val):
        if val != None:
            self.validate('reason', val)
        self._reason = val
    
    @staticmethod
    def get_api_name():
          return "takeover-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'reason',
        ]
    
    def describe_properties(self):
        return {
            'reason': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
