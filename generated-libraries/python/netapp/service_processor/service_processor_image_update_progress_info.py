from netapp.netapp_object import NetAppObject

class ServiceProcessorImageUpdateProgressInfo(NetAppObject):
    """
    Service processor image update progress information
    When returned as part of the output, all elements of this typedef
    are reported, unless limited by a set of desired attributes
    specified by the caller.
    <p>
    When used as input to specify desired attributes to return,
    omitting a given element indicates that it shall not be returned
    in the output.  In contrast, by providing an element (even with
    no value) the caller ensures that a value for that element will
    be returned, given that the value can be retrieved.
    <p>
    When used as input to specify queries, any element can be omitted
    in which case the resulting set of objects is not constrained by
    any specific value of that attribute.
    """
    
    _node = None
    @property
    def node(self):
        """
        Node on which the device is located
        Attributes: key, non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _percent_done = None
    @property
    def percent_done(self):
        """
        Current progress of the firmware update percentage
        Attributes: non-creatable, non-modifiable
        """
        return self._percent_done
    @percent_done.setter
    def percent_done(self, val):
        if val != None:
            self.validate('percent_done', val)
        self._percent_done = val
    
    _is_in_progress = None
    @property
    def is_in_progress(self):
        """
        Is a firmware update in progress
        Attributes: non-creatable, non-modifiable
        """
        return self._is_in_progress
    @is_in_progress.setter
    def is_in_progress(self, val):
        if val != None:
            self.validate('is_in_progress', val)
        self._is_in_progress = val
    
    _end_time = None
    @property
    def end_time(self):
        """
        Time when the firmware finished (if complete, else
        empty)
        Attributes: non-creatable, non-modifiable
        """
        return self._end_time
    @end_time.setter
    def end_time(self, val):
        if val != None:
            self.validate('end_time', val)
        self._end_time = val
    
    _start_time = None
    @property
    def start_time(self):
        """
        Time when the firmware update started
        Attributes: non-creatable, non-modifiable
        """
        return self._start_time
    @start_time.setter
    def start_time(self, val):
        if val != None:
            self.validate('start_time', val)
        self._start_time = val
    
    @staticmethod
    def get_api_name():
          return "service-processor-image-update-progress-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'percent-done',
            'is-in-progress',
            'end-time',
            'start-time',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'percent_done': { 'class': int, 'is_list': False, 'required': 'optional' },
            'is_in_progress': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'end_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'start_time': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
