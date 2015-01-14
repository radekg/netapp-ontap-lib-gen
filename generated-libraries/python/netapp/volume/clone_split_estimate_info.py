from netapp.netapp_object import NetAppObject

class CloneSplitEstimateInfo(NetAppObject):
    """
    Estimate information about a future clone split.
    """
    
    _estimate_blocks = None
    @property
    def estimate_blocks(self):
        """
        The estimated number of 4kb blocks required to
        perform the volume clone split.
        """
        return self._estimate_blocks
    @estimate_blocks.setter
    def estimate_blocks(self, val):
        if val != None:
            self.validate('estimate_blocks', val)
        self._estimate_blocks = val
    
    @staticmethod
    def get_api_name():
          return "clone-split-estimate-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'estimate-blocks',
        ]
    
    def describe_properties(self):
        return {
            'estimate_blocks': { 'class': int, 'is_list': False, 'required': 'required' },
        }
