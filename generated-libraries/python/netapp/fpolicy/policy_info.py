from netapp.fpolicy.monitored_protocol_info import MonitoredProtocolInfo
from netapp.fpolicy.monitored_operation_info import MonitoredOperationInfo
from netapp.netapp_object import NetAppObject

class PolicyInfo(NetAppObject):
    """
    Structure containing information pertaining to policy.
    """
    
    _name = None
    @property
    def name(self):
        """
        Policy name.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _monitored_protocols = None
    @property
    def monitored_protocols(self):
        """
        List of monitored protocols.
        """
        return self._monitored_protocols
    @monitored_protocols.setter
    def monitored_protocols(self, val):
        if val != None:
            self.validate('monitored_protocols', val)
        self._monitored_protocols = val
    
    _is_ads_monitored = None
    @property
    def is_ads_monitored(self):
        """
        True if the policy monitors the cifs operations on
        Alternate Data Streams.
        """
        return self._is_ads_monitored
    @is_ads_monitored.setter
    def is_ads_monitored(self, val):
        if val != None:
            self.validate('is_ads_monitored', val)
        self._is_ads_monitored = val
    
    _number_of_screen_failures = None
    @property
    def number_of_screen_failures(self):
        """
        Number of failed (denied) screen requests.
        This value is reset each time the filer is rebooted or
        the policy is disabled.
        Range : [0..2^32-1].
        """
        return self._number_of_screen_failures
    @number_of_screen_failures.setter
    def number_of_screen_failures(self, val):
        if val != None:
            self.validate('number_of_screen_failures', val)
        self._number_of_screen_failures = val
    
    _is_i2p_enabled = None
    @property
    def is_i2p_enabled(self):
        """
        True if inode to pathname translation for NFS requests
        is supported and enabled.If enabled fpolicy requests
        to fpolicy server will carry full file path for NFS
        requests. The fields which will carry full file path
        are AccessPath and RenamePath for FP_ScreenRequest
        RPC call and sr_accesspath for FP_ScreenRequest2 RPC
        call.
        """
        return self._is_i2p_enabled
    @is_i2p_enabled.setter
    def is_i2p_enabled(self, val):
        if val != None:
            self.validate('is_i2p_enabled', val)
        self._is_i2p_enabled = val
    
    _is_offline_files_only = None
    @property
    def is_offline_files_only(self):
        """
        True if the file policy monitors only offlines files.
        Default is false.
        """
        return self._is_offline_files_only
    @is_offline_files_only.setter
    def is_offline_files_only(self, val):
        if val != None:
            self.validate('is_offline_files_only', val)
        self._is_offline_files_only = val
    
    _monitored_operations = None
    @property
    def monitored_operations(self):
        """
        List of monitored operations.
        """
        return self._monitored_operations
    @monitored_operations.setter
    def monitored_operations(self, val):
        if val != None:
            self.validate('monitored_operations', val)
        self._monitored_operations = val
    
    _is_enabled = None
    @property
    def is_enabled(self):
        """
        True if the policy is enabled. No matter whether
        the policy is enabled or disabled, values returned
        in other elements for the policy are always valid.
        """
        return self._is_enabled
    @is_enabled.setter
    def is_enabled(self, val):
        if val != None:
            self.validate('is_enabled', val)
        self._is_enabled = val
    
    _number_of_requests_blocked_locally = None
    @property
    def number_of_requests_blocked_locally(self):
        """
        Number of locally blocked(denied) screen requests.
        This value is reset each time the filer is rebooted or
        the policy is disabled.
        Range : [0..2^32-1].
        """
        return self._number_of_requests_blocked_locally
    @number_of_requests_blocked_locally.setter
    def number_of_requests_blocked_locally(self, val):
        if val != None:
            self.validate('number_of_requests_blocked_locally', val)
        self._number_of_requests_blocked_locally = val
    
    _number_of_screened_files = None
    @property
    def number_of_screened_files(self):
        """
        Number of screened files since policy has been enabled.
        This value is reset each time the filer is rebooted or
        the policy is disabled.
        Range : [0..2^32-1].
        """
        return self._number_of_screened_files
    @number_of_screened_files.setter
    def number_of_screened_files(self, val):
        if val != None:
            self.validate('number_of_screened_files', val)
        self._number_of_screened_files = val
    
    @staticmethod
    def get_api_name():
          return "policy-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'monitored-protocols',
            'is-ads-monitored',
            'number-of-screen-failures',
            'is-i2p-enabled',
            'is-offline-files-only',
            'monitored-operations',
            'is-enabled',
            'number-of-requests-blocked-locally',
            'number-of-screened-files',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'monitored_protocols': { 'class': MonitoredProtocolInfo, 'is_list': True, 'required': 'required' },
            'is_ads_monitored': { 'class': bool, 'is_list': False, 'required': 'required' },
            'number_of_screen_failures': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_i2p_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_offline_files_only': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'monitored_operations': { 'class': MonitoredOperationInfo, 'is_list': True, 'required': 'required' },
            'is_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'number_of_requests_blocked_locally': { 'class': int, 'is_list': False, 'required': 'required' },
            'number_of_screened_files': { 'class': int, 'is_list': False, 'required': 'required' },
        }
