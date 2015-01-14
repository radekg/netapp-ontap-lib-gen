from netapp.system.system_path_version import SystemPathVersion
from netapp.netapp_object import NetAppObject

class SystemNodeKernelInfo(NetAppObject):
    """
    Diagnostics and firmware details of  a node
    """
    
    _node_name = None
    @property
    def node_name(self):
        """
        Name of the node
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _firmware_info = None
    @property
    def firmware_info(self):
        """
        Firmware path and firmware version
        """
        return self._firmware_info
    @firmware_info.setter
    def firmware_info(self, val):
        if val != None:
            self.validate('firmware_info', val)
        self._firmware_info = val
    
    _compilation_flags = None
    @property
    def compilation_flags(self):
        """
        Displays the verbose output which currently includes the
        compilation flags
        """
        return self._compilation_flags
    @compilation_flags.setter
    def compilation_flags(self, val):
        if val != None:
            self.validate('compilation_flags', val)
        self._compilation_flags = val
    
    _kernel_info = None
    @property
    def kernel_info(self):
        """
        Kernel path and kernel version
        """
        return self._kernel_info
    @kernel_info.setter
    def kernel_info(self, val):
        if val != None:
            self.validate('kernel_info', val)
        self._kernel_info = val
    
    @staticmethod
    def get_api_name():
          return "system-node-kernel-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node-name',
            'firmware-info',
            'compilation-flags',
            'kernel-info',
        ]
    
    def describe_properties(self):
        return {
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'firmware_info': { 'class': SystemPathVersion, 'is_list': True, 'required': 'optional' },
            'compilation_flags': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'kernel_info': { 'class': SystemPathVersion, 'is_list': True, 'required': 'optional' },
        }
