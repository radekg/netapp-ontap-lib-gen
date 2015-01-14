from netapp.netapp_object import NetAppObject

class RaidtypeInfo(NetAppObject):
    """
    RAID types allowed on this filer.
    """
    
    _raidtype = None
    @property
    def raidtype(self):
        """
        Name of an allowed RAID type.  Possible
        values: raid0, raid4, raid_dp.
        """
        return self._raidtype
    @raidtype.setter
    def raidtype(self, val):
        if val != None:
            self.validate('raidtype', val)
        self._raidtype = val
    
    @staticmethod
    def get_api_name():
          return "raidtype-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'raidtype',
        ]
    
    def describe_properties(self):
        return {
            'raidtype': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
