from netapp.system.system_api_element_info import SystemApiElementInfo
from netapp.netapp_object import NetAppObject

class SystemApiTypeEntryInfo(NetAppObject):
    """
    list of type names and their elements
    """
    
    _name = None
    @property
    def name(self):
        """
        type name
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _type_elements = None
    @property
    def type_elements(self):
        """
        list of type elements
        """
        return self._type_elements
    @type_elements.setter
    def type_elements(self, val):
        if val != None:
            self.validate('type_elements', val)
        self._type_elements = val
    
    @staticmethod
    def get_api_name():
          return "system-api-type-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
            'type-elements',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'type_elements': { 'class': SystemApiElementInfo, 'is_list': True, 'required': 'required' },
        }
