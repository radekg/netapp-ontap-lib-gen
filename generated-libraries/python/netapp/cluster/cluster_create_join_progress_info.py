from netapp.netapp_object import NetAppObject

class ClusterCreateJoinProgressInfo(NetAppObject):
    """
    Information that identifies the state or a create or join
    operation
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
    
    _current_status_message = None
    @property
    def current_status_message(self):
        """
        The current status of the create or join operation being
        performed.
        Attributes: non-creatable, non-modifiable
        """
        return self._current_status_message
    @current_status_message.setter
    def current_status_message(self, val):
        if val != None:
            self.validate('current_status_message', val)
        self._current_status_message = val
    
    _is_complete = None
    @property
    def is_complete(self):
        """
        Is the operation complete? true if the operation is
        complete, false otherwise.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_complete
    @is_complete.setter
    def is_complete(self, val):
        if val != None:
            self.validate('is_complete', val)
        self._is_complete = val
    
    @staticmethod
    def get_api_name():
          return "cluster-create-join-progress-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'current-status-message',
            'is-complete',
        ]
    
    def describe_properties(self):
        return {
            'current_status_message': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'is_complete': { 'class': bool, 'is_list': False, 'required': 'optional' },
        }
