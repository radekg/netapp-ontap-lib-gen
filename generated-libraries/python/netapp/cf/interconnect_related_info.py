from netapp.netapp_object import NetAppObject

class InterconnectRelatedInfo(NetAppObject):
    """
    Interconnect Info
    """
    
    _interconnect_links = None
    @property
    def interconnect_links(self):
        """
        States of the individual interconnect links.
        Attributes: non-creatable, non-modifiable
        """
        return self._interconnect_links
    @interconnect_links.setter
    def interconnect_links(self, val):
        if val != None:
            self.validate('interconnect_links', val)
        self._interconnect_links = val
    
    _interconnect_type = None
    @property
    def interconnect_type(self):
        """
        Type and Vendor of the interconnect.
        Attributes: non-creatable, non-modifiable
        """
        return self._interconnect_type
    @interconnect_type.setter
    def interconnect_type(self, val):
        if val != None:
            self.validate('interconnect_type', val)
        self._interconnect_type = val
    
    _is_interconnect_up = None
    @property
    def is_interconnect_up(self):
        """
        True, if storage failover interconnect is up.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_interconnect_up
    @is_interconnect_up.setter
    def is_interconnect_up(self, val):
        if val != None:
            self.validate('is_interconnect_up', val)
        self._is_interconnect_up = val
    
    @staticmethod
    def get_api_name():
          return "interconnect-related-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'interconnect-links',
            'interconnect-type',
            'is-interconnect-up',
        ]
    
    def describe_properties(self):
        return {
            'interconnect_links': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'interconnect_type': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_interconnect_up': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
