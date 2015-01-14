from netapp.netapp_object import NetAppObject

class VolumeIdAttributes(NetAppObject):
    """
    Identification information about a volume.
    """
    
    _comment = None
    @property
    def comment(self):
        """
        A description for the volume. Range:[0..1023]
        <p>
        Attributes: optional-for-create, modifiable
        """
        return self._comment
    @comment.setter
    def comment(self, val):
        if val != None:
            self.validate('comment', val)
        self._comment = val
    
    _creation_time = None
    @property
    def creation_time(self):
        """
        Creation time of the volume in seconds since January 1,
        1970.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._creation_time
    @creation_time.setter
    def creation_time(self, val):
        if val != None:
            self.validate('creation_time', val)
        self._creation_time = val
    
    _containing_aggregate_uuid = None
    @property
    def containing_aggregate_uuid(self):
        """
        The 128-bit universally-unique identifier of the
        aggregate in which the given volume resides.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._containing_aggregate_uuid
    @containing_aggregate_uuid.setter
    def containing_aggregate_uuid(self, val):
        if val != None:
            self.validate('containing_aggregate_uuid', val)
        self._containing_aggregate_uuid = val
    
    _name = None
    @property
    def name(self):
        """
        The name of the volume.
        <p>
        Attributes: key, required-for-create, non-modifiable
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _owning_vserver_name = None
    @property
    def owning_vserver_name(self):
        """
        The name of the Vserver that owns this volume.
        <p>
        Attributes: key, non-creatable, non-modifiable
        """
        return self._owning_vserver_name
    @owning_vserver_name.setter
    def owning_vserver_name(self, val):
        if val != None:
            self.validate('owning_vserver_name', val)
        self._owning_vserver_name = val
    
    _type = None
    @property
    def type(self):
        """
        The type of the volume.
        <p>
        Possible values:
        <ul>
        <li> 'rw'  ... read-write volume,
        <li> 'ls'  ... load-sharing volume,
        <li> 'dp'  ... data-protection volume,
        <li> 'dc'  ... data-cache volume (FlexCache),
        <li> 'tmp' ... temporary volume (not valid for
        create)
        </ul>
        <p>
        Default value is 'rw'.
        <p>
        Attributes: optional-for-create, non-modifiable
        """
        return self._type
    @type.setter
    def type(self, val):
        if val != None:
            self.validate('type', val)
        self._type = val
    
    _uuid = None
    @property
    def uuid(self):
        """
        Universal unique identifier (UUID) for this volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._uuid
    @uuid.setter
    def uuid(self, val):
        if val != None:
            self.validate('uuid', val)
        self._uuid = val
    
    _containing_aggregate_name = None
    @property
    def containing_aggregate_name(self):
        """
        The name of the aggregate in which the given flexible
        volume resides.
        <p>
        Attributes: required-for-create, non-modifiable
        """
        return self._containing_aggregate_name
    @containing_aggregate_name.setter
    def containing_aggregate_name(self, val):
        if val != None:
            self.validate('containing_aggregate_name', val)
        self._containing_aggregate_name = val
    
    _name_ordinal = None
    @property
    def name_ordinal(self):
        """
        The ordinal assignment used in relation to this volume's
        name.
        <p>
        Ordinals are used to disambiguate volumes that have the
        same base name on the same controller.  A value of zero
        indicates that the base volume name is unique on a
        controller. A value greater than zero indicates that the
        volume's base name is used by two or more volumes on the
        same controller, and that appending '(n)' to this
        volume's name uniquely identifies it on that controller.
        A value of -1 indicates that the name ordinal has not yet
        been determined.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._name_ordinal
    @name_ordinal.setter
    def name_ordinal(self, val):
        if val != None:
            self.validate('name_ordinal', val)
        self._name_ordinal = val
    
    _instance_uuid = None
    @property
    def instance_uuid(self):
        """
        Universal unique identifier (UUID) for the volume that
        remains unchanged when the volume is moved to a new
        location. This differs from the volume's regular UUID
        which changes after a move. The instance UUID can be used
        to identify a volume even after it is moved. This field
        is valid for flexible volumes only.
        <p>
        UUIDs are formatted as 36-character strings. These
        strings are composed of 32 hexadecimal characters broken
        up into five groupings separated by '-'s. The first
        grouping has 8 hex characters, the second through fourth
        groupings have four hex characters each, and the fifth
        and final grouping has 12 hex characters. Note that a
        leading '0x' is not used.
        <p>
        Here is an example of an actual UUID:
        <p>
        49e370d6-5b5a-11d9-9eb5-000100000529
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._instance_uuid
    @instance_uuid.setter
    def instance_uuid(self, val):
        if val != None:
            self.validate('instance_uuid', val)
        self._instance_uuid = val
    
    _style = None
    @property
    def style(self):
        """
        The style of the volume.
        <p>
        Possible values:
        <ul>
        <li> 'flex'   ... FlexVol,
        <li> 'infinitevol' . Infinite Volume
        </ul>
        <p>
        Default value is 'flex'.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._style
    @style.setter
    def style(self, val):
        if val != None:
            self.validate('style', val)
        self._style = val
    
    _owning_vserver_uuid = None
    @property
    def owning_vserver_uuid(self):
        """
        The 128-bit universally-unique identifier for the vserver
        that currently owns this volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._owning_vserver_uuid
    @owning_vserver_uuid.setter
    def owning_vserver_uuid(self, val):
        if val != None:
            self.validate('owning_vserver_uuid', val)
        self._owning_vserver_uuid = val
    
    _provenance_uuid = None
    @property
    def provenance_uuid(self):
        """
        Universal unique identifier (UUID) for the volume that is
        used to identify the source volume in a mirroring
        relationship. When the mirroring relationship is broken,
        a volume's Instance UUID and Provenance UUID are made
        identical. An unmirrored volume's Provenance UUID is the
        same as its Instance UUID. This field is valid for
        flexible volumes only.
        <p>
        UUIDs are formatted as 36-character strings. These
        strings are composed of 32 hexadecimal characters broken
        up into five groupings separated by '-'s. The first
        grouping has 8 hex characters, the second through fourth
        groupings have four hex characters each, and the fifth
        and final grouping has 12 hex characters. Note that a
        leading '0x' is not used.
        <p>
        Here is an example of an actual UUID:
        <p>
        49e370d6-5b5a-11d9-9eb5-000100000529
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._provenance_uuid
    @provenance_uuid.setter
    def provenance_uuid(self, val):
        if val != None:
            self.validate('provenance_uuid', val)
        self._provenance_uuid = val
    
    _junction_path = None
    @property
    def junction_path(self):
        """
        The Junction Path at which this volume is mounted. This
        field is valid only for a Cluster-Mode volume.
        <p>
        Attributes: optional-for-create, non-modifiable
        """
        return self._junction_path
    @junction_path.setter
    def junction_path(self, val):
        if val != None:
            self.validate('junction_path', val)
        self._junction_path = val
    
    _msid = None
    @property
    def msid(self):
        """
        The volume's Mirror Set ID.
        <p>
        This field is valid only for a Cluster-Mode volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._msid
    @msid.setter
    def msid(self, val):
        if val != None:
            self.validate('msid', val)
        self._msid = val
    
    _dsid = None
    @property
    def dsid(self):
        """
        The volume's Data Set ID.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._dsid
    @dsid.setter
    def dsid(self, val):
        if val != None:
            self.validate('dsid', val)
        self._dsid = val
    
    _fsid = None
    @property
    def fsid(self):
        """
        The File System Identifier (FSID) value that serves as
        one of this volume's internal indicies.
        <p>
        This value serves as an internal index for a volume. All
        volumes on a given controller must have unique FSIDs,
        except for the two special values described below:
        <p>
        A value of 0 indicates that this volume does not
        currently have a legal FSID for some unexpected reason.
        Such volumes are forcibly kept offline until this
        attribute is assigned a legal value.
        <p>
        A value of 1 indicates that this volume has recently
        appeared on its current controller due to having its
        aggregate be copied from a different controller.  All
        volumes in this newly-created aggregate must be assigned
        legal, controller-unique IDs when they are onlined.  That
        will be handled automatically by WAFL upon mount.
        <p>
        If modifiable, this field may be set only when the volume
        is restricted.  It may be set to any value that is not
        currently being used by any other volume on the same
        controller.  If a request to set this value to '0' is
        received, the system will select a new value that is
        currently unused.  Note that setting a volume's FSID
        sometimes has external effects.  In particular, a 7-Mode
        volume's FSID is part of the NFS file handles constructed
        for its files.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._fsid
    @fsid.setter
    def fsid(self, val):
        if val != None:
            self.validate('fsid', val)
        self._fsid = val
    
    _junction_parent_name = None
    @property
    def junction_parent_name(self):
        """
        The name of the parent volume that contains the junction
        inode of this volume.
        <p>
        The junction parent volume must belong to the same
        vserver that owns this volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._junction_parent_name
    @junction_parent_name.setter
    def junction_parent_name(self, val):
        if val != None:
            self.validate('junction_parent_name', val)
        self._junction_parent_name = val
    
    @staticmethod
    def get_api_name():
          return "volume-id-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'comment',
            'creation-time',
            'containing-aggregate-uuid',
            'name',
            'owning-vserver-name',
            'type',
            'uuid',
            'containing-aggregate-name',
            'name-ordinal',
            'instance-uuid',
            'style',
            'owning-vserver-uuid',
            'provenance-uuid',
            'junction-path',
            'msid',
            'dsid',
            'fsid',
            'junction-parent-name',
        ]
    
    def describe_properties(self):
        return {
            'comment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'creation_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'containing_aggregate_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'owning_vserver_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'containing_aggregate_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name_ordinal': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'instance_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'style': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'owning_vserver_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'provenance_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'junction_path': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'msid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'dsid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'fsid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'junction_parent_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
