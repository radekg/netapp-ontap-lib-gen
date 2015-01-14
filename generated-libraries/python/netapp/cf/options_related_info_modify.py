from netapp.netapp_object import NetAppObject

class OptionsRelatedInfoModify(NetAppObject):
    """
    Storage Failover Options to Modify
    """
    
    _node = None
    @property
    def node(self):
        """
        Node name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _auto_giveback_enabled = None
    @property
    def auto_giveback_enabled(self):
        """
        True, if auto-giveback is enabled, false otherwise.
        Attributes: non-creatable, modifiable
        """
        return self._auto_giveback_enabled
    @auto_giveback_enabled.setter
    def auto_giveback_enabled(self, val):
        if val != None:
            self.validate('auto_giveback_enabled', val)
        self._auto_giveback_enabled = val
    
    @staticmethod
    def get_api_name():
          return "options-related-info-modify"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'auto-giveback-enabled',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'auto_giveback_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
