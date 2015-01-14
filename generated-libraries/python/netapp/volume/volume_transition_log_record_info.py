from netapp.volume.volume_transition_log_attrs_info import VolumeTransitionLogAttrsInfo
from netapp.netapp_object import NetAppObject

class VolumeTransitionLogRecordInfo(NetAppObject):
    """
    Information about a single log record.
    """
    
    _description = None
    @property
    def description(self):
        """
        Detailed description if any associated with this record.
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    _level = None
    @property
    def level(self):
        """
        Describes why this record was logged.
        Possible values:
        "all"
        "error"
        "warning"
        "info"
        "debug"
        "trace"
        """
        return self._level
    @level.setter
    def level(self, val):
        if val != None:
            self.validate('level', val)
        self._level = val
    
    _timestamp = None
    @property
    def timestamp(self):
        """
        Timestamp when record was logged.
        Timestamp will be in the following format:
        "MM/DD HH:MM:SS"
        """
        return self._timestamp
    @timestamp.setter
    def timestamp(self, val):
        if val != None:
            self.validate('timestamp', val)
        self._timestamp = val
    
    _feature = None
    @property
    def feature(self):
        """
        Which feature logged this message. This is valid only for
        plugin_start, plugin_end and action record types.
        """
        return self._feature
    @feature.setter
    def feature(self, val):
        if val != None:
            self.validate('feature', val)
        self._feature = val
    
    _phase = None
    @property
    def phase(self):
        """
        Which phase logged this message.
        Possible values:
        "all"
        "check"
        "lock_config"
        "prepare"
        "pre_commit"
        "commit"
        "post_commit"
        "online"
        "rollback"
        "cleanup"
        "unlock_config"
        "complete"
        """
        return self._phase
    @phase.setter
    def phase(self, val):
        if val != None:
            self.validate('phase', val)
        self._phase = val
    
    _attributes = None
    @property
    def attributes(self):
        """
        Information about attributes included in an Action record.
        """
        return self._attributes
    @attributes.setter
    def attributes(self, val):
        if val != None:
            self.validate('attributes', val)
        self._attributes = val
    
    _record_type = None
    @property
    def record_type(self):
        """
        Type of record.
        Possible values:
        "phase_start"
        "phase_end"
        "plugin_start"
        "plugin_end"
        "action"
        """
        return self._record_type
    @record_type.setter
    def record_type(self, val):
        if val != None:
            self.validate('record_type', val)
        self._record_type = val
    
    @staticmethod
    def get_api_name():
          return "volume-transition-log-record-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'description',
            'level',
            'timestamp',
            'feature',
            'phase',
            'attributes',
            'record-type',
        ]
    
    def describe_properties(self):
        return {
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'level': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'timestamp': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'feature': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'phase': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'attributes': { 'class': VolumeTransitionLogAttrsInfo, 'is_list': True, 'required': 'optional' },
            'record_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
