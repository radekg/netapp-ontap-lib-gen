from netapp.connection import NaConnection
from fileformat import Fileformat # 0 properties
from security_certificate_delete_iter_info import SecurityCertificateDeleteIterInfo # 3 properties
from security_certificate_ca_issued_get_iter_key_td import SecurityCertificateCaIssuedGetIterKeyTd # 4 properties
from hashfunction import Hashfunction # 0 properties
from certificate_ca_issued_info import CertificateCaIssuedInfo # 14 properties
from pubcertificate import Pubcertificate # 0 properties
from security_certificate_delete_iter_key_td import SecurityCertificateDeleteIterKeyTd # 5 properties
from numbits import Numbits # 0 properties
from certificate_info import CertificateInfo # 18 properties
from certificate_file_info import CertificateFileInfo # 10 properties
from security_certificate_file_get_iter_key_td import SecurityCertificateFileGetIterKeyTd # 7 properties
from security_certificate_get_iter_key_td import SecurityCertificateGetIterKeyTd # 5 properties

class SecurityCertificateConnection(NaConnection):
    
    def security_certificate_delete(self, certificate_authority, type, common_name, vserver=None, serial_number=None):
        """
        Delete an existing security-certificate object.
        
        :param certificate_authority: Certificate Authority
        
        :param type: Type of certificate.
                <p>
                Possible values:
                <ul>
                <li> 'server'       - Server certificate,
                <li> 'root_ca'      - Self-Signed Root CA,
                <li> 'client_ca'    - CA who signed user certificates on
                client',
                <li> 'server_ca'    - CA who signed user certificates on
                server',
                <li> 'server_chain' - Intermediate certificate for server
                authentication
                </ul>
                <p>
        
        :param common_name: Represents the domain name in FQDN form that specifies its exact
                location in the tree hierarchy of the Domain Name System (DNS).
        
        :param vserver: Name of vserver.
        
        :param serial_number: Serial number of certificate.
        """
        return self.request( "security-certificate-delete", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'certificate_authority': [ certificate_authority, 'certificate-authority', [ basestring, 'None' ], False ],
            'serial_number': [ serial_number, 'serial-number', [ basestring, 'None' ], False ],
            'type': [ type, 'type', [ basestring, 'None' ], False ],
            'common_name': [ common_name, 'common-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_certificate_sign(self, certificate_authority, ca_serial_number, csr, hash_function=None, filepassword=None, format=None, private_key=None, username=None, destination=None, expire_days=None, vserver=None, password=None):
        """
        Sign a certificate using self-signed root CA
        
        :param certificate_authority: Certificate Authority to Sign
        
        :param ca_serial_number: Serial number of CA certificate.
        
        :param csr: Certificate signing request.
        
        :param hash_function: Hashing function used to sign the certificate. Default value is
                'sha256'.
                <p>
                Possible values:
                <ul>
                <li> 'sha1'      ,
                <li> 'sha256'    ,
                <li> 'md5'
                </ul>
                <p>
        
        :param filepassword: Password for PKCS12 file
        
        :param format: Certificate Format. Default value is 'PEM'.
                <p>
                Possible values:
                <ul>
                <li> 'pkcs12'   ,
                <li> 'pem'
                </ul>
                <p>
        
        :param private_key: Private Key
        
        :param username: Destination URI username
        
        :param destination: URI to send file to. Example: ftp://abc.com.
        
        :param expire_days: Number of days until expiration. Default value is '365'.
        
        :param vserver: Name of vserver.
        
        :param password: Destination URI password
        """
        return self.request( "security-certificate-sign", {
            'certificate_authority': [ certificate_authority, 'certificate-authority', [ basestring, 'None' ], False ],
            'hash_function': [ hash_function, 'hash-function', [ basestring, 'None' ], False ],
            'filepassword': [ filepassword, 'filepassword', [ basestring, 'None' ], False ],
            'format': [ format, 'format', [ basestring, 'None' ], False ],
            'private_key': [ private_key, 'private-key', [ basestring, 'None' ], False ],
            'username': [ username, 'username', [ basestring, 'None' ], False ],
            'destination': [ destination, 'destination', [ basestring, 'uri' ], False ],
            'expire_days': [ expire_days, 'expire-days', [ int, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'password': [ password, 'password', [ basestring, 'None' ], False ],
            'ca_serial_number': [ ca_serial_number, 'ca-serial-number', [ basestring, 'None' ], False ],
            'csr': [ csr, 'csr', [ basestring, 'None' ], False ],
        }, {
            'signed-cert': [ basestring, False ],
        } )
    
    def security_certificate_create(self, common_name, type, hash_function=None, email_address=None, locality=None, country=None, expire_days=None, vserver=None, organization_unit=None, state=None, organization=None, size=None):
        """
        If a certificate is created with the existing Common Name then a
        new certificate is generated with a different serial number
        
        :param common_name: Represents the domain name in FQDN form that specifies its exact
                location in the tree hierarchy of the Domain Name System (DNS).
        
        :param type: Type of certificate.
                <p>
                Possible values:
                <ul>
                <li> 'server'       - Server certificate,
                <li> 'root_ca'      - Self-Signed Root CA,
                <li> 'client_ca'    - CA who signed user certificates on
                client',
                <li> 'server_ca'    - CA who signed user certificates on
                server',
                <li> 'server_chain' - Intermediate certificate for server
                authentication
                </ul>
                <p>
        
        :param hash_function: Hashing function used to sign the certificate. Default value is
                'sha256'.
                <p>
                Possible values:
                <ul>
                <li> 'sha1'      ,
                <li> 'sha256'    ,
                <li> 'md5'
                </ul>
                <p>
        
        :param email_address: Email address of administrator. Default value is empty string.
        
        :param locality: Name of the locality Default value is empty string.
        
        :param country: Name of the country. Default value is 'US'.
        
        :param expire_days: Number of days until expiration. Default value is '365'.
        
        :param vserver: Name of vserver.
        
        :param organization_unit: Name of the unit. Example: IT, Finance. Default value is empty
                string.
        
        :param state: Name of the state. Default value is empty string.
        
        :param organization: Name of the organization. Default value is empty string.
        
        :param size: Size of requested certificate in bits. Default value is '2048'.
                <p>
                Possible values:
                <ul>
                <li> '512'      - 512 bits private key,
                <li> '1024'     - 1024 bits private key,
                <li> '1536'     - 1536 bits private key,
                <li> '2048'     - 2048 bits private key
                </ul>
                <p>
        """
        return self.request( "security-certificate-create", {
            'hash_function': [ hash_function, 'hash-function', [ basestring, 'None' ], False ],
            'email_address': [ email_address, 'email-address', [ basestring, 'None' ], False ],
            'locality': [ locality, 'locality', [ basestring, 'None' ], False ],
            'country': [ country, 'country', [ basestring, 'None' ], False ],
            'expire_days': [ expire_days, 'expire-days', [ int, 'None' ], False ],
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'organization_unit': [ organization_unit, 'organization-unit', [ basestring, 'None' ], False ],
            'state': [ state, 'state', [ basestring, 'None' ], False ],
            'common_name': [ common_name, 'common-name', [ basestring, 'None' ], False ],
            'organization': [ organization, 'organization', [ basestring, 'None' ], False ],
            'type': [ type, 'type', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_certificate_get(self, certificate_authority, type, common_name, serial_number=None, desired_attributes=None):
        """
        Get the attributes of the security-certificate.
        
        :param certificate_authority: Certificate Authority
        
        :param type: Type of certificate.
                <p>
                Possible values:
                <ul>
                <li> 'server'       - Server certificate,
                <li> 'root_ca'      - Self-Signed Root CA,
                <li> 'client_ca'    - CA who signed user certificates on the
                client',
                <li> 'server_ca'    - CA who signed user certificates on the
                server',
                <li> 'server_chain' - Intermediate certificate for server
                authentication
                </ul>
        
        :param common_name: Represents the domain name in FQDN form that specifies its exact
                location in the tree hierarchy of the Domain Name System (DNS).
        
        :param serial_number: Serial number of certificate.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "security-certificate-get", {
            'certificate_authority': [ certificate_authority, 'certificate-authority', [ basestring, 'None' ], False ],
            'serial_number': [ serial_number, 'serial-number', [ basestring, 'None' ], False ],
            'type': [ type, 'type', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CertificateInfo, 'None' ], False ],
            'common_name': [ common_name, 'common-name', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ CertificateInfo, False ],
        } )
    
    def security_certificate_ca_issued_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of security-certificate-ca-issued objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security-certificate-ca-issued object.
                All security-certificate-ca-issued objects matching this query up
                to 'max-records' will be returned.
        
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
        return self.request( "security-certificate-ca-issued-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CertificateCaIssuedInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CertificateCaIssuedInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CertificateCaIssuedInfo, True ],
        } )
    
    def security_certificate_revoke(self, certificate_authority, serial_number, ca_serial_number, vserver=None, common_name=None):
        """
        Revoke a digital certificate
        
        :param certificate_authority: Certificate Authority
        
        :param serial_number: Serial number of certificate.
        
        :param ca_serial_number: Serial number of CA certificate.
        
        :param vserver: Name of vserver.
        
        :param common_name: Represents the domain name in FQDN form that specifies its exact
                location in the tree hierarchy of the Domain Name System (DNS).
        """
        return self.request( "security-certificate-revoke", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'certificate_authority': [ certificate_authority, 'certificate-authority', [ basestring, 'None' ], False ],
            'serial_number': [ serial_number, 'serial-number', [ basestring, 'None' ], False ],
            'ca_serial_number': [ ca_serial_number, 'ca-serial-number', [ basestring, 'None' ], False ],
            'common_name': [ common_name, 'common-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def security_certificate_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of security-certificate objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security-certificate object.
                All security-certificate objects matching this query up to
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
        return self.request( "security-certificate-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CertificateInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CertificateInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CertificateInfo, True ],
        } )
    
    def security_certificate_delete_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete an existing security-certificate or a group of
        security-certificate objects.
        
        :param query: If deleting a specific security-certificate, this input element
                must specify all keys.
                If deleting multiple security-certificate objects based on query,
                this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                security-certificate even when the deletion of a previous
                matching security-certificate fails, and do so until the total
                number of objects failed to be deleted reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of security-certificate objects to delete in
                this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of
                security-certificate objects (just keys) that were successfully
                deleted.
                If set to false, the list of security-certificate objects deleted
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple security-certificate
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                security-certificate even when the deletion of a previous
                security-certificate fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                security-certificate objects (just keys) that were not deleted
                due to some error.
                If set to false, the list of security-certificate objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "security-certificate-delete-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ CertificateInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ SecurityCertificateDeleteIterInfo, True ],
            'failure-list': [ SecurityCertificateDeleteIterInfo, True ],
        } )
    
    def security_certificate_file_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of security-certificate-file objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                security-certificate-file object.
                All security-certificate-file objects matching this query up to
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
        return self.request( "security-certificate-file-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CertificateFileInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CertificateFileInfo, 'None' ], False ],
        }, {
            'attributes-list': [ CertificateFileInfo, True ],
        } )
    
    def security_certificate_generate_csr(self, common_name, email_address=None, locality=None, country=None, hash_function=None, organization_unit=None, state=None, organization=None, size=None):
        """
        Generate a digital certificate signing request(CSR)
        
        :param common_name: Represents the domain name in FQDN form that specifies its exact
                location in the tree hierarchy of the Domain Name System (DNS).
        
        :param email_address: Email address of administrator.
        
        :param locality: Name of the locality.
        
        :param country: Name of the country.
        
        :param hash_function: Hashing function used to sign the certificate. Default value is
                'sha256'.
                <p>
                Possible values:
                <ul>
                <li> 'sha1'      ,
                <li> 'sha256'    ,
                <li> 'md5'
                </ul>
                <p>
        
        :param organization_unit: Name of the unit. Example: IT, Finance.
        
        :param state: Name of the state.
        
        :param organization: Name of the organization.
        
        :param size: Size of requested certificate in bits. Default value is '2048'.
                <p>
                Possible values:
                <ul>
                <li> '512'      - 512 bits private key,
                <li> '1024'     - 1024 bits private key,
                <li> '1536'     - 1536 bits private key,
                <li> '2048'     - 2048 bits private key
                </ul>
                <p>
        """
        return self.request( "security-certificate-generate-csr", {
            'email_address': [ email_address, 'email-address', [ basestring, 'None' ], False ],
            'locality': [ locality, 'locality', [ basestring, 'None' ], False ],
            'country': [ country, 'country', [ basestring, 'None' ], False ],
            'hash_function': [ hash_function, 'hash-function', [ basestring, 'None' ], False ],
            'organization_unit': [ organization_unit, 'organization-unit', [ basestring, 'None' ], False ],
            'state': [ state, 'state', [ basestring, 'None' ], False ],
            'common_name': [ common_name, 'common-name', [ basestring, 'None' ], False ],
            'organization': [ organization, 'organization', [ basestring, 'None' ], False ],
            'size': [ size, 'size', [ basestring, 'None' ], False ],
        }, {
            'private-key': [ basestring, False ],
            'csr': [ basestring, False ],
        } )
    
    def security_certificate_ca_issued_get(self, certificate_authority, serial_number, ca_serial_number, desired_attributes=None):
        """
        Get the attributes of the security-certificate-ca-issued.
        
        :param certificate_authority: Certificate Authority
        
        :param serial_number: Serial number of certificate.
        
        :param ca_serial_number: Serial number of CA certificate.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "security-certificate-ca-issued-get", {
            'certificate_authority': [ certificate_authority, 'certificate-authority', [ basestring, 'None' ], False ],
            'serial_number': [ serial_number, 'serial-number', [ basestring, 'None' ], False ],
            'ca_serial_number': [ ca_serial_number, 'ca-serial-number', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CertificateCaIssuedInfo, 'None' ], False ],
        }, {
            'attributes': [ CertificateCaIssuedInfo, False ],
        } )
    
    def security_certificate_install(self, type, certificate, vserver=None, private_key=None, intermediate_cert_list=None):
        """
        Install a digital certificate
        
        :param type: Type of certificate.
                <p>
                Possible values:
                <ul>
                <li> 'server'       - Server certificate,
                <li> 'client_ca'    - CA who signed user certificates on
                client',
                <li> 'server_ca'    - CA who signed user certificates on
                server',
                </ul>
        
        :param certificate: Public Key Certificate
        
        :param vserver: Name of vserver.
        
        :param private_key: Private Key
        
        :param intermediate_cert_list: Chain of Intermediate Certificates
        """
        return self.request( "security-certificate-install", {
            'vserver': [ vserver, 'vserver', [ basestring, 'None' ], False ],
            'private_key': [ private_key, 'private-key', [ basestring, 'None' ], False ],
            'type': [ type, 'type', [ basestring, 'None' ], False ],
            'intermediate_cert_list': [ intermediate_cert_list, 'intermediate-cert-list', [ basestring, 'pubcertificate' ], True ],
            'certificate': [ certificate, 'certificate', [ basestring, 'None' ], False ],
        }, {
        } )
