from netapp.connection import NaConnection
from kdc_vendor import KdcVendor # 0 properties
from kerberos_config_info import KerberosConfigInfo # 9 properties
from kerberos_realm_get_iter_key_td import KerberosRealmGetIterKeyTd # 1 properties
from kerberos_realm import KerberosRealm # 13 properties
from kerberos_config_get_iter_key_td import KerberosConfigGetIterKeyTd # 2 properties

class KerberosConnection(NaConnection):
    
    def kerberos_realm_modify(self, config_name, kdc_ip=None, comment=None, realm=None, kdc_vendor=None, clock_skew=None, admin_server_port=None, password_server_ip=None, admin_server_ip=None, kdc_port=None, ad_server_name=None, password_server_port=None, ad_server_ip=None):
        """
        Modify the Kerberos realm configuration.
        
        :param config_name: Kerberos configuration name.
        
        :param kdc_ip: IP address of the Key Distribution Centre (KDC) server for this
                Kerberos realm.
        
        :param comment: Comment
        
        :param realm: Kerberos realm name.
        
        :param kdc_vendor: The vendor of the Key Distribution Centre (KDC) server. If the
                configuration uses a Microsoft Active Directory (AD) domain for
                authentication, this field should be 'microsoft'.
                Possible values:
                <ul>
                <li> "microsoft" ,
                <li> "other"
                </ul>
        
        :param clock_skew: The clock skew in minutes is the tolerance for accepting tickets
                with time stamps that do not exactly match the host's system
                clock. The default for this parameter is 5 minutes.
        
        :param admin_server_port: The TCP port on the Kerberos administration server where the
                Kerberos administration service is running. The default for this
                parmater is 749.
        
        :param password_server_ip: IP address of the host where the Kerberos password-changing
                server is running. Typically, this is the same as the host
                indicated in the adminserver-ip. If this parameter is omitted,
                the IP address in kdc-ip is used.
        
        :param admin_server_ip: IP address of the host where the Kerberos administration daemon
                is running. This is usually the master KDC. If this parameter is
                omitted, the IP address specified in kdc-ip is used. If
                specified, this should be the same as the kdc-ip if the
                kdc-vendor is 'microsoft'.
        
        :param kdc_port: TCP port on the KDC to be used for Kerberos communication. The
                default for this parameter is 88.
        
        :param ad_server_name: Host name of the Active Directory Domain Controller (DC). This is
                a mandatory parameter if the kdc-vendor is 'microsoft'
        
        :param password_server_port: The TCP port on the Kerberos password-changing server where the
                Kerberos password-changing service is running. The default for
                this parameter is 464.
        
        :param ad_server_ip: IP Address of the Active Directory Domain Controller (DC). This
                is a mandatory parameter if the kdc-vendor is 'microsoft'.
        """
        return self.request( "kerberos-realm-modify", {
            'kdc_ip': [ kdc_ip, 'kdc-ip', [ basestring, 'ip-address' ], False ],
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'realm': [ realm, 'realm', [ basestring, 'None' ], False ],
            'kdc_vendor': [ kdc_vendor, 'kdc-vendor', [ basestring, 'kdc-vendor' ], False ],
            'clock_skew': [ clock_skew, 'clock-skew', [ int, 'None' ], False ],
            'admin_server_port': [ admin_server_port, 'admin-server-port', [ int, 'None' ], False ],
            'password_server_ip': [ password_server_ip, 'password-server-ip', [ basestring, 'ip-address' ], False ],
            'admin_server_ip': [ admin_server_ip, 'admin-server-ip', [ basestring, 'ip-address' ], False ],
            'kdc_port': [ kdc_port, 'kdc-port', [ int, 'None' ], False ],
            'ad_server_name': [ ad_server_name, 'ad-server-name', [ basestring, 'None' ], False ],
            'password_server_port': [ password_server_port, 'password-server-port', [ int, 'None' ], False ],
            'config_name': [ config_name, 'config-name', [ basestring, 'None' ], False ],
            'ad_server_ip': [ ad_server_ip, 'ad-server-ip', [ basestring, 'ip-address' ], False ],
        }, {
        } )
    
    def kerberos_config_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get Kerberos configuration information for a group of LIFs.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 50
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                kerberos-config object.
                All kerberos-config objects matching this query up to
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
        return self.request( "kerberos-config-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ KerberosConfigInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ KerberosConfigInfo, 'None' ], False ],
        }, {
            'attributes-list': [ KerberosConfigInfo, True ],
        } )
    
    def kerberos_realm_delete(self, config_name):
        """
        Delete the Kerberos realm configuration.
        
        :param config_name: Kerberos configuration name.
        """
        return self.request( "kerberos-realm-delete", {
            'config_name': [ config_name, 'config-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def kerberos_realm_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of Kerberos realm configurations.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                kerberos-realm object.
                All kerberos-realm objects matching this query up to
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
        return self.request( "kerberos-realm-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ KerberosRealm, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ KerberosRealm, 'None' ], False ],
        }, {
            'attributes-list': [ KerberosRealm, True ],
        } )
    
    def kerberos_config_modify(self, interface_name, keytab_uri=None, is_kerberos_enabled=None, organizational_unit=None, admin_user_name=None, service_principal_name=None, admin_password=None):
        """
        Modify Kerberos configuration informaiton for a LIF
        
        :param interface_name: Logical interface.
        
        :param keytab_uri: Keytab to load the uri from.
        
        :param is_kerberos_enabled: If 'true', then kerberos security is enabled.
        
        :param organizational_unit: Organizational Unit.
        
        :param admin_user_name: Administrator username.
        
        :param service_principal_name: Kerberos service principal name.
        
        :param admin_password: Administrator password.
        """
        return self.request( "kerberos-config-modify", {
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
            'keytab_uri': [ keytab_uri, 'keytab-uri', [ basestring, 'None' ], False ],
            'is_kerberos_enabled': [ is_kerberos_enabled, 'is-kerberos-enabled', [ bool, 'None' ], False ],
            'organizational_unit': [ organizational_unit, 'organizational-unit', [ basestring, 'None' ], False ],
            'admin_user_name': [ admin_user_name, 'admin-user-name', [ basestring, 'None' ], False ],
            'service_principal_name': [ service_principal_name, 'service-principal-name', [ basestring, 'None' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def kerberos_config_get(self, interface_name, desired_attributes=None):
        """
        Get Kerberos configuration information for a LIF.
        
        :param interface_name: Logical interface.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "kerberos-config-get", {
            'interface_name': [ interface_name, 'interface-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ KerberosConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ KerberosConfigInfo, False ],
        } )
    
    def kerberos_realm_create(self, kdc_ip, realm, kdc_vendor, config_name, comment=None, clock_skew=None, admin_server_port=None, return_record=None, password_server_ip=None, admin_server_ip=None, kdc_port=None, ad_server_name=None, password_server_port=None, ad_server_ip=None):
        """
        Create a new Kerberos realm configuration.
        
        :param kdc_ip: IP address of the Key Distribution Centre (KDC) server for this
                Kerberos realm.
        
        :param realm: Kerberos realm name.
        
        :param kdc_vendor: The vendor of the Key Distribution Centre (KDC) server. If the
                configuration uses a Microsoft Active Directory (AD) domain for
                authentication, this field should be 'microsoft'.
                Possible values:
                <ul>
                <li> "microsoft" ,
                <li> "other"
                </ul>
        
        :param config_name: Kerberos configuration name.
        
        :param comment: Comment
        
        :param clock_skew: The clock skew in minutes is the tolerance for accepting tickets
                with time stamps that do not exactly match the host's system
                clock. The default for this parameter is 5 minutes.
        
        :param admin_server_port: The TCP port on the Kerberos administration server where the
                Kerberos administration service is running. The default for this
                parmater is 749.
        
        :param return_record: If set to true, returns the kerberos-realm on successful
                creation.
                Default: false
        
        :param password_server_ip: IP address of the host where the Kerberos password-changing
                server is running. Typically, this is the same as the host
                indicated in the adminserver-ip. If this parameter is omitted,
                the IP address in kdc-ip is used.
        
        :param admin_server_ip: IP address of the host where the Kerberos administration daemon
                is running. This is usually the master KDC. If this parameter is
                omitted, the IP address specified in kdc-ip is used. If
                specified, this should be the same as the kdc-ip if the
                kdc-vendor is 'microsoft'.
        
        :param kdc_port: TCP port on the KDC to be used for Kerberos communication. The
                default for this parameter is 88.
        
        :param ad_server_name: Host name of the Active Directory Domain Controller (DC). This is
                a mandatory parameter if the kdc-vendor is 'microsoft'
        
        :param password_server_port: The TCP port on the Kerberos password-changing server where the
                Kerberos password-changing service is running. The default for
                this parameter is 464.
        
        :param ad_server_ip: IP Address of the Active Directory Domain Controller (DC). This
                is a mandatory parameter if the kdc-vendor is 'microsoft'.
        """
        return self.request( "kerberos-realm-create", {
            'kdc_ip': [ kdc_ip, 'kdc-ip', [ basestring, 'ip-address' ], False ],
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'realm': [ realm, 'realm', [ basestring, 'None' ], False ],
            'kdc_vendor': [ kdc_vendor, 'kdc-vendor', [ basestring, 'kdc-vendor' ], False ],
            'clock_skew': [ clock_skew, 'clock-skew', [ int, 'None' ], False ],
            'admin_server_port': [ admin_server_port, 'admin-server-port', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'password_server_ip': [ password_server_ip, 'password-server-ip', [ basestring, 'ip-address' ], False ],
            'admin_server_ip': [ admin_server_ip, 'admin-server-ip', [ basestring, 'ip-address' ], False ],
            'kdc_port': [ kdc_port, 'kdc-port', [ int, 'None' ], False ],
            'ad_server_name': [ ad_server_name, 'ad-server-name', [ basestring, 'None' ], False ],
            'password_server_port': [ password_server_port, 'password-server-port', [ int, 'None' ], False ],
            'config_name': [ config_name, 'config-name', [ basestring, 'None' ], False ],
            'ad_server_ip': [ ad_server_ip, 'ad-server-ip', [ basestring, 'ip-address' ], False ],
        }, {
            'result': [ KerberosRealm, False ],
        } )
