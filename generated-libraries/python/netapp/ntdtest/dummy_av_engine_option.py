from netapp.netapp_object import NetAppObject

class DummyAvEngineOption(NetAppObject):
    """
    AV engine options
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _decompression_layers_limit = None
    @property
    def decompression_layers_limit(self):
        """
        Generic/Dummy Field 3
        Attributes: required-for-create, modifiable
        """
        return self._decompression_layers_limit
    @decompression_layers_limit.setter
    def decompression_layers_limit(self, val):
        if val != None:
            self.validate('decompression_layers_limit', val)
        self._decompression_layers_limit = val
    
    _is_spyware_enabled = None
    @property
    def is_spyware_enabled(self):
        """
        Generic/Dummy Field 5
        Attributes: required-for-create, modifiable
        """
        return self._is_spyware_enabled
    @is_spyware_enabled.setter
    def is_spyware_enabled(self, val):
        if val != None:
            self.validate('is_spyware_enabled', val)
        self._is_spyware_enabled = val
    
    _decompressed_file_size_limit = None
    @property
    def decompressed_file_size_limit(self):
        """
        Generic/Dummy Field 2
        Attributes: required-for-create, modifiable
        """
        return self._decompressed_file_size_limit
    @decompressed_file_size_limit.setter
    def decompressed_file_size_limit(self, val):
        if val != None:
            self.validate('decompressed_file_size_limit', val)
        self._decompressed_file_size_limit = val
    
    _decompressed_file_count_limit = None
    @property
    def decompressed_file_count_limit(self):
        """
        Generic/Dummy Field 1
        Attributes: required-for-create, modifiable
        """
        return self._decompressed_file_count_limit
    @decompressed_file_count_limit.setter
    def decompressed_file_count_limit(self, val):
        if val != None:
            self.validate('decompressed_file_count_limit', val)
        self._decompressed_file_count_limit = val
    
    _decompression_size_factor = None
    @property
    def decompression_size_factor(self):
        """
        Generic/Dummy Field 4
        Attributes: required-for-create, modifiable
        """
        return self._decompression_size_factor
    @decompression_size_factor.setter
    def decompression_size_factor(self, val):
        if val != None:
            self.validate('decompression_size_factor', val)
        self._decompression_size_factor = val
    
    @staticmethod
    def get_api_name():
          return "dummy-av-engine-option"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'decompression-layers-limit',
            'is-spyware-enabled',
            'decompressed-file-size-limit',
            'decompressed-file-count-limit',
            'decompression-size-factor',
        ]
    
    def describe_properties(self):
        return {
            'decompression_layers_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_spyware_enabled': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'decompressed_file_size_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'decompressed_file_count_limit': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'decompression_size_factor': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
