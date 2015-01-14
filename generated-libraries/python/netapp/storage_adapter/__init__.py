from netapp.connection import NaConnection
from sas_qsfp_cable_info import SasQsfpCableInfo # 7 properties
from adapter_sff_info import AdapterSffInfo # 4 properties
from adapter_sfp_info import AdapterSfpInfo # 4 properties
from adapter_bar_info import AdapterBarInfo # 3 properties
from expander_phy_state_info import ExpanderPhyStateInfo # 4 properties
from adapter_fc_info import AdapterFcInfo # 20 properties
from adapter_detail_info import AdapterDetailInfo # 6 properties
from phy_state_info import PhyStateInfo # 3 properties
from adapter_sas_info import AdapterSasInfo # 22 properties
from adapter_parallel_scsi_info import AdapterParallelScsiInfo # 5 properties
from sas_adapter_expander_phy_state_info import SasAdapterExpanderPhyStateInfo # 2 properties
from adapter_name_elem import AdapterNameElem # 2 properties

class StorageAdapterConnection(NaConnection):
    
    def storage_adapter_get_adapter_list(self, node_name=None):
        """
        Get the list of adapters present on this system.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. If node-name is not specified
                when the request is sent to Admin VserverLIF, then all
                matching adapters in the cluster will be returned.
                This is the storage system name the command will
                be executed on.
        """
        return self.request( "storage-adapter-get-adapter-list", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
        }, {
            'adapter-list': [ AdapterNameElem, True ],
        } )
    
    def storage_adapter_enable_adapter(self, node_name, adapter_name):
        """
        Enables specified host adapter.
        I/O traffic can be issued on the adapter.
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. This is the storage system name
                the command will be executed on.
        
        :param adapter_name: The adapter name is either a slot number, or, if a port letter
                is also present, a slot number and port letter concatenated into
                a single name -- for example, "8a" or "11b".  If adapter-name
                is not supplied, the command will return EAPIMISSINGARGUMENT.
        """
        return self.request( "storage-adapter-enable-adapter", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_adapter_get_adapter_info(self, adapter_name, node_name=None):
        """
        Display the information about a specified host adapter.
        The information is displayed base on the controller interface type.
        ATA, Parallel SCSI, SAS, FC.
        
        :param adapter_name: The adapter name is either a slot number, or, if a port letter
                is also presented, a slot number and port letter concatenated into
                a single name -- for example, "8a" or "11b".
        
        :param node_name: This field is only valid when the request is sent to
                the Admin Vserver LIF. If node-name is not specified
                when the request is sent to Admin VserverLIF, then all
                matching adapters in the cluster will be returned.
                This is the storage system name the command will
                be executed on.
        """
        return self.request( "storage-adapter-get-adapter-info", {
            'node_name': [ node_name, 'node-name', [ basestring, 'None' ], False ],
            'adapter_name': [ adapter_name, 'adapter-name', [ basestring, 'None' ], False ],
        }, {
            'adapter-details': [ AdapterDetailInfo, True ],
        } )
