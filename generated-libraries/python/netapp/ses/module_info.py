from netapp.netapp_object import NetAppObject

class ModuleInfo(NetAppObject):
    """
    Shelf enclosure module info.
    """
    
    _is_module_error = None
    @property
    def is_module_error(self):
        """
        Indicated whether this module has encountered an error.
        """
        return self._is_module_error
    @is_module_error.setter
    def is_module_error(self, val):
        if val != None:
            self.validate('is_module_error', val)
        self._is_module_error = val
    
    _is_sas_expander_master_module = None
    @property
    def is_sas_expander_master_module(self):
        """
        When the value of enclosure-type field of
        enclosure-type-info is sas-expander-module, then this
        field indicates whether this module is the SAS expander
        master module. This field will only be present for
        sas-expander-module values.
        """
        return self._is_sas_expander_master_module
    @is_sas_expander_master_module.setter
    def is_sas_expander_master_module(self, val):
        if val != None:
            self.validate('is_sas_expander_master_module', val)
        self._is_sas_expander_master_module = val
    
    _module_number = None
    @property
    def module_number(self):
        """
        shelf module number.
        """
        return self._module_number
    @module_number.setter
    def module_number(self, val):
        if val != None:
            self.validate('module_number', val)
        self._module_number = val
    
    @staticmethod
    def get_api_name():
          return "module-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-module-error',
            'is-sas-expander-master-module',
            'module-number',
        ]
    
    def describe_properties(self):
        return {
            'is_module_error': { 'class': bool, 'is_list': False, 'required': 'required' },
            'is_sas_expander_master_module': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'module_number': { 'class': int, 'is_list': False, 'required': 'required' },
        }
