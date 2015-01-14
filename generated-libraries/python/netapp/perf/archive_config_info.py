from netapp.perf.enabled_preset import EnabledPreset
from netapp.netapp_object import NetAppObject

class ArchiveConfigInfo(NetAppObject):
    """
    Performance Archive Configuration Info
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _datastore_file_rotation = None
    @property
    def datastore_file_rotation(self):
        """
        Minutes Between Performance Archive Data File Rotations
        Attributes: non-creatable, modifiable
        """
        return self._datastore_file_rotation
    @datastore_file_rotation.setter
    def datastore_file_rotation(self, val):
        if val != None:
            self.validate('datastore_file_rotation', val)
        self._datastore_file_rotation = val
    
    _enabled_presets = None
    @property
    def enabled_presets(self):
        """
        Archive-Enabled Performance Preset Info
        """
        return self._enabled_presets
    @enabled_presets.setter
    def enabled_presets(self, val):
        if val != None:
            self.validate('enabled_presets', val)
        self._enabled_presets = val
    
    _version = None
    @property
    def version(self):
        """
        Data ONTAP Version of Installed Configuration
        Attributes: non-creatable, non-modifiable
        """
        return self._version
    @version.setter
    def version(self, val):
        if val != None:
            self.validate('version', val)
        self._version = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        Is the Performance Archive Enabled?
        Attributes: non-creatable, modifiable
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _datastore_max_percent = None
    @property
    def datastore_max_percent(self):
        """
        Maximum Percentage of Root Volume Used for Performance
        Archive Data
        Attributes: non-creatable, modifiable
        """
        return self._datastore_max_percent
    @datastore_max_percent.setter
    def datastore_max_percent(self, val):
        if val != None:
            self.validate('datastore_max_percent', val)
        self._datastore_max_percent = val
    
    _datastore_max_retention = None
    @property
    def datastore_max_retention(self):
        """
        Days to Retain Performance Archive Data
        Attributes: non-creatable, modifiable
        """
        return self._datastore_max_retention
    @datastore_max_retention.setter
    def datastore_max_retention(self, val):
        if val != None:
            self.validate('datastore_max_retention', val)
        self._datastore_max_retention = val
    
    @staticmethod
    def get_api_name():
          return "archive-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'datastore-file-rotation',
            'enabled-presets',
            'version',
            'is-enabled',
            'datastore-max-percent',
            'datastore-max-retention',
        ]
    
    def describe_properties(self):
        return {
            'datastore_file_rotation': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enabled_presets': { 'class': EnabledPreset, 'is_list': True, 'required': 'optional' },
            'version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'datastore_max_percent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'datastore_max_retention': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
