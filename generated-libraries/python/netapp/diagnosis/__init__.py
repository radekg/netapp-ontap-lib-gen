from netapp.connection import NaConnection
from diagnosis_subscriptions_info import DiagnosisSubscriptionsInfo # 16 properties
from hm_alert_type import HmAlertType # 0 properties
from diagnosis_subscriptions_get_iter_key_td import DiagnosisSubscriptionsGetIterKeyTd # 8 properties
from hm_subsystem import HmSubsystem # 0 properties
from hm_event_type import HmEventType # 0 properties
from diagnosis_policy_definition_get_iter_key_td import DiagnosisPolicyDefinitionGetIterKeyTd # 4 properties
from diagnosis_alert_get_iter_key_td import DiagnosisAlertGetIterKeyTd # 5 properties
from hm_perceived_sev import HmPerceivedSev # 0 properties
from diagnosis_config_info import DiagnosisConfigInfo # 11 properties
from diagnosis_alert_info import DiagnosisAlertInfo # 18 properties
from hm_scope import HmScope # 0 properties
from hm_probable_cause import HmProbableCause # 0 properties
from diagnosis_status import DiagnosisStatus # 1 properties
from diagnosis_subsystem_config_get_iter_key_td import DiagnosisSubsystemConfigGetIterKeyTd # 1 properties
from diagnosis_config_get_iter_key_td import DiagnosisConfigGetIterKeyTd # 3 properties
from diagnosis_alert_definition_info import DiagnosisAlertDefinitionInfo # 11 properties
from hm_type import HmType # 0 properties
from hm_notify_type import HmNotifyType # 0 properties
from diagnosis_alert_definition_get_iter_key_td import DiagnosisAlertDefinitionGetIterKeyTd # 4 properties
from filer_id import FilerId # 0 properties
from hm_status import HmStatus # 0 properties
from date import Date # 0 properties
from diagnosis_subsystem_config_info import DiagnosisSubsystemConfigInfo # 5 properties
from hm_subsystem_discovery_state import HmSubsystemDiscoveryState # 0 properties
from diagnosis_policy_definition_info import DiagnosisPolicyDefinitionInfo # 10 properties

