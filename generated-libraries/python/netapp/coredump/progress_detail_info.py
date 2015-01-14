from netapp.netapp_object import NetAppObject

class ProgressDetailInfo(NetAppObject):
    """
    Savecore progress info
    """
    
    _saved_blocks = None
    @property
    def saved_blocks(self):
        """
        Number of blocks that have already been saved
        in the core that is being saved
        """
        return self._saved_blocks
    @saved_blocks.setter
    def saved_blocks(self, val):
        if val != None:
            self.validate('saved_blocks', val)
        self._saved_blocks = val
    
    _corename = None
    @property
    def corename(self):
        """
        Name of the core being saved
        """
        return self._corename
    @corename.setter
    def corename(self, val):
        if val != None:
            self.validate('corename', val)
        self._corename = val
    
    _total_blocks = None
    @property
    def total_blocks(self):
        """
        Total number of blocks of data in the core
        that is being saved.
        """
        return self._total_blocks
    @total_blocks.setter
    def total_blocks(self, val):
        if val != None:
            self.validate('total_blocks', val)
        self._total_blocks = val
    
    @staticmethod
    def get_api_name():
          return "progress-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'saved-blocks',
            'corename',
            'total-blocks',
        ]
    
    def describe_properties(self):
        return {
            'saved_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
            'corename': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'total_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
        }
