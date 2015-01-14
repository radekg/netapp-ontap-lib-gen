from netapp.netapp_object import NetAppObject

class AggrStatusAttributes(NetAppObject):
    """
    Status information related to 64-bit upgrade.
    This information includes whether the 64-bit upgrade
    is in progress.
    """
    
    _is_64_bit_upgrade_in_progress = None
    @property
    def is_64_bit_upgrade_in_progress(self):
        """
        True if the 64-bit upgrade is in
        progress.
        """
        return self._is_64_bit_upgrade_in_progress
    @is_64_bit_upgrade_in_progress.setter
    def is_64_bit_upgrade_in_progress(self, val):
        if val != None:
            self.validate('is_64_bit_upgrade_in_progress', val)
        self._is_64_bit_upgrade_in_progress = val
    
    @staticmethod
    def get_api_name():
          return "aggr-status-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-64-bit-upgrade-in-progress',
        ]
    
    def describe_properties(self):
        return {
            'is_64_bit_upgrade_in_progress': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
