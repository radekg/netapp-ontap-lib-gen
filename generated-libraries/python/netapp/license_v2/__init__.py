from netapp.connection import NaConnection
from license_v2_info import LicenseV2Info # 10 properties
from license_type import LicenseType # 0 properties
from licensed_method import LicensedMethod # 0 properties
from license_v2_type import LicenseV2Type # 0 properties
from license_v2_added import LicenseV2Added # 7 properties
from license_v2_cleanup import LicenseV2Cleanup # 4 properties
from license_op_status import LicenseOpStatus # 0 properties
from license_v2_result import LicenseV2Result # 3 properties
from license_v2_op_status import LicenseV2OpStatus # 0 properties
from node_serial_number import NodeSerialNumber # 0 properties
from license_v2_status_info import LicenseV2StatusInfo # 4 properties
from licensed_package import LicensedPackage # 0 properties

class LicenseV2Connection(NaConnection):
    
    def license_v2_list_info(self):
        """
        Returns infomation for DATA ONTAP licenses.
        """
        return self.request( "license-v2-list-info", {
        }, {
            'licenses': [ LicenseV2Info, True ],
        } )
    
    def license_v2_delete(self, package, serial_number=None):
        """
        Removes license for a Data ONTAP service.
        
        :param package: Package
                Possible values:
                <ul>
                <li> "base"                - Cluster Base License,
                <li> "nfs"                 - NFS License,
                <li> "cifs"                - CIFS License,
                <li> "iscsi"               - iSCSI License,
                <li> "fcp"                 - FCP License,
                <li> "cdmi"                - CDMI License,
                <li> "snaprestore"         - SnapRestore License,
                <li> "snapmirror"          - SnapMirror License,
                <li> "flexclone"           - FlexClone License,
                <li> "snapvault"           - SnapVault License,
                <li> "snaplock"            - SnapLock License,
                <li> "snapmanagersuite"    - SnapManagerSuite License,
                <li> "snapprotectapps"     - SnapProtectApp License,
                <li> "v_storageattach"     - Virtual Attached Storage License
                </ul>
        
        :param serial_number: Serial number of the node associated with the license. If this
                parameter is not provided, the default serial number used is the
                cluster serial number.
        """
        return self.request( "license-v2-delete", {
            'serial_number': [ serial_number, 'serial-number', [ basestring, 'node-serial-number' ], False ],
            'package': [ package, 'package', [ basestring, 'licensed-package' ], False ],
        }, {
        } )
    
    def license_v2_delete_unused(self):
        """
        Remove licenses that have no controller affiliation in the cluster.
        """
        return self.request( "license-v2-delete-unused", {
        }, {
        } )
    
    def license_v2_status_list_info(self):
        """
        Returns license status information for cluster mode packages.
        """
        return self.request( "license-v2-status-list-info", {
        }, {
            'license-v2-status': [ LicenseV2StatusInfo, True ],
        } )
    
    def license_v2_cleanup_list_info(self):
        """
        Returns licenses that can be cleaned up. A license can be cleaned up if it's
        a demo license and its expiration time has passed (expired), or if it is a license
        for a controller that is no longer part of a cluster (unused). One can
        use the cleanup apis to remove these licenses together, or alternatively, they
        can use the standard license-remove api to remove them one at a time.
        """
        return self.request( "license-v2-cleanup-list-info", {
        }, {
            'licenses': [ LicenseV2Cleanup, True ],
        } )
    
    def license_v2_add(self, codes):
        """
        Add license for a Data ONTAP service.
        
        :param codes: Data ONTAP Cluster-Mode service/feature. 24 or 48 uppercase alpha
                only characters.
        """
        return self.request( "license-v2-add", {
            'codes': [ codes, 'codes', [ basestring, 'license-code-v2' ], True ],
        }, {
            'license-v2-success-list': [ LicenseV2Added, True ],
            'license-v2-failure-list': [ LicenseV2Result, True ],
        } )
    
    def license_v2_delete_expired(self):
        """
        Remove licenses that have expired in the cluster.
        """
        return self.request( "license-v2-delete-expired", {
        }, {
        } )
