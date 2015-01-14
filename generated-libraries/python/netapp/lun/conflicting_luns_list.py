from netapp.netapp_object import NetAppObject

class ConflictingLunsList(NetAppObject):
    """
    List of the conflicting luns.
    """
    
    _conflict_lun_path = None
    @property
    def conflict_lun_path(self):
        """
        Path of the lun that has the conflict.
        The format is: /vol/<volume>/<lun> or
        /vol/<volume>/<qtree>/<lun>
        """
        return self._conflict_lun_path
    @conflict_lun_path.setter
    def conflict_lun_path(self, val):
        if val != None:
            self.validate('conflict_lun_path', val)
        self._conflict_lun_path = val
    
    @staticmethod
    def get_api_name():
          return "conflicting-luns-list"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'conflict-lun-path',
        ]
    
    def describe_properties(self):
        return {
            'conflict_lun_path': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
