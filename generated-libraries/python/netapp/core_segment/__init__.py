from netapp.connection import NaConnection
from coreseg_status import CoresegStatus # 0 properties
from core_segment_status_get_iter_key_td import CoreSegmentStatusGetIterKeyTd # 3 properties
from core_segment_status_info import CoreSegmentStatusInfo # 5 properties
from core_segment_config_info import CoreSegmentConfigInfo # 3 properties
from core_segment_info import CoreSegmentInfo # 8 properties
from core_segment_get_iter_key_td import CoreSegmentGetIterKeyTd # 3 properties

class CoreSegmentConnection(NaConnection):
    
    def core_segment_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Returns a list of core segments.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                core-segment object.
                All core-segment objects matching this query up to 'max-records'
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
        return self.request( "core-segment-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CoreSegmentInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CoreSegmentInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CoreSegmentInfo, True ],
        } )
    
    def core_segment_config_get(self, node, desired_attributes=None):
        """
        Get the attributes of the core-segment-config.
        
        :param node: Node to which this core segment configuration belongs.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "core-segment-config-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CoreSegmentConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ CoreSegmentConfigInfo, False ],
        } )
    
    def core_segment_get(self, node, segment, owner_node=None, desired_attributes=None):
        """
        Returns the attributes of the specified core segment.
        
        :param node: Node
        
        :param segment: Name of the Core Segment File
        
        :param owner_node: Node that owns the Core Segment.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "core-segment-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'owner_node': [ owner_node, 'owner-node', [ basestring, 'None' ], False ],
            'segment': [ segment, 'segment', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CoreSegmentInfo, 'None' ], False ],
        }, {
            'attributes': [ CoreSegmentInfo, False ],
        } )
    
    def core_segment_status_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return a status of a list of core segmentation jobs.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                core-segment-status object.
                All core-segment-status objects matching this query up to
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
        return self.request( "core-segment-status-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CoreSegmentStatusInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CoreSegmentStatusInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CoreSegmentStatusInfo, True ],
        } )
    
    def core_segment_config_modify(self, node, is_auto_segment=None, is_auto_delete=None):
        """
        Modify the attributes of core-segment-config object.
        
        :param node: Node to which this core segment configuration belongs.
        
        :param is_auto_segment: If true, enables automatic core segmenting after saving of a full
                core.
        
        :param is_auto_delete: If true, enables deletion of full core after automatic core
                segmenting.
        """
        return self.request( "core-segment-config-modify", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'is_auto_segment': [ is_auto_segment, 'is-auto-segment', [ bool, 'None' ], False ],
            'is_auto_delete': [ is_auto_delete, 'is-auto-delete', [ bool, 'None' ], False ],
        }, {
        } )
    
    def core_segment_delete_all(self, node, owner_node=None):
        """
        Deletes all core segments.
        
        :param node: Node
        
        :param owner_node: Node whose core segments will be deleted.
        """
        return self.request( "core-segment-delete-all", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'owner_node': [ owner_node, 'owner-node', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def core_segment_destroy(self, node, segment, owner_node=None):
        """
        Delete a single core segment
        
        :param node: Node
        
        :param segment: Name of the Core Segment File
        
        :param owner_node: Node that owns the Core Segment.
        """
        return self.request( "core-segment-destroy", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'owner_node': [ owner_node, 'owner-node', [ basestring, 'None' ], False ],
            'segment': [ segment, 'segment', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def core_segment_stop(self, node, job_id):
        """
        Stops the Core Segmentation Job.
        
        :param node: Node
        
        :param job_id: Core Segmentation job to be stopped.
        """
        return self.request( "core-segment-stop", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def core_segment_start(self, node, core_name, owner_node=None, is_delete_core=None):
        """
        Starts the core segmentation of specified Full Core File. Use
        core-segment-status-get to check the status of the core
        segmentation job.
        
        :param node: Node which will do the core segmentation.
        
        :param core_name: Full Core file to be segmented. File name is relative to the
                crash directory.
        
        :param owner_node: Node whose Full Core will be segmented. If not specifies, it
                defaults to the local node.
        
        :param is_delete_core: If true, the Full Core will be deleted after segmenting. The
                default value is not to delete the Full Core after segmenting.
        """
        return self.request( "core-segment-start", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'owner_node': [ owner_node, 'owner-node', [ basestring, 'None' ], False ],
            'is_delete_core': [ is_delete_core, 'is-delete-core', [ bool, 'None' ], False ],
            'core_name': [ core_name, 'core-name', [ basestring, 'None' ], False ],
        }, {
            'job-id': [ int, False ],
        } )
