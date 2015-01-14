from netapp.ses.esh_info import EshInfo
from netapp.netapp_object import NetAppObject

class EsElectronicsInfo(NetAppObject):
    """
    Information on the installed enclosure services (ES) electronics.
    """
    
    _es_electronics_element_no = None
    @property
    def es_electronics_element_no(self):
        """
        Enclosure services electronics element number.
        """
        return self._es_electronics_element_no
    @es_electronics_element_no.setter
    def es_electronics_element_no(self, val):
        if val != None:
            self.validate('es_electronics_element_no', val)
        self._es_electronics_element_no = val
    
    _es_revision = None
    @property
    def es_revision(self):
        """
        CPLD revision of the ES electronics, if applicable.
        This field will not be present if the information
        is not available, not implemented, or if the
        element is not installed.
        """
        return self._es_revision
    @es_revision.setter
    def es_revision(self, val):
        if val != None:
            self.validate('es_revision', val)
        self._es_revision = val
    
    _esh_list = None
    @property
    def esh_list(self):
        """
        Information on attached embedded switched hub, if any.
        """
        return self._esh_list
    @esh_list.setter
    def esh_list(self, val):
        if val != None:
            self.validate('esh_list', val)
        self._esh_list = val
    
    _es_electronics_is_not_installed = None
    @property
    def es_electronics_is_not_installed(self):
        """
        Indicates this enclosure services electronics
        is not installed. This will only be presented when the
        element is missing, no further data for this element
        will be presented.
        """
        return self._es_electronics_is_not_installed
    @es_electronics_is_not_installed.setter
    def es_electronics_is_not_installed(self, val):
        if val != None:
            self.validate('es_electronics_is_not_installed', val)
        self._es_electronics_is_not_installed = val
    
    _es_part_number = None
    @property
    def es_part_number(self):
        """
        Part number for the ES electronics. Field
        will be missing if the information is not available
        or if the element is not installed.
        """
        return self._es_part_number
    @es_part_number.setter
    def es_part_number(self, val):
        if val != None:
            self.validate('es_part_number', val)
        self._es_part_number = val
    
    _es_swap_count = None
    @property
    def es_swap_count(self):
        """
        Number of times, since last boot, that this ES
        electronics elements has been swapped.
        Will not be present if the element is not installed.
        """
        return self._es_swap_count
    @es_swap_count.setter
    def es_swap_count(self, val):
        if val != None:
            self.validate('es_swap_count', val)
        self._es_swap_count = val
    
    _es_electronics_serial_no = None
    @property
    def es_electronics_serial_no(self):
        """
        Serial number for the enclosure services electronics.
        Will not be present if the element is not installed.
        """
        return self._es_electronics_serial_no
    @es_electronics_serial_no.setter
    def es_electronics_serial_no(self, val):
        if val != None:
            self.validate('es_electronics_serial_no', val)
        self._es_electronics_serial_no = val
    
    _es_electronics_is_reporting_element = None
    @property
    def es_electronics_is_reporting_element(self):
        """
        Indicated whether this is the element reporting. Even
        though there might be more than one element installed,
        only will be reporting at any time.
        Will not be present if the element is not installed.
        """
        return self._es_electronics_is_reporting_element
    @es_electronics_is_reporting_element.setter
    def es_electronics_is_reporting_element(self, val):
        if val != None:
            self.validate('es_electronics_is_reporting_element', val)
        self._es_electronics_is_reporting_element = val
    
    _es_electronics_is_error = None
    @property
    def es_electronics_is_error(self):
        """
        indicates whether this enclosure services electronics
        has reported any errors.
        Will not be present if the element is not installed.
        """
        return self._es_electronics_is_error
    @es_electronics_is_error.setter
    def es_electronics_is_error(self, val):
        if val != None:
            self.validate('es_electronics_is_error', val)
        self._es_electronics_is_error = val
    
    @staticmethod
    def get_api_name():
          return "es-electronics-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'es-electronics-element-no',
            'es-revision',
            'esh-list',
            'es-electronics-is-not-installed',
            'es-part-number',
            'es-swap-count',
            'es-electronics-serial-no',
            'es-electronics-is-reporting-element',
            'es-electronics-is-error',
        ]
    
    def describe_properties(self):
        return {
            'es_electronics_element_no': { 'class': int, 'is_list': False, 'required': 'required' },
            'es_revision': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'esh_list': { 'class': EshInfo, 'is_list': True, 'required': 'optional' },
            'es_electronics_is_not_installed': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'es_part_number': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'es_swap_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'es_electronics_serial_no': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'es_electronics_is_reporting_element': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'es_electronics_is_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
