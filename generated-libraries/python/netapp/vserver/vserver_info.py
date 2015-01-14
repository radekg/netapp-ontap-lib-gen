from netapp.vserver.vserver_aggr_info import VserverAggrInfo
from netapp.netapp_object import NetAppObject

class VserverInfo(NetAppObject):
    """
    Vserver Information
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _comment = None
    @property
    def comment(self):
        """
        Comment. When specified as part of a vserver-create, this
        field represents the comment associated with the Vserver.
        When part of vserver-get-iter call, this will return the
        list of matching Vservers.
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _allowed_protocols = None
    @property
    def allowed_protocols(self):
        """
        Allowed Protocols. If conflicting entries are provided as
        input to allowed-protocols and disallowed-protocols list,
        then those entries will become part of the
        disallowed-protocols list. When specified as part of a
        vserver-create, this field represent the list of
        protocols allowed on the Vserver. When part of
        vserver-get-iter call, this will return the list of
        Vservers which have any of the protocols specified as
        part of the allowed-protocols.
        Attributes: non-creatable, modifiable
        Possible values:
        <ul>
        <li> "nfs"       - NFS protocol,
        <li> "cifs"      - CIFS protocol,
        <li> "fcp"       - FCP protocol,
        <li> "iscsi"     - iSCSI protocol,
        <li> "ndmp"      - NDMP protocol
        </ul>
        """
        return self._allowed_protocols
    @allowed_protocols.setter
    def allowed_protocols(self, val):
        if val != None:
            self.validate('allowed_protocols', val)
        self._allowed_protocols = val
    
    _max_volumes = None
    @property
    def max_volumes(self):
        """
        Maximum number of volumes that can be created on the
        Vserver. When specified as part of a vserver-create, this
        field represents the maximum number of volumes that can
        be created on the Vserver. When part of vserver-get-iter
        call, this will return the list of matching Vservers.
        Attributes: non-creatable, modifiable
        """
        return self._max_volumes
    @max_volumes.setter
    def max_volumes(self, val):
        if val != None:
            self.validate('max_volumes', val)
        self._max_volumes = val
    
    _name_mapping_switch = None
    @property
    def name_mapping_switch(self):
        """
        Name Mapping switch configuration details for the
        Vserver. When specified as part of the vserver-create,
        this field represents the list of Name Mapping switch
        configurations to be used. When specified as part of the
        vserver-get-iter, this will return the list of Vservers
        which have any of the specified Name Mapping
        configurations as part of their nm-switch configuration.
        Possible values: 'file', 'ldap'. default: file
        Attributes: optional-for-create, modifiable
        Possible values:
        <ul>
        <li> "file" ,
        <li> "ldap"
        </ul>
        """
        return self._name_mapping_switch
    @name_mapping_switch.setter
    def name_mapping_switch(self, val):
        if val != None:
            self.validate('name_mapping_switch', val)
        self._name_mapping_switch = val
    
    _antivirus_on_access_policy = None
    @property
    def antivirus_on_access_policy(self):
        """
        {Deprecated, this field does not have any effect on the
        operation of the vserver.} Antivirus policy. When
        specified as part of vserver-create, this field
        represents the antivirus on access policy for the
        Vserver. When specified as part vserver-get-iter call,
        this will return the list of matching Vservers. default:
        default
        Attributes: optional-for-create, modifiable
        """
        return self._antivirus_on_access_policy
    @antivirus_on_access_policy.setter
    def antivirus_on_access_policy(self, val):
        if val != None:
            self.validate('antivirus_on_access_policy', val)
        self._antivirus_on_access_policy = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        Universal unique identifier (UUID) for the Vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _snapshot_policy = None
    @property
    def snapshot_policy(self):
        """
        Default snapshot policy setting for all volumes of the
        Vserver. This policy will be assigned to all volumes
        created in this Vserver unless the volume create request
        explicitly provides a snapshot policy or volume is
        modified later with a specific snapshot policy. A
        volume-level snapshot policy always overrides the default
        Vserver-wide snapshot policy. When specified as part
        vserver-get-iter call, this will return the list of
        matching Vservers. default: default
        Attributes: optional-for-create, modifiable
        """
        return self._snapshot_policy
    @snapshot_policy.setter
    def snapshot_policy(self, val):
        if val != None:
            self.validate('snapshot_policy', val)
        self._snapshot_policy = val
    
    _root_volume_security_style = None
    @property
    def root_volume_security_style(self):
        """
        Security Style of the root volume. When specified as part
        of the vserver-create, this field represents the security
        style for the Vserver root volume. When specified as part
        of vserver-get-iter call, this will return the list of
        matching Vservers. Possible values: 'unix', 'ntfs',
        'mixed'. The 'unified' security style, which applies only
        to Infinite Volumes, cannot be applied to a Vserver's
        root volume.
        Attributes: required-for-create, non-modifiable
        Possible values:
        <ul>
        <li> "unix"      - NFS,
        <li> "ntfs"      - CIFS,
        <li> "mixed"     - Mixed,
        <li> "unified"   - Unified
        </ul>
        """
        return self._root_volume_security_style
    @root_volume_security_style.setter
    def root_volume_security_style(self, val):
        if val != None:
            self.validate('root_volume_security_style', val)
        self._root_volume_security_style = val
    
    _state = None
    @property
    def state(self):
        """
        State of the Vserver. This field represents
        the data serving ability of a Vserver, hence is
        applicable only for Data Vservers.
        Attributes: non-creatable, modifiable
        Possible values:
        <ul>
        <li> "running"        ,
        <li> "stopped"        ,
        <li> "starting"       ,
        <li> "stopping"       ,
        <li> "initializing"   ,
        <li> "deleting"
        </ul>
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _aggr_list = None
    @property
    def aggr_list(self):
        """
        List of aggregates assigned for volume operations. These
        aggregates could be shared for use with other Vservers.
        When specified as part of a vserver-create, this field
        represents the list of aggregates that are assigned to
        the Vserver for volume operations. When part of
        vserver-get-iter call, this will return the list of
        Vservers which have any of the aggregates specified as
        part of the aggr-list.
        Attributes: non-creatable, modifiable
        """
        return self._aggr_list
    @aggr_list.setter
    def aggr_list(self, val):
        if val != None:
            self.validate('aggr_list', val)
        self._aggr_list = val
    
    _vserver_name = None
    @property
    def vserver_name(self):
        """
        Name of the Vserver. When specified as part of a
        vserver-create, this field represents the name of the
        Vserver. When part of vserver-get-iter call, this will
        return the list of matching Vservers.
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver_name
    @vserver_name.setter
    def vserver_name(self, val):
        if val != None:
            self.validate('vserver_name', val)
        self._vserver_name = val
    
    _root_volume_aggregate = None
    @property
    def root_volume_aggregate(self):
        """
        The aggregate on which the root volume will be created.
        When specified as part of a vserver-create, this field
        represents the aggregate on which the Vserver root volume
        will be created. When part of vserver-get-iter call, this
        will return the list of matching Vservers.
        Attributes: required-for-create, non-modifiable
        """
        return self._root_volume_aggregate
    @root_volume_aggregate.setter
    def root_volume_aggregate(self, val):
        if val != None:
            self.validate('root_volume_aggregate', val)
        self._root_volume_aggregate = val
    
    _root_volume = None
    @property
    def root_volume(self):
        """
        Root volume of the Vserver. When specified as part of a
        vserver-create, this field represents the name of the
        Vserver root volume. When part of vserver-get-iter call,
        this will return the list of matching Vservers.
        Attributes: required-for-create, non-modifiable
        """
        return self._root_volume
    @root_volume.setter
    def root_volume(self, val):
        if val != None:
            self.validate('root_volume', val)
        self._root_volume = val
    
    _nis_domain = None
    @property
    def nis_domain(self):
        """
        NIS domain configuration details for the
        Vserver.
        Attributes: non-creatable, non-modifiable
        """
        return self._nis_domain
    @nis_domain.setter
    def nis_domain(self, val):
        if val != None:
            self.validate('nis_domain', val)
        self._nis_domain = val
    
    _disallowed_protocols = None
    @property
    def disallowed_protocols(self):
        """
        Disallowed Protocols. If conflicting entries are provided
        as input to allowed-protocols and disallowed-protocols
        list, then those entries will become part of the
        disallowed-protocols list. When specified as part of a
        vserver-create, this field represent the list of
        protocols not allowed on the Vserver. When part of
        vserver-get-iter call, this will return the list of
        Vservers which have any of the protocols specified as
        part of the disallowed-protocols.
        Attributes: non-creatable, modifiable
        Possible values:
        <ul>
        <li> "nfs"       - NFS protocol,
        <li> "cifs"      - CIFS protocol,
        <li> "fcp"       - FCP protocol,
        <li> "iscsi"     - iSCSI protocol,
        <li> "ndmp"      - NDMP protocol
        </ul>
        """
        return self._disallowed_protocols
    @disallowed_protocols.setter
    def disallowed_protocols(self, val):
        if val != None:
            self.validate('disallowed_protocols', val)
        self._disallowed_protocols = val
    
    _name_server_switch = None
    @property
    def name_server_switch(self):
        """
        Name Server switch configuration details for the Vserver.
        When specified as part of the vserver-create, this field
        represents the list of Name Server switch configurations
        to be used. When specified as part of the
        vserver-get-iter, this will return the list of Vservers
        which have any of the specified Name Server
        configurations as part of their ns-switch configuration.
        Possible values: 'nis', 'file', 'ldap'.
        Attributes: required-for-create, modifiable
        Possible values:
        <ul>
        <li> "nis"  ,
        <li> "file" ,
        <li> "ldap"
        </ul>
        """
        return self._name_server_switch
    @name_server_switch.setter
    def name_server_switch(self, val):
        if val != None:
            self.validate('name_server_switch', val)
        self._name_server_switch = val
    
    _language = None
    @property
    def language(self):
        """
        Language to use for the Vserver. Default:
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
        To use UTF-8 as the NFS character set, append
        '.UTF-8'. When specified as part of vserver-create, this
        field represents the language used for the Vserver. When
        part of vserver-get-iter call, this will return the list
        of matching Vservers with the specified language. The
        values with the '*' suffixes are not supported by
        Clustered ONTAP.
        Attributes: optional-for-create, modifiable
        """
        return self._language
    @language.setter
    def language(self, val):
        if val != None:
            self.validate('language', val)
        self._language = val
    
    _quota_policy = None
    @property
    def quota_policy(self):
        """
        Quota policy. When specified as part of vserver-create,
        this field represents the quota policy for the Vserver.
        When specified as part vserver-get-iter call, this will
        return the list of matching Vservers. default: default
        Attributes: optional-for-create, modifiable
        """
        return self._quota_policy
    @quota_policy.setter
    def quota_policy(self, val):
        if val != None:
            self.validate('quota_policy', val)
        self._quota_policy = val
    
    _is_repository_vserver = None
    @property
    def is_repository_vserver(self):
        """
        Specifies if this Vserver is a Vserver with Infinite
        Volume. When part of vserver-get-iter call, this will
        return the list of matching Vservers. Default value is
        false.
        <p>
        Prior to Data ONTAP 8.2.0, Vserver with Infinite Volume
        is called repository Vserver and once a repository
        Vserver is created in a cluster, additional Vservers
        cannot be created. Conversely, a repository Vserver
        cannot be created if non-repository Vservers already
        exist in a cluster.
        Attributes: optional-for-create, non-modifiable
        """
        return self._is_repository_vserver
    @is_repository_vserver.setter
    def is_repository_vserver(self, val):
        if val != None:
            self.validate('is_repository_vserver', val)
        self._is_repository_vserver = val
    
    _qos_policy_group = None
    @property
    def qos_policy_group(self):
        """
        The QoS policy group associated with this volume. This
        optionally specifies which QoS policy group to apply to
        the Vserver. The policy group defines measurable service
        level objectives (SLOs) that apply to the storage objects
        with which the policy group is associated. If you do not
        assign a policy group to a Vserver, the system will not
        monitor and control traffic to it. This parameter is not
        supported on a Vserver with Infinite Volume.
        Attributes: non-creatable, modifiable
        """
        return self._qos_policy_group
    @qos_policy_group.setter
    def qos_policy_group(self, val):
        if val != None:
            self.validate('qos_policy_group', val)
        self._qos_policy_group = val
    
    _vserver_aggr_info_list = None
    @property
    def vserver_aggr_info_list(self):
        """
        List of aggregates assigned to the Vserver with aggregate
        name and available size.
        """
        return self._vserver_aggr_info_list
    @vserver_aggr_info_list.setter
    def vserver_aggr_info_list(self, val):
        if val != None:
            self.validate('vserver_aggr_info_list', val)
        self._vserver_aggr_info_list = val
    
    _ldap_domain = None
    @property
    def ldap_domain(self):
        """
        LDAP client configuration details.
        Attributes: non-creatable, non-modifiable
        """
        return self._ldap_domain
    @ldap_domain.setter
    def ldap_domain(self, val):
        if val != None:
            self.validate('ldap_domain', val)
        self._ldap_domain = val
    
    _vserver_type = None
    @property
    def vserver_type(self):
        """
        Type of the Vserver. Possible values:
        'data', 'admin', and 'node'.
        Attributes: non-creatable, non-modifiable
        """
        return self._vserver_type
    @vserver_type.setter
    def vserver_type(self, val):
        if val != None:
            self.validate('vserver_type', val)
        self._vserver_type = val
    
    @staticmethod
    def get_api_name():
          return "vserver-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'allowed-protocols',
            'max-volumes',
            'name-mapping-switch',
            'antivirus-on-access-policy',
            'uuid',
            'snapshot-policy',
            'root-volume-security-style',
            'state',
            'aggr-list',
            'vserver-name',
            'root-volume-aggregate',
            'root-volume',
            'nis-domain',
            'disallowed-protocols',
            'name-server-switch',
            'language',
            'quota-policy',
            'is-repository-vserver',
            'qos-policy-group',
            'vserver-aggr-info-list',
            'ldap-domain',
            'vserver-type',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'allowed_protocols': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'max_volumes': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name_mapping_switch': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'antivirus_on_access_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'snapshot_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'root_volume_security_style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'aggr_list': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'root_volume_aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'root_volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'nis_domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'disallowed_protocols': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'name_server_switch': { 'class': basestring, 'is_list': True, 'required': 'optional' },
            'language': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'quota_policy': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_repository_vserver': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'qos_policy_group': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver_aggr_info_list': { 'class': VserverAggrInfo, 'is_list': True, 'required': 'optional' },
            'ldap_domain': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
