from netapp.ses.bay_info import BayInfo
from netapp.netapp_object import NetAppObject

class ShelfBayInfo(NetAppObject):
    """
    Shelf bay information.
    """
    
    _bay_list = None
    @property
    def bay_list(self):
        """
        A list of shelf-bay numbers which have disk
        drives.  The bay-list field is not optional, but
        it may contain zero bay-info elements.
        """
        return self._bay_list
    @bay_list.setter
    def bay_list(self, val):
        if val != None:
            self.validate('bay_list', val)
        self._bay_list = val
    
    _bay_count = None
    @property
    def bay_count(self):
        """
        Disk bays are the slots into which disks are placed.
        The bays are numbered from 0 to bay-count-1.  Bay 0 is
        the right most bay (when looking at the front of the
        shelf) and bay bay-count-1 is left most.  These bay
        numbers can be used by other commands, including
        storage-shelf-set-led-state.
        """
        return self._bay_count
    @bay_count.setter
    def bay_count(self, val):
        if val != None:
            self.validate('bay_count', val)
        self._bay_count = val
    
    @staticmethod
    def get_api_name():
          return "shelf-bay-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'bay-list',
            'bay-count',
        ]
    
    def describe_properties(self):
        return {
            'bay_list': { 'class': BayInfo, 'is_list': True, 'required': 'required' },
            'bay_count': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
