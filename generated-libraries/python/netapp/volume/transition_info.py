from netapp.netapp_object import NetAppObject

class TransitionInfo(NetAppObject):
    """
    Information relating to any transition jobs
    running or previously run on this volume.
    """
    
    _transitioned = None
    @property
    def transitioned(self):
        """
        Indicates whether the volume has gone through
        a transition operation.
        """
        return self._transitioned
    @transitioned.setter
    def transitioned(self, val):
        if val != None:
            self.validate('transitioned', val)
        self._transitioned = val
    
    _transition_state = None
    @property
    def transition_state(self):
        """
        Indicates the current state of the volume
        transition operation.
        """
        return self._transition_state
    @transition_state.setter
    def transition_state(self, val):
        if val != None:
            self.validate('transition_state', val)
        self._transition_state = val
    
    @staticmethod
    def get_api_name():
          return "transition-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'transitioned',
            'transition-state',
        ]
    
    def describe_properties(self):
        return {
            'transitioned': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'transition_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
