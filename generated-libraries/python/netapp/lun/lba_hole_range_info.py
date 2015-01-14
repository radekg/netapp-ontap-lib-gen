from netapp.netapp_object import NetAppObject

class LbaHoleRangeInfo(NetAppObject):
    """
    The actual data structure that contains the LBA ranges which
    are holes.  The hole region is inclusive of lba-hole-start and
    exclusive of lba-hole-end
    """
    
    _lba_hole_end = None
    @property
    def lba_hole_end(self):
        """
        Ending LBA of the hole
        """
        return self._lba_hole_end
    @lba_hole_end.setter
    def lba_hole_end(self, val):
        if val != None:
            self.validate('lba_hole_end', val)
        self._lba_hole_end = val
    
    _lba_hole_start = None
    @property
    def lba_hole_start(self):
        """
        Starting LBA of the hole
        """
        return self._lba_hole_start
    @lba_hole_start.setter
    def lba_hole_start(self, val):
        if val != None:
            self.validate('lba_hole_start', val)
        self._lba_hole_start = val
    
    @staticmethod
    def get_api_name():
          return "lba-hole-range-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'lba-hole-end',
            'lba-hole-start',
        ]
    
    def describe_properties(self):
        return {
            'lba_hole_end': { 'class': int, 'is_list': False, 'required': 'required' },
            'lba_hole_start': { 'class': int, 'is_list': False, 'required': 'required' },
        }
