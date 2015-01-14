from netapp.connection import NaConnection
from storage_disk_info import StorageDiskInfo # 8 properties
from disk_spare_info import DiskSpareInfo # 6 properties
from diskchecksumcompatibility import Diskchecksumcompatibility # 0 properties
from disk_outage_info import DiskOutageInfo # 2 properties
from storage_disk_get_iter_key_td import StorageDiskGetIterKeyTd # 2 properties
from disk_stats_info import DiskStatsInfo # 9 properties
from fw_update_status_info import FwUpdateStatusInfo # 4 properties
from vmdisk_backing_info import VmdiskBackingInfo # 4 properties
from disk_aggregate_info import DiskAggregateInfo # 17 properties
from disk_raid_info import DiskRaidInfo # 12 properties
from disk_ownership_info import DiskOwnershipInfo # 10 properties
from disk_inventory_info import DiskInventoryInfo # 25 properties

class StorageDiskConnection(NaConnection):
    
    def storage_disk_fw_status(self, status_type):
        """
        Based on input, displays:
        The number of disks waiting for firmware update,
        Average firmware update duration per disk in seconds,
        Estimate for background firmware download completion in minutes, or
        Name of disk that cannot be updated.
        
        :param status_type: Possible values:
                1. time-estimate
                2. waiting-disks
                3. average-time
                4. pending-disks
        """
        return self.request( "storage-disk-fw-status", {
            'status_type': [ status_type, 'status-type', [ basestring, 'None' ], False ],
        }, {
            'fw-update-status': [ FwUpdateStatusInfo, True ],
        } )
    
    def storage_disk_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Disk enumeration ZAPI.  Get disk information about one or
        more disks, from the Storage Subsystem.  Currently only the
        Data ONTAP Cluster-Mode iterator APIs support filtering of
        output, to constrain the disks that are included in the return
        list, and/or what information is returned about each disk. The
        default is to return all information about all disks in the
        cluster.  That list may be reduced using the 'query' input
        element. For example, the return list may include only
        (1) Disks visible to a particular cluster node "nodeA",
        e.g., "query.disk-paths.disk-name=nodeA:*"
        (2) A particular disk visible to a particular node,
        e.g., "query.disk-paths.node=nodeA:6a.01".
        (3) A disk with a particular unique id, e.g.,
        "query.disk-uid=20000000:87A9652B:00000000:00000000:00000000:00000000:00000000:00000000:00000000:00000000"
        (4) Disks with a name that matches a certain wildcard pattern,
        e.g., "query.disk-paths.disk-name=*:6a*".
        (5) Disks assigned to a particular node. e.g.,
        "query.disk-ownership-info.home-node-id=1252487" or
        "query.disk-ownership-info.home-node-name=nodeA".
        (6) Some subset of disks in the cluster or visible to a
        particular node in the cluster.
        If 'desired-attributes' is included, then only those data
        specified by in 'desired-attributes' are returned for each disk.
        For the Data ONTAP 7-Mode API, since filtering based upon
        'query' and 'desired-attributes' is not yet supported, the
        behavior is currently to return all available information about
        all disks visible to the local node.
        If there is badly formed input or an invalid input value is
        specified, then EINVALIDINPUTERROR is returned.  If there is
        some internal error which prevents processing of this request,
        then EINTERNALERROR is returned.
        
        :param max_records: The maximum number of records to return to the caller per
                iteration.  The default is 2000 for the Data ONTAP Cluster-
                Mode and 200 for other Data ONTAP 7-mode and D-blade calls.
                If the total number of records exceeds either the
                'max-records' supplied, or the number the system is capable
                of returning at one time, then storage-disk-get-iter must
                be called multiple times to get all the records.  The
                'num-records' output field informs the caller how many
                records are returned by a single iterative call to
                storage-disk-get-iter.
        
        :param query: May be used to express which disks to include in the return
                list. If omitted, then all disks are returned.  If the input
                query is badly formed, then EINVALIDINPUTERROR is returned.
                If there are no disks which match the input query, then there
                is no error.  However, no disk records are returned.
        
        :param tag: This indicates where to continue iteration. A first invocation
                would normally omit this, to indicate to start iteration with
                the first disk. If multiple invocations are required to fetch
                all disk records, then each successive call would set 'tag' to
                the 'next-tag' value from the prior invocation.  If an invalid
                value is specified, then EINVAIDINPUTERROR is returned.
        
        :param desired_attributes: May be used to express which data are returned for each disk.
                If omitted, then all available data are returned.
        """
        return self.request( "storage-disk-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ StorageDiskInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ StorageDiskInfo, 'None' ], False ],
        }, {
            'attributes-list': [ StorageDiskInfo, True ],
        } )
