from netapp.job.job_info import JobInfo
from netapp.netapp_object import NetAppObject

class JobPrivateDeleteIterInfo(NetAppObject):
    """
    Information about the operation that was attempted/performed
    against private job object.
    were not operated on due some error.
    due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
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
    
    _job_private_key = None
    @property
    def job_private_key(self):
        """
        The keys for the private job object to which the
        operation applies.
        """
        return self._job_private_key
    @job_private_key.setter
    def job_private_key(self, val):
        if val != None:
            self.validate('job_private_key', val)
        self._job_private_key = val
    
    @staticmethod
    def get_api_name():
          return "job-private-delete-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'job-private-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_private_key': { 'class': JobInfo, 'is_list': False, 'required': 'required' },
        }
