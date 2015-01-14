from netapp.snapmirror.snapmirror_info import SnapmirrorInfo
from netapp.netapp_object import NetAppObject

class SnapmirrorUpdateIterInfo(NetAppObject):
    """
    Information about the operation that was attempted/performed
    against snapmirror object.
    not operated on due some error.
    due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _status = None
    @property
    def status(self):
        """
        The operation status.  Possible values:
        "succeeded",
        "in_progress",
        "failed".
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _snapmirror_key = None
    @property
    def snapmirror_key(self):
        """
        The keys for the snapmirror object to which the operation
        applies.
        """
        return self._snapmirror_key
    @snapmirror_key.setter
    def snapmirror_key(self, val):
        if val != None:
            self.validate('snapmirror_key', val)
        self._snapmirror_key = val
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the operation caused an error.
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
        Error description, if the operation caused an error.
        """
        return self._error_message
    @error_message.setter
    def error_message(self, val):
        if val != None:
            self.validate('error_message', val)
        self._error_message = val
    
    _jobid = None
    @property
    def jobid(self):
        """
        Job Id, if this operation was performed via a job.
        """
        return self._jobid
    @jobid.setter
    def jobid(self, val):
        if val != None:
            self.validate('jobid', val)
        self._jobid = val
    
    @staticmethod
    def get_api_name():
          return "snapmirror-update-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'snapmirror-key',
            'error-code',
            'error-message',
            'jobid',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'snapmirror_key': { 'class': SnapmirrorInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'jobid': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
