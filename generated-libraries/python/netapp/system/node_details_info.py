from netapp.system.vmhost_info import VmhostInfo
from netapp.system.vm_system_disks import VmSystemDisks
from netapp.netapp_object import NetAppObject

class NodeDetailsInfo(NetAppObject):
    """
    Contains information about a specific node
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
    
    _node_location = None
    @property
    def node_location(self):
        """
        The physical location of the node.
        For example, Sunnyvale.
        Attributes: non-creatable, modifiable
        """
        return self._node_location
    @node_location.setter
    def node_location(self, val):
        if val != None:
            self.validate('node_location', val)
        self._node_location = val
    
    _is_node_healthy = None
    @property
    def is_node_healthy(self):
        """
        This parameter is used to determine health of a node in a
        cluster. A boolean value of true means the node is
        healthy.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_node_healthy
    @is_node_healthy.setter
    def is_node_healthy(self, val):
        if val != None:
            self.validate('is_node_healthy', val)
        self._is_node_healthy = val
    
    _maximum_number_of_volumes = None
    @property
    def maximum_number_of_volumes(self):
        """
        The maximum number of flexible volumes supported on this
        node. This does not include the number of volumes which
        can be supported when this node does a takeover of its
        partner node in a High Availability configuration.
        Attributes: non-creatable, non-modifiable
        """
        return self._maximum_number_of_volumes
    @maximum_number_of_volumes.setter
    def maximum_number_of_volumes(self, val):
        if val != None:
            self.validate('maximum_number_of_volumes', val)
        self._maximum_number_of_volumes = val
    
    _maximum_volume_size = None
    @property
    def maximum_volume_size(self):
        """
        The maximum supported volume size in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._maximum_volume_size
    @maximum_volume_size.setter
    def maximum_volume_size(self, val):
        if val != None:
            self.validate('maximum_volume_size', val)
        self._maximum_volume_size = val
    
    _node_nvram_id = None
    @property
    def node_nvram_id(self):
        """
        Vendor specific NVRAM ID of the node.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_nvram_id
    @node_nvram_id.setter
    def node_nvram_id(self, val):
        if val != None:
            self.validate('node_nvram_id', val)
        self._node_nvram_id = val
    
    _node_vendor = None
    @property
    def node_vendor(self):
        """
        The hardware vendor of the node.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_vendor
    @node_vendor.setter
    def node_vendor(self, val):
        if val != None:
            self.validate('node_vendor', val)
        self._node_vendor = val
    
    _is_node_cluster_eligible = None
    @property
    def is_node_cluster_eligible(self):
        """
        This parameter states nodes that are eligible to
        participate in the cluster. A boolean value of true means
        the node is eligible.
        Attributes: non-creatable, modifiable
        """
        return self._is_node_cluster_eligible
    @is_node_cluster_eligible.setter
    def is_node_cluster_eligible(self, val):
        if val != None:
            self.validate('is_node_cluster_eligible', val)
        self._is_node_cluster_eligible = val
    
    _node_owner = None
    @property
    def node_owner(self):
        """
        The owner of the node.
        Attributes: non-creatable, modifiable
        """
        return self._node_owner
    @node_owner.setter
    def node_owner(self, val):
        if val != None:
            self.validate('node_owner', val)
        self._node_owner = val
    
    _cpu_busytime = None
    @property
    def cpu_busytime(self):
        """
        The time (in hundredths of a second) that the CPU has
        been doing useful work since the last boot.
        Attributes: non-creatable, non-modifiable
        """
        return self._cpu_busytime
    @cpu_busytime.setter
    def cpu_busytime(self, val):
        if val != None:
            self.validate('cpu_busytime', val)
        self._cpu_busytime = val
    
    _is_epsilon_node = None
    @property
    def is_epsilon_node(self):
        """
        You can designate a node as epsilon to add weight to its
        voting in a cluster with an even number of nodes. In a
        cluster, only one node can be designated as epsilon at
        any given time. A boolean value of true means the node is
        epsilon.
        Attributes: non-creatable, modifiable
        """
        return self._is_epsilon_node
    @is_epsilon_node.setter
    def is_epsilon_node(self, val):
        if val != None:
            self.validate('is_epsilon_node', val)
        self._is_epsilon_node = val
    
    _node_asset_tag = None
    @property
    def node_asset_tag(self):
        """
        The asset tag of the node. This is defined by the vendor.
        Currently, a string of numbers.
        Attributes: non-creatable, modifiable
        """
        return self._node_asset_tag
    @node_asset_tag.setter
    def node_asset_tag(self, val):
        if val != None:
            self.validate('node_asset_tag', val)
        self._node_asset_tag = val
    
    _vmhost_info = None
    @property
    def vmhost_info(self):
        """
        Contains virtual machine host information
        """
        return self._vmhost_info
    @vmhost_info.setter
    def vmhost_info(self, val):
        if val != None:
            self.validate('vmhost_info', val)
        self._vmhost_info = val
    
    _node_uptime = None
    @property
    def node_uptime(self):
        """
        Total time, in seconds, that the node has been up.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_uptime
    @node_uptime.setter
    def node_uptime(self, val):
        if val != None:
            self.validate('node_uptime', val)
        self._node_uptime = val
    
    _env_failed_fan_message = None
    @property
    def env_failed_fan_message(self):
        """
        Text message describing the current condition of chassis
        fans.  This is useful only if env-failed-fan-count is not
        zero.
        Attributes: non-creatable, non-modifiable
        """
        return self._env_failed_fan_message
    @env_failed_fan_message.setter
    def env_failed_fan_message(self, val):
        if val != None:
            self.validate('env_failed_fan_message', val)
        self._env_failed_fan_message = val
    
    _maximum_aggregate_size = None
    @property
    def maximum_aggregate_size(self):
        """
        The maximum supported aggregate size in bytes.
        Attributes: non-creatable, non-modifiable
        """
        return self._maximum_aggregate_size
    @maximum_aggregate_size.setter
    def maximum_aggregate_size(self, val):
        if val != None:
            self.validate('maximum_aggregate_size', val)
        self._maximum_aggregate_size = val
    
    _node = None
    @property
    def node(self):
        """
        The textual name of a node.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _vm_system_disks = None
    @property
    def vm_system_disks(self):
        """
        Contains virtual machine system disk backing info
        """
        return self._vm_system_disks
    @vm_system_disks.setter
    def vm_system_disks(self, val):
        if val != None:
            self.validate('vm_system_disks', val)
        self._vm_system_disks = val
    
    _node_uuid = None
    @property
    def node_uuid(self):
        """
        The univerally unique identifier for the node.
        It is a 36-character string composed of 32 hexadecimal
        characters.
        For example, '542366ea-a024-11dd-9caa-7302e474c5ae'.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_uuid
    @node_uuid.setter
    def node_uuid(self, val):
        if val != None:
            self.validate('node_uuid', val)
        self._node_uuid = val
    
    _node_model = None
    @property
    def node_model(self):
        """
        The model of the node. For example, FAS3070.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_model
    @node_model.setter
    def node_model(self, val):
        if val != None:
            self.validate('node_model', val)
        self._node_model = val
    
    _env_over_temperature = None
    @property
    def env_over_temperature(self):
        """
        An indication of whether the hardware is currently
        operating outside of its recommended temperature range.
        The hardware will shutdown if the temperature exceeds
        critical thresholds.
        Attributes: non-creatable, non-modifiable
        """
        return self._env_over_temperature
    @env_over_temperature.setter
    def env_over_temperature(self, val):
        if val != None:
            self.validate('env_over_temperature', val)
        self._env_over_temperature = val
    
    _nvram_battery_status = None
    @property
    def nvram_battery_status(self):
        """
        Status of the NVRAM battery. The possible values that
        could be returned:
        <ul>
        <li> 'battery_ok'
        <li> 'battery_partially_discharged'
        <li> 'battery_fully_discharged '
        <li> 'battery_not_present'
        <li> 'battery_near_end_of_life'
        <li> 'battery_at_end_of_life'
        <li> 'battery_unknown'
        <li> 'battery_over_charged'
        <li> 'battery_fully_charged'
        </ul>
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "battery_ok"                    ,
        <li> "battery_partially_discharged"  ,
        <li> "battery_fully_discharged"      ,
        <li> "battery_not_present"           ,
        <li> "battery_near_end_of_life"      ,
        <li> "battery_at_end_of_life"        ,
        <li> "battery_unknown"               ,
        <li> "battery_over_charged"          ,
        <li> "battery_fully_charged"
        </ul>
        """
        return self._nvram_battery_status
    @nvram_battery_status.setter
    def nvram_battery_status(self, val):
        if val != None:
            self.validate('nvram_battery_status', val)
        self._nvram_battery_status = val
    
    _env_failed_power_supply_count = None
    @property
    def env_failed_power_supply_count(self):
        """
        Number of failed power supply units.
        Attributes: non-creatable, non-modifiable
        """
        return self._env_failed_power_supply_count
    @env_failed_power_supply_count.setter
    def env_failed_power_supply_count(self, val):
        if val != None:
            self.validate('env_failed_power_supply_count', val)
        self._env_failed_power_supply_count = val
    
    _env_failed_power_supply_message = None
    @property
    def env_failed_power_supply_message(self):
        """
        Text message describing the state of any power supplies
        which are currently degraded. This is useful only if
        env-failed-power-supply-count is not zero.
        Attributes: non-creatable, non-modifiable
        """
        return self._env_failed_power_supply_message
    @env_failed_power_supply_message.setter
    def env_failed_power_supply_message(self, val):
        if val != None:
            self.validate('env_failed_power_supply_message', val)
        self._env_failed_power_supply_message = val
    
    _env_failed_fan_count = None
    @property
    def env_failed_fan_count(self):
        """
        Count of the number of chassis fans which are not
        operating within the recommended RPM range.
        Attributes: non-creatable, non-modifiable
        """
        return self._env_failed_fan_count
    @env_failed_fan_count.setter
    def env_failed_fan_count(self, val):
        if val != None:
            self.validate('env_failed_fan_count', val)
        self._env_failed_fan_count = val
    
    _product_version = None
    @property
    def product_version(self):
        """
        Product Version
        Attributes: non-creatable, non-modifiable
        """
        return self._product_version
    @product_version.setter
    def product_version(self, val):
        if val != None:
            self.validate('product_version', val)
        self._product_version = val
    
    _cpu_firmware_release = None
    @property
    def cpu_firmware_release(self):
        """
        Firmware release number. Defined by the CPU
        manufacturer.
        Attributes: non-creatable, non-modifiable
        """
        return self._cpu_firmware_release
    @cpu_firmware_release.setter
    def cpu_firmware_release(self, val):
        if val != None:
            self.validate('cpu_firmware_release', val)
        self._cpu_firmware_release = val
    
    _node_serial_number = None
    @property
    def node_serial_number(self):
        """
        The serial number of the node. This is defined by the
        vendor. Currently, a string of numbers.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_serial_number
    @node_serial_number.setter
    def node_serial_number(self, val):
        if val != None:
            self.validate('node_serial_number', val)
        self._node_serial_number = val
    
    _node_system_id = None
    @property
    def node_system_id(self):
        """
        The system Id of the node. This is defined by the vendor.
        Generally, it is a string of numbers.
        Attributes: non-creatable, non-modifiable
        """
        return self._node_system_id
    @node_system_id.setter
    def node_system_id(self, val):
        if val != None:
            self.validate('node_system_id', val)
        self._node_system_id = val
    
    @staticmethod
    def get_api_name():
          return "node-details-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node-location',
            'is-node-healthy',
            'maximum-number-of-volumes',
            'maximum-volume-size',
            'node-nvram-id',
            'node-vendor',
            'is-node-cluster-eligible',
            'node-owner',
            'cpu-busytime',
            'is-epsilon-node',
            'node-asset-tag',
            'vmhost-info',
            'node-uptime',
            'env-failed-fan-message',
            'maximum-aggregate-size',
            'node',
            'vm-system-disks',
            'node-uuid',
            'node-model',
            'env-over-temperature',
            'nvram-battery-status',
            'env-failed-power-supply-count',
            'env-failed-power-supply-message',
            'env-failed-fan-count',
            'product-version',
            'cpu-firmware-release',
            'node-serial-number',
            'node-system-id',
        ]
    
    def describe_properties(self):
        return {
            'node_location': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_node_healthy': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'maximum_number_of_volumes': { 'class': int, 'is_list': False, 'required': 'optional' },
            'maximum_volume_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'node_nvram_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'node_vendor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_node_cluster_eligible': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'node_owner': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cpu_busytime': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_epsilon_node': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'node_asset_tag': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vmhost_info': { 'class': VmhostInfo, 'is_list': False, 'required': 'optional' },
            'node_uptime': { 'class': int, 'is_list': False, 'required': 'optional' },
            'env_failed_fan_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'maximum_aggregate_size': { 'class': int, 'is_list': False, 'required': 'optional' },
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vm_system_disks': { 'class': VmSystemDisks, 'is_list': False, 'required': 'optional' },
            'node_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_model': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'env_over_temperature': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'nvram_battery_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'env_failed_power_supply_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'env_failed_power_supply_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'env_failed_fan_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'product_version': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cpu_firmware_release': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'node_system_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
