from netapp.netapp_object import NetAppObject

class PathnameInfo(NetAppObject):
    """
    Information about a pathname.
    """
    
    _name = None
    @property
    def name(self):
        """
        In Data ONTAP 7-Mode, it must be the name of the path,
        such as &quot;/vol/vol0&quot;.
        In Data ONTAP Cluster-Mode, it must be the path of the
        volume or qtree to be exported such as
        &quot;vol/vol0&quot; or &quot;/vol/vol0/qtree0&quot;.
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    @staticmethod
    def get_api_name():
          return "pathname-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'name',
        ]
    
    def describe_properties(self):
        return {
            'name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
