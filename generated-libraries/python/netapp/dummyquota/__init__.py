from netapp.connection import NaConnection
from dummy_quota_user import DummyQuotaUser # 3 properties
from dummy_quota import DummyQuota # 8 properties
from dummy_quota_stuff import DummyQuotaStuff # 12 properties

class DummyquotaConnection(NaConnection):
    
    def dummy_quota_create(self, soft_file_limit, quota_user_ids, quota_type, quota_user_types, tree, volume, path, file_limit, quota_user_names, volume_index, disk_used, files_used, return_record=None):
        """
        Create a new dummy-quota.
        
        :param soft_file_limit: Soft File Limit
        
        :param quota_user_ids: Quota User IDs
        
        :param quota_type: Type (ZAPI)
        
        :param quota_user_types: Quota User Types
        
        :param tree: Tree
        
        :param volume: Volume Name
        
        :param path: Path Based Report
        
        :param file_limit: Files Limit
        
        :param quota_user_names: Quota User Names
        
        :param volume_index: Volume Index
        
        :param disk_used: Disk Blocks Used
        
        :param files_used: Files Used
        
        :param return_record: If set to true, returns the dummy-quota on successful creation.
                Default: false
        """
        return self.request( "dummy-quota-create", {
            'soft_file_limit': [ soft_file_limit, 'soft-file-limit', [ int, 'None' ], False ],
            'quota_user_ids': [ quota_user_ids, 'quota-user-ids', [ basestring, 'None' ], True ],
            'quota_type': [ quota_type, 'quota-type', [ basestring, 'None' ], False ],
            'quota_user_types': [ quota_user_types, 'quota-user-types', [ basestring, 'None' ], True ],
            'tree': [ tree, 'tree', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'file_limit': [ file_limit, 'file-limit', [ int, 'None' ], False ],
            'quota_user_names': [ quota_user_names, 'quota-user-names', [ basestring, 'None' ], True ],
            'volume_index': [ volume_index, 'volume-index', [ int, 'None' ], False ],
            'disk_used': [ disk_used, 'disk-used', [ int, 'None' ], False ],
            'files_used': [ files_used, 'files-used', [ int, 'None' ], False ],
        }, {
            'result': [ DummyQuotaStuff, False ],
        } )
    
    def dummy_quota_report_no_input(self):
        """
        Get the attributes of the dummy-quota.
        """
        return self.request( "dummy-quota-report-no-input", {
        }, {
            'quotas': [ DummyQuota, True ],
        } )
    
    def dummy_quota_report(self, volume, path):
        """
        Get the attributes of the dummy-quota.
        
        :param volume: Volume Name
        
        :param path: Path Based Report
        """
        return self.request( "dummy-quota-report", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'quotas': [ DummyQuota, True ],
        } )
    
    def dummy_quota_destroy(self, volume_index):
        """
        Delete an existing dummy-quota object.
        
        :param volume_index: Volume Index
        """
        return self.request( "dummy-quota-destroy", {
            'volume_index': [ volume_index, 'volume-index', [ int, 'None' ], False ],
        }, {
        } )
