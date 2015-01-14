from netapp.aggr.aggr_start_attributes import AggrStartAttributes
from netapp.aggr.aggr_status_attributes import AggrStatusAttributes
from netapp.aggr.aggr_check_attributes import AggrCheckAttributes
from netapp.netapp_object import NetAppObject

class Aggr64BitUpgradeAttributes(NetAppObject):
    """
    Information related to 64-bit upgrade.
    """
    
    _aggr_start_attributes = None
    @property
    def aggr_start_attributes(self):
        """
        Information returned when upgrade-64bit-mode in
        aggr-add API is "grow_all", "grow_none",
        or "grow_reserved".
        """
        return self._aggr_start_attributes
    @aggr_start_attributes.setter
    def aggr_start_attributes(self, val):
        if val != None:
            self.validate('aggr_start_attributes', val)
        self._aggr_start_attributes = val
    
    _aggr_status_attributes = None
    @property
    def aggr_status_attributes(self):
        """
        Status information related to 64-bit upgrade.
        This information includes whether the 64-bit upgrade
        is in progress.
        """
        return self._aggr_status_attributes
    @aggr_status_attributes.setter
    def aggr_status_attributes(self, val):
        if val != None:
            self.validate('aggr_status_attributes', val)
        self._aggr_status_attributes = val
    
    _aggr_check_attributes = None
    @property
    def aggr_check_attributes(self):
        """
        Information returned when upgrade-64bit-mode input in
        aggr-add API is "check".
        """
        return self._aggr_check_attributes
    @aggr_check_attributes.setter
    def aggr_check_attributes(self, val):
        if val != None:
            self.validate('aggr_check_attributes', val)
        self._aggr_check_attributes = val
    
    @staticmethod
    def get_api_name():
          return "aggr-64bit-upgrade-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'aggr-start-attributes',
            'aggr-status-attributes',
            'aggr-check-attributes',
        ]
    
    def describe_properties(self):
        return {
            'aggr_start_attributes': { 'class': AggrStartAttributes, 'is_list': False, 'required': 'optional' },
            'aggr_status_attributes': { 'class': AggrStatusAttributes, 'is_list': False, 'required': 'required' },
            'aggr_check_attributes': { 'class': AggrCheckAttributes, 'is_list': False, 'required': 'optional' },
        }
