from netapp.netapp_object import NetAppObject

class VolMoveStatusInfo(NetAppObject):
    """
    status of each move
    """
    
    _source_volume_name = None
    @property
    def source_volume_name(self):
        """
        Name of volume being moved
        """
        return self._source_volume_name
    @source_volume_name.setter
    def source_volume_name(self, val):
        if val != None:
            self.validate('source_volume_name', val)
        self._source_volume_name = val
    
    _cutover_window = None
    @property
    def cutover_window(self):
        """
        Length of the cutover-window in seconds.
        """
        return self._cutover_window
    @cutover_window.setter
    def cutover_window(self, val):
        if val != None:
            self.validate('cutover_window', val)
        self._cutover_window = val
    
    _dest_aggregate = None
    @property
    def dest_aggregate(self):
        """
        Name of aggregate where the volume is being moved
        """
        return self._dest_aggregate
    @dest_aggregate.setter
    def dest_aggregate(self, val):
        if val != None:
            self.validate('dest_aggregate', val)
        self._dest_aggregate = val
    
    _current_transfer = None
    @property
    def current_transfer(self):
        """
        Amount of data in KB being transferred in current transfer. Appears
        only in verbose mode. The maximum value is the size of the volume.
        """
        return self._current_transfer
    @current_transfer.setter
    def current_transfer(self, val):
        if val != None:
            self.validate('current_transfer', val)
        self._current_transfer = val
    
    _last_transfer_duration = None
    @property
    def last_transfer_duration(self):
        """
        Time taken for the last completed transfer in seconds. Appears only
        in verbose mode. There is no upper limit on how long this can take.
        """
        return self._last_transfer_duration
    @last_transfer_duration.setter
    def last_transfer_duration(self, val):
        if val != None:
            self.validate('last_transfer_duration', val)
        self._last_transfer_duration = val
    
    _dest_volume = None
    @property
    def dest_volume(self):
        """
        Name of (temporary) destination volume. Appears only in
        verbose mode.
        """
        return self._dest_volume
    @dest_volume.setter
    def dest_volume(self, val):
        if val != None:
            self.validate('dest_volume', val)
        self._dest_volume = val
    
    _cutover_attempts = None
    @property
    def cutover_attempts(self):
        """
        Number of cutover attempts. A value of -1 signifies manual cutover.
        """
        return self._cutover_attempts
    @cutover_attempts.setter
    def cutover_attempts(self, val):
        if val != None:
            self.validate('cutover_attempts', val)
        self._cutover_attempts = val
    
    _error_string = None
    @property
    def error_string(self):
        """
        Error encountered during the move
        """
        return self._error_string
    @error_string.setter
    def error_string(self, val):
        if val != None:
            self.validate('error_string', val)
        self._error_string = val
    
    _last_transfer_size = None
    @property
    def last_transfer_size(self):
        """
        The size in KB  (1024)  of the last completed transfer. Appears
        only in verbose mode. The maximum value is the size of the volume.
        """
        return self._last_transfer_size
    @last_transfer_size.setter
    def last_transfer_size(self, val):
        if val != None:
            self.validate('last_transfer_size', val)
        self._last_transfer_size = val
    
    _pause_reason = None
    @property
    def pause_reason(self):
        """
        Reason for the pause state of the move
        """
        return self._pause_reason
    @pause_reason.setter
    def pause_reason(self, val):
        if val != None:
            self.validate('pause_reason', val)
        self._pause_reason = val
    
    _move_state = None
    @property
    def move_state(self):
        """
        Status of the move. Possible values are "setup", "move",
        "cutover", "abort", "setup(paused)", "move(paused)".
        """
        return self._move_state
    @move_state.setter
    def move_state(self, val):
        if val != None:
            self.validate('move_state', val)
        self._move_state = val
    
    @staticmethod
    def get_api_name():
          return "vol-move-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'source-volume-name',
            'cutover-window',
            'dest-aggregate',
            'current-transfer',
            'last-transfer-duration',
            'dest-volume',
            'cutover-attempts',
            'error-string',
            'last-transfer-size',
            'pause-reason',
            'move-state',
        ]
    
    def describe_properties(self):
        return {
            'source_volume_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'cutover_window': { 'class': int, 'is_list': False, 'required': 'required' },
            'dest_aggregate': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'current_transfer': { 'class': int, 'is_list': False, 'required': 'optional' },
            'last_transfer_duration': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dest_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cutover_attempts': { 'class': int, 'is_list': False, 'required': 'required' },
            'error_string': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_transfer_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'pause_reason': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'move_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
