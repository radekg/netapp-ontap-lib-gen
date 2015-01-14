from netapp.netapp_object import NetAppObject

class TimeoutInfo(NetAppObject):
    """
    Failover monitor timeouts.
    """
    
    _slow = None
    @property
    def slow(self):
        """
        slow timeout, in milliseconds
        """
        return self._slow
    @slow.setter
    def slow(self, val):
        if val != None:
            self.validate('slow', val)
        self._slow = val
    
    _transit_timer_enabled = None
    @property
    def transit_timer_enabled(self):
        """
        True, if the transit timer is enabled
        """
        return self._transit_timer_enabled
    @transit_timer_enabled.setter
    def transit_timer_enabled(self, val):
        if val != None:
            self.validate('transit_timer_enabled', val)
        self._transit_timer_enabled = val
    
    _transit = None
    @property
    def transit(self):
        """
        transit timeout, in milliseconds
        """
        return self._transit
    @transit.setter
    def transit(self, val):
        if val != None:
            self.validate('transit', val)
        self._transit = val
    
    _firmware = None
    @property
    def firmware(self):
        """
        firmware timeout, in milliseconds
        """
        return self._firmware
    @firmware.setter
    def firmware(self, val):
        if val != None:
            self.validate('firmware', val)
        self._firmware = val
    
    _reboot = None
    @property
    def reboot(self):
        """
        reboot timeout, in milliseconds
        """
        return self._reboot
    @reboot.setter
    def reboot(self, val):
        if val != None:
            self.validate('reboot', val)
        self._reboot = val
    
    _fast = None
    @property
    def fast(self):
        """
        fast timeout, in milliseconds
        """
        return self._fast
    @fast.setter
    def fast(self, val):
        if val != None:
            self.validate('fast', val)
        self._fast = val
    
    _mailbox = None
    @property
    def mailbox(self):
        """
        mailbox timeout, in milliseconds
        """
        return self._mailbox
    @mailbox.setter
    def mailbox(self, val):
        if val != None:
            self.validate('mailbox', val)
        self._mailbox = val
    
    _connect = None
    @property
    def connect(self):
        """
        connect timeout, in milliseconds
        """
        return self._connect
    @connect.setter
    def connect(self, val):
        if val != None:
            self.validate('connect', val)
        self._connect = val
    
    _booting = None
    @property
    def booting(self):
        """
        booting timeout, in milliseconds
        """
        return self._booting
    @booting.setter
    def booting(self, val):
        if val != None:
            self.validate('booting', val)
        self._booting = val
    
    _operator = None
    @property
    def operator(self):
        """
        operator timeout, in milliseconds
        """
        return self._operator
    @operator.setter
    def operator(self, val):
        if val != None:
            self.validate('operator', val)
        self._operator = val
    
    _dumpcore = None
    @property
    def dumpcore(self):
        """
        dumpcore timeout, in milliseconds
        """
        return self._dumpcore
    @dumpcore.setter
    def dumpcore(self, val):
        if val != None:
            self.validate('dumpcore', val)
        self._dumpcore = val
    
    @staticmethod
    def get_api_name():
          return "timeout-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'slow',
            'transit-timer-enabled',
            'transit',
            'firmware',
            'reboot',
            'fast',
            'mailbox',
            'connect',
            'booting',
            'operator',
            'dumpcore',
        ]
    
    def describe_properties(self):
        return {
            'slow': { 'class': int, 'is_list': False, 'required': 'required' },
            'transit_timer_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'transit': { 'class': int, 'is_list': False, 'required': 'required' },
            'firmware': { 'class': int, 'is_list': False, 'required': 'required' },
            'reboot': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fast': { 'class': int, 'is_list': False, 'required': 'required' },
            'mailbox': { 'class': int, 'is_list': False, 'required': 'required' },
            'connect': { 'class': int, 'is_list': False, 'required': 'required' },
            'booting': { 'class': int, 'is_list': False, 'required': 'required' },
            'operator': { 'class': int, 'is_list': False, 'required': 'required' },
            'dumpcore': { 'class': int, 'is_list': False, 'required': 'required' },
        }
