from netapp.system.system_api_element_info import SystemApiElementInfo
from netapp.netapp_object import NetAppObject

class SystemApiEntryInfo(NetAppObject):
    """
    list of api names and their elements
    """
    
    _name = None
    @property
    def name(self):
        """
        api name
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _api_elements = None
    @property
    def api_elements(self):
        """
        list of api elements
        """
        return self._api_elements
    @api_elements.setter
    def api_elements(self, val):
        if val != None:
            self.validate('api_elements', val)
        self._api_elements = val
    
    @staticmethod
    def get_api_name():
          return "system-api-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'api-elements',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'api_elements': { 'class': SystemApiElementInfo, 'is_list': True, 'required': 'required' },
        }
