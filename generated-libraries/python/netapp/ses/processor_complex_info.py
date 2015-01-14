from netapp.netapp_object import NetAppObject

class ProcessorComplexInfo(NetAppObject):
    """
    Available information on the processor complex modules (PCMs)
    in the shelf.
    """
    
    _is_pcm_element_not_installed = None
    @property
    def is_pcm_element_not_installed(self):
        """
        Indicates if PCM element has been installed. Will
        be present only if the element is not installed, in
        which case no further information will be provided.
        """
        return self._is_pcm_element_not_installed
    @is_pcm_element_not_installed.setter
    def is_pcm_element_not_installed(self, val):
        if val != None:
            self.validate('is_pcm_element_not_installed', val)
        self._is_pcm_element_not_installed = val
    
    _pcm_element_no = None
    @property
    def pcm_element_no(self):
        """
        PCM element number
        """
        return self._pcm_element_no
    @pcm_element_no.setter
    def pcm_element_no(self, val):
        if val != None:
            self.validate('pcm_element_no', val)
        self._pcm_element_no = val
    
    _is_pcm_element_error = None
    @property
    def is_pcm_element_error(self):
        """
        Indicates if there has been a failure in the PCM.
        Will not be present if a PCM element is not installed.
        """
        return self._is_pcm_element_error
    @is_pcm_element_error.setter
    def is_pcm_element_error(self, val):
        if val != None:
            self.validate('is_pcm_element_error', val)
        self._is_pcm_element_error = val
    
    @staticmethod
    def get_api_name():
          return "processor-complex-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-pcm-element-not-installed',
            'pcm-element-no',
            'is-pcm-element-error',
        ]
    
    def describe_properties(self):
        return {
            'is_pcm_element_not_installed': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'pcm_element_no': { 'class': int, 'is_list': False, 'required': 'required' },
            'is_pcm_element_error': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
