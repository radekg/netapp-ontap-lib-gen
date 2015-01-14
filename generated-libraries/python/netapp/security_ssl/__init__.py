from netapp.connection import NaConnection
from vserver_ssl_info import VserverSslInfo # 6 properties
from security_ssl_get_iter_key_td import SecuritySslGetIterKeyTd # 1 properties

class SecuritySslConnection(NaConnection):
    
    def security_ssl_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get the attributes of SSL security
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the SSL
                security object.
                All SSL security objects matching this query up to 'max-records'
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
        return self.request( "security-ssl-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VserverSslInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VserverSslInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VserverSslInfo, True ],
        } )
    
    def security_ssl_get(self, desired_attributes=None):
        """
        Get the attributes of SSL security
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "security-ssl-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VserverSslInfo, 'None' ], False ],
        }, {
            'attributes': [ VserverSslInfo, False ],
        } )
    
    def security_ssl_modify(self, certificate_authority=None, vserver=None, certificate_serial_number=None, server_authentication_enabled=None, common_name=None, client_authentication_enabled=None):
        """
        Modify SSL authentication for a Vserver. Only field(s) that are
        provided will be modified.
        
        :param certificate_authority: Issuing Certificate Authority (CA) of server certificate. This
                field is required when you specify server-enabled as true.
        
        :param vserver: Name of vserver.
        
        :param certificate_serial_number: Serial number of certificate in hexadecimal format. This field is
                required when you specify server-enabled as true, if you do not
                specify one it will use the serial number of the default
                certificate.
        
        :param server_authentication_enabled: Informs if SSL Server Authentication is enabled.
        
        :param common_name: Represents the domain name in FQDN form that specifies its exact
                location in the tree hierarchy of the Domain Name System (DNS).
                This field is optional when you specify server-enabled as true.
        
        :param client_authentication_enabled: Informs if SSL Client Authentication is enabled.
        """
        return self.request( "security-ssl-modify", {
            'certificate_authority': [ certificate_authority, 'certificate-authority', [ basestring, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'certificate_serial_number': [ certificate_serial_number, 'certificate-serial-number', [ basestring, 'None' ], False ],
            'server_authentication_enabled': [ server_authentication_enabled, 'server-authentication-enabled', [ bool, 'None' ], False ],
            'common_name': [ common_name, 'common-name', [ basestring, 'None' ], False ],
            'client_authentication_enabled': [ client_authentication_enabled, 'client-authentication-enabled', [ bool, 'None' ], False ],
        }, {
        } )
