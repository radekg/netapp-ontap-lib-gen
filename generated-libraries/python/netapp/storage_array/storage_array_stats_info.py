from netapp.storage_array.storage_array_stats_error_info import StorageArrayStatsErrorInfo
from netapp.netapp_object import NetAppObject

class StorageArrayStatsInfo(NetAppObject):
    """
    Contains statistics about an array.
    """
    
    _errors = None
    @property
    def errors(self):
        """
        A list of all errors for the requested array.
        """
        return self._errors
    @errors.setter
    def errors(self, val):
        if val != None:
            self.validate('errors', val)
        self._errors = val
    
    _upgrade_pending_status = None
    @property
    def upgrade_pending_status(self):
        """
        This field is set to true if an array NDU is in progress. If not it's set to false.
        """
        return self._upgrade_pending_status
    @upgrade_pending_status.setter
    def upgrade_pending_status(self, val):
        if val != None:
            self.validate('upgrade_pending_status', val)
        self._upgrade_pending_status = val
    
    _optimization_policy = None
    @property
    def optimization_policy(self):
        """
        Describes the I/O optimization policy used by this array.
        <p>Possible values are:
        <ul>
        <li>"ialua" - The array supports iALUA.
        <li>"ealua" - The array supports eALUA.
        <li>"symmetric" - All ports on the array will be treated equally.
        <li>"proprietary" - A vendor specific optimization is supported for this array.
        <li>"mixed" - This array supports multiple optimization policies, one per node.
        <li>"unknown" - No known optimization method is supported for this array (will be treated as if Symmetric)
        </ul>
        """
        return self._optimization_policy
    @optimization_policy.setter
    def optimization_policy(self, val):
        if val != None:
            self.validate('optimization_policy', val)
        self._optimization_policy = val
    
    _affinity = None
    @property
    def affinity(self):
        """
        Describes the affinity model supported by the array.
        <p>Possible values are:
        <ul>
        <li>"none" - None
        <li>"aaa" - Active/Active Asymmettric
        <li>"ap"   - Active/Passive
        <li>"mixed" - This array is presenting different affinity models to different controllers within the cluster.
        </ul>
        """
        return self._affinity
    @affinity.setter
    def affinity(self, val):
        if val != None:
            self.validate('affinity', val)
        self._affinity = val
    
    _array_name = None
    @property
    def array_name(self):
        """
        28 character string, no spaces
        The name of the array profile.
        """
        return self._array_name
    @array_name.setter
    def array_name(self, val):
        if val != None:
            self.validate('array_name', val)
        self._array_name = val
    
    _id = None
    @property
    def id(self):
        """
        Primary key (system defined) for the array record.
        Range: [0..2^64-1]
        """
        return self._id
    @id.setter
    def id(self, val):
        if val != None:
            self.validate('id', val)
        self._id = val
    
    @staticmethod
    def get_api_name():
          return "storage-array-stats-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'errors',
            'upgrade-pending-status',
            'optimization-policy',
            'affinity',
            'array-name',
            'id',
        ]
    
    def describe_properties(self):
        return {
            'errors': { 'class': StorageArrayStatsErrorInfo, 'is_list': True, 'required': 'optional' },
            'upgrade_pending_status': { 'class': bool, 'is_list': False, 'required': 'required' },
            'optimization_policy': { 'class': int, 'is_list': False, 'required': 'required' },
            'affinity': { 'class': int, 'is_list': False, 'required': 'required' },
            'array_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'id': { 'class': int, 'is_list': False, 'required': 'required' },
        }
