from netapp.ses.ariodata_specific_info import AriodataSpecificInfo
from netapp.ses.alternate_control_path_info import AlternateControlPathInfo
from netapp.ses.cooling_element_info import CoolingElementInfo
from netapp.ses.processor_complex_info import ProcessorComplexInfo
from netapp.ses.es_electronics_info import EsElectronicsInfo
from netapp.ses.connector_info import ConnectorInfo
from netapp.ses.ses_generic_info import SesGenericInfo
from netapp.ses.sas_specific_info import SasSpecificInfo
from netapp.ses.xyratex_specific_info import XyratexSpecificInfo
from netapp.ses.voltage_sensor_info import VoltageSensorInfo
from netapp.ses.power_supply_info import PowerSupplyInfo
from netapp.ses.enclosure_info import EnclosureInfo
from netapp.ses.current_sensor_info import CurrentSensorInfo
from netapp.ses.eurologic_specific_info import EurologicSpecificInfo
from netapp.ses.temp_sensor_info import TempSensorInfo
from netapp.netapp_object import NetAppObject

class ShelfEnvironShelfInfo(NetAppObject):
    """
    Shelf environment information.
    """
    
    _ariodata_specific_info = None
    @property
    def ariodata_specific_info(self):
        """
        Vendor specific enclosure system information for
        Ariodata shelves.
        """
        return self._ariodata_specific_info
    @ariodata_specific_info.setter
    def ariodata_specific_info(self, val):
        if val != None:
            self.validate('ariodata_specific_info', val)
        self._ariodata_specific_info = val
    
    _control_writes_attempted = None
    @property
    def control_writes_attempted(self):
        """
        Number of times attempted to write shelf controls.
        """
        return self._control_writes_attempted
    @control_writes_attempted.setter
    def control_writes_attempted(self, val):
        if val != None:
            self.validate('control_writes_attempted', val)
        self._control_writes_attempted = val
    
    _alternate_control_path_information = None
    @property
    def alternate_control_path_information(self):
        """
        Available information on the alternate control path (ACP)
        to the shelf.
        """
        return self._alternate_control_path_information
    @alternate_control_path_information.setter
    def alternate_control_path_information(self, val):
        if val != None:
            self.validate('alternate_control_path_information', val)
        self._alternate_control_path_information = val
    
    _cooling_element_list = None
    @property
    def cooling_element_list(self):
        """
        Information on installed cooling elements in the shelf.
        """
        return self._cooling_element_list
    @cooling_element_list.setter
    def cooling_element_list(self, val):
        if val != None:
            self.validate('cooling_element_list', val)
        self._cooling_element_list = val
    
    _processor_complex_information = None
    @property
    def processor_complex_information(self):
        """
        Available information on the processor complex modules (PCMs)
        in the shelf.
        """
        return self._processor_complex_information
    @processor_complex_information.setter
    def processor_complex_information(self, val):
        if val != None:
            self.validate('processor_complex_information', val)
        self._processor_complex_information = val
    
    _status_reads_attempted = None
    @property
    def status_reads_attempted(self):
        """
        Number of times attempted to read shelf status.
        """
        return self._status_reads_attempted
    @status_reads_attempted.setter
    def status_reads_attempted(self, val):
        if val != None:
            self.validate('status_reads_attempted', val)
        self._status_reads_attempted = val
    
    _es_electronics_list = None
    @property
    def es_electronics_list(self):
        """
        Information on the installed enclosure services
        electronics.
        """
        return self._es_electronics_list
    @es_electronics_list.setter
    def es_electronics_list(self, val):
        if val != None:
            self.validate('es_electronics_list', val)
        self._es_electronics_list = val
    
    _connector_information = None
    @property
    def connector_information(self):
        """
        Cable and connector information if available
        and supported by the hardware.
        Will not be present if the feature is not supported
        in the hardware.
        """
        return self._connector_information
    @connector_information.setter
    def connector_information(self, val):
        if val != None:
            self.validate('connector_information', val)
        self._connector_information = val
    
    _controller_device_path_port = None
    @property
    def controller_device_path_port(self):
        """
        If controller-device-path is "local_access",
        then this presents the local access port number.
        """
        return self._controller_device_path_port
    @controller_device_path_port.setter
    def controller_device_path_port(self, val):
        if val != None:
            self.validate('controller_device_path_port', val)
        self._controller_device_path_port = val
    
    _is_shelf_monitor_enabled = None
    @property
    def is_shelf_monitor_enabled(self):
        """
        Indicates whether monitoring is enabled on this shelf.
        """
        return self._is_shelf_monitor_enabled
    @is_shelf_monitor_enabled.setter
    def is_shelf_monitor_enabled(self, val):
        if val != None:
            self.validate('is_shelf_monitor_enabled', val)
        self._is_shelf_monitor_enabled = val
    
    _shelf_id = None
    @property
    def shelf_id(self):
        """
        Shelf number.
        """
        return self._shelf_id
    @shelf_id.setter
    def shelf_id(self, val):
        if val != None:
            self.validate('shelf_id', val)
        self._shelf_id = val
    
    _power_control_status = None
    @property
    def power_control_status(self):
        """
        Power control element status. This is generalization
        of the ESH4 shelf power status. Currently available
        on ESH 4 shelves only. Possible values:
        "ok", "not_supported", "critical", "non_critical", "unknown".
        """
        return self._power_control_status
    @power_control_status.setter
    def power_control_status(self, val):
        if val != None:
            self.validate('power_control_status', val)
        self._power_control_status = val
    
    _control_writes_failed = None
    @property
    def control_writes_failed(self):
        """
        Number of times failed to write shelf controls.
        """
        return self._control_writes_failed
    @control_writes_failed.setter
    def control_writes_failed(self, val):
        if val != None:
            self.validate('control_writes_failed', val)
        self._control_writes_failed = val
    
    _power_control_failure_state = None
    @property
    def power_control_failure_state(self):
        """
        Extension to the power-control-status to provide
        more information in case of shelf failures.
        Possible values:
        "dual_esh4_modules_not_present",
        "power_control_fault_detected",
        "incompatible_power_control_implementation",
        "power_control_function_not_available",
        "backplane_cpld_fault_detected".
        """
        return self._power_control_failure_state
    @power_control_failure_state.setter
    def power_control_failure_state(self, val):
        if val != None:
            self.validate('power_control_failure_state', val)
        self._power_control_failure_state = val
    
    _ses_generic_info = None
    @property
    def ses_generic_info(self):
        """
        Generic SES (scsi enclosure services) information.
        """
        return self._ses_generic_info
    @ses_generic_info.setter
    def ses_generic_info(self, val):
        if val != None:
            self.validate('ses_generic_info', val)
        self._ses_generic_info = val
    
    _sas_specific_info = None
    @property
    def sas_specific_info(self):
        """
        Vendor specific enclosure system information for
        SAS shelves.
        """
        return self._sas_specific_info
    @sas_specific_info.setter
    def sas_specific_info(self, val):
        if val != None:
            self.validate('sas_specific_info', val)
        self._sas_specific_info = val
    
    _controller_device_path = None
    @property
    def controller_device_path(self):
        """
        Device path to the shelf controller. Possible values:
        "embedded_access", "local_access",
        "unknown", "not_available".
        """
        return self._controller_device_path
    @controller_device_path.setter
    def controller_device_path(self, val):
        if val != None:
            self.validate('controller_device_path', val)
        self._controller_device_path = val
    
    _xyratex_specific_info = None
    @property
    def xyratex_specific_info(self):
        """
        Vendor specific enclosure system information for
        Xyratex shelves.
        """
        return self._xyratex_specific_info
    @xyratex_specific_info.setter
    def xyratex_specific_info(self, val):
        if val != None:
            self.validate('xyratex_specific_info', val)
        self._xyratex_specific_info = val
    
    _attached_shelf_bay_list = None
    @property
    def attached_shelf_bay_list(self):
        """
        A list of bays numbers in this shelf that have
        disk devices installed. All bays with disks
        installed will be listed. This is a comma separated
        list from high to low. Example: "13, 11, 10, 4, 3, 2, 1".
        """
        return self._attached_shelf_bay_list
    @attached_shelf_bay_list.setter
    def attached_shelf_bay_list(self, val):
        if val != None:
            self.validate('attached_shelf_bay_list', val)
        self._attached_shelf_bay_list = val
    
    _status_reads_failed = None
    @property
    def status_reads_failed(self):
        """
        Number of times failed to read shelf status.
        """
        return self._status_reads_failed
    @status_reads_failed.setter
    def status_reads_failed(self, val):
        if val != None:
            self.validate('status_reads_failed', val)
        self._status_reads_failed = val
    
    _voltage_sensor_list = None
    @property
    def voltage_sensor_list(self):
        """
        Information on voltage sensors in the shelf.
        """
        return self._voltage_sensor_list
    @voltage_sensor_list.setter
    def voltage_sensor_list(self, val):
        if val != None:
            self.validate('voltage_sensor_list', val)
        self._voltage_sensor_list = val
    
    _power_supply_list = None
    @property
    def power_supply_list(self):
        """
        Information on installed power supplies in the shelf.
        """
        return self._power_supply_list
    @power_supply_list.setter
    def power_supply_list(self, val):
        if val != None:
            self.validate('power_supply_list', val)
        self._power_supply_list = val
    
    _enclosure_information = None
    @property
    def enclosure_information(self):
        """
        Information on the enclosure type. This information will be
        presented for ESH and SAS shelves only.
        """
        return self._enclosure_information
    @enclosure_information.setter
    def enclosure_information(self, val):
        if val != None:
            self.validate('enclosure_information', val)
        self._enclosure_information = val
    
    _shelf_type = None
    @property
    def shelf_type(self):
        """
        Shelf type. Possible values: "edm", "vem", "esp", "lrc",
        "lrc2", "esh", "esh2", "esh4", "eshfx", "emu", "efh",
        "eshtx", "sas", "esas", "sas_fc", "iom3", "at_fcx",
        "at_fcx2", "iom6", "iom6e".
        """
        return self._shelf_type
    @shelf_type.setter
    def shelf_type(self, val):
        if val != None:
            self.validate('shelf_type', val)
        self._shelf_type = val
    
    _current_sensor_list = None
    @property
    def current_sensor_list(self):
        """
        Information on current sensors in the shelf.
        """
        return self._current_sensor_list
    @current_sensor_list.setter
    def current_sensor_list(self, val):
        if val != None:
            self.validate('current_sensor_list', val)
        self._current_sensor_list = val
    
    _eurologic_specific_info = None
    @property
    def eurologic_specific_info(self):
        """
        Vendor specific enclosure system information for
        Eurologic shelves.
        """
        return self._eurologic_specific_info
    @eurologic_specific_info.setter
    def eurologic_specific_info(self, val):
        if val != None:
            self.validate('eurologic_specific_info', val)
        self._eurologic_specific_info = val
    
    _shelf_status = None
    @property
    def shelf_status(self):
        """
        Current shelf status. Possible values: "unrecoverable",
        "critical", "non_critical", "informational", "normal".
        """
        return self._shelf_status
    @shelf_status.setter
    def shelf_status(self, val):
        if val != None:
            self.validate('shelf_status', val)
        self._shelf_status = val
    
    _temp_sensor_list = None
    @property
    def temp_sensor_list(self):
        """
        Information on installed temperature sensors in the shelf.
        """
        return self._temp_sensor_list
    @temp_sensor_list.setter
    def temp_sensor_list(self, val):
        if val != None:
            self.validate('temp_sensor_list', val)
        self._temp_sensor_list = val
    
    _attached_shelf_bay_error_list = None
    @property
    def attached_shelf_bay_error_list(self):
        """
        A list of bays numbers in this shelf that have
        disk devices with errors. All bays with error
        devices will be listed. This is a comma separated
        list from high to low. Example: "13, 10, 4, 1".
        """
        return self._attached_shelf_bay_error_list
    @attached_shelf_bay_error_list.setter
    def attached_shelf_bay_error_list(self, val):
        if val != None:
            self.validate('attached_shelf_bay_error_list', val)
        self._attached_shelf_bay_error_list = val
    
    @staticmethod
    def get_api_name():
          return "shelf-environ-shelf-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'ariodata-specific-info',
            'control-writes-attempted',
            'alternate-control-path-information',
            'cooling-element-list',
            'processor-complex-information',
            'status-reads-attempted',
            'es-electronics-list',
            'connector-information',
            'controller-device-path-port',
            'is-shelf-monitor-enabled',
            'shelf-id',
            'power-control-status',
            'control-writes-failed',
            'power-control-failure-state',
            'ses-generic-info',
            'sas-specific-info',
            'controller-device-path',
            'xyratex-specific-info',
            'attached-shelf-bay-list',
            'status-reads-failed',
            'voltage-sensor-list',
            'power-supply-list',
            'enclosure-information',
            'shelf-type',
            'current-sensor-list',
            'eurologic-specific-info',
            'shelf-status',
            'temp-sensor-list',
            'attached-shelf-bay-error-list',
        ]
    
    def describe_properties(self):
        return {
            'ariodata_specific_info': { 'class': AriodataSpecificInfo, 'is_list': False, 'required': 'optional' },
            'control_writes_attempted': { 'class': int, 'is_list': False, 'required': 'required' },
            'alternate_control_path_information': { 'class': AlternateControlPathInfo, 'is_list': True, 'required': 'optional' },
            'cooling_element_list': { 'class': CoolingElementInfo, 'is_list': True, 'required': 'optional' },
            'processor_complex_information': { 'class': ProcessorComplexInfo, 'is_list': True, 'required': 'optional' },
            'status_reads_attempted': { 'class': int, 'is_list': False, 'required': 'required' },
            'es_electronics_list': { 'class': EsElectronicsInfo, 'is_list': True, 'required': 'optional' },
            'connector_information': { 'class': ConnectorInfo, 'is_list': True, 'required': 'optional' },
            'controller_device_path_port': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_shelf_monitor_enabled': { 'class': bool, 'is_list': False, 'required': 'required' },
            'shelf_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'power_control_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'control_writes_failed': { 'class': int, 'is_list': False, 'required': 'required' },
            'power_control_failure_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'ses_generic_info': { 'class': SesGenericInfo, 'is_list': False, 'required': 'required' },
            'sas_specific_info': { 'class': SasSpecificInfo, 'is_list': False, 'required': 'optional' },
            'controller_device_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'xyratex_specific_info': { 'class': XyratexSpecificInfo, 'is_list': False, 'required': 'optional' },
            'attached_shelf_bay_list': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'status_reads_failed': { 'class': int, 'is_list': False, 'required': 'required' },
            'voltage_sensor_list': { 'class': VoltageSensorInfo, 'is_list': True, 'required': 'optional' },
            'power_supply_list': { 'class': PowerSupplyInfo, 'is_list': True, 'required': 'optional' },
            'enclosure_information': { 'class': EnclosureInfo, 'is_list': False, 'required': 'optional' },
            'shelf_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'current_sensor_list': { 'class': CurrentSensorInfo, 'is_list': True, 'required': 'optional' },
            'eurologic_specific_info': { 'class': EurologicSpecificInfo, 'is_list': False, 'required': 'optional' },
            'shelf_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'temp_sensor_list': { 'class': TempSensorInfo, 'is_list': True, 'required': 'optional' },
            'attached_shelf_bay_error_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
