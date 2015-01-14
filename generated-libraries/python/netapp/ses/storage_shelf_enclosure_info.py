from netapp.netapp_object import NetAppObject

class StorageShelfEnclosureInfo(NetAppObject):
    """
    A list of enclosure details.
    """
    
    _enclosure_volt_sensors_undervolt_failed_list = None
    @property
    def enclosure_volt_sensors_undervolt_failed_list(self):
        """
        The list of voltage sensors reporting
        undervoltage failure in this enclosure.
        This should be a subset of enclosure-volt-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_undervolt_failed_list
    @enclosure_volt_sensors_undervolt_failed_list.setter
    def enclosure_volt_sensors_undervolt_failed_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_undervolt_failed_list', val)
        self._enclosure_volt_sensors_undervolt_failed_list = val
    
    _enclosure_product_revision = None
    @property
    def enclosure_product_revision(self):
        """
        The product revision number of this enclosure.
        """
        return self._enclosure_product_revision
    @enclosure_product_revision.setter
    def enclosure_product_revision(self, val):
        if val != None:
            self.validate('enclosure_product_revision', val)
        self._enclosure_product_revision = val
    
    _enclosure_electronics_failed_list = None
    @property
    def enclosure_electronics_failed_list(self):
        """
        The list of failed electronic modules found
        in this enclosure. This should be a subset
        of enclosure-electronics-list.
        It is a comma separated list.
        """
        return self._enclosure_electronics_failed_list
    @enclosure_electronics_failed_list.setter
    def enclosure_electronics_failed_list(self, val):
        if val != None:
            self.validate('enclosure_electronics_failed_list', val)
        self._enclosure_electronics_failed_list = val
    
    _enclosure_electronics_list = None
    @property
    def enclosure_electronics_list(self):
        """
        The list of enclosure services electronics
        modules that are possible for this enclosure.
        The R200 FC-AT module can be reported as the
        second module and that is normal.
        It is a comma separated list.
        """
        return self._enclosure_electronics_list
    @enclosure_electronics_list.setter
    def enclosure_electronics_list(self, val):
        if val != None:
            self.validate('enclosure_electronics_list', val)
        self._enclosure_electronics_list = val
    
    _enclosure_temp_sensors_undertemp_warn_threshold_list = None
    @property
    def enclosure_temp_sensors_undertemp_warn_threshold_list(self):
        """
        The list of undertemperature warning thresholds
        for all temperature sensors present in this
        enclosure. This should be a subset of
        enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensors_undertemp_warn_threshold_list
    @enclosure_temp_sensors_undertemp_warn_threshold_list.setter
    def enclosure_temp_sensors_undertemp_warn_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_undertemp_warn_threshold_list', val)
        self._enclosure_temp_sensors_undertemp_warn_threshold_list = val
    
    _enclosure_node_name = None
    @property
    def enclosure_node_name(self):
        """
        The node name to which this enclosure belongs.
        """
        return self._enclosure_node_name
    @enclosure_node_name.setter
    def enclosure_node_name(self, val):
        if val != None:
            self.validate('enclosure_node_name', val)
        self._enclosure_node_name = val
    
    _enclosure_connector_type_list = None
    @property
    def enclosure_connector_type_list(self):
        """
        The list of cable types for connectors present in this
        enclosure.  If no cable is attached, entry is shown as "N/A".
        It is a comma separated list.
        An example is: "copper, N/A, copper, N/A".
        """
        return self._enclosure_connector_type_list
    @enclosure_connector_type_list.setter
    def enclosure_connector_type_list(self, val):
        if val != None:
            self.validate('enclosure_connector_type_list', val)
        self._enclosure_connector_type_list = val
    
    _enclosure_connector_list = None
    @property
    def enclosure_connector_list(self):
        """
        The list of connectors present in this enclosure.
        It is a comma separated list.
        """
        return self._enclosure_connector_list
    @enclosure_connector_list.setter
    def enclosure_connector_list(self, val):
        if val != None:
            self.validate('enclosure_connector_list', val)
        self._enclosure_connector_list = val
    
    _enclosure_volt_sensors_undervolt_failed_threshold_list = None
    @property
    def enclosure_volt_sensors_undervolt_failed_threshold_list(self):
        """
        The list of undervoltage failure thresholds for
        all voltage sensors present in this enclosure.
        This should be a subset of enclosure-volt-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_undervolt_failed_threshold_list
    @enclosure_volt_sensors_undervolt_failed_threshold_list.setter
    def enclosure_volt_sensors_undervolt_failed_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_undervolt_failed_threshold_list', val)
        self._enclosure_volt_sensors_undervolt_failed_threshold_list = val
    
    _enclosure_temp_sensors_reading_list = None
    @property
    def enclosure_temp_sensors_reading_list(self):
        """
        The list of temperatures reported by all
        temperature sensors in this enclosure.
        This should be a subset of enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensors_reading_list
    @enclosure_temp_sensors_reading_list.setter
    def enclosure_temp_sensors_reading_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_reading_list', val)
        self._enclosure_temp_sensors_reading_list = val
    
    _enclosure_volt_sensors_undervolt_warn_threshold_list = None
    @property
    def enclosure_volt_sensors_undervolt_warn_threshold_list(self):
        """
        The list of undervoltage warning thresholds for all
        voltage sensors present in this enclosure.
        This should be a subset of enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_undervolt_warn_threshold_list
    @enclosure_volt_sensors_undervolt_warn_threshold_list.setter
    def enclosure_volt_sensors_undervolt_warn_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_undervolt_warn_threshold_list', val)
        self._enclosure_volt_sensors_undervolt_warn_threshold_list = val
    
    _enclosure_product_id = None
    @property
    def enclosure_product_id(self):
        """
        The product ID of this enclosure.
        An example is "DS4243".
        """
        return self._enclosure_product_id
    @enclosure_product_id.setter
    def enclosure_product_id(self, val):
        if val != None:
            self.validate('enclosure_product_id', val)
        self._enclosure_product_id = val
    
    _enclosure_power_supply_list = None
    @property
    def enclosure_power_supply_list(self):
        """
        The list of power supplies present in this enclosure.
        It is a comma separated list.
        For an enclosure with 4 power supplies, an
        example could be "1, 2, 3, 4".
        """
        return self._enclosure_power_supply_list
    @enclosure_power_supply_list.setter
    def enclosure_power_supply_list(self, val):
        if val != None:
            self.validate('enclosure_power_supply_list', val)
        self._enclosure_power_supply_list = val
    
    _enclosure_current_sensors_overcurrent_warn_threshold_list = None
    @property
    def enclosure_current_sensors_overcurrent_warn_threshold_list(self):
        """
        The list of overcurrent warning thresholds for
        all electric current sensors in this enclosure. This should
        be a subset of enclosure-current-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_current_sensors_overcurrent_warn_threshold_list
    @enclosure_current_sensors_overcurrent_warn_threshold_list.setter
    def enclosure_current_sensors_overcurrent_warn_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_current_sensors_overcurrent_warn_threshold_list', val)
        self._enclosure_current_sensors_overcurrent_warn_threshold_list = val
    
    _enclosure_temp_sensors_overtemp_failed_list = None
    @property
    def enclosure_temp_sensors_overtemp_failed_list(self):
        """
        The list of temperature sensors reporting
        overtemperature failure in this enclosure.
        This should be a subset of enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensors_overtemp_failed_list
    @enclosure_temp_sensors_overtemp_failed_list.setter
    def enclosure_temp_sensors_overtemp_failed_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_overtemp_failed_list', val)
        self._enclosure_temp_sensors_overtemp_failed_list = val
    
    _enclosure_vendor = None
    @property
    def enclosure_vendor(self):
        """
        The vendor name of this enclosure.
        An example is Xyratex.
        """
        return self._enclosure_vendor
    @enclosure_vendor.setter
    def enclosure_vendor(self, val):
        if val != None:
            self.validate('enclosure_vendor', val)
        self._enclosure_vendor = val
    
    _enclosure_shelf_addr = None
    @property
    def enclosure_shelf_addr(self):
        """
        The channel and shelf ID of this enclosure.
        Examples are "8a.1" and "switch:5.1".
        """
        return self._enclosure_shelf_addr
    @enclosure_shelf_addr.setter
    def enclosure_shelf_addr(self, val):
        if val != None:
            self.validate('enclosure_shelf_addr', val)
        self._enclosure_shelf_addr = val
    
    _enclosure_current_sensors_overcurrent_failed_list = None
    @property
    def enclosure_current_sensors_overcurrent_failed_list(self):
        """
        The list of current sensors present in this
        enclosure that are reporting overcurrent failure.
        This should be a subset of enclosure-current-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_current_sensors_overcurrent_failed_list
    @enclosure_current_sensors_overcurrent_failed_list.setter
    def enclosure_current_sensors_overcurrent_failed_list(self, val):
        if val != None:
            self.validate('enclosure_current_sensors_overcurrent_failed_list', val)
        self._enclosure_current_sensors_overcurrent_failed_list = val
    
    _enclosure_volt_sensors_max = None
    @property
    def enclosure_volt_sensors_max(self):
        """
        The maximum number of voltage sensors present in this
        enclosure.  A maximum of 12 voltage sensors are supported.
        """
        return self._enclosure_volt_sensors_max
    @enclosure_volt_sensors_max.setter
    def enclosure_volt_sensors_max(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_max', val)
        self._enclosure_volt_sensors_max = val
    
    _enclosure_volt_sensor_list = None
    @property
    def enclosure_volt_sensor_list(self):
        """
        The list of voltage sensors present in
        this enclosure.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensor_list
    @enclosure_volt_sensor_list.setter
    def enclosure_volt_sensor_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensor_list', val)
        self._enclosure_volt_sensor_list = val
    
    _enclosure_current_sensors_overcurrent_failed_threshold_list = None
    @property
    def enclosure_current_sensors_overcurrent_failed_threshold_list(self):
        """
        The list of overcurrent failure thresholds for
        all electric current sensors in this enclosure. This should
        be a subset of enclosure-current-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_current_sensors_overcurrent_failed_threshold_list
    @enclosure_current_sensors_overcurrent_failed_threshold_list.setter
    def enclosure_current_sensors_overcurrent_failed_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_current_sensors_overcurrent_failed_threshold_list', val)
        self._enclosure_current_sensors_overcurrent_failed_threshold_list = val
    
    _enclosure_connector_max = None
    @property
    def enclosure_connector_max(self):
        """
        The maximum number of connectors present in this
        enclosure.  A maximum of 4 connectors are supported.
        """
        return self._enclosure_connector_max
    @enclosure_connector_max.setter
    def enclosure_connector_max(self, val):
        if val != None:
            self.validate('enclosure_connector_max', val)
        self._enclosure_connector_max = val
    
    _enclosure_temp_sensors_overtemp_warn_threshold_list = None
    @property
    def enclosure_temp_sensors_overtemp_warn_threshold_list(self):
        """
        The list of overtemperature warning thresholds
        for all temperature sensors present in this
        enclosure. This should be a subset of
        enclosure-temp-sensor-list.
        """
        return self._enclosure_temp_sensors_overtemp_warn_threshold_list
    @enclosure_temp_sensors_overtemp_warn_threshold_list.setter
    def enclosure_temp_sensors_overtemp_warn_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_overtemp_warn_threshold_list', val)
        self._enclosure_temp_sensors_overtemp_warn_threshold_list = val
    
    _enclosure_current_sensors_overcurrent_warn_list = None
    @property
    def enclosure_current_sensors_overcurrent_warn_list(self):
        """
        The list of current sensors present in this
        enclosure that are reporting overcurrent warning.
        This should be a subset of enclosure-current-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_current_sensors_overcurrent_warn_list
    @enclosure_current_sensors_overcurrent_warn_list.setter
    def enclosure_current_sensors_overcurrent_warn_list(self, val):
        if val != None:
            self.validate('enclosure_current_sensors_overcurrent_warn_list', val)
        self._enclosure_current_sensors_overcurrent_warn_list = val
    
    _enclosure_logical_id = None
    @property
    def enclosure_logical_id(self):
        """
        The logical ID of this enclosure in WWN format.
        An example is "5:005:0cc102:000df1".
        """
        return self._enclosure_logical_id
    @enclosure_logical_id.setter
    def enclosure_logical_id(self, val):
        if val != None:
            self.validate('enclosure_logical_id', val)
        self._enclosure_logical_id = val
    
    _enclosure_temp_sensor_list = None
    @property
    def enclosure_temp_sensor_list(self):
        """
        The list of temperature sensors present in this enclosure.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensor_list
    @enclosure_temp_sensor_list.setter
    def enclosure_temp_sensor_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensor_list', val)
        self._enclosure_temp_sensor_list = val
    
    _enclosure_volt_sensors_overvolt_warn_list = None
    @property
    def enclosure_volt_sensors_overvolt_warn_list(self):
        """
        The list of voltage sensors reporting
        overvoltage warning in this enclosure.
        This should be a subset of enclosure-volt-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_overvolt_warn_list
    @enclosure_volt_sensors_overvolt_warn_list.setter
    def enclosure_volt_sensors_overvolt_warn_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_overvolt_warn_list', val)
        self._enclosure_volt_sensors_overvolt_warn_list = val
    
    _enclosure_fan_max = None
    @property
    def enclosure_fan_max(self):
        """
        The maximum number of fan modules present in this
        enclosure. R100/R150 shelf fans are not incldued in
        this number. A maximum of 8 fan modules are supported.
        """
        return self._enclosure_fan_max
    @enclosure_fan_max.setter
    def enclosure_fan_max(self, val):
        if val != None:
            self.validate('enclosure_fan_max', val)
        self._enclosure_fan_max = val
    
    _enclosure_connector_vendor_list = None
    @property
    def enclosure_connector_vendor_list(self):
        """
        The list of vendors for connectors in this enclosure.
        If no cable is attached, entry is shown as "N/A".
        It is a comma separated list.
        """
        return self._enclosure_connector_vendor_list
    @enclosure_connector_vendor_list.setter
    def enclosure_connector_vendor_list(self, val):
        if val != None:
            self.validate('enclosure_connector_vendor_list', val)
        self._enclosure_connector_vendor_list = val
    
    _enclosure_power_supply_serial_number_list = None
    @property
    def enclosure_power_supply_serial_number_list(self):
        """
        The list of serial numbers of power supplies present
        in this enclosure.
        It is a comma separated list.
        """
        return self._enclosure_power_supply_serial_number_list
    @enclosure_power_supply_serial_number_list.setter
    def enclosure_power_supply_serial_number_list(self, val):
        if val != None:
            self.validate('enclosure_power_supply_serial_number_list', val)
        self._enclosure_power_supply_serial_number_list = val
    
    _enclosure_temp_sensor_max = None
    @property
    def enclosure_temp_sensor_max(self):
        """
        The maximum number of temperature sensors
        present in this enclosure. A maximum of
        12 temperature sensors are supported.
        """
        return self._enclosure_temp_sensor_max
    @enclosure_temp_sensor_max.setter
    def enclosure_temp_sensor_max(self, val):
        if val != None:
            self.validate('enclosure_temp_sensor_max', val)
        self._enclosure_temp_sensor_max = val
    
    _enclosure_fan_speed_list = None
    @property
    def enclosure_fan_speed_list(self):
        """
        The list of fan speeds in revolutions per minute (RPM)
        for fan modules present in this enclosure.
        This is only returned if fan speed status is
        known as not all enclosure types report this data.
        This list is a subset of enclosure-fan-list.
        It is a comma separated list.
        For an enclosure with 4 fan modules, an example could
        be "3600 RPM, 3070 RPM, 3450 RPM, 2700 RPM"
        """
        return self._enclosure_fan_speed_list
    @enclosure_fan_speed_list.setter
    def enclosure_fan_speed_list(self, val):
        if val != None:
            self.validate('enclosure_fan_speed_list', val)
        self._enclosure_fan_speed_list = val
    
    _enclosure_volt_sensors_overvolt_failed_list = None
    @property
    def enclosure_volt_sensors_overvolt_failed_list(self):
        """
        The list of voltage sensors reporting
        overvoltage failure in this enclosure.
        This should be a subset of enclosure-volt-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_overvolt_failed_list
    @enclosure_volt_sensors_overvolt_failed_list.setter
    def enclosure_volt_sensors_overvolt_failed_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_overvolt_failed_list', val)
        self._enclosure_volt_sensors_overvolt_failed_list = val
    
    _enclosure_electronics_part_number_list = None
    @property
    def enclosure_electronics_part_number_list(self):
        """
        The list of part numbers of the enclosure
        services electronic modules present in
        this enclosure. This should be a subset of
        enclosure-electronics-list.
        It is a comma separated list.
        """
        return self._enclosure_electronics_part_number_list
    @enclosure_electronics_part_number_list.setter
    def enclosure_electronics_part_number_list(self, val):
        if val != None:
            self.validate('enclosure_electronics_part_number_list', val)
        self._enclosure_electronics_part_number_list = val
    
    _enclosure_connector_end_list = None
    @property
    def enclosure_connector_end_list(self):
        """
        The list of identifiers of which end of cable is attached to
        this enclosure.  If no cable is attached, entry is shown
        as "N/A". It is a comma separated list.
        """
        return self._enclosure_connector_end_list
    @enclosure_connector_end_list.setter
    def enclosure_connector_end_list(self, val):
        if val != None:
            self.validate('enclosure_connector_end_list', val)
        self._enclosure_connector_end_list = val
    
    _enclosure_electronics_serial_number_list = None
    @property
    def enclosure_electronics_serial_number_list(self):
        """
        The list of serial numbers of the enclosure
        services electronic modules that are possible
        for this enclosure.
        It is a comma separated list.
        """
        return self._enclosure_electronics_serial_number_list
    @enclosure_electronics_serial_number_list.setter
    def enclosure_electronics_serial_number_list(self, val):
        if val != None:
            self.validate('enclosure_electronics_serial_number_list', val)
        self._enclosure_electronics_serial_number_list = val
    
    _enclosure_current_sensors_max = None
    @property
    def enclosure_current_sensors_max(self):
        """
        The maximum number of electic current sensors present
        in this enclosure.
        A maximum of 12 electic current sensors are supported.
        """
        return self._enclosure_current_sensors_max
    @enclosure_current_sensors_max.setter
    def enclosure_current_sensors_max(self, val):
        if val != None:
            self.validate('enclosure_current_sensors_max', val)
        self._enclosure_current_sensors_max = val
    
    _enclosure_volt_sensors_overvolt_failed_threshold_list = None
    @property
    def enclosure_volt_sensors_overvolt_failed_threshold_list(self):
        """
        The list of overvoltage failure thresholds for
        all voltage sensors present in this enclosure.
        This should be a subset of enclosure-volt-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_overvolt_failed_threshold_list
    @enclosure_volt_sensors_overvolt_failed_threshold_list.setter
    def enclosure_volt_sensors_overvolt_failed_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_overvolt_failed_threshold_list', val)
        self._enclosure_volt_sensors_overvolt_failed_threshold_list = val
    
    _enclosure_current_sensor_list = None
    @property
    def enclosure_current_sensor_list(self):
        """
        The list of current sensors present in this enclosure.
        It is a comma separated list.
        """
        return self._enclosure_current_sensor_list
    @enclosure_current_sensor_list.setter
    def enclosure_current_sensor_list(self, val):
        if val != None:
            self.validate('enclosure_current_sensor_list', val)
        self._enclosure_current_sensor_list = val
    
    _enclosure_temp_sensors_overtemp_failed_threshold_list = None
    @property
    def enclosure_temp_sensors_overtemp_failed_threshold_list(self):
        """
        The list of overtemperature failure
        thresholds for all temperature sensors present
        in this enclosure. This should be a subset of
        enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensors_overtemp_failed_threshold_list
    @enclosure_temp_sensors_overtemp_failed_threshold_list.setter
    def enclosure_temp_sensors_overtemp_failed_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_overtemp_failed_threshold_list', val)
        self._enclosure_temp_sensors_overtemp_failed_threshold_list = val
    
    _enclosure_fan_list = None
    @property
    def enclosure_fan_list(self):
        """
        The list of fan modules present in this enclosure.
        R100/R150 shelf fans are not included in this list.
        It is a comma separated list.
        For an enclosure with 4 fan modules, an
        example could be "1, 2, 3, 4".
        """
        return self._enclosure_fan_list
    @enclosure_fan_list.setter
    def enclosure_fan_list(self, val):
        if val != None:
            self.validate('enclosure_fan_list', val)
        self._enclosure_fan_list = val
    
    _enclosure_connector_serial_number_list = None
    @property
    def enclosure_connector_serial_number_list(self):
        """
        The list of serial numbers of the connectors in this
        enclosure. If no cable is attached, entry is shown as "N/A".
        It is a comma separated list.
        """
        return self._enclosure_connector_serial_number_list
    @enclosure_connector_serial_number_list.setter
    def enclosure_connector_serial_number_list(self, val):
        if val != None:
            self.validate('enclosure_connector_serial_number_list', val)
        self._enclosure_connector_serial_number_list = val
    
    _enclosure_electronics_max = None
    @property
    def enclosure_electronics_max(self):
        """
        The maximum number of enclosure services
        electronic modules that are possible for
        this enclosure to detect or monitor.
        A maximum of 2 electronics are supported.
        """
        return self._enclosure_electronics_max
    @enclosure_electronics_max.setter
    def enclosure_electronics_max(self, val):
        if val != None:
            self.validate('enclosure_electronics_max', val)
        self._enclosure_electronics_max = val
    
    _enclosure_power_supply_failed_list = None
    @property
    def enclosure_power_supply_failed_list(self):
        """
        The list of failed power supplies present in this enclosure.
        This should be a subset of enclosure-power-supply-list.
        It is a comma separated list.
        """
        return self._enclosure_power_supply_failed_list
    @enclosure_power_supply_failed_list.setter
    def enclosure_power_supply_failed_list(self, val):
        if val != None:
            self.validate('enclosure_power_supply_failed_list', val)
        self._enclosure_power_supply_failed_list = val
    
    _enclosure_power_supply_part_number_list = None
    @property
    def enclosure_power_supply_part_number_list(self):
        """
        The list of part numbers of power supplies present in this
        enclosure. This list will be a subset of
        enclosure-power-supply-list.
        It is a comma separated list.
        """
        return self._enclosure_power_supply_part_number_list
    @enclosure_power_supply_part_number_list.setter
    def enclosure_power_supply_part_number_list(self, val):
        if val != None:
            self.validate('enclosure_power_supply_part_number_list', val)
        self._enclosure_power_supply_part_number_list = val
    
    _enclosure_temp_sensors_undertemp_failed_threshold_list = None
    @property
    def enclosure_temp_sensors_undertemp_failed_threshold_list(self):
        """
        The list of undertemperature failure
        thresholds for all temperature sensors present
        in this enclosure. This should be a subset of
        enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensors_undertemp_failed_threshold_list
    @enclosure_temp_sensors_undertemp_failed_threshold_list.setter
    def enclosure_temp_sensors_undertemp_failed_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_undertemp_failed_threshold_list', val)
        self._enclosure_temp_sensors_undertemp_failed_threshold_list = val
    
    _enclosure_volt_sensors_overvolt_warn_threshold_list = None
    @property
    def enclosure_volt_sensors_overvolt_warn_threshold_list(self):
        """
        The list of overvoltage warning thresholds for all
        voltage sensors present in this enclosure.
        This should be a subset of enclosure-volt-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_overvolt_warn_threshold_list
    @enclosure_volt_sensors_overvolt_warn_threshold_list.setter
    def enclosure_volt_sensors_overvolt_warn_threshold_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_overvolt_warn_threshold_list', val)
        self._enclosure_volt_sensors_overvolt_warn_threshold_list = val
    
    _enclosure_volt_sensors_undervolt_warn_list = None
    @property
    def enclosure_volt_sensors_undervolt_warn_list(self):
        """
        The list of voltage sensors reporting
        undervoltage warning in this enclosure.
        This should be a subset of enclosure-volt-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_undervolt_warn_list
    @enclosure_volt_sensors_undervolt_warn_list.setter
    def enclosure_volt_sensors_undervolt_warn_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_undervolt_warn_list', val)
        self._enclosure_volt_sensors_undervolt_warn_list = val
    
    _enclosure_connector_part_number_list = None
    @property
    def enclosure_connector_part_number_list(self):
        """
        The list of part numbers for connectors in this enclosure.
        If no cable is attached, entry is shown as "N/A".
        It is a comma separated list.
        """
        return self._enclosure_connector_part_number_list
    @enclosure_connector_part_number_list.setter
    def enclosure_connector_part_number_list(self, val):
        if val != None:
            self.validate('enclosure_connector_part_number_list', val)
        self._enclosure_connector_part_number_list = val
    
    _enclosure_power_supply_max = None
    @property
    def enclosure_power_supply_max(self):
        """
        The maximum number of power supplies in this enclosure.
        A maximum of 4 power supplies are supported.
        """
        return self._enclosure_power_supply_max
    @enclosure_power_supply_max.setter
    def enclosure_power_supply_max(self, val):
        if val != None:
            self.validate('enclosure_power_supply_max', val)
        self._enclosure_power_supply_max = val
    
    _enclosure_cable_tech_list = None
    @property
    def enclosure_cable_tech_list(self):
        """
        The list of cable technologies for connectors present in
        this enclosure.  If no cable is attached, entry is shown
        as "N/A".
        It is a comma separated list.
        """
        return self._enclosure_cable_tech_list
    @enclosure_cable_tech_list.setter
    def enclosure_cable_tech_list(self, val):
        if val != None:
            self.validate('enclosure_cable_tech_list', val)
        self._enclosure_cable_tech_list = val
    
    _enclosure_number = None
    @property
    def enclosure_number(self):
        """
        A number representing the number of enclosures.
        A maximum of 200 enclosures can be present.
        """
        return self._enclosure_number
    @enclosure_number.setter
    def enclosure_number(self, val):
        if val != None:
            self.validate('enclosure_number', val)
        self._enclosure_number = val
    
    _enclosure_contact_state = None
    @property
    def enclosure_contact_state(self):
        """
        The state of the communication between
        the filer or storage engine and the
        enclosure monitoring device in the enclosure.
        Possible values are:
        <ul>
        <li> initializing
        <li> transitioning
        <li> active
        <li> inactive
        <li> reconfiguring
        <li> nonexistent
        </ul>
        """
        return self._enclosure_contact_state
    @enclosure_contact_state.setter
    def enclosure_contact_state(self, val):
        if val != None:
            self.validate('enclosure_contact_state', val)
        self._enclosure_contact_state = val
    
    _enclosure_temp_sensors_undertemp_failed_list = None
    @property
    def enclosure_temp_sensors_undertemp_failed_list(self):
        """
        The list of temperature sensors reporting
        undertemperature failure in this enclosure.
        This should be a subset of enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensors_undertemp_failed_list
    @enclosure_temp_sensors_undertemp_failed_list.setter
    def enclosure_temp_sensors_undertemp_failed_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_undertemp_failed_list', val)
        self._enclosure_temp_sensors_undertemp_failed_list = val
    
    _enclosure_current_sensors_reading_list = None
    @property
    def enclosure_current_sensors_reading_list(self):
        """
        The list of currents reported by all current
        sensors present in this enclosure. This should
        be a subset of enclosure-current-sensor-list.
        """
        return self._enclosure_current_sensors_reading_list
    @enclosure_current_sensors_reading_list.setter
    def enclosure_current_sensors_reading_list(self, val):
        if val != None:
            self.validate('enclosure_current_sensors_reading_list', val)
        self._enclosure_current_sensors_reading_list = val
    
    _enclosure_temp_sensors_undertemp_warn_list = None
    @property
    def enclosure_temp_sensors_undertemp_warn_list(self):
        """
        The list of temperature sensors reporting
        undertemperature warnings in this enclosure.
        This should be a subset of enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensors_undertemp_warn_list
    @enclosure_temp_sensors_undertemp_warn_list.setter
    def enclosure_temp_sensors_undertemp_warn_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_undertemp_warn_list', val)
        self._enclosure_temp_sensors_undertemp_warn_list = val
    
    _enclosure_serial_number = None
    @property
    def enclosure_serial_number(self):
        """
        The serial number of this enclosure.
        """
        return self._enclosure_serial_number
    @enclosure_serial_number.setter
    def enclosure_serial_number(self, val):
        if val != None:
            self.validate('enclosure_serial_number', val)
        self._enclosure_serial_number = val
    
    _enclosure_disk_bay_count = None
    @property
    def enclosure_disk_bay_count(self):
        """
        The number of disk bays in this enclosure.
        Maximum number of bays supported per enclosure is 24.
        """
        return self._enclosure_disk_bay_count
    @enclosure_disk_bay_count.setter
    def enclosure_disk_bay_count(self, val):
        if val != None:
            self.validate('enclosure_disk_bay_count', val)
        self._enclosure_disk_bay_count = val
    
    _enclosure_volt_sensors_reading_list = None
    @property
    def enclosure_volt_sensors_reading_list(self):
        """
        The list of voltage reported by all
        voltage sensors in this enclosure.
        This should be a subset of enclosure-volt-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_volt_sensors_reading_list
    @enclosure_volt_sensors_reading_list.setter
    def enclosure_volt_sensors_reading_list(self, val):
        if val != None:
            self.validate('enclosure_volt_sensors_reading_list', val)
        self._enclosure_volt_sensors_reading_list = val
    
    _enclosure_fan_failed_list = None
    @property
    def enclosure_fan_failed_list(self):
        """
        The list of failed fan modules present in this enclosure.
        This should be a subset of enclosure-fan-list.
        It is a comma separated list.
        """
        return self._enclosure_fan_failed_list
    @enclosure_fan_failed_list.setter
    def enclosure_fan_failed_list(self, val):
        if val != None:
            self.validate('enclosure_fan_failed_list', val)
        self._enclosure_fan_failed_list = val
    
    _enclosure_model = None
    @property
    def enclosure_model(self):
        """
        The model name of this enclosure.
        An example is DiskShelf14.
        """
        return self._enclosure_model
    @enclosure_model.setter
    def enclosure_model(self, val):
        if val != None:
            self.validate('enclosure_model', val)
        self._enclosure_model = val
    
    _enclosure_disk_list = None
    @property
    def enclosure_disk_list(self):
        """
        The list of disks present by bay number in this enclosure.
        It is a comma separated list.
        For a shelf with 8 disks, an example could be
        "0, 1, 2, 3, 4, 5, 6, 7".
        """
        return self._enclosure_disk_list
    @enclosure_disk_list.setter
    def enclosure_disk_list(self, val):
        if val != None:
            self.validate('enclosure_disk_list', val)
        self._enclosure_disk_list = val
    
    _enclosure_electronics_cpld_list = None
    @property
    def enclosure_electronics_cpld_list(self):
        """
        The list of complex programmable logic devices
        (CPLD) present in this enclosure. Not all
        enclosures report this. This should be a subset
        of enclosure-electronics-list.
        It is a comma separated list.
        """
        return self._enclosure_electronics_cpld_list
    @enclosure_electronics_cpld_list.setter
    def enclosure_electronics_cpld_list(self, val):
        if val != None:
            self.validate('enclosure_electronics_cpld_list', val)
        self._enclosure_electronics_cpld_list = val
    
    _enclosure_connector_length_list = None
    @property
    def enclosure_connector_length_list(self):
        """
        The list of cable lengths for connectors present in this
        enclosure. These are in meters. If no cable is attached,
        entry is shown as "N/A".
        It is a comma separated list.
        """
        return self._enclosure_connector_length_list
    @enclosure_connector_length_list.setter
    def enclosure_connector_length_list(self, val):
        if val != None:
            self.validate('enclosure_connector_length_list', val)
        self._enclosure_connector_length_list = val
    
    _enclosure_temp_sensors_overtemp_warn_list = None
    @property
    def enclosure_temp_sensors_overtemp_warn_list(self):
        """
        The list of temperature sensors reporting
        overtemperature warning in this enclosure.
        This should be a subset of enclosure-temp-sensor-list.
        It is a comma separated list.
        """
        return self._enclosure_temp_sensors_overtemp_warn_list
    @enclosure_temp_sensors_overtemp_warn_list.setter
    def enclosure_temp_sensors_overtemp_warn_list(self, val):
        if val != None:
            self.validate('enclosure_temp_sensors_overtemp_warn_list', val)
        self._enclosure_temp_sensors_overtemp_warn_list = val
    
    @staticmethod
    def get_api_name():
          return "storage-shelf-enclosure-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'enclosure-volt-sensors-undervolt-failed-list',
            'enclosure-product-revision',
            'enclosure-electronics-failed-list',
            'enclosure-electronics-list',
            'enclosure-temp-sensors-undertemp-warn-threshold-list',
            'enclosure-node-name',
            'enclosure-connector-type-list',
            'enclosure-connector-list',
            'enclosure-volt-sensors-undervolt-failed-threshold-list',
            'enclosure-temp-sensors-reading-list',
            'enclosure-volt-sensors-undervolt-warn-threshold-list',
            'enclosure-product-id',
            'enclosure-power-supply-list',
            'enclosure-current-sensors-overcurrent-warn-threshold-list',
            'enclosure-temp-sensors-overtemp-failed-list',
            'enclosure-vendor',
            'enclosure-shelf-addr',
            'enclosure-current-sensors-overcurrent-failed-list',
            'enclosure-volt-sensors-max',
            'enclosure-volt-sensor-list',
            'enclosure-current-sensors-overcurrent-failed-threshold-list',
            'enclosure-connector-max',
            'enclosure-temp-sensors-overtemp-warn-threshold-list',
            'enclosure-current-sensors-overcurrent-warn-list',
            'enclosure-logical-id',
            'enclosure-temp-sensor-list',
            'enclosure-volt-sensors-overvolt-warn-list',
            'enclosure-fan-max',
            'enclosure-connector-vendor-list',
            'enclosure-power-supply-serial-number-list',
            'enclosure-temp-sensor-max',
            'enclosure-fan-speed-list',
            'enclosure-volt-sensors-overvolt-failed-list',
            'enclosure-electronics-part-number-list',
            'enclosure-connector-end-list',
            'enclosure-electronics-serial-number-list',
            'enclosure-current-sensors-max',
            'enclosure-volt-sensors-overvolt-failed-threshold-list',
            'enclosure-current-sensor-list',
            'enclosure-temp-sensors-overtemp-failed-threshold-list',
            'enclosure-fan-list',
            'enclosure-connector-serial-number-list',
            'enclosure-electronics-max',
            'enclosure-power-supply-failed-list',
            'enclosure-power-supply-part-number-list',
            'enclosure-temp-sensors-undertemp-failed-threshold-list',
            'enclosure-volt-sensors-overvolt-warn-threshold-list',
            'enclosure-volt-sensors-undervolt-warn-list',
            'enclosure-connector-part-number-list',
            'enclosure-power-supply-max',
            'enclosure-cable-tech-list',
            'enclosure-number',
            'enclosure-contact-state',
            'enclosure-temp-sensors-undertemp-failed-list',
            'enclosure-current-sensors-reading-list',
            'enclosure-temp-sensors-undertemp-warn-list',
            'enclosure-serial-number',
            'enclosure-disk-bay-count',
            'enclosure-volt-sensors-reading-list',
            'enclosure-fan-failed-list',
            'enclosure-model',
            'enclosure-disk-list',
            'enclosure-electronics-cpld-list',
            'enclosure-connector-length-list',
            'enclosure-temp-sensors-overtemp-warn-list',
        ]
    
    def describe_properties(self):
        return {
            'enclosure_volt_sensors_undervolt_failed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_product_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_electronics_failed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_electronics_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_undertemp_warn_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_connector_type_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_connector_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_undervolt_failed_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_reading_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_undervolt_warn_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_product_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_power_supply_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_current_sensors_overcurrent_warn_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_overtemp_failed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_vendor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_shelf_addr': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_current_sensors_overcurrent_failed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_max': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensor_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_current_sensors_overcurrent_failed_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_connector_max': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_overtemp_warn_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_current_sensors_overcurrent_warn_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_logical_id': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensor_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_overvolt_warn_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_fan_max': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_connector_vendor_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_power_supply_serial_number_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensor_max': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_fan_speed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_overvolt_failed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_electronics_part_number_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_connector_end_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_electronics_serial_number_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_current_sensors_max': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_overvolt_failed_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_current_sensor_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_overtemp_failed_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_fan_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_connector_serial_number_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_electronics_max': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_power_supply_failed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_power_supply_part_number_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_undertemp_failed_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_overvolt_warn_threshold_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_undervolt_warn_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_connector_part_number_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_power_supply_max': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_cable_tech_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_number': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_contact_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_undertemp_failed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_current_sensors_reading_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_undertemp_warn_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_serial_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_disk_bay_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'enclosure_volt_sensors_reading_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_fan_failed_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_model': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_disk_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_electronics_cpld_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_connector_length_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'enclosure_temp_sensors_overtemp_warn_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
