from netapp.netapp_object import NetAppObject

class VserverAggrInfo(NetAppObject):
    """
    Assigned aggregate name and available size.
    """
    
    _aggr_availsize = None
    @property
    def aggr_availsize(self):
        """
        Assigned aggregate available size.
        Attributes: non-creatable, non-modifiable
        """
        return self._aggr_availsize
    @aggr_availsize.setter
    def aggr_availsize(self, val):
        if val != None:
            self.validate('aggr_availsize', val)
        self._aggr_availsize = val
    
    _aggr_name = None
    @property
    def aggr_name(self):
        """
        Assigned aggregate name.
        Attributes: non-creatable, modifiable
        """
        return self._aggr_name
    @aggr_name.setter
    def aggr_name(self, val):
        if val != None:
            self.validate('aggr_name', val)
        self._aggr_name = val
    
    @staticmethod
    def get_api_name():
          return "vserver-aggr-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'aggr-availsize',
            'aggr-name',
        ]
    
    def describe_properties(self):
        return {
            'aggr_availsize': { 'class': int, 'is_list': False, 'required': 'optional' },
            'aggr_name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
