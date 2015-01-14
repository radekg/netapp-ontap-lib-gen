from netapp.volume.volume_64bit_upgrade_check_info import Volume64BitUpgradeCheckInfo
from netapp.netapp_object import NetAppObject

class Volume64BitUpgradeInfo(NetAppObject):
    """
    Information related to 64-bit upgrade.
    """
    
    _check = None
    @property
    def check(self):
        """
        Information returned when upgrade-64bit-mode in
        aggr-add is "check".
        """
        return self._check
    @check.setter
    def check(self, val):
        if val != None:
            self.validate('check', val)
        self._check = val
    
    @staticmethod
    def get_api_name():
          return "volume-64bit-upgrade-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'check',
        ]
    
    def describe_properties(self):
        return {
            'check': { 'class': Volume64BitUpgradeCheckInfo, 'is_list': False, 'required': 'optional' },
        }
