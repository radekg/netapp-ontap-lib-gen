from netapp.connection import NaConnection
from enable import Enable # 0 properties
from vserverid import Vserverid # 0 properties
from security_style import SecurityStyle # 0 properties
from security_trace_results_logs import SecurityTraceResultsLogs # 10 properties
from security_trace_filter_get_iter_key_td import SecurityTraceFilterGetIterKeyTd # 2 properties
from security_trace_filter_attributes import SecurityTraceFilterAttributes # 9 properties
from security_trace_result_show_key_td import SecurityTraceResultShowKeyTd # 3 properties

class SectraceConnection(NaConnection):
    
    def security_trace_filter_create(self, index, time_enabled=None, trace_allow=None, enabled=None, windows_name=None, return_record=None, unix_name=None, path=None, client_ip=None):
        """
        Creates a new Security trace entry.
        
        :param index: internally created index for the filter.
        
        :param time_enabled: The admin can specify a timeout for this filter after which it
                would be disabled.
        
        :param trace_allow: The deny events are traced by default. This option is to record
                trace results for allow events as well.
        
        :param enabled: This is used to enable or disable the filter.
        
        :param windows_name: Windows User Name to trace.
        
        :param return_record: If set to true, returns the security-trace-filter on successful
                creation.
                Default: false
        
        :param unix_name: Unix user name to trace.
        
        :param path: Path to match.
        
        :param client_ip: The IP address of the client.
        """
        return self.request( "security-trace-filter-create", {
            'index': [ index, 'index', [ int, 'None' ], False ],
            'time_enabled': [ time_enabled, 'time-enabled', [ int, 'None' ], False ],
            'trace_allow': [ trace_allow, 'trace-allow', [ bool, 'None' ], False ],
            'enabled': [ enabled, 'enabled', [ basestring, 'enable' ], False ],
            'windows_name': [ windows_name, 'windows-name', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'unix_name': [ unix_name, 'unix-name', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'client_ip': [ client_ip, 'client-ip', [ basestring, 'ip-address' ], False ],
        }, {
            'result': [ SecurityTraceFilterAttributes, False ],
        } )
    
    def security_trace_result_show(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of permission tracing results for the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security-trace-result object.
                All security-trace-result objects matching this query up to
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
        return self.request( "security-trace-result-show", {
            'max_records': max_records,
            'query': [ query, 'query', [ SecurityTraceResultsLogs, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecurityTraceResultsLogs, 'None' ], False ],
        }, {
            'attributes-list': [ SecurityTraceResultsLogs, True ],
        } )
    
    def security_trace_filter_modify(self, index, time_enabled=None, trace_allow=None, enabled=None, windows_name=None, unix_name=None, path=None, client_ip=None):
        """
        Modifies settings of a Security trace entry, even if it is in
        use.
        
        :param index: internally created index for the filter.
        
        :param time_enabled: The admin can specify a timeout for this filter after which it
                would be disabled.
        
        :param trace_allow: The deny events are traced by default. This option is to record
                trace results for allow events as well.
        
        :param enabled: This is used to enable or disable the filter.
        
        :param windows_name: Windows User Name to trace.
        
        :param unix_name: Unix user name to trace.
        
        :param path: Path to match.
        
        :param client_ip: The IP address of the client.
        """
        return self.request( "security-trace-filter-modify", {
            'index': [ index, 'index', [ int, 'None' ], False ],
            'time_enabled': [ time_enabled, 'time-enabled', [ int, 'None' ], False ],
            'trace_allow': [ trace_allow, 'trace-allow', [ bool, 'None' ], False ],
            'enabled': [ enabled, 'enabled', [ basestring, 'enable' ], False ],
            'windows_name': [ windows_name, 'windows-name', [ basestring, 'None' ], False ],
            'unix_name': [ unix_name, 'unix-name', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'client_ip': [ client_ip, 'client-ip', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def security_trace_filter_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Gives information about one or more Security trace entries.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security-trace-filter object.
                All security-trace-filter objects matching this query up to
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
        return self.request( "security-trace-filter-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SecurityTraceFilterAttributes, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SecurityTraceFilterAttributes, 'None' ], False ],
        }, {
            'attributes-list': [ SecurityTraceFilterAttributes, True ],
        } )
    
    def security_trace_result_delete(self, node, seqnum):
        """
        Delete the specified security tracing event record.
        
        :param node: The cluster node on which the permission tracing event occured.
        
        :param seqnum: The sequence number of the permission tracing event.
        """
        return self.request( "security-trace-result-delete", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'seqnum': [ seqnum, 'seqnum', [ int, 'None' ], False ],
        }, {
        } )
    
    def security_trace_filter_delete(self, index):
        """
        Deletes the specified Security trace entry.
        
        :param index: internally created index for the filter.
        """
        return self.request( "security-trace-filter-delete", {
            'index': [ index, 'index', [ int, 'None' ], False ],
        }, {
        } )
