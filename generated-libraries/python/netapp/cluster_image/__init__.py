from netapp.connection import NaConnection
from cluster_image_info import ClusterImageInfo # 3 properties

class ClusterImageConnection(NaConnection):
    
    def cluster_image_get(self, node_id, desired_attributes=None):
        """
        Get the attributes of the cluster-image.
        
        :param node_id: Node
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cluster-image-get", {
            'node_id': [ node_id, 'node-id', [ basestring, 'node-name' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ClusterImageInfo, 'None' ], False ],
        }, {
            'attributes': [ ClusterImageInfo, False ],
        } )
