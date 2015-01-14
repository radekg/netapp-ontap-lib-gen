from netapp.netapp_object import NetAppObject

class SystemApiInfo(NetAppObject):
    """
    api information
    """
    
    _name = None
    @property
    def name(self):
        """
        name of api
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _license = None
    @property
    def license(self):
        """
        license needed if any
        """
        return self._license
    @license.setter
    def license(self, val):
        if val != None:
            self.validate('license', val)
        self._license = val
    
    _is_streaming = None
    @property
    def is_streaming(self):
        """
        does api stream data?
        """
        return self._is_streaming
    @is_streaming.setter
    def is_streaming(self, val):
        if val != None:
            self.validate('is_streaming', val)
        self._is_streaming = val
    
    @staticmethod
    def get_api_name():
          return "system-api-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'license',
            'is-streaming',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'license': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_streaming': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
