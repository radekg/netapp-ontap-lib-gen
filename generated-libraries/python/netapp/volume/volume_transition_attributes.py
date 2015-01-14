from netapp.netapp_object import NetAppObject

class VolumeTransitionAttributes(NetAppObject):
    """
    Information about the transition attributes of a volume.
    """
    
    _is_copied_for_transition = None
    @property
    def is_copied_for_transition(self):
        """
        Indicates whether the volume has been copied for copy
        based transition.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_copied_for_transition
    @is_copied_for_transition.setter
    def is_copied_for_transition(self, val):
        if val != None:
            self.validate('is_copied_for_transition', val)
        self._is_copied_for_transition = val
    
    _is_transitioned = None
    @property
    def is_transitioned(self):
        """
        Indicates whether the volume has gone through a
        transition operation at some point in the past.
        Attributes: non-creatable, non-modifiable
        """
        return self._is_transitioned
    @is_transitioned.setter
    def is_transitioned(self, val):
        if val != None:
            self.validate('is_transitioned', val)
        self._is_transitioned = val
    
    _transition_behavior = None
    @property
    def transition_behavior(self):
        """
        For an in progress transition, indicate what the behavior
        is.
        <p>
        Possible values:
        <ul>
        <li> 'none'            ... No transition is in
        progress,
        <li> 'data-move'       ... Transition will follow
        volume move behavior. For example, Lun serial number is
        preserved,
        <li> 'data-protection' ... Transition will follow a
        data protection relationship behavior.
        </ul>
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._transition_behavior
    @transition_behavior.setter
    def transition_behavior(self, val):
        if val != None:
            self.validate('transition_behavior', val)
        self._transition_behavior = val
    
    @staticmethod
    def get_api_name():
          return "volume-transition-attributes"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'is-copied-for-transition',
            'is-transitioned',
            'transition-behavior',
        ]
    
    def describe_properties(self):
        return {
            'is_copied_for_transition': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'is_transitioned': { 'class': bool, 'is_list': False, 'required': 'optional' },
            'transition_behavior': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
