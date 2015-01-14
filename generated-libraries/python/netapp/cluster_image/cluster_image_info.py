from netapp.netapp_object import NetAppObject

class ClusterImageInfo(NetAppObject):
    """
    Information to manage cluster images for Non disruptive-update.
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
    
    _current_version = None
    @property
    def current_version(self):
        """
        Current Version
        Attributes: non-creatable, non-modifiable
        """
        return self._current_version
    @current_version.setter
    def current_version(self, val):
        if val != None:
            self.validate('current_version', val)
        self._current_version = val
    
    _node_id = None
    @property
    def node_id(self):
        """
        Node
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node_id
    @node_id.setter
    def node_id(self, val):
        if val != None:
            self.validate('node_id', val)
        self._node_id = val
    
    _date_installed = None
    @property
    def date_installed(self):
        """
        Date Installed
        Attributes: non-creatable, non-modifiable
        """
        return self._date_installed
    @date_installed.setter
    def date_installed(self, val):
        if val != None:
            self.validate('date_installed', val)
        self._date_installed = val
    
    @staticmethod
    def get_api_name():
          return "cluster-image-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'current-version',
            'node-id',
            'date-installed',
        ]
    
    def describe_properties(self):
        return {
            'current_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'date_installed': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
