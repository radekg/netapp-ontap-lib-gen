class TakeoverReason(basestring):
    """
    FM Takeover Reason
    Possible values:
    <ul>
    <li> "takeover_none"           - None,
    <li> "takeover_immediate"      - Immediate takeover,
    <li> "takeover_ndu"            - NDU Takeover,
    <li> "takeover_forced"         - Forced Takeover,
    <li> "takeover_disaster"       - Disaster Takeover,
    <li> "takeover_early"          - Early Takeover,
    <li> "takeover_operator_exp"   - Takeover Operator Timeout,
    <li> "takeover_post_failed"    - Takeover POST Failed,
    <li> "takeover_panic"          - Takeover On Panic,
    <li> "takeover_shortuptime"    - Takeover On Short Uptime,
    <li> "takeover_sparecore_exp"  - Takeover On Sparecore
    Timeout,
    <li> "takeover_reboot_exp"     - Takeover On Reboot Timeout,
    <li> "takeover_booting_exp"    - Takeover On Booting Timeout,
    <li> "takeover_firmware_exp"   - Takeover On Firmware
    Timeout,
    <li> "takeover_nfo_shutdown"   - Takeover On Negotiated
    Failover,
    <li> "takeover_nfo_timer"      - Takeover On Negotiated
    Failover Timeout,
    <li> "takeover_mdp"            - Takeover On MDP,
    <li> "takeover_reboot"         - Takeover On Reboot,
    <li> "takeover_halt"           - Takeover On Halt,
    <li> "takeover_clam"           - CLAM Initiated Takeover,
    <li> "takeover_hwassist"       - H/w assisted Takeover,
    <li> "takeover_normal"         - Operator initiated takeover
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "takeover-reason"
    