class DiagnosisConnection(NaConnection):
    
    def diagnosis_subscriptions_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Subscriptions for Notifications objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Subscriptions for Notifications object.
                All Subscriptions for Notifications objects matching this query
                up to 'max-records' will be returned.
        
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
        return self.request( "diagnosis-subscriptions-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DiagnosisSubscriptionsInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisSubscriptionsInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DiagnosisSubscriptionsInfo, True ],
        } )
    
    def diagnosis_policy_modify(self, node, policy_id, monitor, enable=None):
        """
        Enable/disable policy
        
        :param node: Node hosting this health monitor.
        
        :param policy_id: Policy identifier.
        
        :param monitor: Type of health monitor (e.g. node_connect, system_connect, system).
        
        :param enable: Enable/disable this policy.
        """
        return self.request( "diagnosis-policy-modify", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'policy_id': [ policy_id, 'policy-id', [ basestring, 'None' ], False ],
            'enable': [ enable, 'enable', [ bool, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
        }, {
        } )
    
    def diagnosis_alert_definition_get(self, node, alert_id, monitor, desired_attributes=None):
        """
        Return alert definition
        
        :param node: Node hosting this health monitor.
        
        :param alert_id: Alert identification.
        
        :param monitor: Type of health monitor (e.g. node_connect,
                system_connect, system).
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "diagnosis-alert-definition-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'alert_id': [ alert_id, 'alert-id', [ basestring, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisAlertDefinitionInfo, 'None' ], False ],
        }, {
            'attributes': [ DiagnosisAlertDefinitionInfo, False ],
        } )
    
    def diagnosis_subsystem_config_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Health Monitor Subsystem Status objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Health Monitor Subsystem Status object.
                All Health Monitor Subsystem Status objects matching this query
                up to 'max-records' will be returned.
        
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
        return self.request( "diagnosis-subsystem-config-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DiagnosisSubsystemConfigInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisSubsystemConfigInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DiagnosisSubsystemConfigInfo, True ],
        } )
    
    def diagnosis_status_get(self, desired_attributes=None):
        """
        Return the overall system health
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "diagnosis-status-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisStatus, 'None' ], False ],
        }, {
            'attributes': [ DiagnosisStatus, False ],
        } )
    
    def diagnosis_delete_alert(self, node, alert_id, monitor, alerting_resource):
        """
        Delete subsystem alert
        
        :param node: Node hosting this health monitor.
        
        :param alert_id: Alert identification.
        
        :param monitor: Type of health monitor (e.g. node_connect,
                system_connect, system).
        
        :param alerting_resource: Unique name of resource that generated the alert.
        """
        return self.request( "diagnosis-delete-alert", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'alert_id': [ alert_id, 'alert-id', [ basestring, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'alerting_resource': [ alerting_resource, 'alerting-resource', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def diagnosis_alert_get(self, node, alert_id, monitor, alerting_resource, desired_attributes=None):
        """
        Return a subsystem alert
        
        :param node: Node hosting this health monitor.
        
        :param alert_id: Alert identification.
        
        :param monitor: Type of health monitor (e.g. node_connect, system_connect, system).
        
        :param alerting_resource: Unique name of resource that generated the alert.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "diagnosis-alert-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisAlertInfo, 'None' ], False ],
            'alert_id': [ alert_id, 'alert-id', [ basestring, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'alerting_resource': [ alerting_resource, 'alerting-resource', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ DiagnosisAlertInfo, False ],
        } )
    
    def diagnosis_policy_definition_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Policy Definition objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Policy Definition object.
                All Policy Definition objects matching this query up to
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
        return self.request( "diagnosis-policy-definition-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DiagnosisPolicyDefinitionInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisPolicyDefinitionInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DiagnosisPolicyDefinitionInfo, True ],
        } )
    
    def diagnosis_subsystem_config_get(self, subsystem, desired_attributes=None):
        """
        Get the attributes of the Health Monitor Subsystem Status.
        
        :param subsystem: Type of subsystem being monitored
                <p>
                Possible values:
                <ul>
                <li> 'sas_connect',
                <li> 'ha_health',
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "diagnosis-subsystem-config-get", {
            'subsystem': [ subsystem, 'subsystem', [ basestring, 'hm-subsystem' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisSubsystemConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ DiagnosisSubsystemConfigInfo, False ],
        } )
    
    def diagnosis_subscriptions_modify(self, node, monitor, notify_dest_hm, class_name, subscription_id, event_type, notify_dest_node, psc_option=None, time_gap_notify=None, notify_table=None, max_notify_period=None, fail_thresh=None, instance_name=None):
        """
        Modify system health subscription
        
        :param node: Node hosting this health monitor and sends out notifications
        
        :param monitor: Type of source health monitor (e.g. node_connect,
                system_connect, system).
        
        :param notify_dest_hm: Health monitor subsribing for notification.
        
        :param class_name: Class name of changed resource.
        
        :param subscription_id: Subscription identifier.
        
        :param event_type: Type of event (rm-add, rm-del, rm-mod) for which notification is
                to be generated.
        
        :param notify_dest_node: Node hosting the health monitor that is subscribing for
                notification.
        
        :param psc_option: Enable/Disable periodic status confirmation.
        
        :param time_gap_notify: Time Period between two notifications.
        
        :param notify_table: Table name for DSMF notification.
        
        :param max_notify_period: Maximum expected time for Notification to complete.
        
        :param fail_thresh: Failure threshold for notification.
        
        :param instance_name: Instance name of changed resource.
        """
        return self.request( "diagnosis-subscriptions-modify", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'psc_option': [ psc_option, 'psc-option', [ bool, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'notify_dest_hm': [ notify_dest_hm, 'notify-dest-hm', [ basestring, 'hm-type' ], False ],
            'time_gap_notify': [ time_gap_notify, 'time-gap-notify', [ int, 'None' ], False ],
            'notify_table': [ notify_table, 'notify-table', [ basestring, 'None' ], False ],
            'class_name': [ class_name, 'class-name', [ basestring, 'None' ], False ],
            'max_notify_period': [ max_notify_period, 'max-notify-period', [ int, 'None' ], False ],
            'subscription_id': [ subscription_id, 'subscription-id', [ basestring, 'None' ], False ],
            'event_type': [ event_type, 'event-type', [ basestring, 'hm-event-type' ], False ],
            'fail_thresh': [ fail_thresh, 'fail-thresh', [ int, 'None' ], False ],
            'instance_name': [ instance_name, 'instance-name', [ basestring, 'None' ], False ],
            'notify_dest_node': [ notify_dest_node, 'notify-dest-node', [ basestring, 'node-name' ], False ],
        }, {
        } )
    
    def diagnosis_alert_modify(self, node, monitor, alert_id, alerting_resource, acknowledge=None, suppress=None, acknowledger=None, suppressor=None):
        """
        Acknowledge/suppress an alert
        
        :param node: Node hosting this health monitor.
        
        :param monitor: Type of health monitor (e.g. node_connect, system_connect, system).
        
        :param alert_id: Alert identification.
        
        :param alerting_resource: Unique name of resource that generated the alert.
        
        :param acknowledge: Acknowledge the alert condition.
        
        :param suppress: Suppress this alert.
        
        :param acknowledger: Person who acknowledged this alert
        
        :param suppressor: Person who suppressed this alert
        """
        return self.request( "diagnosis-alert-modify", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'acknowledge': [ acknowledge, 'acknowledge', [ bool, 'None' ], False ],
            'suppress': [ suppress, 'suppress', [ bool, 'None' ], False ],
            'acknowledger': [ acknowledger, 'acknowledger', [ basestring, 'None' ], False ],
            'alert_id': [ alert_id, 'alert-id', [ basestring, 'None' ], False ],
            'alerting_resource': [ alerting_resource, 'alerting-resource', [ basestring, 'None' ], False ],
            'suppressor': [ suppressor, 'suppressor', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def diagnosis_alert_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Alert Information objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Alert Information object.
                All Alert Information objects matching this query up to
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
        return self.request( "diagnosis-alert-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DiagnosisAlertInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisAlertInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DiagnosisAlertInfo, True ],
        } )
    
    def diagnosis_alert_definition_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Alert Definition objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Alert Definition object.
                All Alert Definition objects matching this query up to
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
        return self.request( "diagnosis-alert-definition-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DiagnosisAlertDefinitionInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisAlertDefinitionInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DiagnosisAlertDefinitionInfo, True ],
        } )
    
    def diagnosis_policy_definition_get(self, node, policy_id, monitor, desired_attributes=None):
        """
        Return policy definition
        
        :param node: Node hosting this health monitor.
        
        :param policy_id: Policy identifier.
        
        :param monitor: Type of health monitor (e.g. node_connect, system_connect, system).
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "diagnosis-policy-definition-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'policy_id': [ policy_id, 'policy-id', [ basestring, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisPolicyDefinitionInfo, 'None' ], False ],
        }, {
            'attributes': [ DiagnosisPolicyDefinitionInfo, False ],
        } )
    
    def diagnosis_subscriptions_create(self, node, monitor, notify_dest_hm, class_name, subscription_id, event_type, notify_dest_node, psc_option=None, time_gap_notify=None, notify_table=None, return_record=None, max_notify_period=None, fail_thresh=None, instance_name=None):
        """
        Create a new Subscriptions for Notifications.
        
        :param node: Node hosting this health monitor and sends out notifications
        
        :param monitor: Type of source health monitor (e.g. node_connect,
                system_connect, system).
        
        :param notify_dest_hm: Health monitor subsribing for notification.
        
        :param class_name: Class name of changed resource.
        
        :param subscription_id: Subscription identifier.
        
        :param event_type: Type of event (rm-add, rm-del, rm-mod) for which notification is
                to be generated.
        
        :param notify_dest_node: Node hosting the health monitor that is subscribing for
                notification.
        
        :param psc_option: Enable/Disable periodic status confirmation.
        
        :param time_gap_notify: Time Period between two notifications.
        
        :param notify_table: Table name for DSMF notification.
        
        :param return_record: If set to true, returns the Subscriptions for Notifications on
                successful creation.
                Default: false
        
        :param max_notify_period: Maximum expected time for Notification to complete.
        
        :param fail_thresh: Failure threshold for notification.
        
        :param instance_name: Instance name of changed resource.
        """
        return self.request( "diagnosis-subscriptions-create", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'psc_option': [ psc_option, 'psc-option', [ bool, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'notify_dest_hm': [ notify_dest_hm, 'notify-dest-hm', [ basestring, 'hm-type' ], False ],
            'time_gap_notify': [ time_gap_notify, 'time-gap-notify', [ int, 'None' ], False ],
            'notify_table': [ notify_table, 'notify-table', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'class_name': [ class_name, 'class-name', [ basestring, 'None' ], False ],
            'max_notify_period': [ max_notify_period, 'max-notify-period', [ int, 'None' ], False ],
            'subscription_id': [ subscription_id, 'subscription-id', [ basestring, 'None' ], False ],
            'event_type': [ event_type, 'event-type', [ basestring, 'hm-event-type' ], False ],
            'fail_thresh': [ fail_thresh, 'fail-thresh', [ int, 'None' ], False ],
            'instance_name': [ instance_name, 'instance-name', [ basestring, 'None' ], False ],
            'notify_dest_node': [ notify_dest_node, 'notify-dest-node', [ basestring, 'node-name' ], False ],
        }, {
            'result': [ DiagnosisSubscriptionsInfo, False ],
        } )
    
    def diagnosis_subscriptions_get(self, node, monitor, notify_dest_hm, class_name, subscription_id, event_type, notify_dest_node, desired_attributes=None):
        """
        Return system health subscription
        
        :param node: Node hosting this health monitor and sends out notifications
        
        :param monitor: Type of source health monitor (e.g. node_connect, system_connect, system).
        
        :param notify_dest_hm: Health monitor subsribing for notification.
        
        :param class_name: Class name of changed resource.
        
        :param subscription_id: Subscription identifier.
        
        :param event_type: Type of event (rm-add, rm-del, rm-mod) for which notification is
                to be generated.
        
        :param notify_dest_node: Node hosting the health monitor that is subscribing for
                notification.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "diagnosis-subscriptions-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisSubscriptionsInfo, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'notify_dest_hm': [ notify_dest_hm, 'notify-dest-hm', [ basestring, 'hm-type' ], False ],
            'class_name': [ class_name, 'class-name', [ basestring, 'None' ], False ],
            'subscription_id': [ subscription_id, 'subscription-id', [ basestring, 'None' ], False ],
            'event_type': [ event_type, 'event-type', [ basestring, 'hm-event-type' ], False ],
            'notify_dest_node': [ notify_dest_node, 'notify-dest-node', [ basestring, 'node-name' ], False ],
        }, {
            'attributes': [ DiagnosisSubscriptionsInfo, False ],
        } )
    
    def diagnosis_config_get(self, node, monitor, desired_attributes=None):
        """
        Return the system health framework configuration
        
        :param node: Node hosting this health monitor.
        
        :param monitor: Type of health monitor (e.g. node_connect, system_connect, system).
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "diagnosis-config-get", {
            'node': [ node, 'node', [ basestring, 'None' ], False ],
            'monitor': [ monitor, 'monitor', [ basestring, 'hm-type' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ DiagnosisConfigInfo, False ],
        } )
    
    def diagnosis_config_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of Health Monitor Configuration objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                Health Monitor Configuration object.
                All Health Monitor Configuration objects matching this query up
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
        return self.request( "diagnosis-config-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ DiagnosisConfigInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ DiagnosisConfigInfo, 'None' ], False ],
        }, {
            'attributes-list': [ DiagnosisConfigInfo, True ],
        } )
