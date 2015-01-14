from netapp.connection import NaConnection
from instance_info import InstanceInfo # 2 properties
from enabled_preset import EnabledPreset # 1 properties
from filter import Filter # 0 properties
from counter_data import CounterData # 2 properties
from filter_data import FilterData # 0 properties
from aggregation_data import AggregationData # 2 properties
from preset_info import PresetInfo # 8 properties
from counter_info import CounterInfo # 11 properties
from archive_config_info import ArchiveConfigInfo # 6 properties
from object_info import ObjectInfo # 4 properties
from perf_archive_get_iter_key_td import PerfArchiveGetIterKeyTd # 1 properties
from preset_detail_info import PresetDetailInfo # 5 properties
from archive_record import ArchiveRecord # 1 properties
from instance_uuid import InstanceUuid # 0 properties
from label_info import LabelInfo # 0 properties
from perf_archive_info import PerfArchiveInfo # 10 properties
from instance_data import InstanceData # 4 properties
from counter import Counter # 0 properties
from archive_header import ArchiveHeader # 1 properties
from instance import Instance # 0 properties
from perf_preset_get_iter_key_td import PerfPresetGetIterKeyTd # 2 properties
from perf_object_instance_list_info_iter_key_td import PerfObjectInstanceListInfoIterKeyTd # 3 properties
from performance_archive_state import PerformanceArchiveState # 0 properties

