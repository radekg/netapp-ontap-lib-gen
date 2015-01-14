from netapp.netapp_object import NetAppObject

class MaintTestResultInfo(NetAppObject):
    """
    Results of tests.
    """
    
    _current_test_iteration = None
    @property
    def current_test_iteration(self):
        """
        Current iteration number of test.
        """
        return self._current_test_iteration
    @current_test_iteration.setter
    def current_test_iteration(self, val):
        if val != None:
            self.validate('current_test_iteration', val)
        self._current_test_iteration = val
    
    _total_test_iterations = None
    @property
    def total_test_iterations(self):
        """
        Total number of iterations to run this test.
        """
        return self._total_test_iterations
    @total_test_iterations.setter
    def total_test_iterations(self, val):
        if val != None:
            self.validate('total_test_iterations', val)
        self._total_test_iterations = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the test.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _current_test_cycle = None
    @property
    def current_test_cycle(self):
        """
        Current cycle number of test.
        """
        return self._current_test_cycle
    @current_test_cycle.setter
    def current_test_cycle(self, val):
        if val != None:
            self.validate('current_test_cycle', val)
        self._current_test_cycle = val
    
    _status = None
    @property
    def status(self):
        """
        Status of the test.
        Possible values are "not-started", "running", "success",
        "error", "aborted", "not-supported", or "unknown-error".
        "not-supported" is returned for a test that was specified
        to be run on a disk that does not support that test.
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _elapsed_time = None
    @property
    def elapsed_time(self):
        """
        Elapsed time of the test in seconds.
        This value is not present for a status of "not-started",
        or "not-supported".
        """
        return self._elapsed_time
    @elapsed_time.setter
    def elapsed_time(self, val):
        if val != None:
            self.validate('elapsed_time', val)
        self._elapsed_time = val
    
    @staticmethod
    def get_api_name():
          return "maint-test-result-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'current-test-iteration',
            'total-test-iterations',
            'name',
            'current-test-cycle',
            'status',
            'elapsed-time',
        ]
    
    def describe_properties(self):
        return {
            'current_test_iteration': { 'class': int, 'is_list': False, 'required': 'required' },
            'total_test_iterations': { 'class': int, 'is_list': False, 'required': 'required' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'current_test_cycle': { 'class': int, 'is_list': False, 'required': 'required' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'elapsed_time': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
