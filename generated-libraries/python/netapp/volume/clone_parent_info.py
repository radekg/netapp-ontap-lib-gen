from netapp.netapp_object import NetAppObject

class CloneParentInfo(NetAppObject):
    """
    Information describing the parentage of a
    flexible volume clone.
    """
    
    _parent_snapshot_name = None
    @property
    def parent_snapshot_name(self):
        """
        The name of the snapshot in
        'parent-volume-name' serving
        as the parent of this clone.
        """
        return self._parent_snapshot_name
    @parent_snapshot_name.setter
    def parent_snapshot_name(self, val):
        if val != None:
            self.validate('parent_snapshot_name', val)
        self._parent_snapshot_name = val
    
    _parent_volume_name = None
    @property
    def parent_volume_name(self):
        """
        The name of the flexible
        volume serving as the
        parent of this clone.
        """
        return self._parent_volume_name
    @parent_volume_name.setter
    def parent_volume_name(self, val):
        if val != None:
            self.validate('parent_volume_name', val)
        self._parent_volume_name = val
    
    @staticmethod
    def get_api_name():
          return "clone-parent-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'parent-snapshot-name',
            'parent-volume-name',
        ]
    
    def describe_properties(self):
        return {
            'parent_snapshot_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'parent_volume_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
