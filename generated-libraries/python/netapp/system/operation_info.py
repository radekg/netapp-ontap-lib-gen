from netapp.netapp_object import NetAppObject

class OperationInfo(NetAppObject):
    """
    Operation details. Contains the operation name, command path and
    API name.
    """
    
    _api_name = None
    @property
    def api_name(self):
        """
        API corresponding to operation, for e.g., if object name
        is 'volume' and operation name is 'create' then
        operation's api name would be 'volume-create'. If
        multiple APIs are associated with same operation then API
        names will be ',' separated.
        Attributes: non-creatable, non-modifiable
        """
        return self._api_name
    @api_name.setter
    def api_name(self, val):
        if val != None:
            self.validate('api_name', val)
        self._api_name = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the operation, for e.g., 'create', 'modify'
        etc..
        Attributes: key, non-creatable, non-modifiable
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _command_path = None
    @property
    def command_path(self):
        """
        Operation Command Directory Path
        Attributes: non-creatable, non-modifiable
        """
        return self._command_path
    @command_path.setter
    def command_path(self, val):
        if val != None:
            self.validate('command_path', val)
        self._command_path = val
    
    @staticmethod
    def get_api_name():
          return "operation-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'api-name',
            'name',
            'command-path',
        ]
    
    def describe_properties(self):
        return {
            'api_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'command_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
