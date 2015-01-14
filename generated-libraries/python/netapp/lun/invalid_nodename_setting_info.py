from netapp.netapp_object import NetAppObject

class InvalidNodenameSettingInfo(NetAppObject):
    """
    Information about different fcp nodenames
    """
    
    _local_fcp_node_name = None
    @property
    def local_fcp_node_name(self):
        """
        fcp nodename for the local filer
        """
        return self._local_fcp_node_name
    @local_fcp_node_name.setter
    def local_fcp_node_name(self, val):
        if val != None:
            self.validate('local_fcp_node_name', val)
        self._local_fcp_node_name = val
    
    _partner_fcp_node_name = None
    @property
    def partner_fcp_node_name(self):
        """
        fcp nodename for the partner filer
        """
        return self._partner_fcp_node_name
    @partner_fcp_node_name.setter
    def partner_fcp_node_name(self, val):
        if val != None:
            self.validate('partner_fcp_node_name', val)
        self._partner_fcp_node_name = val
    
    @staticmethod
    def get_api_name():
          return "invalid-nodename-setting-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'local-fcp-node-name',
            'partner-fcp-node-name',
        ]
    
    def describe_properties(self):
        return {
            'local_fcp_node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'partner_fcp_node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
