from netapp.connection import NaConnection
from storage_array_config_summary import StorageArrayConfigSummary # 8 properties
from storage_array_port_stats import StorageArrayPortStats # 13 properties
from storage_array_stats_info import StorageArrayStatsInfo # 6 properties
from arrayfailovertype import Arrayfailovertype # 0 properties
from arrayerrortype import Arrayerrortype # 0 properties
from lunownershipfiltertype import Lunownershipfiltertype # 0 properties
from storage_array_profile import StorageArrayProfile # 16 properties
from storage_array_port_stats_info import StorageArrayPortStatsInfo # 19 properties
from storage_array_port import StorageArrayPort # 9 properties
from connectiontype import Connectiontype # 0 properties
from storage_array_stats_error_info import StorageArrayStatsErrorInfo # 3 properties
from storage_array_error_info import StorageArrayErrorInfo # 3 properties

class StorageArrayConnection(NaConnection):
    
    def storage_array_modify(self, array_name, max_queue_depth=None, vendor=None, is_upgrade_pending=None, prefix=None, lun_queue_depth=None, model=None, options=None):
        """
        Update an array profile with new or changed information.
        
        :param array_name: The name of the array profile to update. (28 chars max)
        
        :param max_queue_depth: The target port queue depth for all target ports on this array.
        
        :param vendor: The name of the array's manufacturer. (8 chars max)
        
        :param is_upgrade_pending: Used to indicate that the specified array will under go an
                upgrade in the near future.
        
        :param prefix: A unique user supplied 4 character code used to refer to this
                array and used in naming the array's LUNs.
        
        :param lun_queue_depth: The queue depth assigned to array LUNs from this array.
        
        :param model: The model of the array. (16 chars max)
        
        :param options: Array profile specific options. (comma separated list of
                name/value pairs) (127 chars max)
        """
        return self.request( "storage-array-modify", {
            'max_queue_depth': [ max_queue_depth, 'max-queue-depth', [ int, 'None' ], False ],
            'vendor': [ vendor, 'vendor', [ basestring, 'None' ], False ],
            'is_upgrade_pending': [ is_upgrade_pending, 'is-upgrade-pending', [ bool, 'None' ], False ],
            'prefix': [ prefix, 'prefix', [ basestring, 'None' ], False ],
            'lun_queue_depth': [ lun_queue_depth, 'lun-queue-depth', [ int, 'None' ], False ],
            'model': [ model, 'model', [ basestring, 'None' ], False ],
            'array_name': [ array_name, 'array-name', [ basestring, 'None' ], False ],
            'options': [ options, 'options', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_array_profile_change_notification(self, is_modify, array_id):
        """
        Signal the changes made in array profile RDB to the D-Blade
        
        :param is_modify: A boolean value which indicates if it's an rdb_modify operation.
                True  - operation is rdb_modify
                False - operation is rdb_create
        
        :param array_id: Primary key (system defined) for the array record.
        """
        return self.request( "storage-array-profile-change-notification", {
            'is_modify': [ is_modify, 'is-modify', [ bool, 'None' ], False ],
            'array_id': [ array_id, 'array-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def storage_array_rename(self, array_name, new_name):
        """
        Rename an array profile
        
        :param array_name: The name of the array profile to update. (28 chars max)
        
        :param new_name: The new name to assign to this array profile. (28 chars max)
        """
        return self.request( "storage-array-rename", {
            'array_name': [ array_name, 'array-name', [ basestring, 'None' ], False ],
            'new_name': [ new_name, 'new-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_array_port_modify(self, wwpn, wwnn, array_name, max_queue_depth=None):
        """
        Update an array port with new or changed information.
        
        :param wwpn: World wide port name of array's target port (64 chars).
        
        :param wwnn: World wide node name of array's target port (64 chars).
        
        :param array_name: The name of the array profile to update. (28 chars max)
        
        :param max_queue_depth: The target port queue depth for this target port.
        """
        return self.request( "storage-array-port-modify", {
            'wwpn': [ wwpn, 'wwpn', [ basestring, 'None' ], False ],
            'wwnn': [ wwnn, 'wwnn', [ basestring, 'None' ], False ],
            'array_name': [ array_name, 'array-name', [ basestring, 'None' ], False ],
            'max_queue_depth': [ max_queue_depth, 'max-queue-depth', [ int, 'None' ], False ],
        }, {
        } )
    
    def storage_array_port_remove(self, wwpn, wwnn, array_id):
        """
        Remove one port from an array profile record
        
        :param wwpn: The WWPN of the array port to remove.
        
        :param wwnn: The WWNN of the array port to remove.
        
        :param array_id: Primary key (system defined) for the array record.
        """
        return self.request( "storage-array-port-remove", {
            'wwpn': [ wwpn, 'wwpn', [ basestring, 'None' ], False ],
            'wwnn': [ wwnn, 'wwnn', [ basestring, 'None' ], False ],
            'array_id': [ array_id, 'array-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def storage_array_port_change_notification(self, wwpn, wwnn, is_modify, array_id):
        """
        Signal the changes made in array port table to the D-Blade
        
        :param wwpn: The WWPN of the array port whose attributes changed
        
        :param wwnn: The WWNN of the array port whose attributes changed
        
        :param is_modify: A boolean value which indicates if it's an rdb_modify operation.
                True  - operation is rdb_modify
                False - operation is rdb_create
        
        :param array_id: Primary key (system defined) for the array record.
        """
        return self.request( "storage-array-port-change-notification", {
            'wwpn': [ wwpn, 'wwpn', [ basestring, 'None' ], False ],
            'wwnn': [ wwnn, 'wwnn', [ basestring, 'None' ], False ],
            'is_modify': [ is_modify, 'is-modify', [ bool, 'None' ], False ],
            'array_id': [ array_id, 'array-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def storage_array_stats_list_info(self):
        """
        Used to get dynamic information about backend arrays.
        """
        return self.request( "storage-array-stats-list-info", {
        }, {
            'array-stat-info': [ StorageArrayStatsInfo, True ],
        } )
    
    def storage_array_profile_sync(self):
        """
        Purge a node's array profile database, thereby
        synchronizing it with the RDB.
        """
        return self.request( "storage-array-profile-sync", {
        }, {
        } )
    
    def storage_array_port_stats_list_info(self):
        """
        return stats for array ports
        """
        return self.request( "storage-array-port-stats-list-info", {
        }, {
            'port-stat-info': [ StorageArrayPortStatsInfo, True ],
        } )
    
    def storage_array_update(self, array_name, vendor=None, network_address=None, firmware=None, prefix=None, new_array_name=None, model=None, options=None):
        """
        Update an array profile with new or changed information.
        Arguments passed in will be used to update the profile.  Arguments not
        passed will keep their existing values.
        
        :param array_name: 28 character string, no spaces
                The name of the array profile to update.
        
        :param vendor: The name of the array's manufacturer. (8 chars)
        
        :param network_address: The I/O address of the array's SNMP management service in dotted-decimal format (for example, "192.168.11.12").
        
        :param firmware: The firmware revision of the array being entered. (64 chars)
        
        :param prefix: A unique 5 character user defined code used to refer to this array.
        
        :param new_array_name: 28 character string, no spaces
                The new name to assign to this array profile.
        
        :param model: The model number of the array. (16 chars)
        
        :param options: Array profile specific options. (comma separated list of name/value pairs) (128 chars)
        """
        return self.request( "storage-array-update", {
            'vendor': [ vendor, 'vendor', [ basestring, 'None' ], False ],
            'network_address': [ network_address, 'network-address', [ basestring, 'None' ], False ],
            'firmware': [ firmware, 'firmware', [ basestring, 'None' ], False ],
            'prefix': [ prefix, 'prefix', [ basestring, 'None' ], False ],
            'new_array_name': [ new_array_name, 'new-array-name', [ basestring, 'None' ], False ],
            'model': [ model, 'model', [ basestring, 'None' ], False ],
            'array_name': [ array_name, 'array-name', [ basestring, 'None' ], False ],
            'options': [ options, 'options', [ basestring, 'None' ], False ],
        }, {
            'array-profile': [ StorageArrayProfile, False ],
        } )
    
    def storage_array_get_config_summary(self, node=None, ownership_type=None):
        """
        Generates a high level summary of array LUN pathing (connectivity)
        information.
        
        :param node: Obtain array LUN pathing information for a specified node.
        
        :param ownership_type: Option that allows the user to select which array LUNs are displayed.
                Valid values for ownership-type are 'assigned', 'unassigned' and 'all'.
                If ownership-type is set to 'assigned' only assigned array LUNs are displayed.
                If ownership-type is set to 'unassigned' only unassigned array LUNs are
                displayed. If ownership-type is set to 'all', all array LUNs are
                displayed. Default: 'all'.
        """
        return self.request( "storage-array-get-config-summary", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'ownership_type': [ ownership_type, 'ownership-type', [ basestring, 'None' ], False ],
        }, {
            'config-summary': [ StorageArrayConfigSummary, True ],
        } )
    
    def storage_array_ports_list_info(self, array_name=None):
        """
        generate a list of online array ports and their associated arrays
        
        :param array_name: When supplied, only port records for the named array are returned. (28 chars)
        """
        return self.request( "storage-array-ports-list-info", {
            'array_name': [ array_name, 'array-name', [ basestring, 'None' ], False ],
        }, {
            'array-ports': [ StorageArrayPort, True ],
        } )
    
    def storage_array_luns_list_info(self, array_name, ownership_type=None):
        """
        Generate a list of array LUNs associated with the named array.
        
        :param array_name: The name of the array profile to list array LUN information for. (28 chars)
        
        :param ownership_type: Option that allows the user to select which array LUNs are displayed.
                Valid values for ownership-type are 'assigned', 'unassigned' and 'all'.
                If ownership-type is set to 'assigned' only assigned array LUNs are displayed.
                If ownership-type is set to 'unassigned' only unassigned array LUNs are
                displayed. If ownership-type is set to 'all', all array LUNs are
                displayed. Default: 'all'.
        """
        return self.request( "storage-array-luns-list-info", {
            'array_name': [ array_name, 'array-name', [ basestring, 'None' ], False ],
            'ownership_type': [ ownership_type, 'ownership-type', [ basestring, 'None' ], False ],
        }, {
            'array-luns': [ DiskDetailInfo, True ],
        } )
    
    def storage_array_list_info(self, array_name=None):
        """
        Retrieves a list of all array profiles known to the controller.
        
        :param array_name: When specified, only the named array profile record will be returned. (28 chars)
        """
        return self.request( "storage-array-list-info", {
            'array_name': [ array_name, 'array-name', [ basestring, 'None' ], False ],
        }, {
            'array-profiles': [ StorageArrayProfile, True ],
        } )
