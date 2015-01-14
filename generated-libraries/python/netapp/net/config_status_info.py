from netapp.netapp_object import NetAppObject

class ConfigStatusInfo(NetAppObject):
    """
    status of net-config-info object being returned
    used to return non-fatal errors encountered
    """
    
    _status = None
    @property
    def status(self):
        """
        Error status of config object.
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _operation = None
    @property
    def operation(self):
        """
        Operation where error was encountered.
        """
        return self._operation
    @operation.setter
    def operation(self, val):
        if val != None:
            self.validate('operation', val)
        self._operation = val
    
    @staticmethod
    def get_api_name():
          return "config-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'operation',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'operation': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
