from netapp.netapp_object import NetAppObject

class NodeOntapiDetailInfo(NetAppObject):
    """
    The node names along with the ONTAPI version on
    the respective node.
    """
    
    _node_name = None
    @property
    def node_name(self):
        """
        Name of the node.
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _minor_version = None
    @property
    def minor_version(self):
        """
        Current ONTAPI minor version supported by this node.
        Range: [0..2^31-1].
        """
        return self._minor_version
    @minor_version.setter
    def minor_version(self, val):
        if val != None:
            self.validate('minor_version', val)
        self._minor_version = val
    
    _major_version = None
    @property
    def major_version(self):
        """
        Current ONTAPI major version supported by this node.
        Range: [0..2^31-1].
        """
        return self._major_version
    @major_version.setter
    def major_version(self, val):
        if val != None:
            self.validate('major_version', val)
        self._major_version = val
    
    _node_uuid = None
    @property
    def node_uuid(self):
        """
        UUID, Universal Unique IDentifier, of the node.
        """
        return self._node_uuid
    @node_uuid.setter
    def node_uuid(self, val):
        if val != None:
            self.validate('node_uuid', val)
        self._node_uuid = val
    
    @staticmethod
    def get_api_name():
          return "node-ontapi-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node-name',
            'minor-version',
            'major-version',
            'node-uuid',
        ]
    
    def describe_properties(self):
        return {
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'minor_version': { 'class': int, 'is_list': False, 'required': 'required' },
            'major_version': { 'class': int, 'is_list': False, 'required': 'required' },
            'node_uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
