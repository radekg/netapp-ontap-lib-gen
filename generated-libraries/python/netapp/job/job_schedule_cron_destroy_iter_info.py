from netapp.job.job_schedule_cron_info import JobScheduleCronInfo
from netapp.netapp_object import NetAppObject

class JobScheduleCronDestroyIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against job-schedule-cron object.
    were not deleted due to some error.
    due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _job_schedule_cron_key = None
    @property
    def job_schedule_cron_key(self):
        """
        The keys for the job-schedule-cron object to which the
        deletion applies.
        """
        return self._job_schedule_cron_key
    @job_schedule_cron_key.setter
    def job_schedule_cron_key(self, val):
        if val != None:
            self.validate('job_schedule_cron_key', val)
        self._job_schedule_cron_key = val
    
    _error_code = None
    @property
    def error_code(self):
        """
        Error code, if the deletion operation caused an error.
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
    
    @staticmethod
    def get_api_name():
          return "job-schedule-cron-destroy-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-schedule-cron-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'job_schedule_cron_key': { 'class': JobScheduleCronInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
