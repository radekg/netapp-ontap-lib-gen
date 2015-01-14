from netapp.netapp_object import NetAppObject

class PortsetInfo(NetAppObject):
    """
    Information about a port set.
    """
    
    _portset_type = None
    @property
    def portset_type(self):
        """
        Possible values: "fcp", "iscsi", "mixed".
        """
        return self._portset_type
    @portset_type.setter
    def portset_type(self, val):
        if val != None:
            self.validate('portset_type', val)
        self._portset_type = val
    
    _portset_port_total = None
    @property
    def portset_port_total(self):
        """
        Total number of ports in the port set.
        """
        return self._portset_port_total
    @portset_port_total.setter
    def portset_port_total(self, val):
        if val != None:
            self.validate('portset_port_total', val)
        self._portset_port_total = val
    
    _portset_port_info = None
    @property
    def portset_port_info(self):
        """
        Information about the ports belonging to the set.
        """
        return self._portset_port_info
    @portset_port_info.setter
    def portset_port_info(self, val):
        if val != None:
            self.validate('portset_port_info', val)
        self._portset_port_info = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver containing this portset.
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _portset_name = None
    @property
    def portset_name(self):
        """
        Name of this port set.
        """
        return self._portset_name
    @portset_name.setter
    def portset_name(self, val):
        if val != None:
            self.validate('portset_name', val)
        self._portset_name = val
    
    _initiator_group_info = None
    @property
    def initiator_group_info(self):
        """
        Information about the initiator group(s) that are
        bound to the portset.
        """
        return self._initiator_group_info
    @initiator_group_info.setter
    def initiator_group_info(self, val):
        if val != None:
            self.validate('initiator_group_info', val)
        self._initiator_group_info = val
    
    @staticmethod
    def get_api_name():
          return "portset-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'portset-type',
            'portset-port-total',
            'portset-port-info',
            'vserver',
            'portset-name',
            'initiator-group-info',
        ]
    
    def describe_properties(self):
        return {
            'portset_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'portset_port_total': { 'class': int, 'is_list': False, 'required': 'required' },
            'portset_port_info': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'portset_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'initiator_group_info': { 'class': basestring, 'is_list': True, 'required': 'optional' },
        }
