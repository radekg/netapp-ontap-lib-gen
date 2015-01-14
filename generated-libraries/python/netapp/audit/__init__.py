from netapp.connection import NaConnection
from audit_info import AuditInfo # 8 properties

class AuditConnection(NaConnection):
    
    def audit_get(self, desired_attributes=None):
        """
        Get the cluster administrative audit settings
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "audit-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ AuditInfo, 'None' ], False ],
        }, {
            'attributes': [ AuditInfo, False ],
        } )
    
    def audit_modify(self, cli_get=None, http_get=None, cli_set=None, http_set=None, ontapi_set=None, snmp_get=None, ontapi_get=None, snmp_set=None):
        """
        Modify the cluster administrative audit settings
        
        :param cli_get: Enable auditing of CLI get operations
        
        :param http_get: Enable auditing of HTTP get operations
        
        :param cli_set: Enable auditing of CLI set operations
        
        :param http_set: Enable auditing of HTTP set operations
        
        :param ontapi_set: Enable auditing of Data ONTAP API set operations
        
        :param snmp_get: Enable auditing of SNMP get operations
        
        :param ontapi_get: Enable auditing of Data ONTAP API get operations
        
        :param snmp_set: Enable auditing of SNMP set operations
        """
        return self.request( "audit-modify", {
            'cli_get': [ cli_get, 'cli-get', [ bool, 'None' ], False ],
            'http_get': [ http_get, 'http-get', [ bool, 'None' ], False ],
            'cli_set': [ cli_set, 'cli-set', [ bool, 'None' ], False ],
            'http_set': [ http_set, 'http-set', [ bool, 'None' ], False ],
            'ontapi_set': [ ontapi_set, 'ontapi-set', [ bool, 'None' ], False ],
            'snmp_get': [ snmp_get, 'snmp-get', [ bool, 'None' ], False ],
            'ontapi_get': [ ontapi_get, 'ontapi-get', [ bool, 'None' ], False ],
            'snmp_set': [ snmp_set, 'snmp-set', [ bool, 'None' ], False ],
        }, {
        } )
