from netapp.connection import NaConnection
from storage_import_stats_info import StorageImportStatsInfo # 10 properties

class StorageImportConnection(NaConnection):
    
    def storage_import_unbind(self, target_lun_path, vserver_name=None):
        """
        Unbind the import of data to the specified Data ONTAP(R) LUN
        This d-blade ZAPI is for internal use only, and expected
        to be removed in future release.
        
        :param target_lun_path: Data ONTAP(R) LUN Path
                For example, /vol/vol1/qtree1/lun1
        
        :param vserver_name: The name of the vserver hosting the target LUN path.
        """
        return self.request( "storage-import-unbind", {
            'target_lun_path': [ target_lun_path, 'target-lun-path', [ basestring, 'None' ], False ],
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_import_verify(self, target_lun_path, target_volume_dsid=None, target_qtree_name=None, vserver_name=None, target_vdisk_name=None):
        """
        Verify the data imported to the specified Data ONTAP(R) LUN
        This d-blade ZAPI is for internal use only, and expected
        to be removed in future release.
        
        :param target_lun_path: Data ONTAP(R) LUN Path
                For example, /vol/vol1/qtree1/lun1
        
        :param target_volume_dsid: DSID of the target volume where target LUN resides
        
        :param target_qtree_name: This parameter specifies the name of the qtree in which the
                vdisk resides.
        
        :param vserver_name: The name of the vserver hosting the target LUN.
        
        :param target_vdisk_name: The name of the vdisk.
        """
        return self.request( "storage-import-verify", {
            'target_volume_dsid': [ target_volume_dsid, 'target-volume-dsid', [ basestring, 'None' ], False ],
            'target_qtree_name': [ target_qtree_name, 'target-qtree-name', [ basestring, 'None' ], False ],
            'target_lun_path': [ target_lun_path, 'target-lun-path', [ basestring, 'None' ], False ],
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
            'target_vdisk_name': [ target_vdisk_name, 'target-vdisk-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_import_start(self, target_lun_path, target_volume_dsid=None, target_qtree_name=None, vserver_name=None, target_vdisk_name=None):
        """
        Start importing data to the specified Data ONTAP(R) LUN from
        the foreign array LUN.
        This d-blade ZAPI is for internal use only, and expected
        to be removed in future release.
        
        :param target_lun_path: Data ONTAP(R) LUN Path
                For example, /vol/vol1/qtree1/lun1
        
        :param target_volume_dsid: DSID of the target volume where target LUN resides
        
        :param target_qtree_name: This parameter specifies the name of the qtree in which the
                vdisk resides
        
        :param vserver_name: The name of the vserver hosting the target LUN
        
        :param target_vdisk_name: The name of the vdisk
        """
        return self.request( "storage-import-start", {
            'target_volume_dsid': [ target_volume_dsid, 'target-volume-dsid', [ basestring, 'None' ], False ],
            'target_qtree_name': [ target_qtree_name, 'target-qtree-name', [ basestring, 'None' ], False ],
            'target_lun_path': [ target_lun_path, 'target-lun-path', [ basestring, 'None' ], False ],
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
            'target_vdisk_name': [ target_vdisk_name, 'target-vdisk-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_import_bind(self, source_array_lun, target_lun_path, target_qtree_name=None, vserver_name=None, target_vdisk_name=None, source_array_lun_uuid=None, target_volume_dsid=None):
        """
        Bind the specified Data ONTAP(R) LUN to the foreign array LUN for
        data import session.
        This d-blade ZAPI is for internal use only, and expected
        to be removed in future release.
        
        :param source_array_lun: Name of the foreign array LUN
        
        :param target_lun_path: Data ONTAP(R) LUN path
                For example, /vol/vol1/qtree1/lun1
        
        :param target_qtree_name: This parameter specifies the name of the qtree in which the
                vdisk resides
        
        :param vserver_name: The name of the vserver hosting the target LUN
        
        :param target_vdisk_name: The name of the vdisk
        
        :param source_array_lun_uuid: UUID of the foreign array LUN
        
        :param target_volume_dsid: DSID of the target volume where target LUN resides
        """
        return self.request( "storage-import-bind", {
            'target_qtree_name': [ target_qtree_name, 'target-qtree-name', [ basestring, 'None' ], False ],
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
            'target_vdisk_name': [ target_vdisk_name, 'target-vdisk-name', [ basestring, 'None' ], False ],
            'source_array_lun': [ source_array_lun, 'source-array-lun', [ basestring, 'None' ], False ],
            'source_array_lun_uuid': [ source_array_lun_uuid, 'source-array-lun-uuid', [ basestring, 'None' ], False ],
            'target_volume_dsid': [ target_volume_dsid, 'target-volume-dsid', [ basestring, 'None' ], False ],
            'target_lun_path': [ target_lun_path, 'target-lun-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def storage_import_show(self, target_lun_path=None, vserver_name=None):
        """
        Shows all import sessions.
        If target LUN path is provided, shows only that import session.
        This d-blade ZAPI is for internal use only, and expected
        to be removed in future release.
        
        :param target_lun_path: Data ONTAP(R) LUN Path
                For example, /vol/vol1/qtree1/lun1
        
        :param vserver_name: The name of the vserver hosting the target LUN
        """
        return self.request( "storage-import-show", {
            'target_lun_path': [ target_lun_path, 'target-lun-path', [ basestring, 'None' ], False ],
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
        }, {
            'import-stat-info': [ StorageImportStatsInfo, True ],
        } )
    
    def storage_import_abort(self, target_lun_path, vserver_name=None):
        """
        Aborts the data import operation or data verify operation.
        This d-blade ZAPI is for internal use only, and expected
        to be removed in future release.
        
        :param target_lun_path: Data ONTAP(R) LUN Path
                For example, /vol/vol1/qtree1/lun1
        
        :param vserver_name: The name of the vserver hosting the target LUN
        """
        return self.request( "storage-import-abort", {
            'target_lun_path': [ target_lun_path, 'target-lun-path', [ basestring, 'None' ], False ],
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
        }, {
        } )
