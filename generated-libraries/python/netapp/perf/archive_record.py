from netapp.netapp_object import NetAppObject

class ArchiveRecord(NetAppObject):
    """
    Single instance of sampled data in binary form.
    """
    
    _data = None
    @property
    def data(self):
        """
        Binary instance data.  Average expected length
        of each return string is under 10k bytes, though this
        number will fluctuate depending on the number of
        counters being sampled.  May contain error string if
        we are unable to base64 encode the particular instance.
        """
        return self._data
    @data.setter
    def data(self, val):
        if val != None:
            self.validate('data', val)
        self._data = val
    
    @staticmethod
    def get_api_name():
          return "archive-record"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'data',
        ]
    
    def describe_properties(self):
        return {
            'data': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
