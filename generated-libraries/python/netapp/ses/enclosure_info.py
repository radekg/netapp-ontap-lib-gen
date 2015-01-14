from netapp.ses.module_info import ModuleInfo
from netapp.netapp_object import NetAppObject

class EnclosureInfo(NetAppObject):
    """
    Information on the enclosure type. This information will be
    presented for ESH and SAS shelves only.
    """
    
    _module_list = None
    @property
    def module_list(self):
        """
        Information on the enclosure modules.
        """
        return self._module_list
    @module_list.setter
    def module_list(self, val):
        if val != None:
            self.validate('module_list', val)
        self._module_list = val
    
    _enclosure_type = None
    @property
    def enclosure_type(self):
        """
        Enclosure type. Possible values:
        "sas_expander_module", "embedded_switching_hub".
        """
        return self._enclosure_type
    @enclosure_type.setter
    def enclosure_type(self, val):
        if val != None:
            self.validate('enclosure_type', val)
        self._enclosure_type = val
    
    @staticmethod
    def get_api_name():
          return "enclosure-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'module-list',
            'enclosure-type',
        ]
    
    def describe_properties(self):
        return {
            'module_list': { 'class': ModuleInfo, 'is_list': True, 'required': 'required' },
            'enclosure_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
