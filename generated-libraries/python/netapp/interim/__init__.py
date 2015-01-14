from netapp.connection import NaConnection
from cluster_serial_number import ClusterSerialNumber # 0 properties
from interim_license_cluster_info import InterimLicenseClusterInfo # 6 properties
from interim_licensed_feature import InterimLicensedFeature # 0 properties
from license_code import LicenseCode # 0 properties

class InterimConnection(NaConnection):
    
    def interim_license_remove(self, service):
        """
        Disable license for a Data ONTAP service. This API will be
        removed in future Data ONTAP version.
        This API is deprecated in Data ONTAP Cluster-Mode 8.2 and later,
        and will return EAPINOTIMPLEMENTED. Use license-v2-delete
        instead.
        
        :param service: Feature
                Possible values:
                <ul>
                <li> "base"                - Base License w/cluster size limit
                (nodes),
                <li> "mirror"              - Mirror License,
                <li> "flexvol_hpo"         - FlexVol HPO License,
                <li> "cifs"                - CIFS License,
                <li> "snaprestore"         - SnapRestore License,
                <li> "flexclone"           - FlexClone License,
                <li> "nfs"                 - NFS License,
                <li> "snapmirror_dp"       - SnapMirror Data Protection
                License,
                <li> "iscsi"               - iSCSI License,
                <li> "striped_volume"      - Striped Volume License,
                <li> "fcp"                 - FCP License,
                <li> "snapmanager_suite"   - SnapManager Suite License,
                <li> "spa"                 - SPA License,
                <li> "insight_balance"     - OnCommand Balance
                </ul>
        """
        return self.request( "interim-license-remove", {
            'service': [ service, 'service', [ basestring, 'interim-licensed-feature' ], False ],
        }, {
        } )
    
    def interim_license_set(self, code):
        """
        Enable license for a Data ONTAP service. This API will be removed
        in future Data ONTAP version.
        This API is deprecated in Data ONTAP Cluster-Mode 8.2 and later,
        and will return EAPINOTIMPLEMENTED. Use license-v2-add instead
        
        :param code: Data ONTAP Cluster-Mode service/feature. 14 Uppercase Alpha only
                characters.
        """
        return self.request( "interim-license-set", {
            'code': [ code, 'code', [ basestring, 'license-code' ], False ],
        }, {
        } )
    
    def interim_license_list_get(self):
        """
        Returns infomation for cluster mode licenses. This API will be
        removed in future Data ONTAP version.
        This API is deprecated in Data ONTAP Cluster-Mode 8.2 and later,
        and will return EAPINOTIMPLEMENTED. Use license-v2-list-info
        instead.
        """
        return self.request( "interim-license-list-get", {
        }, {
            'licenses': [ InterimLicenseClusterInfo, True ],
        } )
