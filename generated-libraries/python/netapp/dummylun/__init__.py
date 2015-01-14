from netapp.connection import NaConnection
from dummylun_destroy_iter_info import DummylunDestroyIterInfo # 3 properties
from dummylun_get_iter_alt_key_td import DummylunGetIterAltKeyTd # 4 properties
from dummylun_info import DummylunInfo # 10 properties
from dummylun_destroy_iter_key_td import DummylunDestroyIterKeyTd # 4 properties
from dummylun_get_iter_key_td import DummylunGetIterKeyTd # 4 properties
from optionalTest import Optionaltest # 3 properties
from group1_keys_info import Group1KeysInfo # 4 properties

class DummylunConnection(NaConnection):
    
    def ntdtest_action_only_dothat(self, field_4, field_1, field_2, field_3):
        """
        Test action 2 for cluster zapi infrastructure enhancements for
        RR
        
        :param field_4: Dummy/Generic Action Field 4
        
        :param field_1: Dummy/Generic Action Field 1
        
        :param field_2: Dummy/Generic Action Field 2
        
        :param field_3: Dummy/Generic Action Field 3
        """
        return self.request( "ntdtest-action-only-dothat", {
            'field_4': [ field_4, 'field-4', [ basestring, 'None' ], False ],
            'field_1': [ field_1, 'field-1', [ basestring, 'None' ], False ],
            'field_2': [ field_2, 'field-2', [ basestring, 'None' ], False ],
            'field_3': [ field_3, 'field-3', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def dummylun_create_by_size_alt(self, vserver, volume, lun_dummy, ostype=None, size=None):
        """
        Create a new dummylun.
        
        :param vserver: Vserver Name
        
        :param volume: Volume Name
        
        :param lun_dummy: LUN Name
        
        :param ostype: OS type of the LUN
        
        :param size: LUN size
        """
        return self.request( "dummylun-create-by-size-alt", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'lun_dummy': [ lun_dummy, 'lun-dummy', [ basestring, 'None' ], False ],
            'ostype': [ ostype, 'ostype', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ int, 'size' ], False ],
        }, {
            'actual-size': [ int, False ],
        } )
    
    def dummylun_list_info_alt1(self, vserver):
        """
        Get a collection of dummylun objects.
        
        :param vserver: Vserver Name
        """
        return self.request( "dummylun-list-info-alt1", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
        }, {
            'output': [ Group1KeysInfo, True ],
        } )
    
    def dummylun_list_info_alt2(self, vserver, volume=None, state=None):
        """
        Get a collection of dummylun objects.
        
        :param vserver: Vserver Name
        
        :param volume: Volume Name
        
        :param state: LUN State
        """
        return self.request( "dummylun-list-info-alt2", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'state': [ state, 'state', [ basestring, 'None' ], False ],
        }, {
            'output': [ Optionaltest, True ],
        } )
    
    def ntdtest_method_only_method2(self, arg1, field1):
        """
        Test method 2
        
        :param arg1: Argument 1 for method method2
        
        :param field1: Dummy/Generic Field 1 accepts any string
        """
        return self.request( "ntdtest-method-only-method2", {
            'arg1': [ arg1, 'arg1', [ int, 'None' ], False ],
            'field1': [ field1, 'field1', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def dummylun_list_info(self):
        """
        Get a collection of dummylun objects.
        """
        return self.request( "dummylun-list-info", {
        }, {
            'attributes-list': [ DummylunInfo, True ],
        } )
    
    def dummylun_list_info_alt(self, vserver):
        """
        Get a collection of dummylun objects.
        
        :param vserver: Vserver Name
        """
        return self.request( "dummylun-list-info-alt", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
        }, {
            'volume': [ basestring, True ],
        } )
    
    def dummylun_create(self, vserver, ostype, size, volume=None, return_record=None, state=None, path=None, lun=None):
        """
        Create a new dummylun.
        
        :param vserver: Vserver Name
        
        :param ostype: OS type of the LUN
        
        :param size: LUN size
        
        :param volume: Volume Name
        
        :param return_record: If set to true, returns the dummylun on successful creation.
                Default: false
        
        :param state: LUN State
        
        :param path: LUN Path
        
        :param lun: LUN Name
        """
        return self.request( "dummylun-create", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'state': [ state, 'state', [ basestring, 'None' ], False ],
            'ostype': [ ostype, 'ostype', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'lun': [ lun, 'lun', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ int, 'size' ], False ],
        }, {
            'result': [ DummylunInfo, False ],
        } )
    
    def dummylun_modify(self, volume=None, path=None, state=None, lun=None, size=None):
        """
        Modify the attributes of dummylun object.
        
        :param volume: Volume Name
        
        :param path: LUN Path
        
        :param state: LUN State
        
        :param lun: LUN Name
        
        :param size: LUN size
        """
        return self.request( "dummylun-modify", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'state': [ state, 'state', [ basestring, 'None' ], False ],
            'lun': [ lun, 'lun', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ int, 'size' ], False ],
        }, {
        } )
    
    def dummylun_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete an existing dummylun or a group of dummylun objects.
        
        :param query: If deleting a specific dummylun, this input element must specify
                all keys.
                If deleting multiple dummylun objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching dummylun
                even when the deletion of a previous matching dummylun fails, and
                do so until the total number of objects failed to be deleted
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of dummylun objects to delete in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of dummylun objects
                (just keys) that were successfully deleted.
                If set to false, the list of dummylun objects deleted will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple dummylun objects match
                a given query.
                If set to true, the API will continue deleting the next matching
                dummylun even when the deletion of a previous dummylun fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of dummylun objects
                (just keys) that were not deleted due to some error.
                If set to false, the list of dummylun objects not deleted will
                not be returned.
                Default: true
        """
        return self.request( "dummylun-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ DummylunInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ DummylunDestroyIterInfo, True ],
            'failure-list': [ DummylunDestroyIterInfo, True ],
        } )
    
    def dummylun_get_alt(self, vserver, volume, lun):
        """
        Get the attributes of the dummylun.
        
        :param vserver: Vserver Name
        
        :param volume: Volume Name
        
        :param lun: LUN Name
        """
        return self.request( "dummylun-get-alt", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'lun': [ lun, 'lun', [ basestring, 'None' ], False ],
        }, {
            'ostype': [ basestring, False ],
        } )
    
    def dummylun_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of dummylun objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                dummylun object.
                All dummylun objects matching this query up to 'max-records' will
                be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "dummylun-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DummylunInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DummylunInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DummylunInfo, True ],
        } )
    
    def dummylun_create_by_size(self, vserver, volume, lun_dummy, ostype, size):
        """
        Create a new dummylun.
        
        :param vserver: Vserver Name
        
        :param volume: Volume Name
        
        :param lun_dummy: LUN Name
        
        :param ostype: OS type of the LUN
        
        :param size: LUN size
        """
        return self.request( "dummylun-create-by-size", {
            'vserver': [ vserver, 'vserver', [ basestring, 'vserver-name' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'lun_dummy': [ lun_dummy, 'lun-dummy', [ basestring, 'None' ], False ],
            'ostype': [ ostype, 'ostype', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ int, 'size' ], False ],
        }, {
            'actual-size': [ int, False ],
        } )
    
    def dummylun_get_iter_alt(self, max_records=None, query=None, tag=None, desired_attributes=None, get_clone_backing_snapshot=None):
        """
        Iterate over a list of dummylun objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                dummylun object.
                All dummylun objects matching this query up to 'max-records' will
                be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param get_clone_backing_snapshot: Get Backing Snapshot
        """
        return self.request( "dummylun-get-iter-alt", {
            'max_records': max_records,
            'query': [ query, 'query', [ DummylunInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DummylunInfo, 'None' ], False ],
            'get_clone_backing_snapshot': [ get_clone_backing_snapshot, 'get-clone-backing-snapshot', [ bool, 'None' ], False ],
        }, {
            'are-vols-busy': [ bool, False ],
            'attributes-list': [ DummylunInfo, True ],
            'are-vols-onlining': [ bool, False ],
        } )
    
    def dummylun_get(self, volume=None, path=None, desired_attributes=None, lun=None):
        """
        Get the attributes of the dummylun.
        
        :param volume: Volume Name
        
        :param path: LUN Path
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param lun: LUN Name
        """
        return self.request( "dummylun-get", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DummylunInfo, 'None' ], False ],
            'lun': [ lun, 'lun', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ DummylunInfo, False ],
        } )
