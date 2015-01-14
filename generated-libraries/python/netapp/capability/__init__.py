from netapp.connection import NaConnection
from image import Image # 0 properties
from capability_get_iter_key_td import CapabilityGetIterKeyTd # 2 properties

class CapabilityConnection(NaConnection):
    
    def capability_load_manifest_shim(self, image):
        """
        auto generated : UNIT TEST: Replicate local capability manifest.
        
        :param image: The image directory from which to laad the manifest.
                Possible values:
                <ul>
                <li> "default"   - Default image,
                <li> "current"   - Current image
                </ul>
        """
        return self.request( "capability-load-manifest-shim", {
            'image': [ image, 'image', [ basestring, 'image' ], False ],
        }, {
        } )
    
    def capability_is_enabled(self, cap_in):
        """
        auto generated : UNIT TEST: Given a list of capabilities return
        which ones are enabled.
        
        :param cap_in: The set of capabilities to check.
        """
        return self.request( "capability-is-enabled", {
            'cap_in': [ cap_in, 'cap-in', [ basestring, 'None' ], True ],
        }, {
            'cap-out': [ basestring, True ],
        } )
    
    def capability_can_join_shim(self, local_ip, member_ip):
        """
        auto generated : UNIT TEST: simulate what join code will do.
        
        :param local_ip: Local Node IP
        
        :param member_ip: Member clus IP
        """
        return self.request( "capability-can-join-shim", {
            'local_ip': [ local_ip, 'local-ip', [ basestring, 'ip-address' ], False ],
            'member_ip': [ member_ip, 'member-ip', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def capability_disable(self, capabilities):
        """
        auto generated : UNIT TEST: Disable capabilities for every node.
        
        :param capabilities: Capabilities
        """
        return self.request( "capability-disable", {
            'capabilities': [ capabilities, 'capabilities', [ basestring, 'None' ], True ],
        }, {
        } )
    
    def capability_get(self, node, capability, desired_attributes=None):
        """
        Get the attributes of the capability.
        
        :param node: The name of the node in which the capability is installed.
        
        :param capability: The capability name.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "capability-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'capability': [ capability, 'capability', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CapabilityInfo, 'None' ], False ],
        }, {
            'attributes': [ CapabilityInfo, False ],
        } )
    
    def capability_downgrade_prepare_shim(self):
        """
        auto generated : UNIT TEST: Prevent capabilities from be used
        during revert/downgrade.
        """
        return self.request( "capability-downgrade-prepare-shim", {
        }, {
            'missing-capabilities': [ basestring, True ],
        } )
    
    def capability_mark_local_node_enable_ready(self, cap_in):
        """
        auto generated : UNIT TEST: Mark the given list of capabilities
        as enable-ready.
        
        :param cap_in: The set of capabilities to mark enable-ready.
        """
        return self.request( "capability-mark-local-node-enable-ready", {
            'cap_in': [ cap_in, 'cap-in', [ basestring, 'None' ], True ],
        }, {
            'cap-out': [ basestring, True ],
        } )
    
    def capability_is_enabled_during_downgrade_shim(self, capability):
        """
        auto generated : UNIT TEST: Peek through hole in capability
        fence.
        
        :param capability: Capability to check.
        """
        return self.request( "capability-is-enabled-during-downgrade-shim", {
            'capability': [ capability, 'capability', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def capability_can_be_enabled(self, cap_in):
        """
        Check whether or not capabilities can be enabled in the cluster.
        A capability can be enabled if-and-only-if it is installed on
        every node.
        
        :param cap_in: The set of capabilities to check.
        """
        return self.request( "capability-can-be-enabled", {
            'cap_in': [ cap_in, 'cap-in', [ basestring, 'None' ], True ],
        }, {
            'cap-out': [ basestring, True ],
        } )
    
    def capability_node_is_enabled(self, node, capability):
        """
        auto generated : UNIT TEST: Check if given capability is
        enabled.
        
        :param node: Node
        
        :param capability: Capability to check.
        """
        return self.request( "capability-node-is-enabled", {
            'node': [ node, 'node', [ basestring, 'filer-id' ], False ],
            'capability': [ capability, 'capability', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def capability_node_disable(self, node, capability):
        """
        auto generated : UNIT TEST: Disable capability on specified
        node.
        
        :param node: Node
        
        :param capability: Capability to disable
        """
        return self.request( "capability-node-disable", {
            'node': [ node, 'node', [ basestring, 'filer-id' ], False ],
            'capability': [ capability, 'capability', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def capability_is_local_node_enable_ready(self, cap_in):
        """
        auto generated : UNIT TEST: Given a list of capabilities return
        which ones are enable-ready.
        
        :param cap_in: The set of capabilities to check.
        """
        return self.request( "capability-is-local-node-enable-ready", {
            'cap_in': [ cap_in, 'cap-in', [ basestring, 'None' ], True ],
        }, {
            'cap-out': [ basestring, True ],
        } )
    
    def capability_enable(self, cap_in, all_or_none):
        """
        auto generated : UNIT TEST: Enable for every node in the cluster
        if and only if every node has the capability.
        
        :param cap_in: Capabilities to enable
        
        :param all_or_none: Enable all or none
        """
        return self.request( "capability-enable", {
            'cap_in': [ cap_in, 'cap-in', [ basestring, 'None' ], True ],
            'all_or_none': [ all_or_none, 'all-or-none', [ bool, 'None' ], False ],
        }, {
            'cap-out': [ basestring, True ],
        } )
    
    def capability_can_boot_shim(self):
        """
        auto generated : UNIT TEST: Check if local node can continue
        booting.
        """
        return self.request( "capability-can-boot-shim", {
        }, {
        } )
    
    def capability_node_has_capability(self, node, capability):
        """
        auto generated : UNIT TEST: Check if given capability can be
        enabled.
        
        :param node: Node
        
        :param capability: Capability to check.
        """
        return self.request( "capability-node-has-capability", {
            'node': [ node, 'node', [ basestring, 'filer-id' ], False ],
            'capability': [ capability, 'capability', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def capability_software_update_check_shim(self, image_name):
        """
        auto generated : UNIT TEST: Software update image check
        
        :param image_name: Image name: image1 or image2
        """
        return self.request( "capability-software-update-check-shim", {
            'image_name': [ image_name, 'image-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def capability_recommend_release_shim(self, cap_in):
        """
        auto generated : UNIT TEST: Recommend a release having specified
        capabilities.
        
        :param cap_in: The set of capabilities to base recommendation on.
        """
        return self.request( "capability-recommend-release-shim", {
            'cap_in': [ cap_in, 'cap-in', [ basestring, 'None' ], True ],
        }, {
        } )
    
    def capability_node_enable(self, node, capability):
        """
        auto generated : UNIT TEST: Enable capability on specified node.
        
        :param node: Node
        
        :param capability: Capability to enable
        """
        return self.request( "capability-node-enable", {
            'node': [ node, 'node', [ basestring, 'filer-id' ], False ],
            'capability': [ capability, 'capability', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def capability_get_cluster_set(self):
        """
        Get list of capabilities where each capability is installed on
        every node in the cluster.
        """
        return self.request( "capability-get-cluster-set", {
        }, {
            'capabilities': [ basestring, True ],
        } )
    
    def capability_downgrade_commit_shim(self):
        """
        auto generated : UNIT TEST: Replicate the default image's
        manifest.
        """
        return self.request( "capability-downgrade-commit-shim", {
        }, {
            'missing-capabilities': [ basestring, True ],
        } )
    
    def capability_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of capability objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                capability object.
                All capability objects matching this query up to 'max-records'
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
        return self.request( "capability-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CapabilityInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CapabilityInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CapabilityInfo, True ],
        } )
    
    def capability_replicate_manifest_for_join_shim(self):
        """
        auto generated : UNIT TEST: Replicate manifest for join.
        """
        return self.request( "capability-replicate-manifest-for-join-shim", {
        }, {
        } )
