from netapp.netapp_object import NetAppObject

class InterfaceListEntryInfo(NetAppObject):
    """
    Information about a single interface
    """
    
    _interface_name = None
    @property
    def interface_name(self):
        """
        Name of network interface.
        In Data ONTAP 7-Mode, this is the name of a
        physical or virtual ethernet interface,
        for example: "e0c" or "vif0".
        In Data ONTAP Cluster-Mode, this is the name
        of an iSCSI data LIF in the Vserver.
        """
        return self._interface_name
    @interface_name.setter
    def interface_name(self, val):
        if val != None:
            self.validate('interface_name', val)
        self._interface_name = val
    
    @staticmethod
    def get_api_name():
          return "interface-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'interface-name',
        ]
    
    def describe_properties(self):
        return {
            'interface_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
