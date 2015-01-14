from netapp.netapp_object import NetAppObject

class ArchiveHeader(NetAppObject):
    """
    Header that describes information about instances of sampled data.
    If the requested timestamp is greater/newer than available in the archives,
    we will return the most recent header.
    """
    
    _data = None
    @property
    def data(self):
        """
        XML formatted header data.  Average expected length
        of each return string is around 512k bytes, though this
        number will fluctuate depending on the number of
        counters being sampled.
        """
        return self._data
    @data.setter
    def data(self, val):
        if val != None:
            self.validate('data', val)
        self._data = val
    
    @staticmethod
    def get_api_name():
          return "archive-header"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'data',
        ]
    
    def describe_properties(self):
        return {
            'data': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
