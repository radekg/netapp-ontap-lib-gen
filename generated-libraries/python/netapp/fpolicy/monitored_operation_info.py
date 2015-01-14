from netapp.netapp_object import NetAppObject

class MonitoredOperationInfo(NetAppObject):
    """
    Structure containing information pertaining to monitored
    operations.
    """
    
    _operation = None
    @property
    def operation(self):
        """
        Supported values: "file-create", "file- delete",
        "file-open", "file-close", "file-rename",
        "directory-create", "directory-delete",
        "directory-rename", "getattr", "setattr", "lookup",
        "read", "write", "link", "symlink"
        """
        return self._operation
    @operation.setter
    def operation(self, val):
        if val != None:
            self.validate('operation', val)
        self._operation = val
    
    @staticmethod
    def get_api_name():
          return "monitored-operation-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'operation',
        ]
    
    def describe_properties(self):
        return {
            'operation': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
