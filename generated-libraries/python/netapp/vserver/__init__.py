from netapp.connection import NaConnection
from snapshot_policy import SnapshotPolicy # 0 properties
from vserver_aggr_info import VserverAggrInfo # 2 properties
from vserver_info import VserverInfo # 23 properties
from protocol import Protocol # 0 properties
from volume_name import VolumeName # 0 properties
from nsswitch import Nsswitch # 0 properties
from vsadminstate import Vsadminstate # 0 properties
from size import Size # 0 properties
from security_style_enum import SecurityStyleEnum # 0 properties
from vserver_modify_iter_key_td import VserverModifyIterKeyTd # 1 properties
from uuid import Uuid # 0 properties
from language_code import LanguageCode # 0 properties
from vserver_get_iter_key_td import VserverGetIterKeyTd # 1 properties
from nmswitch import Nmswitch # 0 properties
from antivirus_policy import AntivirusPolicy # 0 properties
from vserver_modify_iter_info import VserverModifyIterInfo # 3 properties
from nis_domain import NisDomain # 0 properties
from aggr_name import AggrName # 0 properties

class VserverConnection(NaConnection):
    
    def vserver_create(self, vserver_name, name_server_switch, root_volume_aggregate, root_volume_security_style, root_volume, comment=None, language=None, name_mapping_switch=None, quota_policy=None, return_record=None, snapshot_policy=None, antivirus_on_access_policy=None, is_repository_vserver=None):
        """
        Create a new Vserver. Use a fully qualified domain name(FQDN) -
        for example, 'data.example.com' - for the Vserver name to reduce
        name collisions in cluster leagues.
        
        :param vserver_name: Name of the Vserver. When specified as part of a vserver-create,
                this field represents the name of the Vserver. When part of
                vserver-get-iter call, this will return the list of matching
                Vservers.
        
        :param name_server_switch: Name Server switch configuration details for the Vserver. When
                specified as part of the vserver-create, this field represents
                the list of Name Server switch configurations to be used. When
                specified as part of the vserver-get-iter, this will return the
                list of Vservers which have any of the specified Name Server
                configurations as part of their ns-switch configuration. Possible
                values: 'nis', 'file', 'ldap'.
                Possible values:
                <ul>
                <li> "nis"  ,
                <li> "file" ,
                <li> "ldap"
                </ul>
        
        :param root_volume_aggregate: The aggregate on which the root volume will be created. When
                specified as part of a vserver-create, this field represents the
                aggregate on which the Vserver root volume will be created. When
                part of vserver-get-iter call, this will return the list of
                matching Vservers.
        
        :param root_volume_security_style: Security Style of the root volume. When specified as part of the
                vserver-create, this field represents the security style for the
                Vserver root volume. When specified as part of vserver-get-iter
                call, this will return the list of matching Vservers. Possible
                values: 'unix', 'ntfs', 'mixed'. The 'unified' security style,
                which applies only to Infinite Volumes, cannot be applied to a
                Vserver's root volume.
                Possible values:
                <ul>
                <li> "unix"      - NFS,
                <li> "ntfs"      - CIFS,
                <li> "mixed"     - Mixed,
                <li> "unified"   - Unified
                </ul>
        
        :param root_volume: Root volume of the Vserver. When specified as part of a
                vserver-create, this field represents the name of the Vserver
                root volume. When part of vserver-get-iter call, this will return
                the list of matching Vservers.
        
        :param comment: Comment. When specified as part of a vserver-create, this field
                represents the comment associated with the Vserver. When part of
                vserver-get-iter call, this will return the list of matching
                Vservers.
        
        :param language: Language to use for the Vserver. Default:
                C.UTF-8.
                Available language codes are:
                'c' .............. POSIX
                'ar' ............. Arabic
                'cs' ............. Czech
                'da' ............. Danish
                'de' ............. German
                'en' ............. English
                'en_us' .......... English (US)
                'es' ............. Spanish
                'fi' ............. Finnish
                'fr' ............. French
                'he' ............. Hebrew
                'hr' ............. Croatian
                'hu' ............. Hungarian
                'it' ............. Italian
                'ja' ............. Japanese euc-j*
                'ja_v1' .......... Japanese euc-j
                'ja_jp.pck' ...... Japanese PCK (sjis)*
                'ja_jp.932' ...... Japanese cp932*
                'ja_jp.pck_v2' .... Japanese PCK (sjis)
                'ko' ............. Korean
                'no' ............. Norwegian
                'nl' ............. Dutch
                'pl' ............. Polish
                'pt' ............. Portuguese
                'ro' ............. Romanian
                'ru' ............. Russian
                'sk' ............. Slovak
                'sl' ............. Slovenian
                'sv' ............. Swedish
                'tr' ............. Turkish
                'zh' ............. Simplified Chinese
                'zh.gbk' ......... Simplified Chinese (GBK)
                'zh_tw' .......... Traditional Chinese euc-tw
                'zh_tw.big5' ..... Traditional Chinese Big 5
                To use UTF-8 as the NFS character set, append '.UTF-8'.
                When specified as part of vserver-create, this field represents
                the language used for the Vserver. When part of vserver-get-iter
                call, this will return the list of matching Vservers with the
                specified language. The values with the '*' suffixes are not
                supported by Clustered ONTAP.
        
        :param name_mapping_switch: Name Mapping switch configuration details for the Vserver. When
                specified as part of the vserver-create, this field represents
                the list of Name Mapping switch configurations to be used. When
                specified as part of the vserver-get-iter, this will return the
                list of Vservers which have any of the specified Name Mapping
                configurations as part of their nm-switch configuration. Possible
                values: 'file', 'ldap'. default: file
                Possible values:
                <ul>
                <li> "file" ,
                <li> "ldap"
                </ul>
        
        :param quota_policy: Quota policy. When specified as part of vserver-create, this
                field represents the quota policy for the Vserver. When specified
                as part vserver-get-iter call, this will return the list of
                matching Vservers. default: default
        
        :param return_record: If set to true, returns the vserver on successful creation.
                Default: false
        
        :param snapshot_policy: Default snapshot policy setting for all volumes of the Vserver.
                This policy will be assigned to all volumes created in this
                Vserver unless the volume create request explicitly provides a
                snapshot policy or volume is modified later with a specific
                snapshot policy. A volume-level snapshot policy always overrides
                the default Vserver-wide snapshot policy. When specified as part
                vserver-get-iter call, this will return the list of matching
                Vservers. default: default
        
        :param antivirus_on_access_policy: {Deprecated, this field does not have any effect on the operation
                of the vserver.} Antivirus policy. When specified as part of
                vserver-create, this field represents the antivirus on access
                policy for the Vserver. When specified as part vserver-get-iter
                call, this will return the list of matching Vservers. default:
                default
        
        :param is_repository_vserver: Specifies if this Vserver is a Vserver with Infinite Volume. When
                part of vserver-get-iter call, this will return the list of
                matching Vservers. Default value is false.
                <p>
                Prior to Data ONTAP 8.2.0, Vserver with Infinite Volume is called
                repository Vserver and once a repository Vserver is created in a
                cluster, additional Vservers cannot be created. Conversely, a
                repository Vserver cannot be created if non-repository Vservers
                already exist in a cluster.
        """
        return self.request( "vserver-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'language': [ language, 'language', [ basestring, 'language-code' ], False ],
            'name_mapping_switch': [ name_mapping_switch, 'name-mapping-switch', [ basestring, 'nmswitch' ], True ],
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
            'name_server_switch': [ name_server_switch, 'name-server-switch', [ basestring, 'nsswitch' ], True ],
            'quota_policy': [ quota_policy, 'quota-policy', [ basestring, 'None' ], False ],
            'root_volume_aggregate': [ root_volume_aggregate, 'root-volume-aggregate', [ basestring, 'aggr-name' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'snapshot_policy': [ snapshot_policy, 'snapshot-policy', [ basestring, 'snapshot-policy' ], False ],
            'root_volume_security_style': [ root_volume_security_style, 'root-volume-security-style', [ basestring, 'security-style-enum' ], False ],
            'root_volume': [ root_volume, 'root-volume', [ basestring, 'volume-name' ], False ],
            'antivirus_on_access_policy': [ antivirus_on_access_policy, 'antivirus-on-access-policy', [ basestring, 'antivirus-policy' ], False ],
            'is_repository_vserver': [ is_repository_vserver, 'is-repository-vserver', [ bool, 'None' ], False ],
        }, {
            'result': [ VserverInfo, False ],
        } )
    
    def vserver_rename(self, vserver_name, new_name):
        """
        Rename a Vserver. Use a fully qualified domain name(FQDN) - for
        example, 'data.example.com' - for the Vserver name to reduce name
        collisions in cluster leagues. This operation is not supported
        for a node Vserver. Use the 'system-node-rename' API to rename a
        node Vserver.
        
        :param vserver_name: Vserver
        
        :param new_name: New Vserver name (Use Fully Qualified Domain Name, For example:
                data.example.com)
        """
        return self.request( "vserver-rename", {
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
            'new_name': [ new_name, 'new-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_data_policy_export(self):
        """
        Export a data policy for a Vserver with an Infinite Volume. The
        data policy is exported as a JSON string. For a description of
        the JSON format, please refer to the Data ONTAP System
        Administration Guide for Cluster-Mode.
        """
        return self.request( "vserver-data-policy-export", {
        }, {
            'data-policy-expression': [ basestring, False ],
        } )
    
    def vserver_get(self, desired_attributes=None):
        """
        Get the attributes of the vserver.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "vserver-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VserverInfo, 'None' ], False ],
        }, {
            'attributes': [ VserverInfo, False ],
        } )
    
    def vserver_data_policy_import(self, data_policy_expression):
        """
        Import a data policy for a Vserver with an Infinite Volume. The
        data policy is imported as a JSON string. For a description of
        the required JSON format, please refer to the Data ONTAP System
        Administration Guide for Cluster-Mode.
        
        :param data_policy_expression: Data-policy JSON expression. A JSON string with a maximum length
                of 50 MB. The string should be XML escaped and use the same
                encoding as the XML document of which it is a part (UTF8 for
                APIs).
        """
        return self.request( "vserver-data-policy-import", {
            'data_policy_expression': [ data_policy_expression, 'data-policy-expression', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_destroy(self, vserver_name):
        """
        Destroys the Vserver and its objects. All volumes and mirrors
        belonging to the Vserver must be deleted using other APIs before
        destroying the Vserver. EVOLEXISTS is returned if the Vserver is
        found to have any volumes or mirrors. This APIS removes all
        other objects of this Vserver including its network Interfaces,
        routes, configurations, admin login accounts and roles.
        
        :param vserver_name: Name of the Vserver. When specified as part of a vserver-create,
                this field represents the name of the Vserver. When part of
                vserver-get-iter call, this will return the list of matching
                Vservers.
        """
        return self.request( "vserver-destroy", {
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_modify(self, vserver_name, comment=None, name_server_switch=None, name_mapping_switch=None, antivirus_on_access_policy=None, language=None, quota_policy=None, disallowed_protocols=None, snapshot_policy=None, state=None, allowed_protocols=None, aggr_list=None, max_volumes=None, qos_policy_group=None):
        """
        Modify the attributes of vserver object.
        
        :param vserver_name: Name of the Vserver. When specified as part of a vserver-create,
                this field represents the name of the Vserver. When part of
                vserver-get-iter call, this will return the list of matching
                Vservers.
        
        :param comment: Comment. When specified as part of a vserver-create, this field
                represents the comment associated with the Vserver. When part of
                vserver-get-iter call, this will return the list of matching
                Vservers.
        
        :param name_server_switch: Name Server switch configuration details for the Vserver. When
                specified as part of the vserver-create, this field represents
                the list of Name Server switch configurations to be used. When
                specified as part of the vserver-get-iter, this will return the
                list of Vservers which have any of the specified Name Server
                configurations as part of their ns-switch configuration. Possible
                values: 'nis', 'file', 'ldap'.
                Possible values:
                <ul>
                <li> "nis"  ,
                <li> "file" ,
                <li> "ldap"
                </ul>
        
        :param name_mapping_switch: Name Mapping switch configuration details for the Vserver. When
                specified as part of the vserver-create, this field represents
                the list of Name Mapping switch configurations to be used. When
                specified as part of the vserver-get-iter, this will return the
                list of Vservers which have any of the specified Name Mapping
                configurations as part of their nm-switch configuration. Possible
                values: 'file', 'ldap'. default: file
                Possible values:
                <ul>
                <li> "file" ,
                <li> "ldap"
                </ul>
        
        :param antivirus_on_access_policy: {Deprecated, this field does not have any effect on the operation
                of the vserver.} Antivirus policy. When specified as part of
                vserver-create, this field represents the antivirus on access
                policy for the Vserver. When specified as part vserver-get-iter
                call, this will return the list of matching Vservers. default:
                default
        
        :param language: Language to use for the Vserver. Default:
                C.UTF-8.
                Available language codes are:
                'c' .............. POSIX
                'ar' ............. Arabic
                'cs' ............. Czech
                'da' ............. Danish
                'de' ............. German
                'en' ............. English
                'en_us' .......... English (US)
                'es' ............. Spanish
                'fi' ............. Finnish
                'fr' ............. French
                'he' ............. Hebrew
                'hr' ............. Croatian
                'hu' ............. Hungarian
                'it' ............. Italian
                'ja' ............. Japanese euc-j*
                'ja_v1' .......... Japanese euc-j
                'ja_jp.pck' ...... Japanese PCK (sjis)*
                'ja_jp.932' ...... Japanese cp932*
                'ja_jp.pck_v2' .... Japanese PCK (sjis)
                'ko' ............. Korean
                'no' ............. Norwegian
                'nl' ............. Dutch
                'pl' ............. Polish
                'pt' ............. Portuguese
                'ro' ............. Romanian
                'ru' ............. Russian
                'sk' ............. Slovak
                'sl' ............. Slovenian
                'sv' ............. Swedish
                'tr' ............. Turkish
                'zh' ............. Simplified Chinese
                'zh.gbk' ......... Simplified Chinese (GBK)
                'zh_tw' .......... Traditional Chinese euc-tw
                'zh_tw.big5' ..... Traditional Chinese Big 5
                To use UTF-8 as the NFS character set, append '.UTF-8'.
                When specified as part of vserver-create, this field represents
                the language used for the Vserver. When part of vserver-get-iter
                call, this will return the list of matching Vservers with the
                specified language. The values with the '*' suffixes are not
                supported by Clustered ONTAP.
        
        :param quota_policy: Quota policy. When specified as part of vserver-create, this
                field represents the quota policy for the Vserver. When specified
                as part vserver-get-iter call, this will return the list of
                matching Vservers. default: default
        
        :param disallowed_protocols: Disallowed Protocols. If conflicting entries are provided as
                input to allowed-protocols and disallowed-protocols list, then
                those entries will become part of the disallowed-protocols list.
                When specified as part of a vserver-create, this field represent
                the list of protocols not allowed on the Vserver. When part of
                vserver-get-iter call, this will return the list of Vservers
                which have any of the protocols specified as part of the
                disallowed-protocols.
                Possible values:
                <ul>
                <li> "nfs"       - NFS protocol,
                <li> "cifs"      - CIFS protocol,
                <li> "fcp"       - FCP protocol,
                <li> "iscsi"     - iSCSI protocol,
                <li> "ndmp"      - NDMP protocol
                </ul>
        
        :param snapshot_policy: Default snapshot policy setting for all volumes of the Vserver.
                This policy will be assigned to all volumes created in this
                Vserver unless the volume create request explicitly provides a
                snapshot policy or volume is modified later with a specific
                snapshot policy. A volume-level snapshot policy always overrides
                the default Vserver-wide snapshot policy. When specified as part
                vserver-get-iter call, this will return the list of matching
                Vservers. default: default
        
        :param state: State of the Vserver. This field represents
                the data serving ability of a Vserver, hence is applicable only
                for Data Vservers.
                Possible values:
                <ul>
                <li> "running"        ,
                <li> "stopped"        ,
                <li> "starting"       ,
                <li> "stopping"       ,
                <li> "initializing"   ,
                <li> "deleting"
                </ul>
        
        :param allowed_protocols: Allowed Protocols. If conflicting entries are provided as input
                to allowed-protocols and disallowed-protocols list, then those
                entries will become part of the disallowed-protocols list. When
                specified as part of a vserver-create, this field represent the
                list of protocols allowed on the Vserver. When part of
                vserver-get-iter call, this will return the list of Vservers
                which have any of the protocols specified as part of the
                allowed-protocols.
                Possible values:
                <ul>
                <li> "nfs"       - NFS protocol,
                <li> "cifs"      - CIFS protocol,
                <li> "fcp"       - FCP protocol,
                <li> "iscsi"     - iSCSI protocol,
                <li> "ndmp"      - NDMP protocol
                </ul>
        
        :param aggr_list: List of aggregates assigned for volume operations. These
                aggregates could be shared for use with other Vservers. When
                specified as part of a vserver-create, this field represents the
                list of aggregates that are assigned to the Vserver for volume
                operations. When part of vserver-get-iter call, this will return
                the list of Vservers which have any of the aggregates specified
                as part of the aggr-list.
        
        :param max_volumes: Maximum number of volumes that can be created on the Vserver.
                When specified as part of a vserver-create, this field represents
                the maximum number of volumes that can be created on the Vserver.
                When part of vserver-get-iter call, this will return the list of
                matching Vservers.
        
        :param qos_policy_group: The QoS policy group associated with this volume. This optionally
                specifies which QoS policy group to apply to the Vserver. The
                policy group defines measurable service level objectives (SLOs)
                that apply to the storage objects with which the policy group is
                associated. If you do not assign a policy group to a Vserver, the
                system will not monitor and control traffic to it. This parameter
                is not supported on a Vserver with Infinite Volume.
        """
        return self.request( "vserver-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'name_server_switch': [ name_server_switch, 'name-server-switch', [ basestring, 'nsswitch' ], True ],
            'name_mapping_switch': [ name_mapping_switch, 'name-mapping-switch', [ basestring, 'nmswitch' ], True ],
            'antivirus_on_access_policy': [ antivirus_on_access_policy, 'antivirus-on-access-policy', [ basestring, 'antivirus-policy' ], False ],
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
            'language': [ language, 'language', [ basestring, 'language-code' ], False ],
            'quota_policy': [ quota_policy, 'quota-policy', [ basestring, 'None' ], False ],
            'disallowed_protocols': [ disallowed_protocols, 'disallowed-protocols', [ basestring, 'protocol' ], True ],
            'snapshot_policy': [ snapshot_policy, 'snapshot-policy', [ basestring, 'snapshot-policy' ], False ],
            'state': [ state, 'state', [ basestring, 'vsadminstate' ], False ],
            'allowed_protocols': [ allowed_protocols, 'allowed-protocols', [ basestring, 'protocol' ], True ],
            'aggr_list': [ aggr_list, 'aggr-list', [ basestring, 'aggr-name' ], True ],
            'max_volumes': [ max_volumes, 'max-volumes', [ basestring, 'None' ], False ],
            'qos_policy_group': [ qos_policy_group, 'qos-policy-group', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_start(self, vserver_name):
        """
        Start a Vserver
        
        :param vserver_name: Name of the Vserver. When specified as part of a vserver-create,
                this field represents the name of the Vserver. When part of
                vserver-get-iter call, this will return the list of matching
                Vservers.
        """
        return self.request( "vserver-start", {
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Display information about Vservers.
        Information about Admin Vserver, Node Vserver, and
        Data Vservers is displayed. If the ZAPI is issued to
        the Cluster LIF with no Vserver specified as input,
        then
        information about all Vservers is shown. If the
        request
        is sent to the Vserver LIF, then information about
        that
        Vserver is shown.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                vserver object.
                All vserver objects matching this query up to 'max-records' will
                be returned.
        
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
        return self.request( "vserver-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ VserverInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ VserverInfo, 'None' ], False ],
        }, {
            'attributes-list': [ VserverInfo, True ],
        } )
    
    def vserver_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify the attributes of vserver or a group of
        vserver objects.
        
        :param query: If modifying a specific vserver, this input element must specify
                all keys.
                If modifying vserver objects based on query, this input element
                must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching vserver
                even when the modification of a previous matching vserver fails,
                and do so until the total number of objects failed to be modified
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of vserver objects
                (just keys) that were successfully updated.
                If set to false, the list of vserver objects modified will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple vserver objects match
                a given query.
                If set to true, the API will continue modifying the next matching
                vserver even when modification of a previous vserver fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of vserver objects
                (just keys) that were not modified due to some error.
                If set to false, the list of vserver objects not modified will
                not be returned.
                Default: true
        """
        return self.request( "vserver-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ VserverInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ VserverInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ VserverModifyIterInfo, True ],
            'failure-list': [ VserverModifyIterInfo, True ],
        } )
    
    def vserver_data_policy_validation_get_error(self, expression):
        """
        Validate without importing a data policy for a Vserver with an
        Infinite Volume. The data policy needs to be specified as a JSON
        string. For a description of the required JSON format, please
        refer to the Data ONTAP System Administration Guide for
        Cluster-Mode.
        
        :param expression: Data-policy JSON expression. A JSON string with a maximum length
                of 50 MB. The string should be XML escaped and use the same
                encoding as the XML document of which it is a part (UTF8 for
                APIs).
        """
        return self.request( "vserver-data-policy-validation-get-error", {
            'expression': [ expression, 'expression', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def vserver_stop(self, vserver_name):
        """
        Stop a Vserver
        
        :param vserver_name: Name of the Vserver. When specified as part of a vserver-create,
                this field represents the name of the Vserver. When part of
                vserver-get-iter call, this will return the list of matching
                Vservers.
        """
        return self.request( "vserver-stop", {
            'vserver_name': [ vserver_name, 'vserver-name', [ basestring, 'None' ], False ],
        }, {
        } )
