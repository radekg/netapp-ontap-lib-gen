from netapp.connection import NaConnection
from quota_entry import QuotaEntry # 14 properties
from quota_state_zapi import QuotaStateZapi # 0 properties
from size_or_dash import SizeOrDash # 0 properties
from unsigned64_or_dash import Unsigned64OrDash # 0 properties
from true_false import TrueFalse # 0 properties
from quota_error_msg import QuotaErrorMsg # 0 properties
from qtree_name import QtreeName # 0 properties
from quota import Quota # 14 properties
from error import Error # 3 properties
from quota_info import QuotaInfo # 13 properties
from quota_report_iter_key_td import QuotaReportIterKeyTd # 2 properties
from quota_list_entries_iter_key_td import QuotaListEntriesIterKeyTd # 6 properties
from quota_status_iter_key_td import QuotaStatusIterKeyTd # 1 properties
from quota_user import QuotaUser # 3 properties
from quota_status_attributes import QuotaStatusAttributes # 7 properties
from quota_error import QuotaError # 3 properties

class QuotaConnection(NaConnection):
    
    def quota_status_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over quota status for all volumes in the cluster
        
        :param max_records: The maximum number of records to return in this response.
        
        :param query: A query that specifies which quota status attributes need to be
                returned. A query could be specified on any number of attributes in
                the quota status object. All quota status objects matching this query
                up to 'max-records' will be returned.
        
        :param tag: Specify the tag from the previous iteration. It is usually not
                specified for the first iteration. For subsequent iterations,
                copy the value from the 'next-tag' obtained from the previous
                iteration.
        
        :param desired_attributes: Specify the attributes that should be returned in the quota status
                object. If not present, all attributes for which information is
                available will be returned. If present, only the desired attributes
                for which information is available will be returned.
        """
        return self.request( "quota-status-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ QuotaStatusAttributes, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QuotaStatusAttributes, 'None' ], False ],
        }, {
            'attributes-list': [ QuotaStatusAttributes, True ],
        } )
    
    def quota_modify_entry(self, qtree, quota_type, volume, quota_target, soft_file_limit=None, disk_limit=None, perform_user_mapping=None, threshold=None, soft_disk_limit=None, policy=None, file_limit=None):
        """
        Modifys a quota entry.  If the type, target, volume, and
        tree exist, the entry is modified.  If the type, target,
        volume, and tree do not exist, then an error is returned.
        
        :param qtree: This is the qtree name that the quota resides on. For user or
                group rules, it can be the qtree name or "" if no qtree. For
                tree type rules, this field must be "".
        
        :param quota_type: The type of quota rule. Possible values are "user", "group",
                or "tree".
        
        :param volume: This is the volume name that the quota resides on.
        
        :param quota_target: This is the quota target of the type specified.  The target
                can be of the form:
                &lt;name&gt;, &lt;number&gt;, or &lt;path name&gt;.
                Multiple targets can be specified by a comma-separated list.
                Path should be entered in a format that starts with the
                following "/vol/< volume name >/". For explicit tree rules,
                the qtree should be specified as
                "/vol/< volume name >/ < qtree name >"
        
        :param soft_file_limit: This is the number of files the target would have to exceed
                before a message is logged and an SNMP trap is generated.
                Set the value to "-" if the limit is to be unlimited.
                Default is the current value.
        
        :param disk_limit: This is the amount of disk space that is reserved for the
                the target.  The value is expressed in kilobytes (1024).
                Set the value to "-" if the limit is to be unlimited.
                Default is the current value.
        
        :param perform_user_mapping: If the value is true, quota management will perform user
                mapping for the user specified in quota-target. Only valid for
                user quotas when the quota-target refers to a Windows/UNIX user
                name. Not valid for multiple user targets.
                Default is the current value.
        
        :param threshold: This is the amount of disk space the target would have to
                exceed before a message is logged.  The value is expressed
                in kilobytes (1024).  Set the value to "-" if the limit is
                to be unlimited.  Default is the current value.
        
        :param soft_disk_limit: This is the amount of disk space the target would have to
                exceed before a message is logged and an SNMP trap is
                generated.  The value is expressed in kilobytes (1024).
                Set the value to "-" if the limit is to be unlimited.
                Default is the current value.
        
        :param policy: Name of the quota policy in which the quota rule should be
                modified. If this field is not provided, then the current
                policy that has been assigned to the vserver will be used.
        
        :param file_limit: This is the number of files that the target can have.
                Set the value to "-" if the limit is to be unlimited.
                Default is the current value.
        """
        return self.request( "quota-modify-entry", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'soft_file_limit': [ soft_file_limit, 'soft-file-limit', [ basestring, 'None' ], False ],
            'quota_type': [ quota_type, 'quota-type', [ basestring, 'None' ], False ],
            'disk_limit': [ disk_limit, 'disk-limit', [ basestring, 'None' ], False ],
            'perform_user_mapping': [ perform_user_mapping, 'perform-user-mapping', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'threshold': [ threshold, 'threshold', [ basestring, 'None' ], False ],
            'soft_disk_limit': [ soft_disk_limit, 'soft-disk-limit', [ basestring, 'None' ], False ],
            'policy': [ policy, 'policy', [ basestring, 'None' ], False ],
            'quota_target': [ quota_target, 'quota-target', [ basestring, 'None' ], False ],
            'file_limit': [ file_limit, 'file-limit', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def quota_list_entries_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over the list of quota rules in the cluster.
        
        :param max_records: The maximum number of records to return in this response.
        
        :param query: A query that specifies which quota rules need to be returned.
                A query could be specified on any number of attributes in the
                quota-entry object.  All quota entry objects matching this query
                up to 'max-records' will be returned.
        
        :param tag: Specify the tag from the previous iteration. It is usually not
                specified for the first iteration. For subsequent iterations,
                copy the value from the 'next-tag' obtained from the previous
                iteration.
        
        :param desired_attributes: Specify the attributes that should be returned in the quota-entry
                object. If not present, all attributes for which information is
                available will be returned.  If present, only the desired
                attributes for which information is available will be returned.
        """
        return self.request( "quota-list-entries-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ QuotaEntry, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ QuotaEntry, 'None' ], False ],
        }, {
            'attributes-list': [ QuotaEntry, True ],
        } )
    
    def quota_list_entries_iter_start(self, include_output_entry=None):
        """
        Starts an iteration through the list of quotas entries
        in /etc/quotas.
        
        :param include_output_entry: If specified and true, the entire quota entry is placed in
                the <line> ouput elements.
        """
        return self.request( "quota-list-entries-iter-start", {
            'include_output_entry': [ include_output_entry, 'include-output-entry', [ bool, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def quota_status(self, volume):
        """
        Obtains the status of quotas
        
        :param volume: Name of the volume whose quota status should be obtained.
        """
        return self.request( "quota-status", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'status': [ basestring, False ],
            'percent-complete': [ int, False ],
            'reason': [ basestring, False ],
            'substatus': [ basestring, False ],
            'quota-errors': [ basestring, False ],
        } )
    
    def quota_report(self, volume=None, path=None):
        """
        Returns a report on all quotas.
        
        :param volume: If provided, the report will contain
                only quotas on the specified volume name.
                The name should not contain a "/vol/" prefix.
        
        :param path: If specified, the report will contain only quotas that
                apply to the specified path name.  The path should
                start with "/vol/<volumename>", although paths without
                the "/vol" prefix will work and will be assumed to be
                in the root volume.
        """
        return self.request( "quota-report", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'quotas': [ Quota, True ],
            'error': [ Error, False ],
        } )
    
    def quota_report_iter_start(self, volume=None, path=None):
        """
        Generates a report on quotas, the results of which
        are retrieved by using quota-report-iter-next.
        
        :param volume: Name of a volume.  If specified, the report
                will contain only quotas on the specified volume.
        
        :param path: A path (including a /vol/<volumename> prefix).
                If specified, the report will contain only quotas that
                apply to the specified path name.
        """
        return self.request( "quota-report-iter-start", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
            'error': [ Error, False ],
        } )
    
    def quota_get_entry(self, volume, quota_target, qtree, quota_type, policy=None):
        """
        Obtains a quota entry specified by type, target, volume,
        and tree.
        
        :param volume: Name of the volume for the quota.
        
        :param quota_target: The quota target of the type specified.  Possible
                values are: &lt;name&gt;, &lt;number&gt;, or &lt;path name&gt;.
                Multiple targets can be specified by a comma-separated list.
                Path should be entered in a format that starts with the
                following "/vol/< volume name >/". For explicit tree rules,
                the qtree should be specified as
                "/vol/< volume name >/ < qtree name >"
        
        :param qtree: Name of the qtree for the quota. For user or group rules, it
                can be the qtree name or "" if no qtree. For tree type rules,
                this field must be "".
        
        :param quota_type: The type of quota rule. Possible values are "user", "group",
                or "tree".
        
        :param policy: Name of the quota policy from which the quota rule should be
                obtained.  If this field is not provided, then the current
                policy that has been assigned to the vserver will be used.
        """
        return self.request( "quota-get-entry", {
            'policy': [ policy, 'policy', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'quota_target': [ quota_target, 'quota-target', [ basestring, 'None' ], False ],
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'quota_type': [ quota_type, 'quota-type', [ basestring, 'None' ], False ],
        }, {
            'soft-file-limit': [ basestring, False ],
            'disk-limit': [ basestring, False ],
            'quota-error': [ QuotaError, False ],
            'perform-user-mapping': [ bool, False ],
            'soft-disk-limit': [ basestring, False ],
            'threshold': [ basestring, False ],
            'file-limit': [ basestring, False ],
        } )
    
    def quota_delete_entry(self, volume, quota_target, qtree, quota_type, policy=None):
        """
        Deletes a quota entry specified by type, target, volume,
        and tree.
        
        :param volume: Name of the volume for the quota.
        
        :param quota_target: The quota target of the type specified.  Possible
                values are: &lt;name&gt;, &lt;number&gt;, or &lt;path name&gt;.
                Multiple targets can be specified by a comma-separated list.
                Path should be entered in a format that starts with the
                following "/vol/< volume name >/". For explicit tree rules,
                the qtree should be specified as
                "/vol/< volume name >/ < qtree name >"
        
        :param qtree: Name of the qtree for the quota. For user or group rules, it
                can be the qtree name or "" if no qtree. For tree type rules,
                this field must be "".
        
        :param quota_type: The type of quota rule. Possible values are "user", "group",
                or "tree".
        
        :param policy: Name of the quota policy in which the quota rule should be
                deleted.  If this field is not provided, then the current policy
                that has been assigned to the vserver will be used.
        """
        return self.request( "quota-delete-entry", {
            'policy': [ policy, 'policy', [ basestring, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'quota_target': [ quota_target, 'quota-target', [ basestring, 'None' ], False ],
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'quota_type': [ quota_type, 'quota-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def quota_set_entry(self, qtree, quota_type, volume, quota_target, soft_file_limit=None, disk_limit=None, perform_user_mapping=None, threshold=None, soft_disk_limit=None, policy=None, file_limit=None):
        """
        Sets a quota entry.  If the type, target, volume, and
        tree do not exist, a new entry is created.  If the type,
        target, volume, and tree exist, then the entry is modified.
        
        :param qtree: Name of the qtree for the quota. For user or group rules, it
                can be the qtree name or "" if no qtree. For tree type rules,
                this field must be "".
        
        :param quota_type: The type of quota rule. Possible values are "user", "group",
                or "tree".
        
        :param volume: Name of the volume for the quota.
        
        :param quota_target: The quota target of the type specified.  Possible values are
                &lt;name&gt;, &lt;number&gt;, or &lt;path name&gt;.
                Multiple targets can be specified by a comma-separated list.
                Path should be entered in a format that starts with the
                following "/vol/< volume name >/". For explicit tree rules,
                the qtree should be specified as
                "/vol/< volume name >/ < qtree name >"
        
        :param soft_file_limit: The number of files the target would have to exceed
                before a message is logged and an SNMP trap is generated.
                Set the value to "-" if the limit is to be unlimited.
        
        :param disk_limit: The amount of disk space that is reserved for the
                the target.  The value is expressed in kilobytes (1024).
                Set the value to "-" if the limit is to be unlimited.
        
        :param perform_user_mapping: If the value is true, quota management will perform user
                mapping for the user specified in quota-target. Only valid for
                user quotas when the quota-target refers to a Windows/UNIX user
                name. Not valid for multiple user targets.
                Default is false.
        
        :param threshold: The amount of disk space the target would have to
                exceed before a message is logged.  The value is expressed
                in kilobytes (1024).  Set the value to "-" if the limit is
                to be unlimited.
        
        :param soft_disk_limit: The amount of disk space the target would have to
                exceed before a message is logged and an SNMP trap is
                generated.  The value is expressed in kilobytes (1024).
                Set the value to "-" if the limit is to be unlimited.
        
        :param policy: Name of the quota policy in which the quota rule should be
                set. If this field is not provided, then the current policy
                that has been assigned to the vserver will be used.
        
        :param file_limit: The number of files that the target can have.
                Set the value to "-" if the limit is to be unlimited.
        """
        return self.request( "quota-set-entry", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'soft_file_limit': [ soft_file_limit, 'soft-file-limit', [ basestring, 'None' ], False ],
            'quota_type': [ quota_type, 'quota-type', [ basestring, 'None' ], False ],
            'disk_limit': [ disk_limit, 'disk-limit', [ basestring, 'None' ], False ],
            'perform_user_mapping': [ perform_user_mapping, 'perform-user-mapping', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'threshold': [ threshold, 'threshold', [ basestring, 'None' ], False ],
            'soft_disk_limit': [ soft_disk_limit, 'soft-disk-limit', [ basestring, 'None' ], False ],
            'policy': [ policy, 'policy', [ basestring, 'None' ], False ],
            'quota_target': [ quota_target, 'quota-target', [ basestring, 'None' ], False ],
            'file_limit': [ file_limit, 'file-limit', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def quota_report_iter(self, max_records=None, path=None, tag=None, desired_attributes=None, query=None):
        """
        Iterate over the quota report in the cluster.
        
        :param max_records: The maximum number of records to return in this response.
        
        :param path: A path (including a /vol/<volumename> prefix).
                If specified, the report will contain only quotas that
                apply to the specified path name.
        
        :param tag: Specify the tag from the previous iteration. It is usually not
                specified for the first iteration. For subsequent iterations,
                copy the value from the 'next-tag' obtained from the previous
                iteration.
        
        :param desired_attributes: Specify the attributes that should be returned in the quota
                report object. If not present, all attributes for which
                information is available will be returned.  If present, only
                the desired attributes for which information is available
                will be returned.
        
        :param query: A query that specifies which quota report needs to be returned.
                A query could be specified on any number of attributes in the
                quota report object.  All quota report objects matching this
                query up to 'max-records' will be returned.
        """
        return self.request( "quota-report-iter", {
            'max_records': max_records,
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ Quota, 'None' ], False ],
            'query': [ query, 'query', [ Quota, 'None' ], False ],
        }, {
            'attributes-list': [ Quota, True ],
        } )
    
    def quota_off(self, volume):
        """
        Turns the quota subsystem off for a volume.
        <p>
        For clustered volumes, a jobid will also be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param volume: Name of the volume on which to turn quotas off.
        """
        return self.request( "quota-off", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def quota_list_entries_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous quota-list-entries-iter-start.
        """
        return self.request( "quota-list-entries-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def quota_report_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to quota-report-iter-start
        
        :param tag: Tag from a previous quota-report-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "quota-report-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'quotas': [ QuotaInfo, True ],
        } )
    
    def quota_add_entry(self, qtree, quota_type, volume, quota_target, soft_file_limit=None, disk_limit=None, perform_user_mapping=None, threshold=None, soft_disk_limit=None, policy=None, file_limit=None):
        """
        Adds a quota entry.  If the type, target, volume, and
        tree do not exist, a new entry is created.  If the type,
        target, volume, and tree exist, then an error is returned.
        
        :param qtree: This is the qtree name that the quota resides on. For user or
                group rules, it can be the qtree name or "" if no qtree. For
                tree type rules, this field must be "".
        
        :param quota_type: The type of quota rule. Possible values are "user", "group",
                or "tree".
        
        :param volume: This is the volume name that the quota resides on.
        
        :param quota_target: This is the quota target of the type specified.  The target
                can be of the form:
                &lt;name&gt;, &lt;number&gt;, or &lt;path name&gt;.
                Multiple targets can be specified by a comma-separated list.
                Path should be entered in a format that starts with the
                following "/vol/< volume name >/". For explicit tree rules,
                the qtree should be specified as
                "/vol/< volume name >/ < qtree name >"
        
        :param soft_file_limit: This is the number of files the target would have to exceed
                before a message is logged and an SNMP trap is generated.
                Set the value to "-" if the limit is to be unlimited.
                Default is unlimited.
        
        :param disk_limit: This is the amount of disk space that is reserved for the
                the target.  The value is expressed in kilobytes (1024).
                Set the value to "-" if the limit is to be unlimited.
                Default is unlimited.
        
        :param perform_user_mapping: If the value is true, quota management will perform user
                mapping for the user specified in quota-target. Only valid for
                user quotas when the quota-target refers to a Windows/UNIX user
                name. Not valid for multiple user targets.
                Default is false.
        
        :param threshold: This is the amount of disk space the target would have to
                exceed before a message is logged.  The value is expressed
                in kilobytes (1024).  Set the value to "-" if the limit is
                to be unlimited.  Default is unlimited.
        
        :param soft_disk_limit: This is the amount of disk space the target would have to
                exceed before a message is logged and an SNMP trap is
                generated.  The value is expressed in kilobytes (1024).
                Set the value to "-" if the limit is to be unlimited.
                Default is unlimited.
        
        :param policy: Name of the quota policy in which the quota rule should be
                added. If this field is not provided, then the current policy
                that has been assigned to the vserver will be used.
        
        :param file_limit: This is the number of files that the target can have.
                Set the value to "-" if the limit is to be unlimited.
                Default is unlimited.
        """
        return self.request( "quota-add-entry", {
            'qtree': [ qtree, 'qtree', [ basestring, 'None' ], False ],
            'soft_file_limit': [ soft_file_limit, 'soft-file-limit', [ basestring, 'None' ], False ],
            'quota_type': [ quota_type, 'quota-type', [ basestring, 'None' ], False ],
            'disk_limit': [ disk_limit, 'disk-limit', [ basestring, 'None' ], False ],
            'perform_user_mapping': [ perform_user_mapping, 'perform-user-mapping', [ bool, 'None' ], False ],
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
            'threshold': [ threshold, 'threshold', [ basestring, 'None' ], False ],
            'soft_disk_limit': [ soft_disk_limit, 'soft-disk-limit', [ basestring, 'None' ], False ],
            'policy': [ policy, 'policy', [ basestring, 'None' ], False ],
            'quota_target': [ quota_target, 'quota-target', [ basestring, 'None' ], False ],
            'file_limit': [ file_limit, 'file-limit', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def quota_list_entries(self, include_output_entry=None):
        """
        Returns quota entries from the /etc/quotas file.
        
        :param include_output_entry: If specified and true, the raw quota entry is placed in
                the <line> output element.
        """
        return self.request( "quota-list-entries", {
            'include_output_entry': [ include_output_entry, 'include-output-entry', [ bool, 'None' ], False ],
        }, {
            'quota-entries': [ QuotaEntry, True ],
        } )
    
    def quota_resize(self, volume):
        """
        Starts an ONTAP operation to resize quotas for a volume.
        A successful return from this API does not mean that
        the operation has finished, merely that an attempt
        to start it been triggered.
        Use the quota-status API to check the status.
        <p>
        For clustered volumes, a jobid will also be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param volume: Name of the volume on which to resize quotas.
        """
        return self.request( "quota-resize", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def quota_on(self, volume):
        """
        Starts to turn quotas on for a volume.
        A successful return from this API does not mean that
        quotas are on, merely that an attempt to start it has
        been triggered.  Use the quota-status API to check
        the status.
        <p>
        For clustered volumes, a jobid will also be returned.
        The progress of the job can be tracked using the job APIs.
        
        :param volume: Name of the volume on which to enable quotas.
        """
        return self.request( "quota-on", {
            'volume': [ volume, 'volume', [ basestring, 'None' ], False ],
        }, {
            'result-error-message': [ basestring, False ],
            'result-jobid': [ int, False ],
            'result-error-code': [ int, False ],
            'result-status': [ basestring, False ],
        } )
    
    def quota_list_entries_iter_next(self, tag, maximum):
        """
        Continues an iteration through the list of quotas.
        
        :param tag: Tag from a previous quota-list-entries-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "quota-list-entries-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'quota-entries': [ QuotaEntry, True ],
        } )
    
    def quota_report_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous quota-report-iter-start.
        """
        return self.request( "quota-report-iter-end", {
            'tag': tag,
        }, {
        } )
