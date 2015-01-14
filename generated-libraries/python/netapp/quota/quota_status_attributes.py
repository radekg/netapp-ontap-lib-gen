from netapp.netapp_object import NetAppObject

class QuotaStatusAttributes(NetAppObject):
    """
    Attributes of quota status
    """
    
    _status = None
    @property
    def status(self):
        """
        Primary status of quotas on the indicated volume;
        Possible values:
        <ul>
        <li> "corrupt" </li>
        <li> "initializing" </li>
        <li> "off" </li>
        <li> "on" </li>
        <li> "resizing" </li>
        <li> "reverting" </li>
        <li> "upgrading" </li>
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _volume = None
    @property
    def volume(self):
        """
        Name of the volume to which the quota is applied.
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _quota_error_msgs = None
    @property
    def quota_error_msgs(self):
        """
        Collection of quota errors including the value of the
        reason tag above. Since the quota parser does not stop
        when a parsing error occurs, this tag returns all the
        errors from the quota parser.  If not present, there
        are no errors.
        """
        return self._quota_error_msgs
    @quota_error_msgs.setter
    def quota_error_msgs(self, val):
        if val != None:
            self.validate('quota_error_msgs', val)
        self._quota_error_msgs = val
    
    _substatus = None
    @property
    def substatus(self):
        """
        Minor quota status on the indicated volume.
        This status is only valid when primary status is
        "resizing" or "initializing".  Possible values are:
        <ul>
        <li> "done" </li>
        <li> "etc_scanning" </li>
        <li> "finishing" </li>
        <li> "none" </li>
        <li> "queue_scan" </li>
        <li> "scanning" </li>
        <li> "setup" </li>
        <li> "transferring_rules" </li>
        <li> "upgrading" </li>
        </ul>
        """
        return self._substatus
    @substatus.setter
    def substatus(self, val):
        if val != None:
            self.validate('substatus', val)
        self._substatus = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        The vserver name in which the volume belongs,
        for which the quota is applicable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _reason = None
    @property
    def reason(self):
        """
        The last quota error message.
        If not present, there are no errors.
        """
        return self._reason
    @reason.setter
    def reason(self, val):
        if val != None:
            self.validate('reason', val)
        self._reason = val
    
    _percent_complete = None
    @property
    def percent_complete(self):
        """
        The percentage complete for an "on" or "resize" operation.
        This is present when the status
        is "upgrading", "resizing" or "initializing".
        """
        return self._percent_complete
    @percent_complete.setter
    def percent_complete(self, val):
        if val != None:
            self.validate('percent_complete', val)
        self._percent_complete = val
    
    @staticmethod
    def get_api_name():
          return "quota-status-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'volume',
            'quota-error-msgs',
            'substatus',
            'vserver',
            'reason',
            'percent-complete',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'quota_error_msgs': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'substatus': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'percent_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
