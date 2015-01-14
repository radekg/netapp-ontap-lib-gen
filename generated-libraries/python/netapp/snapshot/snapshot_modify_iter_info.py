from netapp.snapshot.snapshot_info import SnapshotInfo
from netapp.netapp_object import NetAppObject

class SnapshotModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against snapshot object.
    modified due to some error.
    some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _snapshot_key = None
    @property
    def snapshot_key(self):
        """
        The keys for the snapshot object to which the modify
        operation applies.
        """
        return self._snapshot_key
    @snapshot_key.setter
    def snapshot_key(self, val):
        if val != None:
            self.validate('snapshot_key', val)
        self._snapshot_key = val
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the modify operation caused an error.
        """
        return self._error_code
    @error_code.setter
    def error_code(self, val):
        if val != None:
            self.validate('error_code', val)
        self._error_code = val
    
    _error_message = None
    @property
    def error_message(self):
        """
        Error description, if the modify operation caused an
        error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'snapshot-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'snapshot_key': { 'class': SnapshotInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
