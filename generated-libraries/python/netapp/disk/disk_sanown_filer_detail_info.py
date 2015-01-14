from netapp.netapp_object import NetAppObject

class DiskSanownFilerDetailInfo(NetAppObject):
    """
    Disk sanown filer information.
    """
    
    _filer_id = None
    @property
    def filer_id(self):
        """
        ID (NVRAM ID) of owner.
        Range : [0..2^32-1].
        """
        return self._filer_id
    @filer_id.setter
    def filer_id(self, val):
        if val != None:
            self.validate('filer_id', val)
        self._filer_id = val
    
    _filer_name = None
    @property
    def filer_name(self):
        """
        Name of the filer. If the filer name hasn't
        been written to the disks, this will not be returned.
        """
        return self._filer_name
    @filer_name.setter
    def filer_name(self, val):
        if val != None:
            self.validate('filer_name', val)
        self._filer_name = val
    
    @staticmethod
    def get_api_name():
          return "disk-sanown-filer-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'filer-id',
            'filer-name',
        ]
    
    def describe_properties(self):
        return {
            'filer_id': { 'class': int, 'is_list': False, 'required': 'required' },
            'filer_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
