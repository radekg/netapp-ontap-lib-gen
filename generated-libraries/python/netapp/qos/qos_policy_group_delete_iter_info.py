from netapp.qos.qos_policy_group_info import QosPolicyGroupInfo
from netapp.netapp_object import NetAppObject

class QosPolicyGroupDeleteIterInfo(NetAppObject):
    """
    Information about the deletion operation that was
    attempted/performed against qos-policy-group object.
    were not deleted due to some error.
    due to some error.
    This element will be returned only if input element
    'return-failure-list' is true.
    """
    
    _qos_policy_group_key = None
    @property
    def qos_policy_group_key(self):
        """
        The keys for the qos-policy-group object to which the
        deletion applies.
        """
        return self._qos_policy_group_key
    @qos_policy_group_key.setter
    def qos_policy_group_key(self, val):
        if val != None:
            self.validate('qos_policy_group_key', val)
        self._qos_policy_group_key = val
    
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
          return "qos-policy-group-delete-iter-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'qos-policy-group-key',
            'error-code',
            'error-message',
        ]
    
    def describe_properties(self):
        return {
            'qos_policy_group_key': { 'class': QosPolicyGroupInfo, 'is_list': False, 'required': 'required' },
            'error_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'error_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
