from netapp.aggr.aggr_64bit_upgrade_status_info import Aggr64BitUpgradeStatusInfo
from netapp.aggr.aggr_64bit_upgrade_start_info import Aggr64BitUpgradeStartInfo
from netapp.aggr.aggr_64bit_upgrade_check_info import Aggr64BitUpgradeCheckInfo
from netapp.netapp_object import NetAppObject

class Aggr64BitUpgradeInfo(NetAppObject):
    """
    Information related to 64-bit upgrade.
    """
    
    _status = None
    @property
    def status(self):
        """
        Status information related to 64-bit upgrade.
        This information includes the block format
        of the aggregate and the progress of the 64-bit
        upgrade scanner.
        """
        return self._status
    @status.setter
    def status(self, val):
        if val != None:
            self.validate('status', val)
        self._status = val
    
    _start = None
    @property
    def start(self):
        """
        Information returned when upgrade-64bit-mode in
        aggr-add or aggr-64bit-upgrade-start is
        "grow_all", "grow_none", or "grow_reserved".
        """
        return self._start
    @start.setter
    def start(self, val):
        if val != None:
            self.validate('start', val)
        self._start = val
    
    _check = None
    @property
    def check(self):
        """
        Information returned when upgrade-64bit-mode in
        aggr-add or aggr-64bit-upgrade-start is "check".
        """
        return self._check
    @check.setter
    def check(self, val):
        if val != None:
            self.validate('check', val)
        self._check = val
    
    @staticmethod
    def get_api_name():
          return "aggr-64bit-upgrade-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'status',
            'start',
            'check',
        ]
    
    def describe_properties(self):
        return {
            'status': { 'class': Aggr64BitUpgradeStatusInfo, 'is_list': False, 'required': 'required' },
            'start': { 'class': Aggr64BitUpgradeStartInfo, 'is_list': False, 'required': 'optional' },
            'check': { 'class': Aggr64BitUpgradeCheckInfo, 'is_list': False, 'required': 'optional' },
        }
