from netapp.netapp_object import NetAppObject

class AlternateControlPathInfo(NetAppObject):
    """
    Available information on the alternate control path (ACP)
    to the shelf.
    """
    
    _controller_acp_ethernet_port = None
    @property
    def controller_acp_ethernet_port(self):
        """
        This fields presents the ACP's ethernet port on the storage
        controller. Example: e0a, e4d.
        """
        return self._controller_acp_ethernet_port
    @controller_acp_ethernet_port.setter
    def controller_acp_ethernet_port(self, val):
        if val != None:
            self.validate('controller_acp_ethernet_port', val)
        self._controller_acp_ethernet_port = val
    
    _module_mac_address = None
    @property
    def module_mac_address(self):
        """
        MAC address that is used by this module's ACPP. This field
        will not be present if the MAC address is unknown or not
        available, or if an ACP element is not installed.
        """
        return self._module_mac_address
    @module_mac_address.setter
    def module_mac_address(self, val):
        if val != None:
            self.validate('module_mac_address', val)
        self._module_mac_address = val
    
    _is_controller_acp_active = None
    @property
    def is_controller_acp_active(self):
        """
        Indicates whether the ACP function is active on the
        storage controller. Inactive ACP unually means there is
        configuration or connection error that needs to be
        resolved.
        """
        return self._is_controller_acp_active
    @is_controller_acp_active.setter
    def is_controller_acp_active(self, val):
        if val != None:
            self.validate('is_controller_acp_active', val)
        self._is_controller_acp_active = val
    
    _controller_acp_domain = None
    @property
    def controller_acp_domain(self):
        """
        This fields presents the ACP's domain on the storage
        controller. Example: 255.255.255.0
        """
        return self._controller_acp_domain
    @controller_acp_domain.setter
    def controller_acp_domain(self, val):
        if val != None:
            self.validate('controller_acp_domain', val)
        self._controller_acp_domain = val
    
    _is_acp_element_error = None
    @property
    def is_acp_element_error(self):
        """
        Indicates if there has been a failure in the ACP block.
        Will not be present if an ACP element is not installed.
        """
        return self._is_acp_element_error
    @is_acp_element_error.setter
    def is_acp_element_error(self, val):
        if val != None:
            self.validate('is_acp_element_error', val)
        self._is_acp_element_error = val
    
    _controller_acp_netmask = None
    @property
    def controller_acp_netmask(self):
        """
        This fields presents the ACP's netmask on the storage
        controller. Example: 172.168.4.1
        """
        return self._controller_acp_netmask
    @controller_acp_netmask.setter
    def controller_acp_netmask(self, val):
        if val != None:
            self.validate('controller_acp_netmask', val)
        self._controller_acp_netmask = val
    
    _is_acp_element_not_installed = None
    @property
    def is_acp_element_not_installed(self):
        """
        Indicates if ACP element has been installed. Will
        be present only if the element is not installed, in
        which case no further information will be provided.
        """
        return self._is_acp_element_not_installed
    @is_acp_element_not_installed.setter
    def is_acp_element_not_installed(self, val):
        if val != None:
            self.validate('is_acp_element_not_installed', val)
        self._is_acp_element_not_installed = val
    
    _module_status_time = None
    @property
    def module_status_time(self):
        """
        Time of last contact with the ACP controller. This
        is only valid if the value of module-status field is
        inactive_not_responding.
        """
        return self._module_status_time
    @module_status_time.setter
    def module_status_time(self, val):
        if val != None:
            self.validate('module_status_time', val)
        self._module_status_time = val
    
    _controller_acp_ip_address = None
    @property
    def controller_acp_ip_address(self):
        """
        This fields presents the ACP's IP address on the storage
        controller. Example: 172.168.4.4
        """
        return self._controller_acp_ip_address
    @controller_acp_ip_address.setter
    def controller_acp_ip_address(self, val):
        if val != None:
            self.validate('controller_acp_ip_address', val)
        self._controller_acp_ip_address = val
    
    _module_reset_count = None
    @property
    def module_reset_count(self):
        """
        Number of times the corresponding shelf I/O module has
        been reset using this ACPP.
        This field will not be present if it is unknown or
        not available, or if an ACP element is not installed.
        """
        return self._module_reset_count
    @module_reset_count.setter
    def module_reset_count(self, val):
        if val != None:
            self.validate('module_reset_count', val)
        self._module_reset_count = val
    
    _module_ip_address = None
    @property
    def module_ip_address(self):
        """
        IP address that is used by this ACP shelf module.
        This field will not be present if the IP address
        is unknown or not available, or if an ACP element
        is not installed.
        """
        return self._module_ip_address
    @module_ip_address.setter
    def module_ip_address(self, val):
        if val != None:
            self.validate('module_ip_address', val)
        self._module_ip_address = val
    
    _module_name = None
    @property
    def module_name(self):
        """
        Shelf module for this ACPP.
        Possible Values: "A", "B"
        This field will not be present if it is unknown or
        not available, or if an ACP element is not installed.
        """
        return self._module_name
    @module_name.setter
    def module_name(self, val):
        if val != None:
            self.validate('module_name', val)
        self._module_name = val
    
    _acp_element_no = None
    @property
    def acp_element_no(self):
        """
        ACP element number
        """
        return self._acp_element_no
    @acp_element_no.setter
    def acp_element_no(self, val):
        if val != None:
            self.validate('acp_element_no', val)
        self._acp_element_no = val
    
    _is_controller_acp_enabled = None
    @property
    def is_controller_acp_enabled(self):
        """
        Indicates if ACP functionality is enabled in the storage
        controller. If the ACP funtion is not enalbed the
        following fields will not be presented.
        """
        return self._is_controller_acp_enabled
    @is_controller_acp_enabled.setter
    def is_controller_acp_enabled(self, val):
        if val != None:
            self.validate('is_controller_acp_enabled', val)
        self._is_controller_acp_enabled = val
    
    _module_firmware_revision = None
    @property
    def module_firmware_revision(self):
        """
        Firmware version of the ACP controller. This field will
        not be present if the value is unknown or not available,
        or if an ACP element is not installed.
        """
        return self._module_firmware_revision
    @module_firmware_revision.setter
    def module_firmware_revision(self, val):
        if val != None:
            self.validate('module_firmware_revision', val)
        self._module_firmware_revision = val
    
    _module_status = None
    @property
    def module_status(self):
        """
        ACP status of this shelf module.
        This field will not be present if it is unknown or
        not available, or if an ACP element is not installed.
        Possible values:
        "active",
        "inactive_not_ready",
        "inactive_waiting_for_inband_info",
        "inactive_no_inband_connectivity",
        "inactive_not_responding",
        "inactive_updating_firmware",
        "inactive_initializing",
        "inactive_unknown".
        """
        return self._module_status
    @module_status.setter
    def module_status(self, val):
        if val != None:
            self.validate('module_status', val)
        self._module_status = val
    
    _controller_acp_connection_status = None
    @property
    def controller_acp_connection_status(self):
        """
        Storage controller's ACP connection status.
        Possible values:
        "no_connectivity",
        "partial_connectivity",
        "full_connectivity",
        "additional_connectivity",
        "unknown",
        "not_available",
        "not_applicable".
        """
        return self._controller_acp_connection_status
    @controller_acp_connection_status.setter
    def controller_acp_connection_status(self, val):
        if val != None:
            self.validate('controller_acp_connection_status', val)
        self._controller_acp_connection_status = val
    
    @staticmethod
    def get_api_name():
          return "alternate-control-path-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'controller-acp-ethernet-port',
            'module-mac-address',
            'is-controller-acp-active',
            'controller-acp-domain',
            'is-acp-element-error',
            'controller-acp-netmask',
            'is-acp-element-not-installed',
            'module-status-time',
            'controller-acp-ip-address',
            'module-reset-count',
            'module-ip-address',
            'module-name',
            'acp-element-no',
            'is-controller-acp-enabled',
            'module-firmware-revision',
            'module-status',
            'controller-acp-connection-status',
        ]
    
    def describe_properties(self):
        return {
            'controller_acp_ethernet_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'module_mac_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_controller_acp_active': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'controller_acp_domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_acp_element_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'controller_acp_netmask': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_acp_element_not_installed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'module_status_time': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'controller_acp_ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'module_reset_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'module_ip_address': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'module_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'acp_element_no': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_controller_acp_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'module_firmware_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'module_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'controller_acp_connection_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
