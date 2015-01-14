from netapp.netapp_object import NetAppObject

class ObjectInfo(NetAppObject):
    """
    Description of a performance object.
    """
    
    _description = None
    @property
    def description(self):
        """
        Description of the object
        """
        return self._description
    @description.setter
    def description(self, val):
        if val != None:
            self.validate('description', val)
        self._description = val
    
    _get_instances_preferred_counter = None
    @property
    def get_instances_preferred_counter(self):
        """
        Name of the counter, either instance_name or instance_uuid, which should be used for
        perf-object-get-instances ZAPI for optimal performance. If this element is absent
        for an object, the value of this element defaults to instance_name counter. This
        element is a performance hint for getting optimal performance for the
        perf-object-get-instances ZAPI. If the value of this element is set to instance UUID
        counter of an object, using the instance UUID counter in the
        perf-object-get-instances query will return the counter information faster than
        using instance name counter. Otherwise, instance_name will yield faster results.
        """
        return self._get_instances_preferred_counter
    @get_instances_preferred_counter.setter
    def get_instances_preferred_counter(self, val):
        if val != None:
            self.validate('get_instances_preferred_counter', val)
        self._get_instances_preferred_counter = val
    
    _name = None
    @property
    def name(self):
        """
        Name of the object
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _privilege_level = None
    @property
    def privilege_level(self):
        """
        The object privilege level.  Any object with a privilege level
        of "diag" is not guaranteed to work, to exist in future releases,
        or to remain unchanged. <br>
        Possible values: basic, admin, advanced or diag.
        """
        return self._privilege_level
    @privilege_level.setter
    def privilege_level(self, val):
        if val != None:
            self.validate('privilege_level', val)
        self._privilege_level = val
    
    @staticmethod
    def get_api_name():
          return "object-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'description',
            'get-instances-preferred-counter',
            'name',
            'privilege-level',
        ]
    
    def describe_properties(self):
        return {
            'description': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'get_instances_preferred_counter': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'privilege_level': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
