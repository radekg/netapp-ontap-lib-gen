from netapp.netapp_object import NetAppObject

class CoreSegmentConfigInfo(NetAppObject):
    """
    Core Segmentation Configuration
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
        Node to which this core segment configuration belongs.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _is_auto_segment = None
    @property
    def is_auto_segment(self):
        """
        If true, enables automatic core segmenting after saving
        of a full core.
        Attributes: non-creatable, modifiable
        """
        return self._is_auto_segment
    @is_auto_segment.setter
    def is_auto_segment(self, val):
        if val != None:
            self.validate('is_auto_segment', val)
        self._is_auto_segment = val
    
    _is_auto_delete = None
    @property
    def is_auto_delete(self):
        """
        If true, enables deletion of full core after automatic
        core segmenting.
        Attributes: non-creatable, modifiable
        """
        return self._is_auto_delete
    @is_auto_delete.setter
    def is_auto_delete(self, val):
        if val != None:
            self.validate('is_auto_delete', val)
        self._is_auto_delete = val
    
    @staticmethod
    def get_api_name():
          return "core-segment-config-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'is-auto-segment',
            'is-auto-delete',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_auto_segment': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_auto_delete': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
