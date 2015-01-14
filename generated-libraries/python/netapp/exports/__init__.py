from netapp.connection import NaConnection
from export_policy_info import ExportPolicyInfo # 3 properties
from export_policy_get_iter_key_td import ExportPolicyGetIterKeyTd # 2 properties
from export_rule_get_iter_key_td import ExportRuleGetIterKeyTd # 3 properties
from exportchownmode import Exportchownmode # 0 properties
from security_flavor import SecurityFlavor # 0 properties
from export_rule_info import ExportRuleInfo # 13 properties
from access_protocol import AccessProtocol # 0 properties
from exportntfsunixsecops import Exportntfsunixsecops # 0 properties

class ExportsConnection(NaConnection):
    
    def export_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get a group of  Export policy configurations.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Export policy configuration. object.
                All Export policy configuration. objects matching this query up
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
        return self.request( "export-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ExportPolicyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ExportPolicyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ ExportPolicyInfo, True ],
        } )
    
    def export_rule_destroy(self, policy_name, rule_index):
        """
        Delete an Export rule configuration.
        
        :param policy_name: Export policy name.
        
        :param rule_index: Export rule index.
        """
        return self.request( "export-rule-destroy", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'rule_index': [ rule_index, 'rule-index', [ int, 'None' ], False ],
        }, {
        } )
    
    def export_rule_modify(self, policy_name, rule_index, export_ntfs_unix_security_ops=None, is_allow_set_uid_enabled=None, protocol=None, export_chown_mode=None, rw_rule=None, super_user_security=None, client_match=None, is_allow_dev_is_enabled=None, ro_rule=None, anonymous_user_id=None):
        """
        Modify an Export rule configuration.
        
        :param policy_name: Export policy name.
        
        :param rule_index: Export rule index.
        
        :param export_ntfs_unix_security_ops: Ignore/Fail unix security operations on NTFS volumes. Possible
                values are 'ignore', 'fail'. Default value is 'fail'.
        
        :param is_allow_set_uid_enabled: If 'true', NFS server will honor SetUID bits in SETATTR
                operation. Default value is 'true'.
        
        :param protocol: Client access protocol. Default value is 'any'.
        
        :param export_chown_mode: Change ownership mode. Possible values are 'restricted',
                'unrestricted'. Default value is 'restricted'.
        
        :param rw_rule: Rule for read-write access.
        
        :param super_user_security: Security flavors for the superuser. Default value is 'none'.
        
        :param client_match: Client match specification for Export rule. The clients specified
                are enforced with this Export rule. The rule with the higher rule
                index value takes precedence.
        
        :param is_allow_dev_is_enabled: If 'true', the NFS server will allow creation of devices.
                Default value is 'true'.
        
        :param ro_rule: Rule for read-only access.
        
        :param anonymous_user_id: User name or ID to which anonymous users are mapped. Default
                value is '65534'.
        """
        return self.request( "export-rule-modify", {
            'export_ntfs_unix_security_ops': [ export_ntfs_unix_security_ops, 'export-ntfs-unix-security-ops', [ basestring, 'exportntfsunixsecops' ], False ],
            'is_allow_set_uid_enabled': [ is_allow_set_uid_enabled, 'is-allow-set-uid-enabled', [ bool, 'None' ], False ],
            'protocol': [ protocol, 'protocol', [ basestring, 'access-protocol' ], True ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'export_chown_mode': [ export_chown_mode, 'export-chown-mode', [ basestring, 'exportchownmode' ], False ],
            'rule_index': [ rule_index, 'rule-index', [ int, 'None' ], False ],
            'rw_rule': [ rw_rule, 'rw-rule', [ basestring, 'security-flavor' ], True ],
            'super_user_security': [ super_user_security, 'super-user-security', [ basestring, 'security-flavor' ], True ],
            'client_match': [ client_match, 'client-match', [ basestring, 'None' ], False ],
            'is_allow_dev_is_enabled': [ is_allow_dev_is_enabled, 'is-allow-dev-is-enabled', [ bool, 'None' ], False ],
            'ro_rule': [ ro_rule, 'ro-rule', [ basestring, 'security-flavor' ], True ],
            'anonymous_user_id': [ anonymous_user_id, 'anonymous-user-id', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def export_rule_create(self, policy_name, rw_rule, client_match, ro_rule, export_ntfs_unix_security_ops=None, is_allow_set_uid_enabled=None, protocol=None, export_chown_mode=None, rule_index=None, super_user_security=None, is_allow_dev_is_enabled=None, anonymous_user_id=None):
        """
        Create an Export rule configuration.
        
        :param policy_name: Export policy name.
        
        :param rw_rule: Rule for read-write access.
        
        :param client_match: Client match specification for Export rule. The clients specified
                are enforced with this Export rule. The rule with the higher rule
                index value takes precedence.
        
        :param ro_rule: Rule for read-only access.
        
        :param export_ntfs_unix_security_ops: Ignore/Fail unix security operations on NTFS volumes. Possible
                values are 'ignore', 'fail'. Default value is 'fail'.
        
        :param is_allow_set_uid_enabled: If 'true', NFS server will honor SetUID bits in SETATTR
                operation. Default value is 'true'.
        
        :param protocol: Client access protocol. Default value is 'any'.
        
        :param export_chown_mode: Change ownership mode. Possible values are 'restricted',
                'unrestricted'. Default value is 'restricted'.
        
        :param rule_index: Export rule index. A next available value is assigned if no value
                is provided during create else the rule is inserted at the given
                rule index position in the export-rule table.
        
        :param super_user_security: Security flavors for the superuser. Default value is 'none'.
        
        :param is_allow_dev_is_enabled: If 'true', the NFS server will allow creation of devices.
                Default value is 'true'.
        
        :param anonymous_user_id: User name or ID to which anonymous users are mapped. Default
                value is '65534'.
        """
        return self.request( "export-rule-create", {
            'export_ntfs_unix_security_ops': [ export_ntfs_unix_security_ops, 'export-ntfs-unix-security-ops', [ basestring, 'exportntfsunixsecops' ], False ],
            'is_allow_set_uid_enabled': [ is_allow_set_uid_enabled, 'is-allow-set-uid-enabled', [ bool, 'None' ], False ],
            'protocol': [ protocol, 'protocol', [ basestring, 'access-protocol' ], True ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'export_chown_mode': [ export_chown_mode, 'export-chown-mode', [ basestring, 'exportchownmode' ], False ],
            'rule_index': [ rule_index, 'rule-index', [ int, 'None' ], False ],
            'rw_rule': [ rw_rule, 'rw-rule', [ basestring, 'security-flavor' ], True ],
            'super_user_security': [ super_user_security, 'super-user-security', [ basestring, 'security-flavor' ], True ],
            'client_match': [ client_match, 'client-match', [ basestring, 'None' ], False ],
            'is_allow_dev_is_enabled': [ is_allow_dev_is_enabled, 'is-allow-dev-is-enabled', [ bool, 'None' ], False ],
            'ro_rule': [ ro_rule, 'ro-rule', [ basestring, 'security-flavor' ], True ],
            'anonymous_user_id': [ anonymous_user_id, 'anonymous-user-id', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def export_policy_destroy(self, policy_name):
        """
        Delete an Export policy configuration.
        
        :param policy_name: Export policy name.
        """
        return self.request( "export-policy-destroy", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def export_policy_get(self, policy_name, desired_attributes=None):
        """
        Get an Export policy configuration.
        
        :param policy_name: Export policy name.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "export-policy-get", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ExportPolicyInfo, 'None' ], False ],
        }, {
            'attributes': [ ExportPolicyInfo, False ],
        } )
    
    def export_policy_create(self, policy_name, return_record=None):
        """
        Create an Export policy configuration.
        
        :param policy_name: Export policy name.
        
        :param return_record: If set to true, returns the Export policy configuration. on
                successful creation.
                Default: false
        """
        return self.request( "export-policy-create", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ ExportPolicyInfo, False ],
        } )
    
    def export_rule_get(self, policy_name, rule_index, desired_attributes=None):
        """
        Get an Export rule configuration.
        
        :param policy_name: Export policy name.
        
        :param rule_index: Export rule index.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "export-rule-get", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ExportRuleInfo, 'None' ], False ],
            'rule_index': [ rule_index, 'rule-index', [ int, 'None' ], False ],
        }, {
            'attributes': [ ExportRuleInfo, False ],
        } )
    
    def export_rule_get_create_defaults(self, attributes=None):
        """
        Obtain the default values for Export rule configuration
        
        :param attributes: Optionally specify the value for attributes if available.
                The default values for some attributes may depend on the values
                specified for some other attribute.
        """
        return self.request( "export-rule-get-create-defaults", {
            'attributes': [ attributes, 'attributes', [ ExportRuleInfo, 'None' ], False ],
        }, {
            'defaults': [ ExportRuleInfo, False ],
        } )
    
    def export_rule_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get a group of  Export rule configurations.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Export rule configuration. object.
                All Export rule configuration. objects matching this query up to
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
        return self.request( "export-rule-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ ExportRuleInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ ExportRuleInfo, 'None' ], False ],
        }, {
            'attributes-list': [ ExportRuleInfo, True ],
        } )
    
    def export_rule_set_index(self, new_rule_index, policy_name, rule_index):
        """
        Move a rule to the specified index
        
        :param new_rule_index: New ruleindex value for the Export rule. The rule will be
                inserted into the rule-index position in the export-rule table.
        
        :param policy_name: Export policy name.
        
        :param rule_index: Export policy rule index.
        """
        return self.request( "export-rule-set-index", {
            'new_rule_index': [ new_rule_index, 'new-rule-index', [ int, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'rule_index': [ rule_index, 'rule-index', [ int, 'None' ], False ],
        }, {
        } )
    
    def export_policy_rename(self, policy_name, new_policy_name):
        """
        Rename an Export policy
        
        :param policy_name: Export policy name.
        
        :param new_policy_name: New Export policy name.
        """
        return self.request( "export-policy-rename", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'None' ], False ],
            'new_policy_name': [ new_policy_name, 'new-policy-name', [ basestring, 'None' ], False ],
        }, {
        } )
