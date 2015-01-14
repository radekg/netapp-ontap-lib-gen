from netapp.storage_adapter.adapter_fc_info import AdapterFcInfo
from netapp.storage_adapter.adapter_parallel_scsi_info import AdapterParallelScsiInfo
from netapp.storage_adapter.adapter_sas_info import AdapterSasInfo
from netapp.netapp_object import NetAppObject

class AdapterDetailInfo(NetAppObject):
    """
    Detailed information for specific adapter.
    Display different info base on the type of adapter.
    """
    
    _adapter_fc = None
    @property
    def adapter_fc(self):
        """
        Information for fc (Fibre Channel) adapter.
        """
        return self._adapter_fc
    @adapter_fc.setter
    def adapter_fc(self, val):
        if val != None:
            self.validate('adapter_fc', val)
        self._adapter_fc = val
    
    _adapter_type = None
    @property
    def adapter_type(self):
        """
        Type of adapter present in the system.
        Possible values: "ADT_IF_ATA", "ADT_IF_PARALLEL_SCSI",
        "ADT_IF_SAS", "ADT_IF_FC".
        """
        return self._adapter_type
    @adapter_type.setter
    def adapter_type(self, val):
        if val != None:
            self.validate('adapter_type', val)
        self._adapter_type = val
    
    _adapter_parallel_scsi = None
    @property
    def adapter_parallel_scsi(self):
        """
        Information for parallel SCSI adapter.
        """
        return self._adapter_parallel_scsi
    @adapter_parallel_scsi.setter
    def adapter_parallel_scsi(self, val):
        if val != None:
            self.validate('adapter_parallel_scsi', val)
        self._adapter_parallel_scsi = val
    
    _adapter_sas = None
    @property
    def adapter_sas(self):
        """
        Information for sas (serial attached SCSI) adapter.
        """
        return self._adapter_sas
    @adapter_sas.setter
    def adapter_sas(self, val):
        if val != None:
            self.validate('adapter_sas', val)
        self._adapter_sas = val
    
    _node_name = None
    @property
    def node_name(self):
        """
        This field is only valid when the request is sent to
        the Admin Vserver LIF, in which case it is the
        storage system name.
        """
        return self._node_name
    @node_name.setter
    def node_name(self, val):
        if val != None:
            self.validate('node_name', val)
        self._node_name = val
    
    _adapter_name = None
    @property
    def adapter_name(self):
        """
        Adapter port name, which is adapter slot number and, if presented,
        the port letter designator together. Examples are 8a, 11b.
        Note that a physical adapter may contain multiple ports.
        """
        return self._adapter_name
    @adapter_name.setter
    def adapter_name(self, val):
        if val != None:
            self.validate('adapter_name', val)
        self._adapter_name = val
    
    @staticmethod
    def get_api_name():
          return "adapter-detail-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'adapter-fc',
            'adapter-type',
            'adapter-parallel-scsi',
            'adapter-sas',
            'node-name',
            'adapter-name',
        ]
    
    def describe_properties(self):
        return {
            'adapter_fc': { 'class': AdapterFcInfo, 'is_list': False, 'required': 'optional' },
            'adapter_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'adapter_parallel_scsi': { 'class': AdapterParallelScsiInfo, 'is_list': False, 'required': 'optional' },
            'adapter_sas': { 'class': AdapterSasInfo, 'is_list': False, 'required': 'optional' },
            'node_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'adapter_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
