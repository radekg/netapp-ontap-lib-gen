from netapp.netapp_object import NetAppObject

class NodeVersionDetailInfo(NetAppObject):
    """
    The node names along with the ONTAP version on
    the respective node.
    """
    
    _build_timestamp = None
    @property
    def build_timestamp(self):
        """
        Time of build creation, in seconds since January 1, 1970, of
        the image running on the node. This field is available in
        Data ONTAP 8.1 or later.
        """
        return self._build_timestamp
    @build_timestamp.setter
    def build_timestamp(self, val):
        if val != None:
            self.validate('build_timestamp', val)
        self._build_timestamp = val
    
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
    
    _version = None
    @property
    def version(self):
        """
        Data ONTAP version running on the node.
        """
        return self._version
    @version.setter
    def version(self, val):
        if val != None:
            self.validate('version', val)
        self._version = val
    
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
          return "node-version-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'build-timestamp',
            'node-name',
            'version',
            'node-uuid',
        ]
    
    def describe_properties(self):
        return {
            'build_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'version': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'node_uuid': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
