from netapp.netapp_object import NetAppObject

class LifPlacementInfo(NetAppObject):
    """
    SAN LIF placement
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
    
    _home_port = None
    @property
    def home_port(self):
        """
        Port info
        Attributes: non-creatable, non-modifiable
        """
        return self._home_port
    @home_port.setter
    def home_port(self, val):
        if val != None:
            self.validate('home_port', val)
        self._home_port = val
    
    _home_node = None
    @property
    def home_node(self):
        """
        Home node info
        Attributes: non-creatable, non-modifiable
        """
        return self._home_node
    @home_node.setter
    def home_node(self, val):
        if val != None:
            self.validate('home_node', val)
        self._home_node = val
    
    @staticmethod
    def get_api_name():
          return "lif-placement-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'home-port',
            'home-node',
        ]
    
    def describe_properties(self):
        return {
            'home_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'home_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
