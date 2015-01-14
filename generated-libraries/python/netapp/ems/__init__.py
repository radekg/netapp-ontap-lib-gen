from netapp.connection import NaConnection
from ems_destination_destroy_iter_key_td import EmsDestinationDestroyIterKeyTd # 1 properties
from ems_routing_modify_iter_info import EmsRoutingModifyIterInfo # 3 properties
from ems_mail_history_destroy_iter_info import EmsMailHistoryDestroyIterInfo # 3 properties
from ems_status_info import EmsStatusInfo # 21 properties
from ems_destination_info import EmsDestinationInfo # 7 properties
from eventseverity import Eventseverity # 0 properties
from ems_routing_info import EmsRoutingInfo # 8 properties
from remote_ip import RemoteIp # 0 properties
from ems_destination import EmsDestination # 0 properties
from ems_message_get_iter_key_td import EmsMessageGetIterKeyTd # 3 properties
from ems_snmp_history_destroy_iter_info import EmsSnmpHistoryDestroyIterInfo # 3 properties
from seqnum import Seqnum # 0 properties
from ems_mail_history_get_iter_key_td import EmsMailHistoryGetIterKeyTd # 3 properties
from param import Param # 0 properties
from mail_address import MailAddress # 0 properties
from ems_routing_modify_iter_key_td import EmsRoutingModifyIterKeyTd # 1 properties
from syslog_facility import SyslogFacility # 0 properties
from ems_destination_modify_iter_key_td import EmsDestinationModifyIterKeyTd # 1 properties
from ems_destination_modify_iter_info import EmsDestinationModifyIterInfo # 3 properties
from event_log_get_iter_key_td import EventLogGetIterKeyTd # 2 properties
from ems_config_info import EmsConfigInfo # 9 properties
from ems_id import EmsId # 0 properties
from event_log_info import EventLogInfo # 14 properties
from ems_status_get_iter_key_td import EmsStatusGetIterKeyTd # 2 properties
from ems_snmp_history_get_iter_key_td import EmsSnmpHistoryGetIterKeyTd # 3 properties
from ems_routing_get_iter_key_td import EmsRoutingGetIterKeyTd # 1 properties
from ems_snmp_history_destroy_iter_key_td import EmsSnmpHistoryDestroyIterKeyTd # 3 properties
from ems_destination_get_iter_key_td import EmsDestinationGetIterKeyTd # 1 properties
from ems_message_info import EmsMessageInfo # 12 properties
from emsseverity import Emsseverity # 0 properties
from ems_mail_history_destroy_iter_key_td import EmsMailHistoryDestroyIterKeyTd # 3 properties
from ems_destination_destroy_iter_info import EmsDestinationDestroyIterInfo # 3 properties
from ems_mail_history_info import EmsMailHistoryInfo # 8 properties
from ems_snmp_history_info import EmsSnmpHistoryInfo # 8 properties

