from netapp.netapp_object import NetAppObject

class VSeriesDetailInfo(NetAppObject):
    """
    LUN status from RAID array LUNs
    """
    
    _alternate_array_node_wwn = None
    @property
    def alternate_array_node_wwn(self):
        """
        The RAID array LUN alternate path is the path
        that can be used to communicate with the LUN,
        but not currently used.
        This is the WWNN (World Wide Node Name) of the array FC port used as
        the secondary path.
        """
        return self._alternate_array_node_wwn
    @alternate_array_node_wwn.setter
    def alternate_array_node_wwn(self, val):
        if val != None:
            self.validate('alternate_array_node_wwn', val)
        self._alternate_array_node_wwn = val
    
    _product_id = None
    @property
    def product_id(self):
        """
        Product id string of the raid array lun
        resides on.
        """
        return self._product_id
    @product_id.setter
    def product_id(self, val):
        if val != None:
            self.validate('product_id', val)
        self._product_id = val
    
    _alternate_switch_name = None
    @property
    def alternate_switch_name(self):
        """
        Switch name of the alternate path. Present for
        switch attached
        configurations only.
        """
        return self._alternate_switch_name
    @alternate_switch_name.setter
    def alternate_switch_name(self, val):
        if val != None:
            self.validate('alternate_switch_name', val)
        self._alternate_switch_name = val
    
    _primary_switch_name = None
    @property
    def primary_switch_name(self):
        """
        Switch name of the primary path. Present for
        switch attached	configurations only.
        """
        return self._primary_switch_name
    @primary_switch_name.setter
    def primary_switch_name(self, val):
        if val != None:
            self.validate('primary_switch_name', val)
        self._primary_switch_name = val
    
    _alternate_array_switch_port_wwn = None
    @property
    def alternate_array_switch_port_wwn(self):
        """
        The RAID array LUN alternate path is the path
        that can be used to communicate with the LUN,
        but not currently used.
        This is the WWN of the switch FC port connected
        to the array FC port used as primary path.
        This field is present in switch attached
        configrations only.
        """
        return self._alternate_array_switch_port_wwn
    @alternate_array_switch_port_wwn.setter
    def alternate_array_switch_port_wwn(self, val):
        if val != None:
            self.validate('alternate_array_switch_port_wwn', val)
        self._alternate_array_switch_port_wwn = val
    
    _primary_array_port_wwn = None
    @property
    def primary_array_port_wwn(self):
        """
        The RAID array LUN primary path is the path
        that is currently used to communicate with the
        LUN. This is the WWPN (World Wide Port Name) of the array FC port
        used as primary path.
        """
        return self._primary_array_port_wwn
    @primary_array_port_wwn.setter
    def primary_array_port_wwn(self, val):
        if val != None:
            self.validate('primary_array_port_wwn', val)
        self._primary_array_port_wwn = val
    
    _primary_lun_number = None
    @property
    def primary_lun_number(self):
        """
        LUN number on the primary path
        Range: [0..65535]
        """
        return self._primary_lun_number
    @primary_lun_number.setter
    def primary_lun_number(self, val):
        if val != None:
            self.validate('primary_lun_number', val)
        self._primary_lun_number = val
    
    _alternate_vseries_port_wwn = None
    @property
    def alternate_vseries_port_wwn(self):
        """
        This is the same as alternate-controller-port-wwn, presented for
        backwards compatibility.
        """
        return self._alternate_vseries_port_wwn
    @alternate_vseries_port_wwn.setter
    def alternate_vseries_port_wwn(self, val):
        if val != None:
            self.validate('alternate_vseries_port_wwn', val)
        self._alternate_vseries_port_wwn = val
    
    _primary_switch_port = None
    @property
    def primary_switch_port(self):
        """
        Switch port of the primary path. Present for
        switch attached configurations only.
        Range: [0..1024].
        """
        return self._primary_switch_port
    @primary_switch_port.setter
    def primary_switch_port(self, val):
        if val != None:
            self.validate('primary_switch_port', val)
        self._primary_switch_port = val
    
    _alternate_controller_port_wwn = None
    @property
    def alternate_controller_port_wwn(self):
        """
        The RAID array LUN alternate path is the path
        that can be used to communicate with the LUN,
        but not currently used.
        This is the WWN of the  FC
        port controller used as secondary path.
        """
        return self._alternate_controller_port_wwn
    @alternate_controller_port_wwn.setter
    def alternate_controller_port_wwn(self, val):
        if val != None:
            self.validate('alternate_controller_port_wwn', val)
        self._alternate_controller_port_wwn = val
    
    _primary_array_node_wwn = None
    @property
    def primary_array_node_wwn(self):
        """
        The RAID array LUN primary path is the path
        that is currently used to communicate with the
        LUN. This is the WWNN (World Wide Node Name) of the array FC port
        used as primary path.
        """
        return self._primary_array_node_wwn
    @primary_array_node_wwn.setter
    def primary_array_node_wwn(self, val):
        if val != None:
            self.validate('primary_array_node_wwn', val)
        self._primary_array_node_wwn = val
    
    _primary_array_switch_port_wwn = None
    @property
    def primary_array_switch_port_wwn(self):
        """
        The RAID array LUN primary path is the path
        that is currently used to communicate with the
        LUN. This is the WWN of the switch FC port
        connected to the array FC port used as primary
        path. This field is present in switch attached
        configrations only.
        """
        return self._primary_array_switch_port_wwn
    @primary_array_switch_port_wwn.setter
    def primary_array_switch_port_wwn(self, val):
        if val != None:
            self.validate('primary_array_switch_port_wwn', val)
        self._primary_array_switch_port_wwn = val
    
    _alternate_array_port_wwn = None
    @property
    def alternate_array_port_wwn(self):
        """
        The RAID array LUN alternate path is the path
        that can be used to communicate with the LUN,
        but not currently used.
        This is the WWPN (World Wide Port Name) of the array FC port used as
        the secondary path.
        """
        return self._alternate_array_port_wwn
    @alternate_array_port_wwn.setter
    def alternate_array_port_wwn(self, val):
        if val != None:
            self.validate('alternate_array_port_wwn', val)
        self._alternate_array_port_wwn = val
    
    _primary_vseries_port_wwn = None
    @property
    def primary_vseries_port_wwn(self):
        """
        This is the same as primary-controller-port-wwn, presented for
        backwards compatibility.
        """
        return self._primary_vseries_port_wwn
    @primary_vseries_port_wwn.setter
    def primary_vseries_port_wwn(self, val):
        if val != None:
            self.validate('primary_vseries_port_wwn', val)
        self._primary_vseries_port_wwn = val
    
    _alternate_switch_port = None
    @property
    def alternate_switch_port(self):
        """
        Switch port of the alternate path. Present for
        switch attached configurations only.
        Range: [0..1024].
        """
        return self._alternate_switch_port
    @alternate_switch_port.setter
    def alternate_switch_port(self, val):
        if val != None:
            self.validate('alternate_switch_port', val)
        self._alternate_switch_port = val
    
    _primary_controller_port_wwn = None
    @property
    def primary_controller_port_wwn(self):
        """
        The RAID array LUN primary path is the path
        that is currently used to communicate with the
        LUN. This is the WWN of the
        FC port controller used as primary path.
        """
        return self._primary_controller_port_wwn
    @primary_controller_port_wwn.setter
    def primary_controller_port_wwn(self, val):
        if val != None:
            self.validate('primary_controller_port_wwn', val)
        self._primary_controller_port_wwn = val
    
    _alternate_lun_number = None
    @property
    def alternate_lun_number(self):
        """
        LUN number on the alternate path
        Range: [0..65535]
        """
        return self._alternate_lun_number
    @alternate_lun_number.setter
    def alternate_lun_number(self, val):
        if val != None:
            self.validate('alternate_lun_number', val)
        self._alternate_lun_number = val
    
    @staticmethod
    def get_api_name():
          return "v-series-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'alternate-array-node-wwn',
            'product-id',
            'alternate-switch-name',
            'primary-switch-name',
            'alternate-array-switch-port-wwn',
            'primary-array-port-wwn',
            'primary-lun-number',
            'alternate-vseries-port-wwn',
            'primary-switch-port',
            'alternate-controller-port-wwn',
            'primary-array-node-wwn',
            'primary-array-switch-port-wwn',
            'alternate-array-port-wwn',
            'primary-vseries-port-wwn',
            'alternate-switch-port',
            'primary-controller-port-wwn',
            'alternate-lun-number',
        ]
    
    def describe_properties(self):
        return {
            'alternate_array_node_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'product_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'alternate_switch_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'primary_switch_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alternate_array_switch_port_wwn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'primary_array_port_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'primary_lun_number': { 'class': int, 'is_list': False, 'required': 'required' },
            'alternate_vseries_port_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'primary_switch_port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'alternate_controller_port_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'primary_array_node_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'primary_array_switch_port_wwn': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'alternate_array_port_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'primary_vseries_port_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'alternate_switch_port': { 'class': int, 'is_list': False, 'required': 'optional' },
            'primary_controller_port_wwn': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'alternate_lun_number': { 'class': int, 'is_list': False, 'required': 'required' },
        }
