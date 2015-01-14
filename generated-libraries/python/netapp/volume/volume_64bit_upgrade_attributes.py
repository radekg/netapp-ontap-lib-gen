from netapp.volume.volume_64bit_upgrade_check_attributes import Volume64BitUpgradeCheckAttributes
from netapp.netapp_object import NetAppObject

class Volume64BitUpgradeAttributes(NetAppObject):
    """
    Information related to 64-bit upgrade.
    """
    
    _volume_64bit_upgrade_check_attributes = None
    @property
    def volume_64bit_upgrade_check_attributes(self):
        """
        Information returned when 'upgrade-64bit-mode' input in
        'aggr-add' is 'check'. Upgrade check results such as
        'used-space', 'available-space', 'capacity', and
        'grow-space' are only updated after the space estimate is
        completed successfully.
        """
        return self._volume_64bit_upgrade_check_attributes
    @volume_64bit_upgrade_check_attributes.setter
    def volume_64bit_upgrade_check_attributes(self, val):
        if val != None:
            self.validate('volume_64bit_upgrade_check_attributes', val)
        self._volume_64bit_upgrade_check_attributes = val
    
    @staticmethod
    def get_api_name():
          return "volume-64bit-upgrade-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'volume-64bit-upgrade-check-attributes',
        ]
    
    def describe_properties(self):
        return {
            'volume_64bit_upgrade_check_attributes': { 'class': Volume64BitUpgradeCheckAttributes, 'is_list': False, 'required': 'optional' },
        }
