from netapp.netapp_object import NetAppObject

class AvOnDemandJobInfo(NetAppObject):
    """
    on demand job
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
        This parameter specifies get jobs running on the
        specified node.
        Attributes: non-creatable, non-modifiable
        """
        return self._node
    @node.setter
    def node(self, val):
        if val != None:
            self.validate('node', val)
        self._node = val
    
    _name = None
    @property
    def name(self):
        """
        Command Name
        Attributes: non-creatable, non-modifiable
        """
        return self._name
    @name.setter
    def name(self, val):
        if val != None:
            self.validate('name', val)
        self._name = val
    
    _schedule = None
    @property
    def schedule(self):
        """
        Schedule Name
        Attributes: non-creatable, non-modifiable
        """
        return self._schedule
    @schedule.setter
    def schedule(self, val):
        if val != None:
            self.validate('schedule', val)
        self._schedule = val
    
    _jobid = None
    @property
    def jobid(self):
        """
        Job ID
        Attributes: key, non-creatable, non-modifiable
        """
        return self._jobid
    @jobid.setter
    def jobid(self, val):
        if val != None:
            self.validate('jobid', val)
        self._jobid = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        Vserver Name
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _state = None
    @property
    def state(self):
        """
        State
        Attributes: non-creatable, non-modifiable
        Possible values:
        <ul>
        <li> "initial"        - Initializing,
        <li> "queued"         - Queued,
        <li> "running"        - Running,
        <li> "waiting"        - Waiting For Another Job,
        <li> "pausing"        - Entering Paused State,
        <li> "paused"         - Paused,
        <li> "quitting"       - Entering Quit State,
        <li> "success"        - Succeeded,
        <li> "failure"        - Failed,
        <li> "reschedule"     - Forcing Reschedule,
        <li> "error"          - Internal Error,
        <li> "quit"           - Quit,
        <li> "dead"           - Died,
        <li> "unknown"        - Unknown,
        <li> "restart"        - Forcing Restart,
        <li> "dormant"        - Waiting For External Event
        </ul>
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    @staticmethod
    def get_api_name():
          return "av-on-demand-job-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'node',
            'name',
            'schedule',
            'jobid',
            'vserver',
            'state',
        ]
    
    def describe_properties(self):
        return {
            'node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'name': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'schedule': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'jobid': { 'class': int, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
