from netapp.disk.maint_test_result_info import MaintTestResultInfo
from netapp.netapp_object import NetAppObject

class MaintTestStatusInfo(NetAppObject):
    """
    Maintenance Center test information.
    """
    
    _status = None
    @property
    def status(self):
        """
        status
        Possible values are: "running", "copying", "pending",
        "not-testing", "disk-not-found", and "status-failed".
        "copying" is returned for disks that will start testing when
        the copy of their data to a replacement disk is complete.
        "pending" is returned for disks that are marked to be copied before
        testing starts but have not started the copy yet.
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _current_test = None
    @property
    def current_test(self):
        """
        Current test number. This is the index number in
        maint-test-results, starting with 1.
        This value is only present if status is "running".
        """
        return self._current_test
    @current_test.setter
    def current_test(self, val):
        if val != None:
            self.validate('current_test', val)
        self._current_test = val
    
    _total_tests = None
    @property
    def total_tests(self):
        """
        Total number of test.
        This value is only present if status is "running".
        """
        return self._total_tests
    @total_tests.setter
    def total_tests(self, val):
        if val != None:
            self.validate('total_tests', val)
        self._total_tests = val
    
    _total_cycles = None
    @property
    def total_cycles(self):
        """
        Total number of test cycles.
        This value is only present if status is "running".
        """
        return self._total_cycles
    @total_cycles.setter
    def total_cycles(self, val):
        if val != None:
            self.validate('total_cycles', val)
        self._total_cycles = val
    
    _maint_test_results = None
    @property
    def maint_test_results(self):
        """
        Results of tests.
        These results are only present if status is "running".
        """
        return self._maint_test_results
    @maint_test_results.setter
    def maint_test_results(self, val):
        if val != None:
            self.validate('maint_test_results', val)
        self._maint_test_results = val
    
    _disk_name = None
    @property
    def disk_name(self):
        """
        name of disk.
        """
        return self._disk_name
    @disk_name.setter
    def disk_name(self, val):
        if val != None:
            self.validate('disk_name', val)
        self._disk_name = val
    
    _current_cycle = None
    @property
    def current_cycle(self):
        """
        Current cycle number.
        This value is only present if status is "running".
        """
        return self._current_cycle
    @current_cycle.setter
    def current_cycle(self, val):
        if val != None:
            self.validate('current_cycle', val)
        self._current_cycle = val
    
    @staticmethod
    def get_api_name():
          return "maint-test-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'current-test',
            'total-tests',
            'total-cycles',
            'maint-test-results',
            'disk-name',
            'current-cycle',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'current_test': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_tests': { 'class': int, 'is_list': False, 'required': 'optional' },
            'total_cycles': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maint_test_results': { 'class': MaintTestResultInfo, 'is_list': True, 'required': 'optional' },
            'disk_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'current_cycle': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
