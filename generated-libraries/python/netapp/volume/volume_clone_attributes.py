from netapp.volume.volume_clone_parent_attributes import VolumeCloneParentAttributes
from netapp.netapp_object import NetAppObject

class VolumeCloneAttributes(NetAppObject):
    """
    Information about volume clones.
    """
    
    _clone_child_count = None
    @property
    def clone_child_count(self):
        """
        Number of clones for which this volume is the parent.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._clone_child_count
    @clone_child_count.setter
    def clone_child_count(self, val):
        if val != None:
            self.validate('clone_child_count', val)
        self._clone_child_count = val
    
    _volume_clone_parent_attributes = None
    @property
    def volume_clone_parent_attributes(self):
        """
        This field appears for a flexible volume if it is a clone
        of another flexible volume, describing the clone's
        parentage.
        """
        return self._volume_clone_parent_attributes
    @volume_clone_parent_attributes.setter
    def volume_clone_parent_attributes(self, val):
        if val != None:
            self.validate('volume_clone_parent_attributes', val)
        self._volume_clone_parent_attributes = val
    
    @staticmethod
    def get_api_name():
          return "volume-clone-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'clone-child-count',
            'volume-clone-parent-attributes',
        ]
    
    def describe_properties(self):
        return {
            'clone_child_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume_clone_parent_attributes': { 'class': VolumeCloneParentAttributes, 'is_list': False, 'required': 'optional' },
        }
