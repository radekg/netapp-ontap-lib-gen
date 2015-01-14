from netapp.netapp_object import NetAppObject

class JobLogConfigInfo(NetAppObject):
    """
    Contains job-manager-logging configuration for a single module in
    the system.
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
    
    _job_log_level = None
    @property
    def job_log_level(self):
        """
        The verbosity of logging enabled in the given module.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "emerg"     ,
        <li> "alert"     ,
        <li> "crit"      ,
        <li> "err"       ,
        <li> "warning"   ,
        <li> "notice"    ,
        <li> "info"      ,
        <li> "debug"
        </ul>
        """
        return self._job_log_level
    @job_log_level.setter
    def job_log_level(self, val):
        if val != None:
            self.validate('job_log_level', val)
        self._job_log_level = val
    
    _job_log_module = None
    @property
    def job_log_module(self):
        """
        The module being logged.  These are pre-defined in the
        system binaries. To get an up-to-date list call
        job-log-config-get-iter without a query.
        Attributes: key, required-for-create, non-modifiable
        """
        return self._job_log_module
    @job_log_module.setter
    def job_log_module(self, val):
        if val != None:
            self.validate('job_log_module', val)
        self._job_log_module = val
    
    @staticmethod
    def get_api_name():
          return "job-log-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'job-log-level',
            'job-log-module',
        ]
    
    def describe_properties(self):
        return {
            'job_log_level': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_log_module': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
