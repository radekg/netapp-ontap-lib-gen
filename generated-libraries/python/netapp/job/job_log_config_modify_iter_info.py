from netapp.job.job_log_config_info import JobLogConfigInfo
from netapp.netapp_object import NetAppObject

class JobLogConfigModifyIterInfo(NetAppObject):
    """
    Information about the modify operation that was
    attempted/performed against job-log-config object.
    not modified due to some error.
    due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
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
    
    _job_log_config_key = None
    @property
    def job_log_config_key(self):
        """
        The keys for the job-log-config object to which the
        modify operation applies.
        """
        return self._job_log_config_key
    @job_log_config_key.setter
    def job_log_config_key(self, val):
        if val != None:
            self.validate('job_log_config_key', val)
        self._job_log_config_key = val
    
    @staticmethod
    def get_api_name():
          return "job-log-config-modify-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'error-code',
            'error-message',
            'job-log-config-key',
        ]
    
    def describe_properties(self):
        return {
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_log_config_key': { 'class': JobLogConfigInfo, 'is_list': False, 'required': 'required' },
        }
