from netapp.netapp_object import NetAppObject

class SnapAutodeleteInfo(NetAppObject):
    """
    Snapshot autodelete policy settings.
    This appears only if the "verbose"
    parameter above is set to "true".
    """
    
    _prefix = None
    @property
    def prefix(self):
        """
        This option provides the prefix string for
        the "prefix" value of the "defer_delete" option.
        """
        return self._prefix
    @prefix.setter
    def prefix(self, val):
        if val != None:
            self.validate('prefix', val)
        self._prefix = val
    
    _state = None
    @property
    def state(self):
        """
        Possible values: "on" or "off".
        This option determines if the snapshot autodelete is
        currently enabled for the volume.
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _commitment = None
    @property
    def commitment(self):
        """
        Possible values: "try", "disrupt", or "destroy".
        This option determines the snapshots which snapshot
        autodelete is allowed to delete to get back space.
        Setting this option to "try" only permits the snapshots
        which are not locked by data protection utilities
        (dump, mirroring, NDMPcopy) and data backing functionalities
        (volume and LUN clones) to be deleted.
        Setting this option to "disrupt" only permits the snapshots
        which are not locked by data backing functionalities
        (volume and LUN clones) to be deleted.
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
        Possible values "oldest_first", "newest_first".
        This option determines if the oldest or newest snapshot
        is deleted first.
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
        Possible values: "volume", "snap_reserve",
        or "space_reserve".
        This option determines the condition in which snapshots
        should be automatically deleted.
        Setting this option to "volume" triggers snapshot autodelete
        to run when the volume is near full.
        Setting this option to "snap_reseve" triggers snapshot
        autodelete to run when the snap reserve of the volume is
        near full.
        Setting this option to "space_reserve" triggers snapshot
        autodelete to run when the space reserved in the volume
        is near full.
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
        Possible values are the combination of "lun_clone",
        "vol_clone", "cifs_share", "file_clone" or
        "none".
        These options specify the list of service that
        can be destroyed if the snapshot is backing that
        service. This option is valid only when the commitment
        is set to destroy.
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
        Possible values "scheduled", "user_created", "prefix",
        or "none".
        This option determines which kind of snapshots to delete in
        the end.
        Setting this option value to "scheduled" will delete
        the snapshots created by the snapshot scheduler last.
        Setting this option value to "user_created" will delete
        the snapshots not created by the snapshot scheduler last.
        Setting this option value to "prefix" will delete
        the snapshots matching the prefix string to be deleted last.
        Setting this option value to "none" will disable the above
        choices.
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
        This option determines when snapshot autodelete should stop
        deleting snapshot. Depending on the trigger, snapshots
        are deleted till we reach the target free space
        percentage.
        Range: [1..100]
        """
        return self._target_free_space
    @target_free_space.setter
    def target_free_space(self, val):
        if val != None:
            self.validate('target_free_space', val)
        self._target_free_space = val
    
    @staticmethod
    def get_api_name():
          return "snap-autodelete-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'prefix',
            'state',
            'commitment',
            'delete-order',
            'trigger',
            'destroy-list',
            'defer-delete',
            'target-free-space',
        ]
    
    def describe_properties(self):
        return {
            'prefix': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'commitment': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'delete_order': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'trigger': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'destroy_list': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'defer_delete': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'target_free_space': { 'class': int, 'is_list': False, 'required': 'required' },
        }
