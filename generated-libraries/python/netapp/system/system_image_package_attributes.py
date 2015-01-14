from netapp.netapp_object import NetAppObject

class SystemImagePackageAttributes(NetAppObject):
    """
    These attributes provide details about the software packages
    available on the system.
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
    
    _node = None
    @property
    def node(self):
        """
        Node
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _package = None
    @property
    def package(self):
        """
        Package File Name
        Attributes: key, optional-for-create, non-modifiable
        """
        return self._package
    @package.setter
    def package(self, val):
        if val != None:
            self.validate('package', val)
        self._package = val
    
    @staticmethod
    def get_api_name():
          return "system-image-package-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'package',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'package': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
