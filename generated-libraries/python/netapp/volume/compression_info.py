from netapp.netapp_object import NetAppObject

class CompressionInfo(NetAppObject):
    """
    Note that the use of this element is deprecated,
    refer to the 'dense-status' element for compression
    status instead.
    """
    
    _is_compression_enabled = None
    @property
    def is_compression_enabled(self):
        """
        Note that the use of this field is deprecated,
        refer to the 'is-compression-enabled' field in
        the 'dense-status' element instead.
        """
        return self._is_compression_enabled
    @is_compression_enabled.setter
    def is_compression_enabled(self, val):
        if val != None:
            self.validate('is_compression_enabled', val)
        self._is_compression_enabled = val
    
    @staticmethod
    def get_api_name():
          return "compression-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-compression-enabled',
        ]
    
    def describe_properties(self):
        return {
            'is_compression_enabled': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
