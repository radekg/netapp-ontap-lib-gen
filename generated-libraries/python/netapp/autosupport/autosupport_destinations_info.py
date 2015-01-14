from netapp.netapp_object import NetAppObject

class AutosupportDestinationsInfo(NetAppObject):
    """
    AutoSupport destination summary
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _node_name = None
    @property
    def node_name(self):
        """
        The name of the filer that owns this destination
        configuration.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _destinations = None
    @property
    def destinations(self):
        """
        A comma separated list of destinations used to deliver
        AutoSupport messages.
        Attributes: non-creatable, non-modifiable
        """
        return self._destinations
    @destinations.setter
    def destinations(self, val):
        if val != None:
            self.validate('destinations', val)
        self._destinations = val
    
    @staticmethod
    def get_api_name():
          return "autosupport-destinations-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node-name',
            'destinations',
        ]
    
    def describe_properties(self):
        return {
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destinations': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
