from netapp.netapp_object import NetAppObject

class CloneChildInfo(NetAppObject):
    """
    Information describing each of the clones that
    are children of the current flexible volume.
    """
    
    _clone_child_name = None
    @property
    def clone_child_name(self):
        """
        The name of a clone volume
        whose parent is the given
        flexible volume.
        """
        return self._clone_child_name
    @clone_child_name.setter
    def clone_child_name(self, val):
        if val != None:
            self.validate('clone_child_name', val)
        self._clone_child_name = val
    
    @staticmethod
    def get_api_name():
          return "clone-child-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'clone-child-name',
        ]
    
    def describe_properties(self):
        return {
            'clone_child_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
