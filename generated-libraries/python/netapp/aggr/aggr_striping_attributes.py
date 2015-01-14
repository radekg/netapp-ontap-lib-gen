from netapp.netapp_object import NetAppObject

class AggrStripingAttributes(NetAppObject):
    """
    Striping specific information of a striped aggregate
    This information will not be returned for the not-striped aggregate.
    """
    
    _member_count = None
    @property
    def member_count(self):
        """
        Number of members in a striped aggregate.
        """
        return self._member_count
    @member_count.setter
    def member_count(self, val):
        if val != None:
            self.validate('member_count', val)
        self._member_count = val
    
    @staticmethod
    def get_api_name():
          return "aggr-striping-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'member-count',
        ]
    
    def describe_properties(self):
        return {
            'member_count': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
