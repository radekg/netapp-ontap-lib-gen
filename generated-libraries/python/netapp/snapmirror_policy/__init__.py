from netapp.connection import NaConnection
from sm_transfer_priority_enum import SmTransferPriorityEnum # 0 properties
from sm_policy import SmPolicy # 0 properties
from snapmirror_policy_get_iter_key_td import SnapmirrorPolicyGetIterKeyTd # 2 properties
from sm_restart_enum import SmRestartEnum # 0 properties
from policy_owner import PolicyOwner # 0 properties
from snapmirror_policy_rule_info import SnapmirrorPolicyRuleInfo # 4 properties
from snapmirror_policy_info import SnapmirrorPolicyInfo # 11 properties

class SnapmirrorPolicyConnection(NaConnection):
    
    def snapmirror_policy_get(self, policy_name, desired_attributes=None):
        """
        Get Information about a single SnapMirror Policy
        
        :param policy_name: The name of the SnapMirror policy.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "snapmirror-policy-get", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'sm-policy' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapmirrorPolicyInfo, 'None' ], False ],
        }, {
            'attributes': [ SnapmirrorPolicyInfo, False ],
        } )
    
    def snapmirror_policy_delete(self, policy_name):
        """
        Delete the specified SnapMirror Policy
        
        :param policy_name: The name of the SnapMirror policy.
        """
        return self.request( "snapmirror-policy-delete", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'sm-policy' ], False ],
        }, {
        } )
    
    def snapmirror_policy_modify(self, policy_name, comment=None, transfer_priority=None, tries=None, ignore_atime=None, restart=None):
        """
        Modify the specified SnapMirror Policy
        
        :param policy_name: The name of the SnapMirror policy.
        
        :param comment: A human readable description associated with the SnapMirror
                policy.
        
        :param transfer_priority: Specifies the priority at which a SnapMirror transfer runs.
                'normal' : By default every transfer in the system has this
                priority. These transfers are scheduled before most 'low'
                priority transfers.
                'low': These transfers have least priority and usually are
                scheduled after most 'normal' priority transfers.
                Possible values:
                <ul>
                <li> "low"       ,
                <li> "normal"
                </ul>
        
        :param tries: Specifies the maximum number of times to attempt each manual or
                scheduled transfer for a SnapMirror relationship. Valid input is
                a positive integer or 'unlimited'. The default is '8'.
        
        :param ignore_atime: Specifies whether incremental transfers will ignore files which
                have only their access time changed. Applies to SnapMirror vault
                relationships only.
        
        :param restart: Defines the behavior of SnapMirror if an interrupted transfer
                exists. Applies to SnapMirror data protection relationship only.
                Possible values:
                <ul>
                <li> "always"    ,
                <li> "never"     ,
                <li> "default"
                </ul>
        """
        return self.request( "snapmirror-policy-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'sm-policy' ], False ],
            'transfer_priority': [ transfer_priority, 'transfer-priority', [ basestring, 'sm-transfer-priority-enum' ], False ],
            'tries': [ tries, 'tries', [ basestring, 'None' ], False ],
            'ignore_atime': [ ignore_atime, 'ignore-atime', [ bool, 'None' ], False ],
            'restart': [ restart, 'restart', [ basestring, 'sm-restart-enum' ], False ],
        }, {
        } )
    
    def snapmirror_policy_modify_rule(self, policy_name, snapmirror_label, preserve=None, warn=None, keep=None):
        """
        Modify a SnapMirror policy rule
        
        :param policy_name: The name of the SnapMirror policy.
        
        :param snapmirror_label: Specifies the Snapshot copy label.
        
        :param preserve: Specifies whether Snapshot copy preserve is enabled.
        
        :param warn: Specifies the warning threshold count.
        
        :param keep: Specifies the Snapshot copy retention count.
        """
        return self.request( "snapmirror-policy-modify-rule", {
            'preserve': [ preserve, 'preserve', [ bool, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'sm-policy' ], False ],
            'warn': [ warn, 'warn', [ int, 'None' ], False ],
            'snapmirror_label': [ snapmirror_label, 'snapmirror-label', [ basestring, 'None' ], False ],
            'keep': [ keep, 'keep', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_policy_add_rule(self, policy_name, snapmirror_label, keep, preserve=None, warn=None):
        """
        Add a rule to SnapMirror policy
        
        :param policy_name: The name of the SnapMirror policy.
        
        :param snapmirror_label: Specifies the Snapshot copy label.
        
        :param keep: Specifies the Snapshot copy retention count.
        
        :param preserve: Specifies whether Snapshot copy preserve is enabled.
        
        :param warn: Specifies the warning threshold count.
        """
        return self.request( "snapmirror-policy-add-rule", {
            'preserve': [ preserve, 'preserve', [ bool, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'sm-policy' ], False ],
            'warn': [ warn, 'warn', [ int, 'None' ], False ],
            'snapmirror_label': [ snapmirror_label, 'snapmirror-label', [ basestring, 'None' ], False ],
            'keep': [ keep, 'keep', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def snapmirror_policy_create(self, policy_name, comment=None, transfer_priority=None, return_record=None, tries=None, ignore_atime=None, restart=None):
        """
        Create the specified SnapMirror Policy
        
        :param policy_name: The name of the SnapMirror policy.
        
        :param comment: A human readable description associated with the SnapMirror
                policy.
        
        :param transfer_priority: Specifies the priority at which a SnapMirror transfer runs.
                'normal' : By default every transfer in the system has this
                priority. These transfers are scheduled before most 'low'
                priority transfers.
                'low': These transfers have least priority and usually are
                scheduled after most 'normal' priority transfers.
                Possible values:
                <ul>
                <li> "low"       ,
                <li> "normal"
                </ul>
        
        :param return_record: If set to true, returns the snapmirror-policy on successful
                creation.
                Default: false
        
        :param tries: Specifies the maximum number of times to attempt each manual or
                scheduled transfer for a SnapMirror relationship. Valid input is
                a positive integer or 'unlimited'. The default is '8'.
        
        :param ignore_atime: Specifies whether incremental transfers will ignore files which
                have only their access time changed. Applies to SnapMirror vault
                relationships only.
        
        :param restart: Defines the behavior of SnapMirror if an interrupted transfer
                exists. Applies to SnapMirror data protection relationship only.
                Possible values:
                <ul>
                <li> "always"    ,
                <li> "never"     ,
                <li> "default"
                </ul>
        """
        return self.request( "snapmirror-policy-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'sm-policy' ], False ],
            'transfer_priority': [ transfer_priority, 'transfer-priority', [ basestring, 'sm-transfer-priority-enum' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'tries': [ tries, 'tries', [ basestring, 'None' ], False ],
            'ignore_atime': [ ignore_atime, 'ignore-atime', [ bool, 'None' ], False ],
            'restart': [ restart, 'restart', [ basestring, 'sm-restart-enum' ], False ],
        }, {
            'result': [ SnapmirrorPolicyInfo, False ],
        } )
    
    def snapmirror_policy_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get Information about multiple SnapMirror Policies
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                snapmirror-policy object.
                All snapmirror-policy objects matching this query up to
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
        return self.request( "snapmirror-policy-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ SnapmirrorPolicyInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ SnapmirrorPolicyInfo, 'None' ], False ],
        }, {
            'attributes-list': [ SnapmirrorPolicyInfo, True ],
        } )
    
    def snapmirror_policy_remove_rule(self, policy_name, snapmirror_label):
        """
        Remove a rule from SnapMirror policy
        
        :param policy_name: The name of the SnapMirror policy.
        
        :param snapmirror_label: Specifies the Snapshot copy label.
        """
        return self.request( "snapmirror-policy-remove-rule", {
            'policy_name': [ policy_name, 'policy-name', [ basestring, 'sm-policy' ], False ],
            'snapmirror_label': [ snapmirror_label, 'snapmirror-label', [ basestring, 'None' ], False ],
        }, {
        } )
