from netapp.connection import NaConnection
from autogenzapi_get_iter_key_td import AutogenzapiGetIterKeyTd # 1 properties
from autogenzapi3_get_iter_key_td import Autogenzapi3GetIterKeyTd # 1 properties
from autogenzapi2_get_iter_key_td import Autogenzapi2GetIterKeyTd # 2 properties
from autogenzapi_info import AutogenzapiInfo # 2 properties
from autozapiview_info import AutozapiviewInfo # 3 properties
from autozapiview_get_iter_key_td import AutozapiviewGetIterKeyTd # 3 properties
from autogenzapi3_info import Autogenzapi3Info # 2 properties
from autogenzapi2_info import Autogenzapi2Info # 8 properties

class DummyConnection(NaConnection):
    
    def autogenzapi2_modify(self, id, field1=None, field6=None, field4=None, name=None):
        """
        auto generated
        
        :param id: id of object
        
        :param field1: optional field1
        
        :param field6: modify-noread field6
        
        :param field4: write-noread field4
        
        :param name: name of object
        """
        return self.request( "autogenzapi2-modify", {
            'field1': [ field1, 'field1', [ basestring, 'None' ], False ],
            'field6': [ field6, 'field6', [ basestring, 'None' ], False ],
            'id': [ id, 'id', [ int, 'None' ], False ],
            'field4': [ field4, 'field4', [ basestring, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def autozapiview_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        auto generated : Iterate over a list of autozapiview objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autozapiview object.
                All autozapiview objects matching this query up to 'max-records'
                will be returned.
        
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
        return self.request( "autozapiview-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutozapiviewInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutozapiviewInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutozapiviewInfo, True ],
        } )
    
    def autogenzapi3_destroy(self, id):
        """
        auto generated
        
        :param id: id of object
        """
        return self.request( "autogenzapi3-destroy", {
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
        } )
    
    def autogenzapi_modify(self, id, name=None):
        """
        auto generated
        
        :param id: id of object
        
        :param name: name of object
        """
        return self.request( "autogenzapi-modify", {
            'id': [ id, 'id', [ int, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def autogenzapi_create(self, id, name, return_record=None):
        """
        auto generated : Create a new autogenzapi.
        
        :param id: id of object
        
        :param name: name of object
        
        :param return_record: If set to true, returns the autogenzapi on successful creation.
                Default: false
        """
        return self.request( "autogenzapi-create", {
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'id': [ id, 'id', [ int, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
            'result': [ AutogenzapiInfo, False ],
        } )
    
    def autogenzapi3_method1(self, id):
        """
        auto generated : help for dummy autozapi3 method1 crazy
        
        :param id: id of object
        """
        return self.request( "autogenzapi3-method1", {
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
        } )
    
    def autogenzapi3_create(self, id, name, return_record=None):
        """
        auto generated : Create a new autogenzapi3.
        
        :param id: id of object
        
        :param name: name of object
        
        :param return_record: If set to true, returns the autogenzapi3 on successful creation.
                Default: false
        """
        return self.request( "autogenzapi3-create", {
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'id': [ id, 'id', [ int, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
            'result': [ Autogenzapi3Info, False ],
        } )
    
    def autogenzapi_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        auto generated : Iterate over a list of autogenzapi objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autogenzapi object.
                All autogenzapi objects matching this query up to 'max-records'
                will be returned.
        
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
        return self.request( "autogenzapi-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ AutogenzapiInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AutogenzapiInfo, 'None' ], False ],
        }, {
            'attributes-list': [ AutogenzapiInfo, True ],
        } )
    
    def autogenzapi_destroy(self, id):
        """
        auto generated
        
        :param id: id of object
        """
        return self.request( "autogenzapi-destroy", {
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
        } )
    
    def autogenzapi2_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        auto generated : Iterate over a list of autogenzapi2 objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autogenzapi2 object.
                All autogenzapi2 objects matching this query up to 'max-records'
                will be returned.
        
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
        return self.request( "autogenzapi2-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ Autogenzapi2Info, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ Autogenzapi2Info, 'None' ], False ],
        }, {
            'attributes-list': [ Autogenzapi2Info, True ],
        } )
    
    def autogenzapi3_modify(self, id, name=None):
        """
        auto generated
        
        :param id: id of object
        
        :param name: name of object
        """
        return self.request( "autogenzapi3-modify", {
            'id': [ id, 'id', [ int, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def autogenzapi2_destroy(self, id):
        """
        auto generated
        
        :param id: id of object
        """
        return self.request( "autogenzapi2-destroy", {
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
        } )
    
    def autogenzapi3_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        auto generated : Iterate over a list of autogenzapi3 objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                autogenzapi3 object.
                All autogenzapi3 objects matching this query up to 'max-records'
                will be returned.
        
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
        return self.request( "autogenzapi3-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ Autogenzapi3Info, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ Autogenzapi3Info, 'None' ], False ],
        }, {
            'attributes-list': [ Autogenzapi3Info, True ],
        } )
    
    def autogenzapiaction_dummy_autozapi_action_cmd(self, id, name):
        """
        auto generated : a dummy autozapi action ...should get name
        
        :param id: id of object
        
        :param name: some field
        """
        return self.request( "autogenzapiaction-dummy-autozapi-action-cmd", {
            'id': [ id, 'id', [ int, 'None' ], False ],
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def autogenzapi2_create(self, name, field4, field5, id, field1=None, return_record=None):
        """
        auto generated : Create a new autogenzapi2.
        
        :param name: name of object
        
        :param field4: write-noread field4
        
        :param field5: create-noread field5
        
        :param id: id of object
        
        :param field1: optional field1
        
        :param return_record: If set to true, returns the autogenzapi2 on successful creation.
                Default: false
        """
        return self.request( "autogenzapi2-create", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'field1': [ field1, 'field1', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'field4': [ field4, 'field4', [ basestring, 'None' ], False ],
            'field5': [ field5, 'field5', [ basestring, 'None' ], False ],
            'id': [ id, 'id', [ int, 'None' ], False ],
        }, {
            'result': [ Autogenzapi2Info, False ],
        } )
