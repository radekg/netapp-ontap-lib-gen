from netapp.netapp_object import NetAppObject

class EshInfo(NetAppObject):
    """
    Information on individual ESH modules in the shelf.
    """
    
    _esh_element_no = None
    @property
    def esh_element_no(self):
        """
        ESH element number of installed ESH module
        """
        return self._esh_element_no
    @esh_element_no.setter
    def esh_element_no(self, val):
        if val != None:
            self.validate('esh_element_no', val)
        self._esh_element_no = val
    
    _esh_is_error = None
    @property
    def esh_is_error(self):
        """
        Indicates whether the ESH module has reported any errors.
        """
        return self._esh_is_error
    @esh_is_error.setter
    def esh_is_error(self, val):
        if val != None:
            self.validate('esh_is_error', val)
        self._esh_is_error = val
    
    @staticmethod
    def get_api_name():
          return "esh-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'esh-element-no',
            'esh-is-error',
        ]
    
    def describe_properties(self):
        return {
            'esh_element_no': { 'class': int, 'is_list': False, 'required': 'required' },
            'esh_is_error': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
