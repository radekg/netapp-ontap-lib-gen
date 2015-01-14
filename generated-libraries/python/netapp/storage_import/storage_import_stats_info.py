from netapp.netapp_object import NetAppObject

class StorageImportStatsInfo(NetAppObject):
    """
    Contains statistics about an import session
    """
    
    _verify_end_time = None
    @property
    def verify_end_time(self):
        """
        Storage import verify end time in secs
        """
        return self._verify_end_time
    @verify_end_time.setter
    def verify_end_time(self, val):
        if val != None:
            self.validate('verify_end_time', val)
        self._verify_end_time = val
    
    _vserver_name = None
    @property
    def vserver_name(self):
        """
        The name of the vserver hosting the target LUN
        """
        return self._vserver_name
    @vserver_name.setter
    def vserver_name(self, val):
        if val != None:
            self.validate('vserver_name', val)
        self._vserver_name = val
    
    _import_state = None
    @property
    def import_state(self):
        """
        Import State
        <p>
        Possible values:
        <ul>
        <li> 'ready'			... Ready for import,
        <li> 'in_progress'		... Import in progress,
        <li> 'failed'			... Import failed,
        <li> 'completed'		... Import completed,
        <li> 'aborted'			... Import aborted,
        <li> 'verify_in_progress'	... Verify in progress,
        <li> 'verify_completed'		... verify completed,
        <li> 'verify_failed'		... Verify failed,
        <li> 'verify_aborted'		... Verify aborted,
        </ul>
        """
        return self._import_state
    @import_state.setter
    def import_state(self, val):
        if val != None:
            self.validate('import_state', val)
        self._import_state = val
    
    _import_start_time = None
    @property
    def import_start_time(self):
        """
        Import start time in secs
        """
        return self._import_start_time
    @import_start_time.setter
    def import_start_time(self, val):
        if val != None:
            self.validate('import_start_time', val)
        self._import_start_time = val
    
    _import_end_time = None
    @property
    def import_end_time(self):
        """
        Import end time in secs
        """
        return self._import_end_time
    @import_end_time.setter
    def import_end_time(self, val):
        if val != None:
            self.validate('import_end_time', val)
        self._import_end_time = val
    
    _source_array_lun = None
    @property
    def source_array_lun(self):
        """
        Name of the foreign array LUN
        """
        return self._source_array_lun
    @source_array_lun.setter
    def source_array_lun(self, val):
        if val != None:
            self.validate('source_array_lun', val)
        self._source_array_lun = val
    
    _data_imported = None
    @property
    def data_imported(self):
        """
        Data imported in Bytes
        """
        return self._data_imported
    @data_imported.setter
    def data_imported(self, val):
        if val != None:
            self.validate('data_imported', val)
        self._data_imported = val
    
    _percentage_complete = None
    @property
    def percentage_complete(self):
        """
        Import complete percentage
        """
        return self._percentage_complete
    @percentage_complete.setter
    def percentage_complete(self, val):
        if val != None:
            self.validate('percentage_complete', val)
        self._percentage_complete = val
    
    _target_lun_path = None
    @property
    def target_lun_path(self):
        """
        Data ONTAP(R) LUN Path
        """
        return self._target_lun_path
    @target_lun_path.setter
    def target_lun_path(self, val):
        if val != None:
            self.validate('target_lun_path', val)
        self._target_lun_path = val
    
    _verify_start_time = None
    @property
    def verify_start_time(self):
        """
        Storage import verify start time in secs
        """
        return self._verify_start_time
    @verify_start_time.setter
    def verify_start_time(self, val):
        if val != None:
            self.validate('verify_start_time', val)
        self._verify_start_time = val
    
    @staticmethod
    def get_api_name():
          return "storage-import-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'verify-end-time',
            'vserver-name',
            'import-state',
            'import-start-time',
            'import-end-time',
            'source-array-lun',
            'data-imported',
            'percentage-complete',
            'target-lun-path',
            'verify-start-time',
        ]
    
    def describe_properties(self):
        return {
            'verify_end_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'import_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'import_start_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'import_end_time': { 'class': int, 'is_list': False, 'required': 'required' },
            'source_array_lun': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'data_imported': { 'class': int, 'is_list': False, 'required': 'required' },
            'percentage_complete': { 'class': int, 'is_list': False, 'required': 'required' },
            'target_lun_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'verify_start_time': { 'class': int, 'is_list': False, 'required': 'required' },
        }
