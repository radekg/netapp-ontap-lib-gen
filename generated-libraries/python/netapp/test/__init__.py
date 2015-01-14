from netapp.connection import NaConnection
from test_zapi_sleep_method_async_iter_info import TestZapiSleepMethodAsyncIterInfo # 5 properties
from test_intrinsic_apis_4_destroy_iter_key_td import TestIntrinsicApis4DestroyIterKeyTd # 1 properties
from test_zapi_sleep_modify_iter_info import TestZapiSleepModifyIterInfo # 3 properties
from test_zapi_ro_view_5_get_iter_key_td import TestZapiRoView5GetIterKeyTd # 1 properties
from test_zapi_sleep_modify_async_iter_key_td import TestZapiSleepModifyAsyncIterKeyTd # 1 properties
from test_zapi_sleep_destroy_async_iter_key_td import TestZapiSleepDestroyAsyncIterKeyTd # 1 properties
from schema_validator_info import SchemaValidatorInfo # 1 properties
from test_zapi_sleep_method_iter_key_td import TestZapiSleepMethodIterKeyTd # 1 properties
from test_sleep_info import TestSleepInfo # 5 properties
from test_zapi_ro_view_6_modify_iter_info import TestZapiRoView6ModifyIterInfo # 3 properties
from test_intrinsic_apis_4_get_iter_key_td import TestIntrinsicApis4GetIterKeyTd # 1 properties
from testinfo import Testinfo # 2 properties
from stringalias import Stringalias # 0 properties
from test_zapi_ro_view_6_destroy_iter_info import TestZapiRoView6DestroyIterInfo # 3 properties
from test_zapi_sleep_get_iter_key_td import TestZapiSleepGetIterKeyTd # 1 properties
from cluster_name import ClusterName # 0 properties
from test_return_string import TestReturnString # 0 properties
from test_intrinsic_apis_2_modify_iter_info import TestIntrinsicApis2ModifyIterInfo # 3 properties
from test_zapi_sleep_destroy_async_iter_info import TestZapiSleepDestroyAsyncIterInfo # 5 properties
from test_intrinsic_apis_2_modify_iter_key_td import TestIntrinsicApis2ModifyIterKeyTd # 1 properties
from test_zapi_ro_view_5_destroy_iter_info import TestZapiRoView5DestroyIterInfo # 3 properties
from test_zapi_sleep_method_async_iter_key_td import TestZapiSleepMethodAsyncIterKeyTd # 1 properties
from test_intrinsic_apis_2 import TestIntrinsicApis2 # 1 properties
from test_zapi_sleep_modify_iter_key_td import TestZapiSleepModifyIterKeyTd # 1 properties
from test_zapi_ro_view_5_info import TestZapiRoView5Info # 1 properties
from test_zapi_sleep_destroy_iter_key_td import TestZapiSleepDestroyIterKeyTd # 1 properties
from test_intrinsic_apis_3 import TestIntrinsicApis3 # 1 properties
from test_intrinsic_apis_1 import TestIntrinsicApis1 # 1 properties
from test_intrinsic_apis_4 import TestIntrinsicApis4 # 1 properties
from test_zapi_sleep_destroy_iter_info import TestZapiSleepDestroyIterInfo # 3 properties
from test_intrinsic_apis_3_destroy_iter_key_td import TestIntrinsicApis3DestroyIterKeyTd # 1 properties
from test_intrinsic_apis_1_destroy_iter_info import TestIntrinsicApis1DestroyIterInfo # 3 properties
from test_intrinsic_apis_2_get_iter_key_td import TestIntrinsicApis2GetIterKeyTd # 1 properties
from test_zapi_ro_view_6_modify_iter_key_td import TestZapiRoView6ModifyIterKeyTd # 1 properties
from test_zapi_ro_view_6_destroy_iter_key_td import TestZapiRoView6DestroyIterKeyTd # 1 properties
from sleep_location import SleepLocation # 0 properties
from test_2_info import Test2Info # 2 properties
from test_zapi_ro_view_6_get_iter_key_td import TestZapiRoView6GetIterKeyTd # 1 properties
from test_intrinsic_apis_3_get_iter_key_td import TestIntrinsicApis3GetIterKeyTd # 1 properties
from test_intrinsic_apis_2_destroy_iter_info import TestIntrinsicApis2DestroyIterInfo # 3 properties
from test_zapi_ro_view_5_destroy_iter_key_td import TestZapiRoView5DestroyIterKeyTd # 1 properties
from test_intrinsic_apis_4_destroy_iter_info import TestIntrinsicApis4DestroyIterInfo # 3 properties
from peer_node_name import PeerNodeName # 0 properties
from test_intrinsic_apis_1_get_iter_key_td import TestIntrinsicApis1GetIterKeyTd # 1 properties
from test_zapi_ro_view_6_info import TestZapiRoView6Info # 1 properties
from test_intrinsic_apis_1_destroy_iter_key_td import TestIntrinsicApis1DestroyIterKeyTd # 1 properties
from test_intrinsic_apis_3_destroy_iter_info import TestIntrinsicApis3DestroyIterInfo # 3 properties
from test_intrinsic_apis_2_destroy_iter_key_td import TestIntrinsicApis2DestroyIterKeyTd # 1 properties
from test_zapi_sleep_modify_async_iter_info import TestZapiSleepModifyAsyncIterInfo # 5 properties
from test_zapi_sleep_method_iter_info import TestZapiSleepMethodIterInfo # 3 properties

