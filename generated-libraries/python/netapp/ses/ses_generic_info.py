from netapp.netapp_object import NetAppObject

class SesGenericInfo(NetAppObject):
    """
    Generic SES (SCSI enclosure services) information.
    """
    
    _ses_config_access = None
    @property
    def ses_config_access(self):
        """
        The method shelf configuration was obtained.
        Possible values:
        "via_embedded_ses",
        "via_scsi_from_shelf",
        "via_loop_from_shelf",
        "remote_access_via_controller",
        "not_available".
        """
        return self._ses_config_access
    @ses_config_access.setter
    def ses_config_access(self, val):
        if val != None:
            self.validate('ses_config_access', val)
        self._ses_config_access = val
    
    _ses_chassis_part_number = None
    @property
    def ses_chassis_part_number(self):
        """
        Chassis part number. The field will not be present
        if the part number is unavailable or not implemented.
        """
        return self._ses_chassis_part_number
    @ses_chassis_part_number.setter
    def ses_chassis_part_number(self, val):
        if val != None:
            self.validate('ses_chassis_part_number', val)
        self._ses_chassis_part_number = val
    
    _ses_vendor_id = None
    @property
    def ses_vendor_id(self):
        """
        Enclosure vendor identifier.
        """
        return self._ses_vendor_id
    @ses_vendor_id.setter
    def ses_vendor_id(self, val):
        if val != None:
            self.validate('ses_vendor_id', val)
        self._ses_vendor_id = val
    
    _ses_midplane_serial_number = None
    @property
    def ses_midplane_serial_number(self):
        """
        Enclosure midplane serial number. The field will not be
        present if the midplane is not present.
        """
        return self._ses_midplane_serial_number
    @ses_midplane_serial_number.setter
    def ses_midplane_serial_number(self, val):
        if val != None:
            self.validate('ses_midplane_serial_number', val)
        self._ses_midplane_serial_number = val
    
    _ses_midplane_part_number = None
    @property
    def ses_midplane_part_number(self):
        """
        Enclosure midplane part number. The field will not be present
        if the midplane is not present.
        """
        return self._ses_midplane_part_number
    @ses_midplane_part_number.setter
    def ses_midplane_part_number(self, val):
        if val != None:
            self.validate('ses_midplane_part_number', val)
        self._ses_midplane_part_number = val
    
    _ses_logical_id = None
    @property
    def ses_logical_id(self):
        """
        Enclosure logical identifier.
        """
        return self._ses_logical_id
    @ses_logical_id.setter
    def ses_logical_id(self, val):
        if val != None:
            self.validate('ses_logical_id', val)
        self._ses_logical_id = val
    
    _ses_contact_state = None
    @property
    def ses_contact_state(self):
        """
        Enclosure contact state.
        Possible values are:
        "active",
        "initializing",
        "transitioning",
        "inactive",
        "reconfiguring",
        "non_existent".
        """
        return self._ses_contact_state
    @ses_contact_state.setter
    def ses_contact_state(self, val):
        if val != None:
            self.validate('ses_contact_state', val)
        self._ses_contact_state = val
    
    _ses_config_access_shelf_id = None
    @property
    def ses_config_access_shelf_id(self):
        """
        If ses-config-access is either
        "via_scsi_from_shelf" or "via_loop_from_shelf"
        then this would be the shelf id of the device the
        configuration was obtained from.
        """
        return self._ses_config_access_shelf_id
    @ses_config_access_shelf_id.setter
    def ses_config_access_shelf_id(self, val):
        if val != None:
            self.validate('ses_config_access_shelf_id', val)
        self._ses_config_access_shelf_id = val
    
    _ses_product_revision = None
    @property
    def ses_product_revision(self):
        """
        Enclosure product revision.
        """
        return self._ses_product_revision
    @ses_product_revision.setter
    def ses_product_revision(self, val):
        if val != None:
            self.validate('ses_product_revision', val)
        self._ses_product_revision = val
    
    _ses_product_id = None
    @property
    def ses_product_id(self):
        """
        Enclosure product identifier. Not available on all shelf
        types.
        """
        return self._ses_product_id
    @ses_product_id.setter
    def ses_product_id(self, val):
        if val != None:
            self.validate('ses_product_id', val)
        self._ses_product_id = val
    
    _ses_config_access_source_id = None
    @property
    def ses_config_access_source_id(self):
        """
        If ses-config-access is either
        "via_scsi_from_shelf" or "via_loop_from_shelf"
        then this would be the SCSI or loop id of the device
        that the configuration was obtained from.
        """
        return self._ses_config_access_source_id
    @ses_config_access_source_id.setter
    def ses_config_access_source_id(self, val):
        if val != None:
            self.validate('ses_config_access_source_id', val)
        self._ses_config_access_source_id = val
    
    _ses_config_access_controller_name = None
    @property
    def ses_config_access_controller_name(self):
        """
        If the value of ses-config-access field is
        "remote_access_via_controller" then this field will return
        the name of storage controller the configuration was
        obtained from. This field will not be present if storage
        controller name is not available or if the value of
        ses-config-access field is not "remote_access_via_controller".
        """
        return self._ses_config_access_controller_name
    @ses_config_access_controller_name.setter
    def ses_config_access_controller_name(self, val):
        if val != None:
            self.validate('ses_config_access_controller_name', val)
        self._ses_config_access_controller_name = val
    
    @staticmethod
    def get_api_name():
          return "ses-generic-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ses-config-access',
            'ses-chassis-part-number',
            'ses-vendor-id',
            'ses-midplane-serial-number',
            'ses-midplane-part-number',
            'ses-logical-id',
            'ses-contact-state',
            'ses-config-access-shelf-id',
            'ses-product-revision',
            'ses-product-id',
            'ses-config-access-source-id',
            'ses-config-access-controller-name',
        ]
    
    def describe_properties(self):
        return {
            'ses_config_access': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ses_chassis_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ses_vendor_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ses_midplane_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ses_midplane_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ses_logical_id': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ses_contact_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ses_config_access_shelf_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ses_product_revision': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'ses_product_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ses_config_access_source_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'ses_config_access_controller_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
