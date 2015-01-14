from netapp.netapp_object import NetAppObject

class VolumeSnapshotAutodeleteAttributes(NetAppObject):
    """
    Snapshot autodelete policy settings.
    """
    
    _is_autodelete_enabled = None
    @property
    def is_autodelete_enabled(self):
        """
        This option determines if the snapshot autodelete is
        currently enabled for the volume. The default value is
        false.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._is_autodelete_enabled
    @is_autodelete_enabled.setter
    def is_autodelete_enabled(self, val):
        if val != None:
            self.validate('is_autodelete_enabled', val)
        self._is_autodelete_enabled = val
    
    _prefix = None
    @property
    def prefix(self):
        """
        This option provides the prefix string for the 'prefix'
        field value of the 'defer-delete' option. If the null
        prefix is set, the string '(not specified)' is returned
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._prefix
    @prefix.setter
    def prefix(self, val):
        if val != None:
            self.validate('prefix', val)
        self._prefix = val
    
    _commitment = None
    @property
    def commitment(self):
        """
        Possible values:
        <ul>
        <li> 'try',
        <li> 'disrupt', or
        <li> 'destroy'
        </ul>
        <p>
        This option determines the snapshots that 'snapshot
        autodelete' is allowed to delete to get back space.
        Setting this option to 'try' only permits the snapshots
        which are not locked by data protection utilities (dump,
        mirroring, NDMPcopy) and data-backing functionalities
        (volume and LUN clones) to be deleted. Setting this
        option to 'disrupt' permits all snapshots including the
        snapshots which are locked by data-backing
        functionalities (volume and LUN clones) to be deleted.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._commitment
    @commitment.setter
    def commitment(self, val):
        if val != None:
            self.validate('commitment', val)
        self._commitment = val
    
    _delete_order = None
    @property
    def delete_order(self):
        """
        Possible values:
        <ul>
        <li> 'oldest_first',
        <li> 'newest_first'
        </ul>
        <p>
        This option determines if the oldest or newest snapshot
        is deleted first.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._delete_order
    @delete_order.setter
    def delete_order(self, val):
        if val != None:
            self.validate('delete_order', val)
        self._delete_order = val
    
    _trigger = None
    @property
    def trigger(self):
        """
        Possible values:
        <ul>
        <li> 'volume',
        <li> 'snap_reserve', or
        <li> 'space_reserve'
        </ul>
        <p>
        This option determines the condition in which snapshots
        should be automatically deleted.
        <p>
        If modifiable, setting this option to 'volume' triggers
        snapshot autodelete to run when the volume is near full.
        Setting this option to 'snap_reserve' triggers snapshot
        autodelete to run when the snap reserve of the volume is
        near full. Setting this option to 'space_reserve'
        triggers snapshot autodelete to run when the space
        reserved in the volume is near full.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._trigger
    @trigger.setter
    def trigger(self, val):
        if val != None:
            self.validate('trigger', val)
        self._trigger = val
    
    _destroy_list = None
    @property
    def destroy_list(self):
        """
        Possible values are the combination of:
        <ul>
        <li> 'lun_clone',
        <li> 'vol_clone',
        <li> 'cifs_share',
        <li> 'file_clone',
        <li> 'sfsr', or
        <li> 'none'
        </ul>
        <p>
        This options specifies the list of service that can be
        destroyed if the snapshot is backing that service. This
        option is valid only when the commitment is set to
        'destroy'.
        The option 'lun_clone,file_clone' should be used for
        deleting snapshot backing LUN clone and/or File clone.
        The option 'lun_clone,sfsr' should be used for deleting
        snapshot backing LUN clone and/or SFSR. It must be noted
        that 'lun_clone', 'file_clone' and 'sfsr' individually
        are not valid values. Only pairs of
        'lun_clone,file_clone' and 'lun_clone,sfsr' are
        supported.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._destroy_list
    @destroy_list.setter
    def destroy_list(self, val):
        if val != None:
            self.validate('destroy_list', val)
        self._destroy_list = val
    
    _defer_delete = None
    @property
    def defer_delete(self):
        """
        Possible values:
        <ul>
        <li> 'scheduled',
        <li> 'user_created',
        <li> 'prefix', or
        <li> 'none'
        </ul>
        <p>
        This option determines which kind of snapshots to delete.
        Setting this option value to 'scheduled' will delete the
        snapshots created by the snapshot scheduler last. Setting
        this option value to 'user_created' will delete the
        snapshots not created by the snapshot scheduler last.
        Setting this option value to 'prefix' will delete the
        snapshots matching the prefix string to be deleted last.
        Setting this option value to 'none' will disable the
        above choices.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._defer_delete
    @defer_delete.setter
    def defer_delete(self, val):
        if val != None:
            self.validate('defer_delete', val)
        self._defer_delete = val
    
    _target_free_space = None
    @property
    def target_free_space(self):
        """
        This option determines when snapshot autodelete should
        stop deleting snapshot. Depending on the trigger,
        snapshots are deleted until we reach the target free
        space percentage.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._target_free_space
    @target_free_space.setter
    def target_free_space(self, val):
        if val != None:
            self.validate('target_free_space', val)
        self._target_free_space = val
    
    @staticmethod
    def get_api_name():
          return "volume-snapshot-autodelete-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-autodelete-enabled',
            'prefix',
            'commitment',
            'delete-order',
            'trigger',
            'destroy-list',
            'defer-delete',
            'target-free-space',
        ]
    
    def describe_properties(self):
        return {
            'is_autodelete_enabled': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'prefix': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'commitment': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'delete_order': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'trigger': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destroy_list': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'defer_delete': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'target_free_space': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
