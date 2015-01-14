from netapp.connection import NaConnection
from flexcache_info import FlexcacheInfo # 11 properties
from flexcache_get_iter_key_td import FlexcacheGetIterKeyTd # 2 properties
from flexcache_cache_policy_get_iter_key_td import FlexcacheCachePolicyGetIterKeyTd # 2 properties
from flexcache_cache_policy_info import FlexcacheCachePolicyInfo # 9 properties

class FlexcacheConnection(NaConnection):
    
    def flexcache_cache_policy_modify(self, vserver, cache_policy_name, deleg_lru_timeout=None, time_to_live_files=None, time_to_live_metafiles=None, time_to_live_symbolic=None, prefer_local_cache=None, time_to_live_other=None, time_to_live_directories=None):
        """
        Modify the attributes of flexcache-cache-policy object.
        
        :param vserver: The name of the managing Vserver. Maximum length is 255
                characters.
        
        :param cache_policy_name: The name of the FlexCache Cache Policy being created, modified or
                deleted. The maximum length is 255 characters.
        
        :param deleg_lru_timeout: The Timeout for the Delegations LRU represents the time in
                seconds since the last use of the delegation, after which a Cache
                considers it unused and returns it to Origin.
        
        :param time_to_live_files: The Time To Live (TTL) for files represents the time, in seconds,
                that attributes and data of a file are served from the Cache
                volume before they are verified with the Origin volume.
        
        :param time_to_live_metafiles: The Time To Live (TTL) for ONTAP Metafiles represents the time,
                in seconds, that attributes and data of an ONTAP Metafile are
                served from the Cache volume before they are verified with the
                Origin volume.
        
        :param time_to_live_symbolic: The Time To Live (TTL) for Symbolic Links represents the time, in
                seconds, that attributes and data of a Symbolic Link are served
                from the Cache volume before they are verified with the Origin
                volume.
        
        :param prefer_local_cache: If set to true, data is served from the local cache, otherwise
                from the local origin.
        
        :param time_to_live_other: The Time To Live (TTL) for any file that doesn't fall into the
                other TTL categories represents the time, in seconds, that
                attributes and data of that file are served from the Cache volume
                before they are verified with the Origin volume.
        
        :param time_to_live_directories: The Time To Live (TTL) for Directories represents the time, in
                seconds, that attributes and data of a Directory are served from
                the Cache volume before they are verified with the Origin
                volume.
        """
        return self.request( "flexcache-cache-policy-modify", {
            'deleg_lru_timeout': [ deleg_lru_timeout, 'deleg-lru-timeout', [ int, 'None' ], False ],
            'time_to_live_files': [ time_to_live_files, 'time-to-live-files', [ int, 'None' ], False ],
            'time_to_live_metafiles': [ time_to_live_metafiles, 'time-to-live-metafiles', [ int, 'None' ], False ],
            'time_to_live_symbolic': [ time_to_live_symbolic, 'time-to-live-symbolic', [ int, 'None' ], False ],
            'prefer_local_cache': [ prefer_local_cache, 'prefer-local-cache', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'time_to_live_other': [ time_to_live_other, 'time-to-live-other', [ int, 'None' ], False ],
            'cache_policy_name': [ cache_policy_name, 'cache-policy-name', [ basestring, 'None' ], False ],
            'time_to_live_directories': [ time_to_live_directories, 'time-to-live-directories', [ int, 'None' ], False ],
        }, {
        } )
    
    def flexcache_delete(self, vserver, origin_volume):
        """
        Delete cluster-wide caching for a given volume.
        
        :param vserver: Vserver Name
        
        :param origin_volume: Origin Volume Name
        """
        return self.request( "flexcache-delete", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'origin_volume': [ origin_volume, 'origin-volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def flexcache_cache_policy_get(self, vserver, cache_policy_name, desired_attributes=None):
        """
        Get the attributes of the flexcache-cache-policy.
        
        :param vserver: The name of the managing Vserver. Maximum length is 255
                characters.
        
        :param cache_policy_name: The name of the FlexCache Cache Policy being created, modified or
                deleted. The maximum length is 255 characters.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "flexcache-cache-policy-get", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FlexcacheCachePolicyInfo, 'None' ], False ],
            'cache_policy_name': [ cache_policy_name, 'cache-policy-name', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ FlexcacheCachePolicyInfo, False ],
        } )
    
    def flexcache_create(self, vserver, origin_volume):
        """
        Create cluster-wide caching for a given volume.
        
        :param vserver: Vserver
        
        :param origin_volume: Origin Volume Name
        """
        return self.request( "flexcache-create", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'origin_volume': [ origin_volume, 'origin-volume', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def flexcache_cache_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of flexcache-cache-policy objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                flexcache-cache-policy object.
                All flexcache-cache-policy objects matching this query up to
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
        return self.request( "flexcache-cache-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FlexcacheCachePolicyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FlexcacheCachePolicyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FlexcacheCachePolicyInfo, True ],
        } )
    
    def flexcache_get(self, cache_volume, desired_attributes=None):
        """
        Get the attributes of the flexcache.
        
        :param cache_volume: Cache Volume Name
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "flexcache-get", {
            'cache_volume': [ cache_volume, 'cache-volume', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FlexcacheInfo, 'None' ], False ],
        }, {
            'attributes': [ FlexcacheInfo, False ],
        } )
    
    def flexcache_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of flexcache objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                flexcache object.
                All flexcache objects matching this query up to 'max-records'
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
        return self.request( "flexcache-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ FlexcacheInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ FlexcacheInfo, 'None' ], False ],
        }, {
            'attributes-list': [ FlexcacheInfo, True ],
        } )
    
    def flexcache_cache_policy_create(self, time_to_live_files, vserver, cache_policy_name, time_to_live_directories, deleg_lru_timeout=None, time_to_live_metafiles=None, return_record=None, time_to_live_symbolic=None, prefer_local_cache=None, time_to_live_other=None):
        """
        Create a new flexcache-cache-policy.
        
        :param time_to_live_files: The Time To Live (TTL) for files represents the time, in seconds,
                that attributes and data of a file are served from the Cache
                volume before they are verified with the Origin volume.
        
        :param vserver: The name of the managing Vserver. Maximum length is 255
                characters.
        
        :param cache_policy_name: The name of the FlexCache Cache Policy being created, modified or
                deleted. The maximum length is 255 characters.
        
        :param time_to_live_directories: The Time To Live (TTL) for Directories represents the time, in
                seconds, that attributes and data of a Directory are served from
                the Cache volume before they are verified with the Origin
                volume.
        
        :param deleg_lru_timeout: The Timeout for the Delegations LRU represents the time in
                seconds since the last use of the delegation, after which a Cache
                considers it unused and returns it to Origin.
        
        :param time_to_live_metafiles: The Time To Live (TTL) for ONTAP Metafiles represents the time,
                in seconds, that attributes and data of an ONTAP Metafile are
                served from the Cache volume before they are verified with the
                Origin volume.
        
        :param return_record: If set to true, returns the flexcache-cache-policy on successful
                creation.
                Default: false
        
        :param time_to_live_symbolic: The Time To Live (TTL) for Symbolic Links represents the time, in
                seconds, that attributes and data of a Symbolic Link are served
                from the Cache volume before they are verified with the Origin
                volume.
        
        :param prefer_local_cache: If set to true, data is served from the local cache, otherwise
                from the local origin.
        
        :param time_to_live_other: The Time To Live (TTL) for any file that doesn't fall into the
                other TTL categories represents the time, in seconds, that
                attributes and data of that file are served from the Cache volume
                before they are verified with the Origin volume.
        """
        return self.request( "flexcache-cache-policy-create", {
            'deleg_lru_timeout': [ deleg_lru_timeout, 'deleg-lru-timeout', [ int, 'None' ], False ],
            'time_to_live_files': [ time_to_live_files, 'time-to-live-files', [ int, 'None' ], False ],
            'time_to_live_metafiles': [ time_to_live_metafiles, 'time-to-live-metafiles', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'time_to_live_symbolic': [ time_to_live_symbolic, 'time-to-live-symbolic', [ int, 'None' ], False ],
            'prefer_local_cache': [ prefer_local_cache, 'prefer-local-cache', [ bool, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'time_to_live_other': [ time_to_live_other, 'time-to-live-other', [ int, 'None' ], False ],
            'cache_policy_name': [ cache_policy_name, 'cache-policy-name', [ basestring, 'None' ], False ],
            'time_to_live_directories': [ time_to_live_directories, 'time-to-live-directories', [ int, 'None' ], False ],
        }, {
            'result': [ FlexcacheCachePolicyInfo, False ],
        } )
    
    def flexcache_cache_policy_destroy(self, vserver, cache_policy_name):
        """
        Delete an existing flexcache-cache-policy object.
        
        :param vserver: The name of the managing Vserver. Maximum length is 255
                characters.
        
        :param cache_policy_name: The name of the FlexCache Cache Policy being created, modified or
                deleted. The maximum length is 255 characters.
        """
        return self.request( "flexcache-cache-policy-destroy", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'cache_policy_name': [ cache_policy_name, 'cache-policy-name', [ basestring, 'None' ], False ],
        }, {
        } )
