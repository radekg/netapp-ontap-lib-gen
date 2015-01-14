from netapp.connection import NaConnection
from storage_error_info import StorageErrorInfo # 8 properties
from disk_path_info import DiskPathInfo # 32 properties
from storage_initiator_load_info import StorageInitiatorLoadInfo # 9 properties
from storage_initiator_path_info import StorageInitiatorPathInfo # 20 properties
from disk_name import DiskName # 0 properties

class StorageInitiatorConnection(NaConnection):
    
    def storage_initiator_path_resume(self, node, initiator, target_wwpn, lun_number):
        """
        Resumes I/O to array LUN on a path that was previously quiesced.
        Resuming I/O to a non-quiesced array LUN is a no-op and not an error.
        
        :param node: The node name on which the resume is issued
        
        :param initiator: The initiator port of the path that I/O will be resumed to.
        
        :param target_wwpn: The array target port of the path that I/O will be resumed to.
                World wide port number has to be specified without colons.
        
        :param lun_number: LU number.
                Range: [0..65535]
        """
        return self.request( "storage-initiator-path-resume", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
            'target_wwpn': [ target_wwpn, 'target-wwpn', [ basestring, 'None' ], False ],
            'lun_number': [ lun_number, 'lun-number', [ int, 'None' ], False ],
        }, {
        } )
    
    def storage_initiator_errors_list_info(self, disk_name=None, array_name=None):
        """
        Lists all known disk/configuration errors associated with an array
        or shelves acting like array.
        
        :param disk_name: The name of the disk or array lun to list error information
                for.  If not specified, all errors for all disks/array LUNs
                will be returned.
        
        :param array_name: The name of the array to list error information for. (28 chars)
        """
        return self.request( "storage-initiator-errors-list-info", {
            'disk_name': [ disk_name, 'disk-name', [ basestring, 'None' ], False ],
            'array_name': [ array_name, 'array-name', [ basestring, 'None' ], False ],
        }, {
            'errors': [ StorageErrorInfo, True ],
        } )
    
    def storage_initiator_path_list_info(self, node=None):
        """
        Returns information and statistics on all known paths to
        back end storage.
        
        :param node: Obtain back end storage path statistics for this node.
        """
        return self.request( "storage-initiator-path-list-info", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
            'path-info': [ StorageInitiatorPathInfo, True ],
        } )
    
    def storage_initiator_get_load(self, node=None, port=None):
        """
        Gets disk I/O rates for a given fibre channel initiator
        port or for all initiator ports if no port is specified.
        The term disk refers to an array LUN, actual disk, or
        solid state device.
        
        :param node: Obtain disk I/O rates for initiator ports on the
                specified node.
        
        :param port: Port to show load on, e.g. 0a.
        """
        return self.request( "storage-initiator-get-load", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'port': [ port, 'port', [ basestring, 'None' ], False ],
        }, {
            'load-info': [ StorageInitiatorLoadInfo, True ],
        } )
    
    def storage_initiator_disk_path_list_info(self, disk_name=None):
        """
        Returns path information and statistics for a given disk or all disks.
        We use the word disk to refer to an array lun, real disk, or Solid State Device
        
        :param disk_name: The name of the disk to list path information
                for.  If not supplied all paths to all attached targets
                are returned.
        """
        return self.request( "storage-initiator-disk-path-list-info", {
            'disk_name': [ disk_name, 'disk-name', [ basestring, 'None' ], False ],
        }, {
            'disk-path-info': [ DiskPathInfo, True ],
        } )
    
    def storage_initiator_path_quiesce(self, node, initiator, target_wwpn, lun_number):
        """
        Quiesces an array LUN on a path.
        A quiesced array LUN will not be sent I/O on the specified path.
        
        :param node: The node name on which the quiesce is issued
        
        :param initiator: The initiator port of the path that I/O will be quiesced on.
        
        :param target_wwpn: The array target port of the path that I/O will be quiesced on.
                World wide port number has to be specified without colons.
        
        :param lun_number: LU number.
                Range: [0..65535]
        """
        return self.request( "storage-initiator-path-quiesce", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'initiator': [ initiator, 'initiator', [ basestring, 'None' ], False ],
            'target_wwpn': [ target_wwpn, 'target-wwpn', [ basestring, 'None' ], False ],
            'lun_number': [ lun_number, 'lun-number', [ int, 'None' ], False ],
        }, {
        } )
    
    def storage_initiator_balance(self, node):
        """
        Balances primary/secondary array LUN paths across available
        initiator ports based on I/O load.
        
        :param node: node to balance initiator ports on
        """
        return self.request( "storage-initiator-balance", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
        }, {
        } )
