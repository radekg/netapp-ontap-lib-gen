from netapp.netapp_object import NetAppObject

class VmAlignInfo(NetAppObject):
    """
    Information relating to Virtual Machine
    alignment settings on the volume.
    """
    
    _vm_align_sector = None
    @property
    def vm_align_sector(self):
        """
        The Virtual Machine alignment 512 byte sector number.
        All files created with the suffix specified in the
        'vm-align-suffix' input parameter will have zero-filled
        <512 * 'vm-align-sector'> bytes data at the beginning so that
        it's actual data starts at a different offset instead of zero.
        This is done so that the read & writes to such files are
        aligned to WAFL's 4k block boundary
        """
        return self._vm_align_sector
    @vm_align_sector.setter
    def vm_align_sector(self, val):
        if val != None:
            self.validate('vm_align_sector', val)
        self._vm_align_sector = val
    
    _vm_align_suffix = None
    @property
    def vm_align_suffix(self):
        """
        The Virtual Machine alignment suffix. The suffix such as
        '.xyz' is used to identify the files which needs to be aligned.
        See the description for 'vm-align-sector' above for more
        information on this.
        """
        return self._vm_align_suffix
    @vm_align_suffix.setter
    def vm_align_suffix(self, val):
        if val != None:
            self.validate('vm_align_suffix', val)
        self._vm_align_suffix = val
    
    @staticmethod
    def get_api_name():
          return "vm-align-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'vm-align-sector',
            'vm-align-suffix',
        ]
    
    def describe_properties(self):
        return {
            'vm_align_sector': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vm_align_suffix': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
