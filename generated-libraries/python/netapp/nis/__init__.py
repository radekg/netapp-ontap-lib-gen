from netapp.connection import NaConnection
from nis_get_iter_key_td import NisGetIterKeyTd # 2 properties
from nis_domain_config_info import NisDomainConfigInfo # 4 properties

class NisConnection(NaConnection):
    
    def nis_get(self, nis_domain, desired_attributes=None):
        """
        Get NIS domain configuration.
        
        :param nis_domain: Specifies the NIS domain.
                For example: 'example.com'
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "nis-get", {
            'nis_domain': [ nis_domain, 'nis-domain', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NisDomainConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ NisDomainConfigInfo, False ],
        } )
    
    def nis_destroy(self, nis_domain):
        """
        Destroy an existing NIS configuration.
        
        :param nis_domain: Specifies the NIS domain.
                For example: 'example.com'
        """
        return self.request( "nis-destroy", {
            'nis_domain': [ nis_domain, 'nis-domain', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def nis_modify(self, nis_domain, is_active=None, nis_servers=None):
        """
        Modify the attributes of NIS configuration.
        
        :param nis_domain: Specifies the NIS domain.
                For example: 'example.com'
        
        :param is_active: Specifies whether the NIS domain configuration is active or
                inactive.
        
        :param nis_servers: Specifies the IP address of one or more NIS servers in the
                domain.
        """
        return self.request( "nis-modify", {
            'is_active': [ is_active, 'is-active', [ bool, 'None' ], False ],
            'nis_domain': [ nis_domain, 'nis-domain', [ basestring, 'None' ], False ],
            'nis_servers': [ nis_servers, 'nis-servers', [ basestring, 'ip-address' ], True ],
        }, {
        } )
    
    def nis_create(self, is_active, nis_domain, nis_servers, return_record=None):
        """
        Create an NIS domain configuration.
        Multiple NIS domains can be configured on a single Vserver, but
        only one NIS domain can be active at any given time.
        
        :param is_active: Specifies whether the NIS domain configuration is active or
                inactive.
        
        :param nis_domain: Specifies the NIS domain.
                For example: 'example.com'
        
        :param nis_servers: Specifies the IP address of one or more NIS servers in the
                domain.
        
        :param return_record: If set to true, returns the NIS domain configuration on
                successful creation.
                Default: false
        """
        return self.request( "nis-create", {
            'is_active': [ is_active, 'is-active', [ bool, 'None' ], False ],
            'nis_domain': [ nis_domain, 'nis-domain', [ basestring, 'None' ], False ],
            'nis_servers': [ nis_servers, 'nis-servers', [ basestring, 'ip-address' ], True ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ NisDomainConfigInfo, False ],
        } )
    
    def nis_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of NIS configurations.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the NIS
                domain configuration object.
                All NIS domain configuration objects matching this query up to
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
        return self.request( "nis-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ NisDomainConfigInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ NisDomainConfigInfo, 'None' ], False ],
        }, {
            'attributes-list': [ NisDomainConfigInfo, True ],
        } )