class PerfConnection(NaConnection):
    
    def perf_object_instance_list_info(self, objectname):
        """
        Get the list of names of current instances of an object.
        This will return the names of all current instances of the
        specified object with one call.  If the object is expected to
        have a large number of instances, the iterator version
        of this API should be used.
        
        :param objectname: Name of the object to get instance information for.
        """
        return self.request( "perf-object-instance-list-info", {
            'objectname': [ objectname, 'objectname', [ basestring, 'None' ], False ],
        }, {
            'instances': [ InstanceInfo, True ],
        } )
    
    def perf_archive_config_modify(self, datastore_file_rotation=None, datastore_max_percent=None, datastore_max_retention=None, is_enabled=None):
        """
        Modify the current Performance Archive configuration
        
        :param datastore_file_rotation: Minutes Between Performance Archive Data File Rotations
        
        :param datastore_max_percent: Maximum Percentage of Root Volume Used for Performance Archive
                Data
        
        :param datastore_max_retention: Days to Retain Performance Archive Data
        
        :param is_enabled: Is the Performance Archive Enabled?
        """
        return self.request( "perf-archive-config-modify", {
            'datastore_file_rotation': [ datastore_file_rotation, 'datastore-file-rotation', [ int, 'None' ], False ],
            'datastore_max_percent': [ datastore_max_percent, 'datastore-max-percent', [ int, 'None' ], False ],
            'datastore_max_retention': [ datastore_max_retention, 'datastore-max-retention', [ int, 'None' ], False ],
            'is_enabled': [ is_enabled, 'is-enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def perf_preset_create(self, preset, comment=None, preset_detail_infos=None, is_archive_enabled=None, expiration_length=None, privilege=None):
        """
        Create a single Performance Preset configuration and all of its
        details
        
        :param preset: Preset Name
        
        :param comment: Preset Description
        
        :param preset_detail_infos: Details of the Performance Preset
        
        :param is_archive_enabled: Is Preset Enabled?
        
        :param expiration_length: Default expiration length (in minutes) until the Performance
                Preset will be automatically disabled.
        
        :param privilege: Privilege level
                <br/>Possible Values: admin, advanced, diagnostic
        """
        return self.request( "perf-preset-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'preset_detail_infos': [ preset_detail_infos, 'preset-detail-infos', [ PresetDetailInfo, 'None' ], True ],
            'is_archive_enabled': [ is_archive_enabled, 'is-archive-enabled', [ bool, 'None' ], False ],
            'expiration_length': [ expiration_length, 'expiration-length', [ int, 'None' ], False ],
            'privilege': [ privilege, 'privilege', [ basestring, 'None' ], False ],
            'preset': [ preset, 'preset', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def perf_archive_get_instances_iter_next(self, tag, maximum):
        """
        Continue retrieving the instances of an archive.
        When the 'records' output element is 0, all
        instance data have been retrieved and the
        perf-object-instance-list-info-iter-end API should be called.
        
        :param tag: Tag from earlier call to perf-object-instance-list-info-iter-start
                Note that any tag not used for 1 hour will be deleted.
        
        :param maximum: Maximum number of records to retrieve with this call.<b>
                Range: [0..2^31-1]
        """
        return self.request( "perf-archive-get-instances-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'generation': [ int, False ],
            'records': [ int, False ],
            'archive-records': [ ArchiveRecord, True ],
        } )
    
    def perf_archive_get_instances_iter_end(self, tag):
        """
        Terminate a perf-archive-get-instances iterator.
        
        :param tag: Tag from a previous perf-archive-get-instances-iter-start
        """
        return self.request( "perf-archive-get-instances-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def perf_archive_destroy(self, archive):
        """
        Destroy a Performance Archive
        
        :param archive: Performance Archive Name
        """
        return self.request( "perf-archive-destroy", {
            'archive': [ archive, 'archive', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def perf_archive_config_get(self, desired_attributes=None):
        """
        Display the current Performance Archive configuration
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "perf-archive-config-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ArchiveConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ ArchiveConfigInfo, False ],
        } )
    
    def perf_object_instance_list_info_iter_end(self, tag):
        """
        Terminate a perf-object-instance-list-info iterator.
        
        :param tag: Tag from a previous perf-object-instance-list-info-iter-start
        """
        return self.request( "perf-object-instance-list-info-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def perf_object_instance_list_info_iter_start(self, objectname):
        """
        Begin retrieving the names of instances of an object. This
        call should be followed with one or more calls to
        perf-object-instance-list-info-iter-next
        
        :param objectname: Name of the object to get instance information for.
        """
        return self.request( "perf-object-instance-list-info-iter-start", {
            'objectname': [ objectname, 'objectname', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def perf_object_get_instances_iter_end(self, tag):
        """
        Terminate a perf-object-get-instances iterator.
        
        :param tag: Tag from a pervious perf-object-get-instances-iter-start
        """
        return self.request( "perf-object-get-instances-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def perf_preset_modify(self, preset, comment=None, privilege=None, is_archive_enabled=None, new_name=None):
        """
        Modify a Performance Preset
        
        :param preset: Preset Name
        
        :param comment: Preset Description
        
        :param privilege: Preset Privilege Level
        
        :param is_archive_enabled: Is Preset Archive-Enabled?
        
        :param new_name: New Preset Name
        """
        return self.request( "perf-preset-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'privilege': [ privilege, 'privilege', [ basestring, 'privilege-level' ], False ],
            'is_archive_enabled': [ is_archive_enabled, 'is-archive-enabled', [ bool, 'None' ], False ],
            'preset': [ preset, 'preset', [ basestring, 'None' ], False ],
            'new_name': [ new_name, 'new-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def perf_object_get_instances_iter_next(self, tag, maximum):
        """
        Continue retrieving the values of counters of instances of an
        object.  This call will return a partial list instance names,
        continued from the previous call with the same tag.  When the
        'records' output element is 0, all counter values of all instances
        have been retrieved and the perf-object-instance-list-info-iter-end
        API should be called.
        
        :param tag: Tag from a previous perf-object-get-instances-iter-start
        
        :param maximum: Maximum number of entries to retrieve with this call.<br>
                Range: [0..2^31-1]
        """
        return self.request( "perf-object-get-instances-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'instances': [ InstanceData, True ],
        } )
    
    def perf_preset_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iteratively get information about Performance Presets
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                perf-preset object.
                All perf-preset objects matching this query up to 'max-records'
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
        return self.request( "perf-preset-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ PresetInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ PresetInfo, 'None' ], False ],
        }, {
            'attributes-list': [ PresetInfo, True ],
        } )
    
    def perf_archive_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iteratively get information about Performance Archives
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                perf-archive object.
                All perf-archive objects matching this query up to 'max-records'
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
        return self.request( "perf-archive-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ PerfArchiveInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ PerfArchiveInfo, 'None' ], False ],
        }, {
            'attributes-list': [ PerfArchiveInfo, True ],
        } )
    
    def perf_preset_detail_get(self, preset):
        """
        Get detailed information about a single Performance Preset configuration
        
        :param preset: Preset Name
        """
        return self.request( "perf-preset-detail-get", {
            'preset': [ preset, 'preset', [ basestring, 'None' ], False ],
        }, {
            'comment': [ basestring, False ],
            'uuid': [ basestring, False ],
            'is-read-only': [ bool, False ],
            'generation-id': [ int, False ],
            'preset': [ basestring, False ],
            'expiration-length': [ int, False ],
            'expiration-end-date': [ int, False ],
            'privilege': [ basestring, False ],
            'is-archive-enabled': [ bool, False ],
            'preset-detail-infos': [ PresetDetailInfo, True ],
        } )
    
    def perf_archive_create(self, end_time, start_time, archive, comment=None, case_number=None, source_nodes=None):
        """
        Save a new Performance Archive
        
        :param end_time: End of Performance Archive's time range (UTC)
        
        :param start_time: Start of Performance Archive's time range (UTC)
        
        :param archive: Performance Archive Name
        
        :param comment: Performance Archive Comment
        
        :param case_number: Support Case Number Associated with Archive
        
        :param source_nodes: Originating Nodes for Archive Data
        """
        return self.request( "perf-archive-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'end_time': [ end_time, 'end-time', [ int, 'None' ], False ],
            'start_time': [ start_time, 'start-time', [ int, 'None' ], False ],
            'case_number': [ case_number, 'case-number', [ basestring, 'None' ], False ],
            'source_nodes': [ source_nodes, 'source-nodes', [ basestring, 'node-name' ], True ],
            'archive': [ archive, 'archive', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result': [ PerfArchiveInfo, False ],
            'result-status': [ basestring, False ],
        } )
    
    def perf_object_get_instances(self, objectname, instance_uuids=None, filter_data=None, privilege_level=None, instances=None, counters=None):
        """
        Get a list of current counter values of instances of an object. This will
        return the values of all specified counters and instances of the specified
        object with one call.<p>
        In Data ONTAP 7-Mode, if the object is expected to have a large number of
        instances and/or counters, the iterator version of this API should be
        used.
        
        :param objectname: Name of the object to get counter values for.
        
        :param instance_uuids: List of instance UUIDs for which to get counter values. This element
                can be used to limit data collection to a specified subset of the
                instances of the object. Either instances or instance-uuids input
                must be provided. The API errors out if both of these inputs are
                provided or neither of these inputs is provided, or if more than 500
                instances are requested.
        
        :param filter_data: Filter to apply to the performance data.
        
        :param privilege_level: Name of the privilege level. Possible values: "basic", "admin", "advanced", "diag"
                If the element is absent, the default privilege of the object will be used.
        
        :param instances: List of instance names for which to get counter values. This element
                can be used to limit data collection to a specified subset of the
                instances of the object.<p>
                In Data ONTAP 7-Mode, counter values of all instances of the object
                will be retrieved when this element is absent.<p>
                In Data ONTAP Cluster-Mode, either instances or instance-uuids input
                must be provided. The API errors out if both of these inputs are
                provided or neither of these inputs is provided, or if more than 500
                instances are requested.
        
        :param counters: List of counters whose values will be retrieved. This element can
                be used to limit data collection to a specified subset of the counters
                of instances of the object.  If this element is absent, values of all
                counters will be retrieved.
        """
        return self.request( "perf-object-get-instances", {
            'instance_uuids': [ instance_uuids, 'instance-uuids', [ basestring, 'instance-uuid' ], True ],
            'filter_data': [ filter_data, 'filter-data', [ basestring, 'filter-data' ], False ],
            'objectname': [ objectname, 'objectname', [ basestring, 'None' ], False ],
            'privilege_level': [ privilege_level, 'privilege-level', [ basestring, 'None' ], False ],
            'instances': [ instances, 'instances', [ basestring, 'instance' ], True ],
            'counters': [ counters, 'counters', [ basestring, 'counter' ], True ],
        }, {
            'timestamp': [ basestring, False ],
            'instances': [ InstanceData, True ],
        } )
    
    def perf_preset_delete(self, preset):
        """
        Delete a Performance Preset and all of its Preset Details
        
        :param preset: Preset Name
        """
        return self.request( "perf-preset-delete", {
            'preset': [ preset, 'preset', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def perf_archive_get_headers(self, duration, timestamp):
        """
        Retrieve all headers available of archive datafiles.
        This call should be preceded by a call to
        perf-archive-get-oldest-timestamp, otherwise an error may
        be returned if the input timestamp is too old.
        
        :param duration: Duration in milliseconds to retrieve headers
                A zero value duration signifies to go until the most recent timestamp.
                Range: [0..2^31-1]
        
        :param timestamp: Timestamp (in seconds, Unix Epoch Time) to start searching for headers.
                Range: [0..2^31-1]
        """
        return self.request( "perf-archive-get-headers", {
            'duration': [ duration, 'duration', [ int, 'None' ], False ],
            'timestamp': [ timestamp, 'timestamp', [ basestring, 'None' ], False ],
        }, {
            'archive-headers': [ ArchiveHeader, True ],
        } )
    
    def perf_archive_get_oldest_timestamp(self):
        """
        Retrieve the oldest timestamp available.
        """
        return self.request( "perf-archive-get-oldest-timestamp", {
        }, {
            'timestamp': [ int, False ],
        } )
    
    def perf_object_instance_list_info_iter_next(self, tag, maximum):
        """
        Continue retrieving the names of instances of an object.  This call
        will return a partial list instance names, continued from the previous
        call with the same name.  When the 'records' output element is 0, all
        instance names have been retrieved and the
        perf-object-instance-list-info-iter-end API should be called.
        
        :param tag: Tag from earlier call to perf-object-instance-list-info-iter-start
        
        :param maximum: Maximum number of instance names to retrieve with this call.<b>
                Range: [0..2^31-1]
        """
        return self.request( "perf-object-instance-list-info-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'instances': [ InstanceInfo, True ],
        } )
    
    def perf_object_get_instances_iter_start(self, objectname, instances=None, counters=None):
        """
        Begin retrieving the counter values of instances of an object.
        This call should be followed with one or more calls to
        perf-object-get-instances-iter-next
        
        :param objectname: Name of the object to get counter values for.
        
        :param instances: List of instances to get counter values for.  This element can be
                used to limit data collection to a specified subset of the instances of
                the object.  If this element is absent, counter values of all instances
                of the object will be retrieved.
        
        :param counters: List of counters whose values will be retrieved. This element can
                be used to limit data collection to a specified subset of the counters
                of instances of the object.  If this element is absent, values of all
                counters will be retrieved.
        """
        return self.request( "perf-object-get-instances-iter-start", {
            'instances': [ instances, 'instances', [ basestring, 'instance' ], True ],
            'objectname': [ objectname, 'objectname', [ basestring, 'None' ], False ],
            'counters': [ counters, 'counters', [ basestring, 'counter' ], True ],
        }, {
            'timestamp': [ basestring, False ],
            'tag': [ basestring, False ],
            'records': [ int, False ],
        } )
    
    def perf_object_counter_list_info(self, objectname, filter_data=None):
        """
        Get information about the counters of an object.  This information
        is static and independent of any particular instance of the object.
        It includes counter names and descriptions, as well as properties
        which are necessary to to interpret counter values.
        
        :param objectname: Name of the object to get information for.
        
        :param filter_data: Allows selecting counters from a particular node.  An example filter is "node_name=hostname".<br><br>
                This element is <b>deprecated</b> in Data ONTAP 8.2 and later, as filtering by node is
                no longer necessary.  Each node contains the same set of counter definitions,
                so filtering by node yields the same results as not filtering at all.
        """
        return self.request( "perf-object-counter-list-info", {
            'filter_data': [ filter_data, 'filter-data', [ basestring, 'filter-data' ], False ],
            'objectname': [ objectname, 'objectname', [ basestring, 'None' ], False ],
        }, {
            'counters': [ CounterInfo, True ],
        } )
    
    def perf_archive_get_instances_iter_start(self, timestamp):
        """
        Begin retrieving the instances of an archive.
        This call should be followed with one or more calls to
        perf-archive-get-instances-iter-next.
        This call should be preceded by a call to
        perf-archive-get-oldest-timestamp, otherwise an error may
        be returned if the input timestamp is too old.
        
        :param timestamp: Timestamp (in seconds, Unix Epoch Time) to start.
                Range: [0..2^31-1]
        """
        return self.request( "perf-archive-get-instances-iter-start", {
            'timestamp': [ timestamp, 'timestamp', [ basestring, 'None' ], False ],
        }, {
            'tag': [ basestring, False ],
        } )
    
    def perf_object_list_info(self, filter_data=None):
        """
        Get list of performance objects in the system.
        
        :param filter_data: Allows selecting objects from a particular node.  An example filter is "node_name=hostname".  <br><br>
                This element is <b>deprecated</b> in Data ONTAP 8.2 and later as filtering by node is
                no longer necessary.  Each node contains the same set of object definitions,
                so filtering by node yields the same results as not filtering at all.
        """
        return self.request( "perf-object-list-info", {
            'filter_data': [ filter_data, 'filter-data', [ basestring, 'filter-data' ], False ],
        }, {
            'objects': [ ObjectInfo, True ],
        } )
    
    def perf_archive_modify(self, archive, comment=None, case_number=None):
        """
        Modify properties of a Performance Archive
        
        :param archive: Performance Archive Name
        
        :param comment: Performance Archive Comment
        
        :param case_number: Support Case Number Associated with Archive
        """
        return self.request( "perf-archive-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'archive': [ archive, 'archive', [ basestring, 'None' ], False ],
            'case_number': [ case_number, 'case-number', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def perf_object_instance_list_info_iter(self, objectname, filter_data=None, desired_attributes=None, max_records=None, tag=None, query=None):
        """
        Gets the list of names and UUIDs of current instances of an
        object.
        This iterative API will return names and UUIDs of the
        current instances
        of the specified object; the number of records returned
        is specified by
        the max-records input element.<p>
        To retrieve all the instances of the specified object,
        the value of the
        next-tag output element should be passed in as the value
        of the tag
        input element on the subsequent API call.
        
        :param objectname: Name of the object for which to get instance information.
        
        :param filter_data: Filter to apply to instance list; see <a
                href='#filter-data'>filter-data</a> type for details.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 1000
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                perf object.
                All perf objects matching this query up to 'max-records' will be
                returned.
        """
        return self.request( "perf-object-instance-list-info-iter", {
            'filter_data': [ filter_data, 'filter-data', [ basestring, 'None' ], False ],
            'objectname': [ objectname, 'objectname', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ InstanceInfo, 'None' ], False ],
            'max_records': max_records,
            'tag': tag,
            'query': [ query, 'query', [ InstanceInfo, 'None' ], False ],
        }, {
            'attributes-list': [ InstanceInfo, True ],
        } )
