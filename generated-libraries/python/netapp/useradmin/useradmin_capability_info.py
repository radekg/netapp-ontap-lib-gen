from netapp.netapp_object import NetAppObject

class UseradminCapabilityInfo(NetAppObject):
    """
    Capability to run a command or commands on the filer.
    """
    
    _name = None
    @property
    def name(self):
        """
        Name of the capability
        Possible values include: "*", "login-*", "cli-*",
        "api-*", "security-*"...
        Instead of "*", commands and subcommands can be specified
        directly. Please see man page or other documentation for
        more details.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "useradmin-capability-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
