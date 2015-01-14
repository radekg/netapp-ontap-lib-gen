from netapp.netapp_object import NetAppObject

class SfOptionsInfo(NetAppObject):
    """
    Options for debugging purpose.
    """
    
    _hwassist_partner_port = None
    @property
    def hwassist_partner_port(self):
        """
        Port number on which hwassist receives alerts.
        """
        return self._hwassist_partner_port
    @hwassist_partner_port.setter
    def hwassist_partner_port(self, val):
        if val != None:
            self.validate('hwassist_partner_port', val)
        self._hwassist_partner_port = val
    
    _hwassist_health_check_interval = None
    @property
    def hwassist_health_check_interval(self):
        """
        Hardware assist h/w sends a heartbeat every '-health-check-interval'
        seconds.
        """
        return self._hwassist_health_check_interval
    @hwassist_health_check_interval.setter
    def hwassist_health_check_interval(self, val):
        if val != None:
            self.validate('hwassist_health_check_interval', val)
        self._hwassist_health_check_interval = val
    
    _takeover_on_panic = None
    @property
    def takeover_on_panic(self):
        """
        Indicates if we will automatically takeover upon
        partner panic.
        """
        return self._takeover_on_panic
    @takeover_on_panic.setter
    def takeover_on_panic(self, val):
        if val != None:
            self.validate('takeover_on_panic', val)
        self._takeover_on_panic = val
    
    _send_home_auto_delay_seconds = None
    @property
    def send_home_auto_delay_seconds(self):
        """
        The number of seconds of delay before initiating
        automatic send-home. This will be the minimum
        time a node will be in takeover state before
        performing auto sendhome.
        """
        return self._send_home_auto_delay_seconds
    @send_home_auto_delay_seconds.setter
    def send_home_auto_delay_seconds(self, val):
        if val != None:
            self.validate('send_home_auto_delay_seconds', val)
        self._send_home_auto_delay_seconds = val
    
    _giveback_auto = None
    @property
    def giveback_auto(self):
        """
        Indicates if the automatic giveback is
        enabled. Same as send-home-auto.
        """
        return self._giveback_auto
    @giveback_auto.setter
    def giveback_auto(self, val):
        if val != None:
            self.validate('giveback_auto', val)
        self._giveback_auto = val
    
    _takeover_on_reboot = None
    @property
    def takeover_on_reboot(self):
        """
        Indicates if we will automatically takeover upon
        partner reboot.
        """
        return self._takeover_on_reboot
    @takeover_on_reboot.setter
    def takeover_on_reboot(self, val):
        if val != None:
            self.validate('takeover_on_reboot', val)
        self._takeover_on_reboot = val
    
    _node_status_in_mailbox_disks_write_interval = None
    @property
    def node_status_in_mailbox_disks_write_interval(self):
        """
        Rate in seconds at which we write node status to
        mailbox disks.
        """
        return self._node_status_in_mailbox_disks_write_interval
    @node_status_in_mailbox_disks_write_interval.setter
    def node_status_in_mailbox_disks_write_interval(self, val):
        if val != None:
            self.validate('node_status_in_mailbox_disks_write_interval', val)
        self._node_status_in_mailbox_disks_write_interval = val
    
    _takeover_on_short_uptime = None
    @property
    def takeover_on_short_uptime(self):
        """
        Indicates if we will automatically takeover if the
        partner fails within 60 seconds of booting.
        """
        return self._takeover_on_short_uptime
    @takeover_on_short_uptime.setter
    def takeover_on_short_uptime(self, val):
        if val != None:
            self.validate('takeover_on_short_uptime', val)
        self._takeover_on_short_uptime = val
    
    _send_home_auto = None
    @property
    def send_home_auto(self):
        """
        Indicates if the automatic send-home facility enabled.
        """
        return self._send_home_auto
    @send_home_auto.setter
    def send_home_auto(self, val):
        if val != None:
            self.validate('send_home_auto', val)
        self._send_home_auto = val
    
    _bypass_takeover_optimization = None
    @property
    def bypass_takeover_optimization(self):
        """
        If true, then optimized negotiated takeover is
        bypassed. If false, negotiated takeover will be
        optimized. The default value for this option is
        false. This option will be available starting
        with Data ONTAP 8.2.
        """
        return self._bypass_takeover_optimization
    @bypass_takeover_optimization.setter
    def bypass_takeover_optimization(self, val):
        if val != None:
            self.validate('bypass_takeover_optimization', val)
        self._bypass_takeover_optimization = val
    
    _send_home_auto_attempts = None
    @property
    def send_home_auto_attempts(self):
        """
        The number of times we'll try to do an automatic
        giveback within send-home-auto-minutes
        """
        return self._send_home_auto_attempts
    @send_home_auto_attempts.setter
    def send_home_auto_attempts(self, val):
        if val != None:
            self.validate('send_home_auto_attempts', val)
        self._send_home_auto_attempts = val
    
    _hwassist_enable = None
    @property
    def hwassist_enable(self):
        """
        Indicate if hardware assist takeover is enabled.
        """
        return self._hwassist_enable
    @hwassist_enable.setter
    def hwassist_enable(self, val):
        if val != None:
            self.validate('hwassist_enable', val)
        self._hwassist_enable = val
    
    _takeover_detection_time = None
    @property
    def takeover_detection_time(self):
        """
        Takeover detection time in seconds.
        """
        return self._takeover_detection_time
    @takeover_detection_time.setter
    def takeover_detection_time(self, val):
        if val != None:
            self.validate('takeover_detection_time', val)
        self._takeover_detection_time = val
    
    _takeover_on_failure = None
    @property
    def takeover_on_failure(self):
        """
        Indicates if we will automatically takeover upon
        partner failure.
        """
        return self._takeover_on_failure
    @takeover_on_failure.setter
    def takeover_on_failure(self, val):
        if val != None:
            self.validate('takeover_on_failure', val)
        self._takeover_on_failure = val
    
    _aggregate_migration_timeout = None
    @property
    def aggregate_migration_timeout(self):
        """
        Number of seconds the source node has to wait for the
        destination node to complete the aggregate migration
        before declaring the migration as failed. The default
        setting is 40 seconds.
        """
        return self._aggregate_migration_timeout
    @aggregate_migration_timeout.setter
    def aggregate_migration_timeout(self, val):
        if val != None:
            self.validate('aggregate_migration_timeout', val)
        self._aggregate_migration_timeout = val
    
    _hwassist_retry_count = None
    @property
    def hwassist_retry_count(self):
        """
        Number of times we repeat sending an alert.
        """
        return self._hwassist_retry_count
    @hwassist_retry_count.setter
    def hwassist_retry_count(self, val):
        if val != None:
            self.validate('hwassist_retry_count', val)
        self._hwassist_retry_count = val
    
    _hwassist_partner_ip = None
    @property
    def hwassist_partner_ip(self):
        """
        Hardware assist Ip address of the partner.
        """
        return self._hwassist_partner_ip
    @hwassist_partner_ip.setter
    def hwassist_partner_ip(self, val):
        if val != None:
            self.validate('hwassist_partner_ip', val)
        self._hwassist_partner_ip = val
    
    _send_home_check_partner_waiting = None
    @property
    def send_home_check_partner_waiting(self):
        """
        Indicates if we require the partner to be waiting for a
        send-home in order to do a send-home.
        """
        return self._send_home_check_partner_waiting
    @send_home_check_partner_waiting.setter
    def send_home_check_partner_waiting(self, val):
        if val != None:
            self.validate('send_home_check_partner_waiting', val)
        self._send_home_check_partner_waiting = val
    
    _node_status_in_mailbox_disks_read_interval = None
    @property
    def node_status_in_mailbox_disks_read_interval(self):
        """
        Rate in seconds at which we read node status from
        mailbox disks.
        """
        return self._node_status_in_mailbox_disks_read_interval
    @node_status_in_mailbox_disks_read_interval.setter
    def node_status_in_mailbox_disks_read_interval(self, val):
        if val != None:
            self.validate('node_status_in_mailbox_disks_read_interval', val)
        self._node_status_in_mailbox_disks_read_interval = val
    
    _mode = None
    @property
    def mode(self):
        """
        HA mode in registry
        """
        return self._mode
    @mode.setter
    def mode(self, val):
        if val != None:
            self.validate('mode', val)
        self._mode = val
    
    _send_home_auto_attempts_minutes = None
    @property
    def send_home_auto_attempts_minutes(self):
        """
        The number of minutes in which we should not execeed
        send-home-auto-attempts automatic send-home attempts.
        """
        return self._send_home_auto_attempts_minutes
    @send_home_auto_attempts_minutes.setter
    def send_home_auto_attempts_minutes(self, val):
        if val != None:
            self.validate('send_home_auto_attempts_minutes', val)
        self._send_home_auto_attempts_minutes = val
    
    _node_status_in_mailbox_disks = None
    @property
    def node_status_in_mailbox_disks(self):
        """
        Indicates if we propagate node status via mailbox disks.
        """
        return self._node_status_in_mailbox_disks
    @node_status_in_mailbox_disks.setter
    def node_status_in_mailbox_disks(self, val):
        if val != None:
            self.validate('node_status_in_mailbox_disks', val)
        self._node_status_in_mailbox_disks = val
    
    @staticmethod
    def get_api_name():
          return "sf-options-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'hwassist-partner-port',
            'hwassist-health-check-interval',
            'takeover-on-panic',
            'send-home-auto-delay-seconds',
            'giveback-auto',
            'takeover-on-reboot',
            'node-status-in-mailbox-disks-write-interval',
            'takeover-on-short-uptime',
            'send-home-auto',
            'bypass-takeover-optimization',
            'send-home-auto-attempts',
            'hwassist-enable',
            'takeover-detection-time',
            'takeover-on-failure',
            'aggregate-migration-timeout',
            'hwassist-retry-count',
            'hwassist-partner-ip',
            'send-home-check-partner-waiting',
            'node-status-in-mailbox-disks-read-interval',
            'mode',
            'send-home-auto-attempts-minutes',
            'node-status-in-mailbox-disks',
        ]
    
    def describe_properties(self):
        return {
            'hwassist_partner_port': { 'class': int, 'is_list': False, 'required': 'required' },
            'hwassist_health_check_interval': { 'class': int, 'is_list': False, 'required': 'required' },
            'takeover_on_panic': { 'class': bool, 'is_list': False, 'required': 'required' },
            'send_home_auto_delay_seconds': { 'class': int, 'is_list': False, 'required': 'required' },
            'giveback_auto': { 'class': bool, 'is_list': False, 'required': 'required' },
            'takeover_on_reboot': { 'class': bool, 'is_list': False, 'required': 'required' },
            'node_status_in_mailbox_disks_write_interval': { 'class': int, 'is_list': False, 'required': 'required' },
            'takeover_on_short_uptime': { 'class': bool, 'is_list': False, 'required': 'required' },
            'send_home_auto': { 'class': bool, 'is_list': False, 'required': 'required' },
            'bypass_takeover_optimization': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'send_home_auto_attempts': { 'class': int, 'is_list': False, 'required': 'required' },
            'hwassist_enable': { 'class': bool, 'is_list': False, 'required': 'required' },
            'takeover_detection_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'takeover_on_failure': { 'class': bool, 'is_list': False, 'required': 'required' },
            'aggregate_migration_timeout': { 'class': int, 'is_list': False, 'required': 'optional' },
            'hwassist_retry_count': { 'class': int, 'is_list': False, 'required': 'required' },
            'hwassist_partner_ip': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'send_home_check_partner_waiting': { 'class': bool, 'is_list': False, 'required': 'required' },
            'node_status_in_mailbox_disks_read_interval': { 'class': int, 'is_list': False, 'required': 'required' },
            'mode': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'send_home_auto_attempts_minutes': { 'class': int, 'is_list': False, 'required': 'required' },
            'node_status_in_mailbox_disks': { 'class': bool, 'is_list': False, 'required': 'required' },
        }
