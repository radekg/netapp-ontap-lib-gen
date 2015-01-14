from netapp.connection import NaConnection
from gpo_applied_info_get_iter_key_td import GpoAppliedInfoGetIterKeyTd # 2 properties
from gpo_get_iter_key_td import GpoGetIterKeyTd # 1 properties
from hash_publication_mode import HashPublicationMode # 0 properties
from gpo_gpresult_info_get_iter_key_td import GpoGpresultInfoGetIterKeyTd # 2 properties
from gpo_gpresult_info import GpoGpresultInfo # 18 properties
from hash_version_type import HashVersionType # 0 properties
from gpo_config import GpoConfig # 2 properties
from gpo_applied_info import GpoAppliedInfo # 18 properties

class GpoConnection(NaConnection):
    
    def gpo_modify(self, is_gpo_enabled=None):
        """
        Change the Vserver's group policy configuration.
        
        :param is_gpo_enabled: Group Policy Zapi Status.
        """
        return self.request( "gpo-modify", {
            'is_gpo_enabled': [ is_gpo_enabled, 'is-gpo-enabled', [ bool, 'None' ], False ],
        }, {
        } )
    
    def gpo_applied_info_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get the list of entries of the applied GPO rules, organized on a
        per-Vserver basis.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the gpo
                object.
                All gpo objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "gpo-applied-info-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ GpoAppliedInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ GpoAppliedInfo, 'None' ], False ],
        }, {
            'attributes-list': [ GpoAppliedInfo, True ],
        } )
    
    def gpo_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the Vserver's group policy configuration.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the gpo
                object.
                All gpo objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "gpo-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ GpoConfig, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ GpoConfig, 'None' ], False ],
        }, {
            'attributes-list': [ GpoConfig, True ],
        } )
    
    def gpo_update(self):
        """
        Download and apply the latest version of the group policy defined
        in Active Directory.
        """
        return self.request( "gpo-update", {
        }, {
        } )
    
    def gpo_gpresult_info_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get a list of entries of the GPO RSoP(Resultant Set of Policy)
        data, organized on a per-Vserver basis.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the gpo
                object.
                All gpo objects matching this query up to 'max-records' will be
                returned.
        
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
        return self.request( "gpo-gpresult-info-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ GpoGpresultInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ GpoGpresultInfo, 'None' ], False ],
        }, {
            'attributes-list': [ GpoGpresultInfo, True ],
        } )