class EmsConnection(NaConnection):
    
    def ems_snmp_history_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete SNMP history entries.
        
        :param query: If deleting a specific ems-snmp-history, this input element must
                specify all keys.
                If deleting multiple ems-snmp-history objects based on query,
                this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                ems-snmp-history even when the deletion of a previous matching
                ems-snmp-history fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of ems-snmp-history objects to delete in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of ems-snmp-history
                objects (just keys) that were successfully deleted.
                If set to false, the list of ems-snmp-history objects deleted
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple ems-snmp-history
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                ems-snmp-history even when the deletion of a previous
                ems-snmp-history fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of ems-snmp-history
                objects (just keys) that were not deleted due to some error.
                If set to false, the list of ems-snmp-history objects not deleted
                will not be returned.
                Default: true
        """
        return self.request( "ems-snmp-history-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ EmsSnmpHistoryInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ EmsSnmpHistoryDestroyIterInfo, True ],
            'failure-list': [ EmsSnmpHistoryDestroyIterInfo, True ],
        } )
    
    def ems_destination_destroy(self, name):
        """
        Deletes the specified EMS destination.
        
        :param name: The name of the EMS destination.
        """
        return self.request( "ems-destination-destroy", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def ems_invoke(self, event_id, severity=None, snmp=None, syslog=None, params=None, event_version=None):
        """
        Invoke an ems event.
        This functionality is intended for use in testing syslog
        parsers or upper level SNMP management software.  The
        event will be forwarded to the ems log at /etc/log/ems
        and optionally to the syslog or SNMP trap generator.
        Invoked events in /etc/log/ems will have the attribute
        'inv' set to "1".  This is to allow auto-support to
        differentiate between real and invoked events.
        Syslog entries resulting from invoked events will contain
        the text "invoked event:" so that they aren't confused
        with real events.
        Invoked events by default are only logged to the /etc/log/ems
        log.  To have an event go to the syslog or generate an
        snmp trap, the 'syslog' and/or 'snmp' flags need to be set.
        
        :param event_id: Name of the event to invoke.
                Each ems event has a unique identifier (event-id) that can
                be used by this api to 'fake' an event.
                Example event-id's:
                kern.syslog.msg
                kern.uptime.filer
                raid.cksum.replay.nvram
                raid.cksum.replay.summary
                raid.fsm.commitStateTransit
        
        :param severity: For events with variable severity, specfies the
                severity to invoke the event at.  Shouldn't be set for events
                that don't have variable severity.
                Possible Values:
                debug info notice warning svc_error node_error
                svc_fault node_fault
        
        :param snmp: If set, and event has an SNMP definition,
                generate SNMP trap for event.  Invoked messages
                by default do not generate SNMP traps.
        
        :param syslog: If set, and the event has a syslog format definition,
                forward invoked message to syslog.
                Invoked messages are by default not forwarded
                to syslog
        
        :param {}: not documented
        
        :param event_version: If set, specifies the version of the event to
                invoke.  By default, the latest version is used.
                Accepted values are [1..n].  Event-version is only used when
                multiple versions of an event exist simultaneously within
                a given build of ONTAP.  Most events have an event-version of 1.
        """
        return self.request( "ems-invoke", {
            'severity': [ severity, 'severity', [ basestring, 'None' ], False ],
            'snmp': [ snmp, 'snmp', [ bool, 'None' ], False ],
            'syslog': [ syslog, 'syslog', [ bool, 'None' ], False ],
            'params': [ params, 'params', [ basestring, 'param' ], True ],
            'event_version': [ event_version, 'event-version', [ int, 'None' ], False ],
            'event_id': [ event_id, 'event-id', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def ems_routing_get(self, message_name, desired_attributes=None):
        """
        Return the specified EMS route information.
        
        :param message_name: The name of the EMS message.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ems-routing-get", {
            'message_name': [ message_name, 'message-name', [ basestring, 'ems-id' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsRoutingInfo, 'None' ], False ],
        }, {
            'attributes': [ EmsRoutingInfo, False ],
        } )
    
    def ems_destination_create(self, name, snmp=None, return_record=None, syslog=None, snmp_community=None, syslog_facility=None, mail=None, hide_parameters=None):
        """
        Creates an EMS destination.
        
        :param name: The name of the EMS destination.
        
        :param snmp: The SNMP addresses to which traps are sent.
        
        :param return_record: If set to true, returns the ems-destination on successful
                creation.
                Default: false
        
        :param syslog: The remote syslog servers to which messages are sent.
        
        :param snmp_community: The SNMP community name.
        
        :param syslog_facility: The syslog logging facility.
        
        :param mail: The e-mail address to which events are sent.
        
        :param hide_parameters: Hide parameter values?
        """
        return self.request( "ems-destination-create", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'snmp': [ snmp, 'snmp', [ basestring, 'remote-ip' ], True ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'syslog': [ syslog, 'syslog', [ basestring, 'remote-ip' ], True ],
            'snmp_community': [ snmp_community, 'snmp-community', [ basestring, 'None' ], False ],
            'syslog_facility': [ syslog_facility, 'syslog-facility', [ basestring, 'syslog-facility' ], False ],
            'mail': [ mail, 'mail', [ basestring, 'mail-address' ], True ],
            'hide_parameters': [ hide_parameters, 'hide-parameters', [ bool, 'None' ], False ],
        }, {
            'result': [ EmsDestinationInfo, False ],
        } )
    
    def ems_snmp_history_get(self, node, seq_num, desired_attributes=None):
        """
        Return an individual SNMP history entry.
        
        :param node: Node emitting the EMS message.
        
        :param seq_num: The message sequence number.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ems-snmp-history-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'seq_num': [ seq_num, 'seq-num', [ int, 'seqnum' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsSnmpHistoryInfo, 'None' ], False ],
        }, {
            'attributes': [ EmsSnmpHistoryInfo, False ],
        } )
    
    def ems_mail_history_get(self, node, seq_num, desired_attributes=None):
        """
        Return an individual mail history entry.
        
        :param node: Node emitting the EMS message.
        
        :param seq_num: The message sequence number.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ems-mail-history-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'seq_num': [ seq_num, 'seq-num', [ int, 'seqnum' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsMailHistoryInfo, 'None' ], False ],
        }, {
            'attributes': [ EmsMailHistoryInfo, False ],
        } )
    
    def ems_config_get(self, desired_attributes=None):
        """
        Return the EMS Configuration.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ems-config-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsConfigInfo, 'None' ], False ],
        }, {
            'attributes': [ EmsConfigInfo, False ],
        } )
    
    def ems_routing_remove_destination(self, message_name, destinations):
        """
        Remote EMS Destinations.
        
        :param message_name: The name of the EMS message.
        
        :param destinations: Destinations
        """
        return self.request( "ems-routing-remove-destination", {
            'message_name': [ message_name, 'message-name', [ basestring, 'ems-id' ], False ],
            'destinations': [ destinations, 'destinations', [ basestring, 'ems-destination' ], True ],
        }, {
        } )
    
    def ems_destination_modify(self, name, snmp=None, syslog=None, snmp_community=None, syslog_facility=None, mail=None, hide_parameters=None):
        """
        Modifies the specified EMS destination.
        
        :param name: The name of the EMS destination.
        
        :param snmp: The SNMP addresses to which traps are sent.
        
        :param syslog: The remote syslog servers to which messages are sent.
        
        :param snmp_community: The SNMP community name.
        
        :param syslog_facility: The syslog logging facility.
        
        :param mail: The e-mail address to which events are sent.
        
        :param hide_parameters: Hide parameter values?
        """
        return self.request( "ems-destination-modify", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'snmp': [ snmp, 'snmp', [ basestring, 'remote-ip' ], True ],
            'syslog': [ syslog, 'syslog', [ basestring, 'remote-ip' ], True ],
            'snmp_community': [ snmp_community, 'snmp-community', [ basestring, 'None' ], False ],
            'syslog_facility': [ syslog_facility, 'syslog-facility', [ basestring, 'syslog-facility' ], False ],
            'mail': [ mail, 'mail', [ basestring, 'mail-address' ], True ],
            'hide_parameters': [ hide_parameters, 'hide-parameters', [ bool, 'None' ], False ],
        }, {
        } )
    
    def event_log_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        auto generated : Iterate over a list of event-log objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                event-log object.
                All event-log objects matching this query up to 'max-records'
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
        return self.request( "event-log-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ EventLogInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EventLogInfo, 'None' ], False ],
        }, {
            'attributes-list': [ EventLogInfo, True ],
        } )
    
    def ems_routing_add_destination(self, message_name, destinations):
        """
        Add EMS Destinations.
        
        :param message_name: The name of the EMS message.
        
        :param destinations: Destinations
        """
        return self.request( "ems-routing-add-destination", {
            'message_name': [ message_name, 'message-name', [ basestring, 'ems-id' ], False ],
            'destinations': [ destinations, 'destinations', [ basestring, 'ems-destination' ], True ],
        }, {
        } )
    
    def ems_snmp_history_destroy(self, node, seq_num):
        """
        Delete an individual SNMP history entry.
        
        :param node: Node emitting the EMS message.
        
        :param seq_num: The message sequence number.
        """
        return self.request( "ems-snmp-history-destroy", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'seq_num': [ seq_num, 'seq-num', [ int, 'seqnum' ], False ],
        }, {
        } )
    
    def ems_routing_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modifies several EMS route.
        
        :param query: If modifying a specific ems-routing, this input element must
                specify all keys.
                If modifying ems-routing objects based on query, this input
                element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                ems-routing even when the modification of a previous matching
                ems-routing fails, and do so until the total number of objects
                failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of ems-routing
                objects (just keys) that were successfully updated.
                If set to false, the list of ems-routing objects modified will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple ems-routing objects
                match a given query.
                If set to true, the API will continue modifying the next matching
                ems-routing even when modification of a previous ems-routing
                fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of ems-routing
                objects (just keys) that were not modified due to some error.
                If set to false, the list of ems-routing objects not modified
                will not be returned.
                Default: true
        """
        return self.request( "ems-routing-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ EmsRoutingInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ EmsRoutingInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ EmsRoutingModifyIterInfo, True ],
            'failure-list': [ EmsRoutingModifyIterInfo, True ],
        } )
    
    def ems_destination_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Deletes several EMS destinations.
        
        :param query: If deleting a specific ems-destination, this input element must
                specify all keys.
                If deleting multiple ems-destination objects based on query, this
                input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                ems-destination even when the deletion of a previous matching
                ems-destination fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of ems-destination objects to delete in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of ems-destination
                objects (just keys) that were successfully deleted.
                If set to false, the list of ems-destination objects deleted will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple ems-destination
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                ems-destination even when the deletion of a previous
                ems-destination fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of ems-destination
                objects (just keys) that were not deleted due to some error.
                If set to false, the list of ems-destination objects not deleted
                will not be returned.
                Default: true
        """
        return self.request( "ems-destination-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ EmsDestinationInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ EmsDestinationDestroyIterInfo, True ],
            'failure-list': [ EmsDestinationDestroyIterInfo, True ],
        } )
    
    def ems_mail_history_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return information mail history.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ems-mail-history object.
                All ems-mail-history objects matching this query up to
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
        return self.request( "ems-mail-history-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ EmsMailHistoryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsMailHistoryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ EmsMailHistoryInfo, True ],
        } )
    
    def ems_message_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return EMS messages.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ems-message object.
                All ems-message objects matching this query up to 'max-records'
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
        return self.request( "ems-message-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ EmsMessageInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsMessageInfo, 'None' ], False ],
        }, {
            'attributes-list': [ EmsMessageInfo, True ],
        } )
    
    def ems_mail_history_destroy(self, node, seq_num):
        """
        Delete an individual mail history entry.
        
        :param node: Node emitting the EMS message.
        
        :param seq_num: The message sequence number.
        """
        return self.request( "ems-mail-history-destroy", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'seq_num': [ seq_num, 'seq-num', [ int, 'seqnum' ], False ],
        }, {
        } )
    
    def ems_destination_get(self, name, desired_attributes=None):
        """
        Return the specified EMS destination information.
        
        :param name: The name of the EMS destination.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ems-destination-get", {
            'name': [ name, 'name', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsDestinationInfo, 'None' ], False ],
        }, {
            'attributes': [ EmsDestinationInfo, False ],
        } )
    
    def ems_routing_modify(self, message_name, frequency_threshold=None, time_threshold=None, destinations=None):
        """
        Modifies the specified EMS route.
        
        :param message_name: The name of the EMS message.
        
        :param frequency_threshold: Number of times an event occurs before a repeat notification of
                the event is sent.
        
        :param time_threshold: Minimum number of seconds between repeat notifications of an
                event.
        
        :param destinations: The event destinations.
        """
        return self.request( "ems-routing-modify", {
            'frequency_threshold': [ frequency_threshold, 'frequency-threshold', [ int, 'None' ], False ],
            'message_name': [ message_name, 'message-name', [ basestring, 'ems-id' ], False ],
            'time_threshold': [ time_threshold, 'time-threshold', [ int, 'None' ], False ],
            'destinations': [ destinations, 'destinations', [ basestring, 'ems-destination' ], True ],
        }, {
        } )
    
    def ems_status_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return information on EMS messages.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ems-status object.
                All ems-status objects matching this query up to 'max-records'
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
        return self.request( "ems-status-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ EmsStatusInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsStatusInfo, 'None' ], False ],
        }, {
            'attributes-list': [ EmsStatusInfo, True ],
        } )
    
    def ems_message_get(self, node, seq_num, desired_attributes=None):
        """
        Return an EMS message.
        
        :param node: Node emitting the EMS message.
        
        :param seq_num: The message sequence number.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ems-message-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'seq_num': [ seq_num, 'seq-num', [ int, 'seqnum' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsMessageInfo, 'None' ], False ],
        }, {
            'attributes': [ EmsMessageInfo, False ],
        } )
    
    def ems_snmp_history_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return information SNMP history.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ems-snmp-history object.
                All ems-snmp-history objects matching this query up to
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
        return self.request( "ems-snmp-history-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ EmsSnmpHistoryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsSnmpHistoryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ EmsSnmpHistoryInfo, True ],
        } )
    
    def ems_autosupport_log(self, category, app_version, event_source, auto_support, event_description, computer_name, log_level, event_id):
        """
        This API is used by SnapDrive to log SnapDrive specific
        events occurring on a host system to the the appliance
        and optionally use the appliance to generate an
        autosupport message.
        This event information will be encapsulated in an
        app.log.x EMS event based on error level.
        If auto-support is true, an autosupport message
        will be sent from the filer.
        
        :param category: Application defined category of the event.
        
        :param app_version: Version of application invoking the API.
        
        :param event_source: Name of the application invoking the API.
        
        :param auto_support: If 'true', an AutoSupport message will be generated.
        
        :param event_description: Description of event to log.  An application defined
                message to log.
        
        :param computer_name: Host name invoking the API.
        
        :param log_level: Log level.  Accepted values are 0 for 'emergency',
                1 for 'alert', 2 for 'critical', 3 for 'error',
                4 for 'warning', 5 for 'notice', 6 for 'info', and
                7 for 'debug'.
        
        :param event_id: ID of event.  A user defined event-id, range [0..2^32-2].
        """
        return self.request( "ems-autosupport-log", {
            'category': [ category, 'category', [ basestring, 'None' ], False ],
            'app_version': [ app_version, 'app-version', [ basestring, 'None' ], False ],
            'event_source': [ event_source, 'event-source', [ basestring, 'None' ], False ],
            'auto_support': [ auto_support, 'auto-support', [ bool, 'None' ], False ],
            'event_description': [ event_description, 'event-description', [ basestring, 'None' ], False ],
            'computer_name': [ computer_name, 'computer-name', [ basestring, 'None' ], False ],
            'log_level': [ log_level, 'log-level', [ int, 'None' ], False ],
            'event_id': [ event_id, 'event-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def ems_destination_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modifies several EMS destinations.
        
        :param query: If modifying a specific ems-destination, this input element must
                specify all keys.
                If modifying ems-destination objects based on query, this input
                element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                ems-destination even when the modification of a previous matching
                ems-destination fails, and do so until the total number of
                objects failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of ems-destination
                objects (just keys) that were successfully updated.
                If set to false, the list of ems-destination objects modified
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple ems-destination
                objects match a given query.
                If set to true, the API will continue modifying the next matching
                ems-destination even when modification of a previous
                ems-destination fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of ems-destination
                objects (just keys) that were not modified due to some error.
                If set to false, the list of ems-destination objects not modified
                will not be returned.
                Default: true
        """
        return self.request( "ems-destination-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ EmsDestinationInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ EmsDestinationInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ EmsDestinationModifyIterInfo, True ],
            'failure-list': [ EmsDestinationModifyIterInfo, True ],
        } )
    
    def ems_status_get(self, node, message_name, desired_attributes=None):
        """
        Return information an EMS message.
        
        :param node: Node emitting the EMS message.
        
        :param message_name: The message name.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "ems-status-get", {
            'node': [ node, 'node', [ basestring, 'node-name' ], False ],
            'message_name': [ message_name, 'message-name', [ basestring, 'ems-id' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsStatusInfo, 'None' ], False ],
        }, {
            'attributes': [ EmsStatusInfo, False ],
        } )
    
    def ems_destination_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return information on EMS destinations.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ems-destination object.
                All ems-destination objects matching this query up to
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
        return self.request( "ems-destination-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ EmsDestinationInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsDestinationInfo, 'None' ], False ],
        }, {
            'attributes-list': [ EmsDestinationInfo, True ],
        } )
    
    def ems_config_modify(self, max_target_log_size=None, console=None, suppression=None, max_target_event_bytes=None, max_log_show_size=None, trace_log_size=None, mail_from=None, mail_server=None, console_log_level=None):
        """
        Modify the EMS Configuration.
        
        :param max_target_log_size: The target upper limit of the event log file size in bytes. Used
                by autosuppression to control growth of log file size.
        
        :param console: Whether console logging should be used.
        
        :param suppression: Whether suppression should be used.
        
        :param max_target_event_bytes: Maximum bytes per event per week. Used by autosuppression to
                control growth of log file size.
        
        :param max_log_show_size: Maximum number of events to show.
        
        :param trace_log_size: Maximum number of traces kept.
        
        :param mail_from: The from address of ems mail.
        
        :param mail_server: The mail server to use when sending mail.
        
        :param console_log_level: Console logging level.
                Possible values:
                <ul>
                <li> "node_fault"     - A data corruption has been detected or
                the node is unable to provide client service,
                <li> "svc_fault"      - A temporary loss of service has been
                detected, typically a transient software fault,
                <li> "node_error"     - A hardware error has been detected
                which is not immediately fatal,
                <li> "svc_error"      - A software error has been detected
                which is not immediately fatal,
                <li> "warning"        - A high-priority message, does not
                indicate a fault,
                <li> "notice"         - A normal-priority message, does not
                indicate a fault,
                <li> "info"           - A low-priority message, does not
                indicate a fault,
                <li> "debug"          - A debugging message, typically
                suppressed from customer,
                <li> "var"            - Message has variable severity, selected
                at runtime
                </ul>
        """
        return self.request( "ems-config-modify", {
            'max_target_log_size': [ max_target_log_size, 'max-target-log-size', [ int, 'None' ], False ],
            'console': [ console, 'console', [ bool, 'None' ], False ],
            'suppression': [ suppression, 'suppression', [ bool, 'None' ], False ],
            'max_target_event_bytes': [ max_target_event_bytes, 'max-target-event-bytes', [ int, 'None' ], False ],
            'max_log_show_size': [ max_log_show_size, 'max-log-show-size', [ int, 'None' ], False ],
            'trace_log_size': [ trace_log_size, 'trace-log-size', [ int, 'None' ], False ],
            'mail_from': [ mail_from, 'mail-from', [ basestring, 'mail-address' ], False ],
            'mail_server': [ mail_server, 'mail-server', [ basestring, 'remote-ip' ], False ],
            'console_log_level': [ console_log_level, 'console-log-level', [ basestring, 'emsseverity' ], False ],
        }, {
        } )
    
    def ems_routing_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return information on several EMS routes.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                ems-routing object.
                All ems-routing objects matching this query up to 'max-records'
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
        return self.request( "ems-routing-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ EmsRoutingInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsRoutingInfo, 'None' ], False ],
        }, {
            'attributes-list': [ EmsRoutingInfo, True ],
        } )
    
    def ems_mail_history_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete mail history entries.
        
        :param query: If deleting a specific ems-mail-history, this input element must
                specify all keys.
                If deleting multiple ems-mail-history objects based on query,
                this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                ems-mail-history even when the deletion of a previous matching
                ems-mail-history fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of ems-mail-history objects to delete in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of ems-mail-history
                objects (just keys) that were successfully deleted.
                If set to false, the list of ems-mail-history objects deleted
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple ems-mail-history
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                ems-mail-history even when the deletion of a previous
                ems-mail-history fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of ems-mail-history
                objects (just keys) that were not deleted due to some error.
                If set to false, the list of ems-mail-history objects not deleted
                will not be returned.
                Default: true
        """
        return self.request( "ems-mail-history-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ EmsMailHistoryInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ EmsMailHistoryDestroyIterInfo, True ],
            'failure-list': [ EmsMailHistoryDestroyIterInfo, True ],
        } )
