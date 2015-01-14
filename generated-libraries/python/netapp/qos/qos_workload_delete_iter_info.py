from netapp.qos.qos_workload_info import QosWorkloadInfo
from netapp.netapp_object import NetAppObject

class QosWorkloadDeleteIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against qos-workload object.
    not deleted due to some error.
    to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _qos_workload_key = None
    @property
    def qos_workload_key(self):
        """
        The keys for the qos-workload object to which the
        deletion applies.
        """
        return self._qos_workload_key
    @qos_workload_key.setter
    def qos_workload_key(self, val):
        if val != None:
            self.validate('qos_workload_key', val)
        self._qos_workload_key = val
    
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
          return "qos-workload-delete-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'qos-workload-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'qos_workload_key': { 'class': QosWorkloadInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
