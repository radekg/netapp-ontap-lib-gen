from netapp.netapp_object import NetAppObject

class ServiceProcessorImageInfo(NetAppObject):
    """
    Service processor firmware information
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
    
    _node = None
    @property
    def node(self):
        """
        Node on which the device is located
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _status = None
    @property
    def status(self):
        """
        Status of this firmware image
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "installed"      - Firmware installed and in
        normal state,
        <li> "corrupt"        - Firmware is corrupt,
        <li> "updating"       - Firmware is undergoing a manual
        update,
        <li> "auto_updating"  - Firmware is undergoing an
        automatic update,
        <li> "none"           - Firmware status not known
        </ul>
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _running_version = None
    @property
    def running_version(self):
        """
        Firmware version in this image
        Attributes: non-creatable, non-modifiable
        """
        return self._running_version
    @running_version.setter
    def running_version(self, val):
        if val != None:
            self.validate('running_version', val)
        self._running_version = val
    
    _is_current = None
    @property
    def is_current(self):
        """
        Is device currently booted from this image
        Attributes: non-creatable, non-modifiable
        """
        return self._is_current
    @is_current.setter
    def is_current(self, val):
        if val != None:
            self.validate('is_current', val)
        self._is_current = val
    
    _last_update_status = None
    @property
    def last_update_status(self):
        """
        Did last firmware install on the device pass or fail
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "failed"    - Operation failed,
        <li> "passed"    - Operation was successful
        </ul>
        """
        return self._last_update_status
    @last_update_status.setter
    def last_update_status(self, val):
        if val != None:
            self.validate('last_update_status', val)
        self._last_update_status = val
    
    _type = None
    @property
    def type(self):
        """
        Type of device
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "rlm"  - Remote LAN Module,
        <li> "sp"   - Service Processor,
        <li> "none" - None
        </ul>
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _firmware_image = None
    @property
    def firmware_image(self):
        """
        Is this image primary or backup firmware for the device
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "primary"   - Firmware which the device boots into
        by default,
        <li> "backup"    - Firmware which the device boots into
        if primary fails
        </ul>
        """
        return self._firmware_image
    @firmware_image.setter
    def firmware_image(self, val):
        if val != None:
            self.validate('firmware_image', val)
        self._firmware_image = val
    
    _is_autoupdate_enabled = None
    @property
    def is_autoupdate_enabled(self):
        """
        Is firmware autoupdate enabled on the device
        Attributes: non-creatable, modifiable
        """
        return self._is_autoupdate_enabled
    @is_autoupdate_enabled.setter
    def is_autoupdate_enabled(self, val):
        if val != None:
            self.validate('is_autoupdate_enabled', val)
        self._is_autoupdate_enabled = val
    
    @staticmethod
    def get_api_name():
          return "service-processor-image-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'status',
            'running-version',
            'is-current',
            'last-update-status',
            'type',
            'firmware-image',
            'is-autoupdate-enabled',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'running_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_current': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'last_update_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'firmware_image': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_autoupdate_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