class TestConnection(NaConnection):
    
    def test_iter_start(self, iterations):
        """
        A test API for the iteration primitives.
        
        :param iterations: Number of items to generate in the iteration.
        """
        return self.request( "test-iter-start", {
            'iterations': [ iterations, 'iterations', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def test_zapi_sleep_method_async_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Method Iter
        A job will be spawned to operate on the test-zapi-sleep and the
        job id will be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param query: If operating on a specific test-zapi-sleep, this input element
                must specify all keys.
                If operating on test-zapi-sleep objects based on query, this
                input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching
                test-zapi-sleep even when the operation on a previous matching
                test-zapi-sleep fails, and do so until the total number of
                objects failed to be operated on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-zapi-sleep objects to be operated in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were successfully operated on or
                scheduled to be worked on.
                If set to false, the list of test-zapi-sleep objects operated on
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-sleep
                objects match a given query.
                If set to true, the API will continue with the next matching
                test-zapi-sleep even when the operation fails for the
                test-zapi-sleep.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of test-zapi-sleep objects not operated
                on will not be returned.
                Default: true
        """
        return self.request( "test-zapi-sleep-method-async-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestSleepInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiSleepMethodAsyncIterInfo, True ],
            'failure-list': [ TestZapiSleepMethodAsyncIterInfo, True ],
        } )
    
    def test_zapi_ro_view_5_get(self, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "test-zapi-ro-view-5-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestZapiRoView5Info, 'None' ], False ],
        }, {
            'attributes': [ TestZapiRoView5Info, False ],
        } )
    
    def test_zapi_ro_view_6_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                test-zapi-ro-view-6 object.
                All test-zapi-ro-view-6 objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "test-zapi-ro-view-6-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ TestZapiRoView6Info, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestZapiRoView6Info, 'None' ], False ],
        }, {
            'attributes-list': [ TestZapiRoView6Info, True ],
        } )
    
    def test_zapi_ro_view_5_get_create_defaults(self, attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param attributes: Optionally specify the value for attributes if available.
                The default values for some attributes may depend on the values
                specified for some other attribute.
        """
        return self.request( "test-zapi-ro-view-5-get-create-defaults", {
            'attributes': [ attributes, 'attributes', [ TestZapiRoView5Info, 'None' ], False ],
        }, {
            'defaults': [ TestZapiRoView5Info, False ],
        } )
    
    def test_zapi_ro_view_1_writable4(self):
        """
        Test method 1 - does nothing, not for execution - verifies that
        zapi's defined on read-write methods are not marked readonly in
        the zapidoc.
        """
        return self.request( "test-zapi-ro-view-1-writable4", {
        }, {
        } )
    
    def test_zapi_sleep_destroy_async_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        TEST Sleep Iter
        
        :param query: If deleting a specific test-zapi-sleep, this input element must
                specify all keys.
                If deleting multiple test-zapi-sleep objects based on query, this
                input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                test-zapi-sleep even when the deletion of a previous matching
                test-zapi-sleep fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-zapi-sleep objects to delete in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were successfully deleted or submitted
                for deletion.
                If set to false, the list of test-zapi-sleep objects deleted will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-sleep
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                test-zapi-sleep even when the deletion of a previous
                test-zapi-sleep fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were not deleted due to some error.
                If set to false, the list of test-zapi-sleep objects not deleted
                will not be returned.
                Default: true
        """
        return self.request( "test-zapi-sleep-destroy-async-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestSleepInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiSleepDestroyAsyncIterInfo, True ],
            'failure-list': [ TestZapiSleepDestroyAsyncIterInfo, True ],
        } )
    
    def test_intrinsic_apis_1_get_create_defaults(self, attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param attributes: Optionally specify the value for attributes if available.
                The default values for some attributes may depend on the values
                specified for some other attribute.
        """
        return self.request( "test-intrinsic-apis-1-get-create-defaults", {
            'attributes': [ attributes, 'attributes', [ TestIntrinsicApis1, 'None' ], False ],
        }, {
            'defaults': [ TestIntrinsicApis1, False ],
        } )
    
    def test_intrinsic_apis_2_get(self, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "test-intrinsic-apis-2-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestIntrinsicApis2, 'None' ], False ],
        }, {
            'attributes': [ TestIntrinsicApis2, False ],
        } )
    
    def test_intrinsic_apis_3_destroy(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-3-destroy", {
        }, {
        } )
    
    def test_iter_end(self, tag):
        """
        A test API for the iteration primitives.
        
        :param tag: Tag from a previous test-iter-start.
        """
        return self.request( "test-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def test_intrinsic_apis_1_list_info(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-1-list-info", {
        }, {
            'attributes-list': [ TestIntrinsicApis1, True ],
        } )
    
    def test_intrinsic_apis_3_create(self, return_record=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param return_record: If set to true, returns the test-intrinsic-apis-3 on successful
                creation.
                Default: false
        """
        return self.request( "test-intrinsic-apis-3-create", {
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ TestIntrinsicApis3, False ],
        } )
    
    def test_zapi_sleep_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        TEST Sleep Iter
        
        :param query: If deleting a specific test-zapi-sleep, this input element must
                specify all keys.
                If deleting multiple test-zapi-sleep objects based on query, this
                input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                test-zapi-sleep even when the deletion of a previous matching
                test-zapi-sleep fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-zapi-sleep objects to delete in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were successfully deleted.
                If set to false, the list of test-zapi-sleep objects deleted will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-sleep
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                test-zapi-sleep even when the deletion of a previous
                test-zapi-sleep fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were not deleted due to some error.
                If set to false, the list of test-zapi-sleep objects not deleted
                will not be returned.
                Default: true
        """
        return self.request( "test-zapi-sleep-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestSleepInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiSleepDestroyIterInfo, True ],
            'failure-list': [ TestZapiSleepDestroyIterInfo, True ],
        } )
    
    def test_intrinsic_apis_1_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param query: If deleting a specific test-intrinsic-apis-1, this input element
                must specify all keys.
                If deleting multiple test-intrinsic-apis-1 objects based on
                query, this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                test-intrinsic-apis-1 even when the deletion of a previous
                matching test-intrinsic-apis-1 fails, and do so until the total
                number of objects failed to be deleted reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-intrinsic-apis-1 objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                test-intrinsic-apis-1 objects (just keys) that were successfully
                deleted.
                If set to false, the list of test-intrinsic-apis-1 objects
                deleted will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-intrinsic-apis-1
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                test-intrinsic-apis-1 even when the deletion of a previous
                test-intrinsic-apis-1 fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                test-intrinsic-apis-1 objects (just keys) that were not deleted
                due to some error.
                If set to false, the list of test-intrinsic-apis-1 objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "test-intrinsic-apis-1-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestIntrinsicApis1, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestIntrinsicApis1DestroyIterInfo, True ],
            'failure-list': [ TestIntrinsicApis1DestroyIterInfo, True ],
        } )
    
    def test_intrinsic_apis_2_get_total_records(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-2-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def test_zapi_sleep_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        TEST Sleep Iter
        
        :param query: If modifying a specific test-zapi-sleep, this input element must
                specify all keys.
                If modifying test-zapi-sleep objects based on query, this input
                element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                test-zapi-sleep even when the modification of a previous matching
                test-zapi-sleep fails, and do so until the total number of
                objects failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were successfully updated.
                If set to false, the list of test-zapi-sleep objects modified
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-sleep
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                test-zapi-sleep even when modification of a previous
                test-zapi-sleep fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were not modified due to some error.
                If set to false, the list of test-zapi-sleep objects not modified
                will not be returned.
                Default: true
        """
        return self.request( "test-zapi-sleep-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestSleepInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ TestSleepInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiSleepModifyIterInfo, True ],
            'failure-list': [ TestZapiSleepModifyIterInfo, True ],
        } )
    
    def test_zapi_sleep(self, sleep_time=None, seq_id=None, cluster=None, host=None, return_string_size=None, location=None):
        """
        This zapi will go to the location specified, sleep for the time
        given and then return a list of arbitrary characters of the
        amount requested.
        
        :param sleep_time: The amount of time to sleep in seconds.
                Range : [0..3600].
                If a value is not provided, 0 will be used.
        
        :param seq_id: The sequence id.
                If a value is not provided, 0 will be used.
        
        :param cluster: The local cluster or the cluster from a peer relationship to run
                the zapi on.  If a value is not provided, the cluster receiving
                the zapi will be used.
        
        :param host: The node from the cluster specified to run the zapi on.  If a
                value is not provided, the node receiving the zapi will be used.
        
        :param return_string_size: The amount off data to return in the return-strings element.
                Range : [0..104857600].
                If a value is not provided, 0 will be used.
        
        :param location: This specifies whether the zapi should sleep and generate
                return strings from the dblade or mgwd.
                If a value is not provided, mgwd will be used.
                <p>
                Possible values are:
                <ul>
                <li> "mgwd",
                <li> "dblade"
                </ul>
        """
        return self.request( "test-zapi-sleep", {
            'sleep_time': [ sleep_time, 'sleep-time', [ int, 'None' ], False ],
            'seq_id': [ seq_id, 'seq-id', [ int, 'None' ], False ],
            'cluster': [ cluster, 'cluster', [ basestring, 'None' ], False ],
            'host': [ host, 'host', [ basestring, 'None' ], False ],
            'return_string_size': [ return_string_size, 'return-string-size', [ int, 'None' ], False ],
            'location': [ location, 'location', [ basestring, 'None' ], False ],
        }, {
            'return-strings': [ basestring, True ],
            'md5-checksum': [ basestring, False ],
            'mgwd-after-string-gen-time': [ int, False ],
            'seq-id': [ int, False ],
            'mgwd-end-time': [ int, False ],
            'dblade-after-sleep-time': [ int, False ],
            'dblade-start-time': [ int, False ],
            'mgwd-after-sleep-time': [ int, False ],
            'mgwd-start-time': [ int, False ],
            'dblade-after-string-gen-time': [ int, False ],
            'xcdr-start-time': [ int, False ],
        } )
    
    def test_intrinsic_apis_4_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param query: If deleting a specific test-intrinsic-apis-4, this input element
                must specify all keys.
                If deleting multiple test-intrinsic-apis-4 objects based on
                query, this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                test-intrinsic-apis-4 even when the deletion of a previous
                matching test-intrinsic-apis-4 fails, and do so until the total
                number of objects failed to be deleted reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-intrinsic-apis-4 objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                test-intrinsic-apis-4 objects (just keys) that were successfully
                deleted.
                If set to false, the list of test-intrinsic-apis-4 objects
                deleted will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-intrinsic-apis-4
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                test-intrinsic-apis-4 even when the deletion of a previous
                test-intrinsic-apis-4 fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                test-intrinsic-apis-4 objects (just keys) that were not deleted
                due to some error.
                If set to false, the list of test-intrinsic-apis-4 objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "test-intrinsic-apis-4-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestIntrinsicApis4, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestIntrinsicApis4DestroyIterInfo, True ],
            'failure-list': [ TestIntrinsicApis4DestroyIterInfo, True ],
        } )
    
    def test_zapi_ro_view_6_get_create_defaults(self, attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param attributes: Optionally specify the value for attributes if available.
                The default values for some attributes may depend on the values
                specified for some other attribute.
        """
        return self.request( "test-zapi-ro-view-6-get-create-defaults", {
            'attributes': [ attributes, 'attributes', [ TestZapiRoView6Info, 'None' ], False ],
        }, {
            'defaults': [ TestZapiRoView6Info, False ],
        } )
    
    def test_zapi_ro_view_6_get_total_records(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-zapi-ro-view-6-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def test_intrinsic_apis_1_get_total_records(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-1-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def test_intrinsic_apis_3_list_info(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-3-list-info", {
        }, {
            'attributes-list': [ TestIntrinsicApis3, True ],
        } )
    
    def test_intrinsic_apis_2_get_create_defaults(self, attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param attributes: Optionally specify the value for attributes if available.
                The default values for some attributes may depend on the values
                specified for some other attribute.
        """
        return self.request( "test-intrinsic-apis-2-get-create-defaults", {
            'attributes': [ attributes, 'attributes', [ TestIntrinsicApis2, 'None' ], False ],
        }, {
            'defaults': [ TestIntrinsicApis2, False ],
        } )
    
    def test_zapi_ro_view_5_destroy(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-zapi-ro-view-5-destroy", {
        }, {
        } )
    
    def test_password_get(self, password=None):
        """
        Test routine to get the encrypted version of a password.
        
        :param password: If provided, this value is used rather than a built-in default
                value (which is "this_is_the_unencrypted_password_value").
        """
        return self.request( "test-password-get", {
            'password': [ password, 'password', [ basestring, 'None' ], False ],
        }, {
            'decrypted-password': [ basestring, False ],
            'password': [ basestring, False ],
        } )
    
    def test_rw_method_writable2(self, field1):
        """
        does nothing, not for execution - verifies that zapi's defined on
        read-write methods are not marked readonly in the zapidoc.
        
        :param field1: Dummy/Generic Field 1 accepts any string
        """
        return self.request( "test-rw-method-writable2", {
            'field1': [ field1, 'field1', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def test_zapi_ro_view_6_get(self, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "test-zapi-ro-view-6-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestZapiRoView6Info, 'None' ], False ],
        }, {
            'attributes': [ TestZapiRoView6Info, False ],
        } )
    
    def test_intrinsic_apis_2_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param query: If modifying a specific test-intrinsic-apis-2, this input element
                must specify all keys.
                If modifying test-intrinsic-apis-2 objects based on query, this
                input element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                test-intrinsic-apis-2 even when the modification of a previous
                matching test-intrinsic-apis-2 fails, and do so until the total
                number of objects failed to be modified reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                test-intrinsic-apis-2 objects (just keys) that were successfully
                updated.
                If set to false, the list of test-intrinsic-apis-2 objects
                modified will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-intrinsic-apis-2
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                test-intrinsic-apis-2 even when modification of a previous
                test-intrinsic-apis-2 fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                test-intrinsic-apis-2 objects (just keys) that were not modified
                due to some error.
                If set to false, the list of test-intrinsic-apis-2 objects not
                modified will not be returned.
                Default: true
        """
        return self.request( "test-intrinsic-apis-2-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestIntrinsicApis2, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ TestIntrinsicApis2, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestIntrinsicApis2ModifyIterInfo, True ],
            'failure-list': [ TestIntrinsicApis2ModifyIterInfo, True ],
        } )
    
    def test_intrinsic_apis_3_get_total_records(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-3-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def test_zapi_ro_view_6_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param query: If deleting a specific test-zapi-ro-view-6, this input element
                must specify all keys.
                If deleting multiple test-zapi-ro-view-6 objects based on query,
                this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                test-zapi-ro-view-6 even when the deletion of a previous matching
                test-zapi-ro-view-6 fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-zapi-ro-view-6 objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                test-zapi-ro-view-6 objects (just keys) that were successfully
                deleted.
                If set to false, the list of test-zapi-ro-view-6 objects deleted
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-ro-view-6
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                test-zapi-ro-view-6 even when the deletion of a previous
                test-zapi-ro-view-6 fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                test-zapi-ro-view-6 objects (just keys) that were not deleted due
                to some error.
                If set to false, the list of test-zapi-ro-view-6 objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "test-zapi-ro-view-6-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestZapiRoView6Info, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiRoView6DestroyIterInfo, True ],
            'failure-list': [ TestZapiRoView6DestroyIterInfo, True ],
        } )
    
    def test_zapi_ro_view_5_create(self, field3, return_record=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param field3: Dummy/Generic Field 3 accepts an integer
        
        :param return_record: If set to true, returns the test-zapi-ro-view-5 on successful
                creation.
                Default: false
        """
        return self.request( "test-zapi-ro-view-5-create", {
            'field3': [ field3, 'field3', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ TestZapiRoView5Info, False ],
        } )
    
    def test_ro_method_readonly1(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        readonly methods are marked readonly in the zapidoc.
        """
        return self.request( "test-ro-method-readonly1", {
        }, {
        } )
    
    def test_2_iter_next(self, tag, maximum):
        """
        A test API for the new iterator primitives.
        
        :param tag: Tag from a previous test-iter-start.
        
        :param maximum: Maximum number of entries to retrieve.
        """
        return self.request( "test-2-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'testinfos': [ Test2Info, True ],
        } )
    
    def test_intrinsic_apis_4_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                test-intrinsic-apis-4 object.
                All test-intrinsic-apis-4 objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "test-intrinsic-apis-4-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ TestIntrinsicApis4, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestIntrinsicApis4, 'None' ], False ],
        }, {
            'attributes-list': [ TestIntrinsicApis4, True ],
        } )
    
    def test_ro_table_readonly1(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        readonly methods are marked readonly in the zapidoc.
        """
        return self.request( "test-ro-table-readonly1", {
        }, {
        } )
    
    def test_intrinsic_apis_2_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                test-intrinsic-apis-2 object.
                All test-intrinsic-apis-2 objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "test-intrinsic-apis-2-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ TestIntrinsicApis2, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestIntrinsicApis2, 'None' ], False ],
        }, {
            'attributes-list': [ TestIntrinsicApis2, True ],
        } )
    
    def test_zapi_sleep_method_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Method Iter
        
        :param query: If operating on a specific test-zapi-sleep, this input element
                must specify all keys.
                If operating on test-zapi-sleep objects based on query, this
                input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching
                test-zapi-sleep even when the operation on a previous matching
                test-zapi-sleep fails, and do so until the total number of
                objects failed to be operated on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-zapi-sleep objects to be operated in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were successfully operated on.
                If set to false, the list of test-zapi-sleep objects operated on
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-sleep
                objects match a given query.
                If set to true, the API will continue with the next matching
                test-zapi-sleep even when the operation fails for the
                test-zapi-sleep.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of test-zapi-sleep objects not operated
                on will not be returned.
                Default: true
        """
        return self.request( "test-zapi-sleep-method-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestSleepInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiSleepMethodIterInfo, True ],
            'failure-list': [ TestZapiSleepMethodIterInfo, True ],
        } )
    
    def test_zapi_ro_view_6_create(self, field3, return_record=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param field3: Dummy/Generic Field 3 accepts an integer
        
        :param return_record: If set to true, returns the test-zapi-ro-view-6 on successful
                creation.
                Default: false
        """
        return self.request( "test-zapi-ro-view-6-create", {
            'field3': [ field3, 'field3', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ TestZapiRoView6Info, False ],
        } )
    
    def test_zapi_sleep_get_iter(self, seconds=None, max_records=None, tag=None, desired_attributes=None, query=None):
        """
        TEST Sleep Iter
        
        :param seconds: Seconds
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                test-zapi-sleep object.
                All test-zapi-sleep objects matching this query up to
                'max-records' will be returned.
        """
        return self.request( "test-zapi-sleep-get-iter", {
            'seconds': [ seconds, 'seconds', [ int, 'None' ], False ],
            'max_records': max_records,
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestSleepInfo, 'None' ], False ],
            'query': [ query, 'query', [ TestSleepInfo, 'None' ], False ],
        }, {
            'attributes-list': [ TestSleepInfo, True ],
        } )
    
    def test_intrinsic_apis_4_get(self, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "test-intrinsic-apis-4-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestIntrinsicApis4, 'None' ], False ],
        }, {
            'attributes': [ TestIntrinsicApis4, False ],
        } )
    
    def test_ro_action_2_readonly4(self, field_1, field_2, field_3):
        """
        does nothing, not for execution - verifies that zapi's defined on
        readonly actions are marked readonly in the zapidoc.
        
        :param field_1: Dummy/Generic Action Field 1
        
        :param field_2: Dummy/Generic Action Field 2
        
        :param field_3: Dummy/Generic Action Field 3
        """
        return self.request( "test-ro-action-2-readonly4", {
            'field_1': [ field_1, 'field-1', [ basestring, 'None' ], False ],
            'field_2': [ field_2, 'field-2', [ basestring, 'None' ], False ],
            'field_3': [ field_3, 'field-3', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def test_intrinsic_apis_2_modify(self, field3=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param field3: Dummy/Generic Field 3 accepts an integer
        """
        return self.request( "test-intrinsic-apis-2-modify", {
            'field3': [ field3, 'field3', [ int, 'None' ], False ],
        }, {
        } )
    
    def test_intrinsic_apis_3_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                test-intrinsic-apis-3 object.
                All test-intrinsic-apis-3 objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "test-intrinsic-apis-3-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ TestIntrinsicApis3, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestIntrinsicApis3, 'None' ], False ],
        }, {
            'attributes-list': [ TestIntrinsicApis3, True ],
        } )
    
    def test_ro_action_1_readonly3(self, field_1, field_2):
        """
        @desc
        
        :param field_1: Dummy/Generic Action Field 1
        
        :param field_2: Dummy/Generic Action Field 2
        """
        return self.request( "test-ro-action-1-readonly3", {
            'field_1': [ field_1, 'field-1', [ basestring, 'None' ], False ],
            'field_2': [ field_2, 'field-2', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def test_intrinsic_apis_1_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                test-intrinsic-apis-1 object.
                All test-intrinsic-apis-1 objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "test-intrinsic-apis-1-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ TestIntrinsicApis1, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestIntrinsicApis1, 'None' ], False ],
        }, {
            'attributes-list': [ TestIntrinsicApis1, True ],
        } )
    
    def test_intrinsic_apis_3_get_create_defaults(self, attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param attributes: Optionally specify the value for attributes if available.
                The default values for some attributes may depend on the values
                specified for some other attribute.
        """
        return self.request( "test-intrinsic-apis-3-get-create-defaults", {
            'attributes': [ attributes, 'attributes', [ TestIntrinsicApis3, 'None' ], False ],
        }, {
            'defaults': [ TestIntrinsicApis3, False ],
        } )
    
    def test_zapi_ro_view_6_destroy(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-zapi-ro-view-6-destroy", {
        }, {
        } )
    
    def test_intrinsic_apis_1_destroy(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-1-destroy", {
        }, {
        } )
    
    def test_zapi_ro_view_5_get_total_records(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-zapi-ro-view-5-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def test_zapi_ro_view_6_modify(self, field3=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param field3: Dummy/Generic Field 3 accepts an integer
        """
        return self.request( "test-zapi-ro-view-6-modify", {
            'field3': [ field3, 'field3', [ int, 'None' ], False ],
        }, {
        } )
    
    def test_intrinsic_apis_4_get_total_records(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-4-get-total-records", {
        }, {
            'count': [ int, False ],
        } )
    
    def test_intrinsic_apis_4_list_info(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-4-list-info", {
        }, {
            'attributes-list': [ TestIntrinsicApis4, True ],
        } )
    
    def test_zapi_ro_view_6_list_info(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-zapi-ro-view-6-list-info", {
        }, {
            'attributes-list': [ TestZapiRoView6Info, True ],
        } )
    
    def test_zapi_sleep_modify_async_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        TEST Sleep Iter
        
        :param query: If modifying a specific test-zapi-sleep, this input element must
                specify all keys.
                If modifying test-zapi-sleep objects based on query, this input
                element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                test-zapi-sleep even when the modification of a previous matching
                test-zapi-sleep fails, and do so until the total number of
                objects failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were successfully updated or scheduled
                for update.
                If set to false, the list of test-zapi-sleep objects modified
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-sleep
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                test-zapi-sleep even when modification of a previous
                test-zapi-sleep fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of test-zapi-sleep
                objects (just keys) that were not modified due to some error.
                If set to false, the list of test-zapi-sleep objects not modified
                will not be returned.
                Default: true
        """
        return self.request( "test-zapi-sleep-modify-async-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestSleepInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ TestSleepInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiSleepModifyAsyncIterInfo, True ],
            'failure-list': [ TestZapiSleepModifyAsyncIterInfo, True ],
        } )
    
    def test_zapi_ro_view_5_list_info(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-zapi-ro-view-5-list-info", {
        }, {
            'attributes-list': [ TestZapiRoView5Info, True ],
        } )
    
    def test_intrinsic_apis_2_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param query: If deleting a specific test-intrinsic-apis-2, this input element
                must specify all keys.
                If deleting multiple test-intrinsic-apis-2 objects based on
                query, this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                test-intrinsic-apis-2 even when the deletion of a previous
                matching test-intrinsic-apis-2 fails, and do so until the total
                number of objects failed to be deleted reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-intrinsic-apis-2 objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                test-intrinsic-apis-2 objects (just keys) that were successfully
                deleted.
                If set to false, the list of test-intrinsic-apis-2 objects
                deleted will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-intrinsic-apis-2
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                test-intrinsic-apis-2 even when the deletion of a previous
                test-intrinsic-apis-2 fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                test-intrinsic-apis-2 objects (just keys) that were not deleted
                due to some error.
                If set to false, the list of test-intrinsic-apis-2 objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "test-intrinsic-apis-2-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestIntrinsicApis2, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestIntrinsicApis2DestroyIterInfo, True ],
            'failure-list': [ TestIntrinsicApis2DestroyIterInfo, True ],
        } )
    
    def test_intrinsic_apis_2_create(self, field3, return_record=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param field3: Dummy/Generic Field 3 accepts an integer
        
        :param return_record: If set to true, returns the test-intrinsic-apis-2 on successful
                creation.
                Default: false
        """
        return self.request( "test-intrinsic-apis-2-create", {
            'field3': [ field3, 'field3', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ TestIntrinsicApis2, False ],
        } )
    
    def test_password_set(self, password):
        """
        Test routine to test input encrypted values.
        
        :param password: Test password.
        """
        return self.request( "test-password-set", {
            'password': [ password, 'password', [ basestring, 'None' ], False ],
        }, {
            'decrypted-password': [ basestring, False ],
        } )
    
    def test_intrinsic_apis_4_create(self, return_record=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param return_record: If set to true, returns the test-intrinsic-apis-4 on successful
                creation.
                Default: false
        """
        return self.request( "test-intrinsic-apis-4-create", {
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ TestIntrinsicApis4, False ],
        } )
    
    def test_zapi_ro_view_1_readonly6(self):
        """
        Test method 2 - does nothing, not for execution - verifies that
        zapi's defined on read-write methods are not marked readonly in
        the zapidoc.
        """
        return self.request( "test-zapi-ro-view-1-readonly6", {
        }, {
        } )
    
    def test_schema_validator(self, output_type):
        """
        A test API for the schema validator.  The input value
        specifies what type of output we want the API to generate.
        When invalid output is generated, the API will fail
        with an EAPIERROR error, and the reason value will be a
        string containing semicolon-separated entries describing
        each error that was found.
        
        :param output_type: Type of output to generate.
                Possible values: correct, incorrect1, incorrect2,
                incorrect3, incorrect4.
                "incorrect1" output tests misspelled tag names and
                bad array formatting.  "incorrect2" tests misspelled output
                and typedef names, and omits the array outputs.
                "incorrect3" tests other misspellings, and omits the arrays.
                "incorrect4" leaves out some required output values inside
                the typedef elements.
        """
        return self.request( "test-schema-validator", {
            'output_type': [ output_type, 'output-type', [ basestring, 'None' ], False ],
        }, {
            'array2': [ basestring, True ],
            'array1': [ SchemaValidatorInfo, True ],
            'output1': [ SchemaValidatorInfo, False ],
            'schema-validator-info': [ SchemaValidatorInfo, False ],
        } )
    
    def test_iter_next(self, tag, maximum):
        """
        A test API for the iteration primitives.
        
        :param tag: Tag from a previous test-iter-start.
        
        :param maximum: Maximum number of entries to retrieve.
        """
        return self.request( "test-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'testinfos': [ Testinfo, True ],
        } )
    
    def test_zapi_ro_view_5_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                test-zapi-ro-view-5 object.
                All test-zapi-ro-view-5 objects matching this query up to
                'max-records' will be returned.
        
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
        return self.request( "test-zapi-ro-view-5-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ TestZapiRoView5Info, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestZapiRoView5Info, 'None' ], False ],
        }, {
            'attributes-list': [ TestZapiRoView5Info, True ],
        } )
    
    def test_intrinsic_apis_4_destroy(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-4-destroy", {
        }, {
        } )
    
    def test_intrinsic_apis_1_get(self, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "test-intrinsic-apis-1-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestIntrinsicApis1, 'None' ], False ],
        }, {
            'attributes': [ TestIntrinsicApis1, False ],
        } )
    
    def test_ro_table_writable1(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        read-write methods are not marked readonly in the zapidoc.
        """
        return self.request( "test-ro-table-writable1", {
        }, {
        } )
    
    def test_intrinsic_apis_2_destroy(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-2-destroy", {
        }, {
        } )
    
    def invoke_api(self, username, host, api_name, password, use_SSL=None, vfiler=None, timeout=None):
        """
        invoke api on other filer or vfiler.
        
        :param username: username of the host
        
        :param host: Host name or IP address of the storage system on which the
                API needs to be invoked. IP address needs to be provided in
                w.x.y.z format.
        
        :param api_name: API to be invoked on the host.
        
        :param password: password of the host
        
        :param use_SSL: If the value of use-SSL is false then HTTP communication
                mechanism will be used for API query data transfer. Otherwise
                HTTPS will be used.
                Note: HTTP will be used by default.
        
        :param vfiler: Name of vfiler. This needs to be used if the API needs to be
                queried using vfiler tunneling feature
        
        :param timeout: Connection timeout.
        """
        return self.request( "invoke-api", {
            'username': [ username, 'username', [ basestring, 'None' ], False ],
            'use_SSL': [ use_SSL, 'use-SSL', [ bool, 'None' ], False ],
            'vfiler': [ vfiler, 'vfiler', [ basestring, 'None' ], False ],
            'host': [ host, 'host', [ basestring, 'None' ], False ],
            'api_name': [ api_name, 'api-name', [ basestring, 'None' ], False ],
            'timeout': [ timeout, 'timeout', [ int, 'None' ], False ],
            'password': [ password, 'password', [ basestring, 'None' ], False ],
        }, {
            'output-data': [ basestring, False ],
        } )
    
    def test_intrinsic_apis_4_get_create_defaults(self, attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param attributes: Optionally specify the value for attributes if available.
                The default values for some attributes may depend on the values
                specified for some other attribute.
        """
        return self.request( "test-intrinsic-apis-4-get-create-defaults", {
            'attributes': [ attributes, 'attributes', [ TestIntrinsicApis4, 'None' ], False ],
        }, {
            'defaults': [ TestIntrinsicApis4, False ],
        } )
    
    def test_intrinsic_apis_3_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param query: If deleting a specific test-intrinsic-apis-3, this input element
                must specify all keys.
                If deleting multiple test-intrinsic-apis-3 objects based on
                query, this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                test-intrinsic-apis-3 even when the deletion of a previous
                matching test-intrinsic-apis-3 fails, and do so until the total
                number of objects failed to be deleted reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-intrinsic-apis-3 objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                test-intrinsic-apis-3 objects (just keys) that were successfully
                deleted.
                If set to false, the list of test-intrinsic-apis-3 objects
                deleted will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-intrinsic-apis-3
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                test-intrinsic-apis-3 even when the deletion of a previous
                test-intrinsic-apis-3 fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                test-intrinsic-apis-3 objects (just keys) that were not deleted
                due to some error.
                If set to false, the list of test-intrinsic-apis-3 objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "test-intrinsic-apis-3-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestIntrinsicApis3, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestIntrinsicApis3DestroyIterInfo, True ],
            'failure-list': [ TestIntrinsicApis3DestroyIterInfo, True ],
        } )
    
    def test_intrinsic_apis_2_list_info(self):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        """
        return self.request( "test-intrinsic-apis-2-list-info", {
        }, {
            'attributes-list': [ TestIntrinsicApis2, True ],
        } )
    
    def test_ro_action_3_writable3(self, field_1, field_2, field_3):
        """
        does nothing, not for execution - verifies that zapi's defined on
        read-write actions are not marked readonly in the zapidoc.
        
        :param field_1: Dummy/Generic Action Field 1
        
        :param field_2: Dummy/Generic Action Field 2
        
        :param field_3: Dummy/Generic Action Field 3
        """
        return self.request( "test-ro-action-3-writable3", {
            'field_1': [ field_1, 'field-1', [ basestring, 'None' ], False ],
            'field_2': [ field_2, 'field-2', [ basestring, 'None' ], False ],
            'field_3': [ field_3, 'field-3', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def test_intrinsic_apis_1_create(self, return_record=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param return_record: If set to true, returns the test-intrinsic-apis-1 on successful
                creation.
                Default: false
        """
        return self.request( "test-intrinsic-apis-1-create", {
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ TestIntrinsicApis1, False ],
        } )
    
    def test_2_iter_start(self, input2, input1):
        """
        A test API for the new iterator primitives.
        
        :param input2: Prefix of item values.
        
        :param input1: Number of items to generate in the iteration.
        """
        return self.request( "test-2-iter-start", {
            'input2': [ input2, 'input2', [ basestring, 'None' ], False ],
            'input1': [ input1, 'input1', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def test_zapi_ro_view_6_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param query: If modifying a specific test-zapi-ro-view-6, this input element
                must specify all keys.
                If modifying test-zapi-ro-view-6 objects based on query, this
                input element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                test-zapi-ro-view-6 even when the modification of a previous
                matching test-zapi-ro-view-6 fails, and do so until the total
                number of objects failed to be modified reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                test-zapi-ro-view-6 objects (just keys) that were successfully
                updated.
                If set to false, the list of test-zapi-ro-view-6 objects modified
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-ro-view-6
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                test-zapi-ro-view-6 even when modification of a previous
                test-zapi-ro-view-6 fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                test-zapi-ro-view-6 objects (just keys) that were not modified
                due to some error.
                If set to false, the list of test-zapi-ro-view-6 objects not
                modified will not be returned.
                Default: true
        """
        return self.request( "test-zapi-ro-view-6-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestZapiRoView6Info, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ TestZapiRoView6Info, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiRoView6ModifyIterInfo, True ],
            'failure-list': [ TestZapiRoView6ModifyIterInfo, True ],
        } )
    
    def test_zapi_ro_view_5_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param query: If deleting a specific test-zapi-ro-view-5, this input element
                must specify all keys.
                If deleting multiple test-zapi-ro-view-5 objects based on query,
                this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                test-zapi-ro-view-5 even when the deletion of a previous matching
                test-zapi-ro-view-5 fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of test-zapi-ro-view-5 objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                test-zapi-ro-view-5 objects (just keys) that were successfully
                deleted.
                If set to false, the list of test-zapi-ro-view-5 objects deleted
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple test-zapi-ro-view-5
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                test-zapi-ro-view-5 even when the deletion of a previous
                test-zapi-ro-view-5 fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                test-zapi-ro-view-5 objects (just keys) that were not deleted due
                to some error.
                If set to false, the list of test-zapi-ro-view-5 objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "test-zapi-ro-view-5-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ TestZapiRoView5Info, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ TestZapiRoView5DestroyIterInfo, True ],
            'failure-list': [ TestZapiRoView5DestroyIterInfo, True ],
        } )
    
    def test_intrinsic_apis_3_get(self, desired_attributes=None):
        """
        does nothing, not for execution - verifies that zapi's defined on
        intrinsic methods have correct readonly values in the zapidoc.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "test-intrinsic-apis-3-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ TestIntrinsicApis3, 'None' ], False ],
        }, {
            'attributes': [ TestIntrinsicApis3, False ],
        } )
