from netapp.netapp_object import NetAppObject

class HoleRangeInfo(NetAppObject):
    """
    The hole start need not be an integral multiple of the
    block size. It will be rounded up to the start of the
    next block. The hole-size does not need to be the
    size of a block. It will be rounded down to the
    beginning of the block. It is possible that after the
    adjustments there is nothing to punch. That is ok and
    will be treated as success. Note that presently in WAFL
    small files are entirely within the inode. It is possible
    to "hole punch" those however nothing happens. The data
    is left alone. Considering the use case fot this ZAPI
    and the amount of effort to code the "correct" solution
    this is deemed an acceptable condition. If the file is
    vm-aligned then the range chosen to hole-punch could be
    rounded down by a block to ensure that we don't punch
    block containing valid user data.
    """
    
    _hole_size = None
    @property
    def hole_size(self):
        """
        Size of the hole in terms of bytes. If punching
        a hole WAFL presently limits this value to 4MB.
        Range :		[0..2^63-1]
        """
        return self._hole_size
    @hole_size.setter
    def hole_size(self, val):
        if val != None:
            self.validate('hole_size', val)
        self._hole_size = val
    
    _hole_start = None
    @property
    def hole_start(self):
        """
        Starting offset of the hole.
        Range :		[0..2^63-1]
        """
        return self._hole_start
    @hole_start.setter
    def hole_start(self, val):
        if val != None:
            self.validate('hole_start', val)
        self._hole_start = val
    
    @staticmethod
    def get_api_name():
          return "hole-range-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'hole-size',
            'hole-start',
        ]
    
    def describe_properties(self):
        return {
            'hole_size': { 'class': int, 'is_list': False, 'required': 'required' },
            'hole_start': { 'class': int, 'is_list': False, 'required': 'required' },
        }
