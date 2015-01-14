from netapp.connection import NaConnection
from options_modify_iter_info import OptionsModifyIterInfo # 3 properties
from option_info import OptionInfo # 8 properties
from options_modify_iter_key_td import OptionsModifyIterKeyTd # 2 properties
from options_get_iter_key_td import OptionsGetIterKeyTd # 2 properties

class OptionsConnection(NaConnection):
    
    def options_list_info(self):
        """
        Get a list of all options
        """
        return self.request( "options-list-info", {
        }, {
            'options': [ OptionInfo, True ],
        } )
    
    def options_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of options objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                options object.
                All options objects matching this query up to 'max-records' will
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
        return self.request( "options-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ OptionInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ OptionInfo, 'None' ], False ],
        }, {
            'attributes-list': [ OptionInfo, True ],
        } )
    
    def options_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of options or a group of
        options objects.
        
        :param query: If modifying a specific options, this input element must specify
                all keys.
                If modifying options objects based on query, this input element
                must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching options
                even when the modification of a previous matching options fails,
                and do so until the total number of objects failed to be modified
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of options objects
                (just keys) that were successfully updated.
                If set to false, the list of options objects modified will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple options objects match
                a given query.
                If set to true, the API will continue modifying the next matching
                options even when modification of a previous options fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of options objects
                (just keys) that were not modified due to some error.
                If set to false, the list of options objects not modified will
                not be returned.
                Default: true
        """
        return self.request( "options-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ OptionInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ OptionInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ OptionsModifyIterInfo, True ],
            'failure-list': [ OptionsModifyIterInfo, True ],
        } )
    
    def options_set(self, name, value):
        """
        Set the value of a single option.
        For complete list of names and values of options,
        please refer to options man pages.
        
        :param name: Name of the option.
        
        :param value: Value of the option.
        """
        return self.request( "options-set", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'value': [ value, 'value', [ basestring, 'None' ], False ],
        }, {
            'message': [ basestring, False ],
            'cluster-constraint': [ basestring, False ],
        } )
    
    def options_get(self, name):
        """
        Get the value of a single option.
        
        :param name: Name of the option.
        """
        return self.request( "options-get", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
            'cluster-constraint': [ basestring, False ],
            'value': [ basestring, False ],
        } )
