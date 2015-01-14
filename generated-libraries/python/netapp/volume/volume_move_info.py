from netapp.netapp_object import NetAppObject

class VolumeMoveInfo(NetAppObject):
    """
    Status of the move operation
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
    
    _replication_throughput = None
    @property
    def replication_throughput(self):
        """
        The current replication throughput of the move operation
        in terms of Kb/s, Mb/s or Gb/s.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._replication_throughput
    @replication_throughput.setter
    def replication_throughput(self, val):
        if val != None:
            self.validate('replication_throughput', val)
        self._replication_throughput = val
    
    _cutover_attempted_count = None
    @property
    def cutover_attempted_count(self):
        """
        Number of times cutover has been attempted during the
        move operation. This is a diag only field.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._cutover_attempted_count
    @cutover_attempted_count.setter
    def cutover_attempted_count(self, val):
        if val != None:
            self.validate('cutover_attempted_count', val)
        self._cutover_attempted_count = val
    
    _cutovers_soft_deferred_count = None
    @property
    def cutovers_soft_deferred_count(self):
        """
        Number of times cutover has been soft deferred during the
        move operation due to transient conditions. This is a
        diag only field.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._cutovers_soft_deferred_count
    @cutovers_soft_deferred_count.setter
    def cutovers_soft_deferred_count(self, val):
        if val != None:
            self.validate('cutovers_soft_deferred_count', val)
        self._cutovers_soft_deferred_count = val
    
    _source_aggregate = None
    @property
    def source_aggregate(self):
        """
        The name of the aggregate where the volume being moved
        originally resides or resided.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._source_aggregate
    @source_aggregate.setter
    def source_aggregate(self, val):
        if val != None:
            self.validate('source_aggregate', val)
        self._source_aggregate = val
    
    _last_cutover_trigger_timestamp = None
    @property
    def last_cutover_trigger_timestamp(self):
        """
        The time when move operation initiated cutover.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._last_cutover_trigger_timestamp
    @last_cutover_trigger_timestamp.setter
    def last_cutover_trigger_timestamp(self, val):
        if val != None:
            self.validate('last_cutover_trigger_timestamp', val)
        self._last_cutover_trigger_timestamp = val
    
    _cutover_window = None
    @property
    def cutover_window(self):
        """
        The time window in seconds given as input for the cutover
        phase of volume move.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._cutover_window
    @cutover_window.setter
    def cutover_window(self, val):
        if val != None:
            self.validate('cutover_window', val)
        self._cutover_window = val
    
    _volume_instance_uuid = None
    @property
    def volume_instance_uuid(self):
        """
        This is the instance uuid of the vserver-scoped volume
        being moved.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._volume_instance_uuid
    @volume_instance_uuid.setter
    def volume_instance_uuid(self, val):
        if val != None:
            self.validate('volume_instance_uuid', val)
        self._volume_instance_uuid = val
    
    _actual_duration = None
    @property
    def actual_duration(self):
        """
        The duration in days, hours, minutes and seconds for
        which the volume move was or is in progress.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._actual_duration
    @actual_duration.setter
    def actual_duration(self, val):
        if val != None:
            self.validate('actual_duration', val)
        self._actual_duration = val
    
    _cutover_action = None
    @property
    def cutover_action(self):
        """
        The action to be taken for cutover or during cutover
        failure. Can be one of abort_on_failure,
        defer_on_failure, force or wait. This is the input given
        during the start of volume move.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._cutover_action
    @cutover_action.setter
    def cutover_action(self, val):
        if val != None:
            self.validate('cutover_action', val)
        self._cutover_action = val
    
    _destination_node = None
    @property
    def destination_node(self):
        """
        The name of the node where the destination aggregate is.
        This will be a diagnostic only field.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_node
    @destination_node.setter
    def destination_node(self, val):
        if val != None:
            self.validate('destination_node', val)
        self._destination_node = val
    
    _vserver = None
    @property
    def vserver(self):
        """
        This is the name of the vserver in which the volume being
        moved is part of.
        <p>
        Attributes: key, non-creatable, non-modifiable
        """
        return self._vserver
    @vserver.setter
    def vserver(self, val):
        if val != None:
            self.validate('vserver', val)
        self._vserver = val
    
    _estimated_completion_time = None
    @property
    def estimated_completion_time(self):
        """
        The approximate date and time in the cluster time zone
        when the entire volume move operation is expected to
        complete. The move operation completes when the volume
        instance on the destination aggregate has become the
        master copy and the volume instance on the source
        aggregate has been deleted or is no longer the master
        copy. The format will be in Ontap's Date format. Note
        that this time may keep increasing when the move goes
        into Cutover-Deferrred mode. In those cases where the
        input for cutover-action is wait, during data copy phase,
        estimated time of completion will approximate the time to
        reach cutover point and wait for user intervention.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._estimated_completion_time
    @estimated_completion_time.setter
    def estimated_completion_time(self, val):
        if val != None:
            self.validate('estimated_completion_time', val)
        self._estimated_completion_time = val
    
    _state = None
    @property
    def state(self):
        """
        The state of the volume move at the time of issuing the
        command and the system gathering up the information about
        the move. The states can have the following values: <ul>
        <li>Healthy - Volume move is proceeding as planned,
        with no issues so far
        <li>Done - Volume move has finished successfully.
        <li>Failed - Volume move has failed due to some
        reason, with the reason being available in the Detailed
        Status section.
        <li>Warning - Volume move has encountered a transient
        error condition during its operation, but is continuing
        on since then. The details and phase section has more
        context into the cause of the error.
        <li>Alert - Volume move has encountered a serious
        condition that cannot be rectified by the system alone
        and needs input from the upper layers (admin or tools)
        before proceeding. The volume move will go into
        Cutover-Deferred phase waiting for user intervention in
        case of errors, with volume move trigger-cutover being
        the way the move operation can be restarted.
        </ul>
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._state
    @state.setter
    def state(self, val):
        if val != None:
            self.validate('state', val)
        self._state = val
    
    _actual_completion_timestamp = None
    @property
    def actual_completion_timestamp(self):
        """
        The date and time in cluster timezone when the volume
        move completed (successfully or otherwise). If the volume
        move operation completed successfully, this is the time
        when the volume on the destination aggregate has been
        made master and the original volume on the source
        aggregate has been deleted or is no longer a master
        copy.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._actual_completion_timestamp
    @actual_completion_timestamp.setter
    def actual_completion_timestamp(self, val):
        if val != None:
            self.validate('actual_completion_timestamp', val)
        self._actual_completion_timestamp = val
    
    _percent_complete = None
    @property
    def percent_complete(self):
        """
        The amount of work to move the volume completed thus far
        in terms of percentage.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._percent_complete
    @percent_complete.setter
    def percent_complete(self, val):
        if val != None:
            self.validate('percent_complete', val)
        self._percent_complete = val
    
    _job_id = None
    @property
    def job_id(self):
        """
        The ui job id of the move job. This is available in diag
        mode only.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._job_id
    @job_id.setter
    def job_id(self, val):
        if val != None:
            self.validate('job_id', val)
        self._job_id = val
    
    _execution_progress = None
    @property
    def execution_progress(self):
        """
        The execution progress of the job as reported by the job.
        This is used for debugging purposes only and is only
        available in diag mode.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._execution_progress
    @execution_progress.setter
    def execution_progress(self, val):
        if val != None:
            self.validate('execution_progress', val)
        self._execution_progress = val
    
    _details = None
    @property
    def details(self):
        """
        This field contains details about any warnings, errors
        and state of the move operation. This is a string field.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._details
    @details.setter
    def details(self, val):
        if val != None:
            self.validate('details', val)
        self._details = val
    
    _managing_node = None
    @property
    def managing_node(self):
        """
        The node in the cluster on which the move operation/job
        is or was running. This is usually on the node hosting
        the volume to be moved.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._managing_node
    @managing_node.setter
    def managing_node(self, val):
        if val != None:
            self.validate('managing_node', val)
        self._managing_node = val
    
    _completion_status = None
    @property
    def completion_status(self):
        """
        Once a volume move is complete, the final state of the
        volume move operation. This is available in diag mode
        only.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._completion_status
    @completion_status.setter
    def completion_status(self, val):
        if val != None:
            self.validate('completion_status', val)
        self._completion_status = val
    
    _bytes_remaining = None
    @property
    def bytes_remaining(self):
        """
        The number of bytes remaining to be sent during volume
        move. This is an approximate number and lags the current
        status by a few (3) minutes while the volume move is in
        operation. The bytes-remaining is applicable only for
        ongoing volume moves. It is not applicable to completed
        or failed moves. The data inside the volume is considered
        to be much much larger than data outside the volume. This
        value most of the time will track data inside the volume
        yet to be sent. Note that the bytes-remaining can
        increase over a period of time depending on the rate of
        change of volume by protocols or other consumers of the
        volume.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._bytes_remaining
    @bytes_remaining.setter
    def bytes_remaining(self, val):
        if val != None:
            self.validate('bytes_remaining', val)
        self._bytes_remaining = val
    
    _cutover_attempts = None
    @property
    def cutover_attempts(self):
        """
        The number of attempts to be used by the move operation
        to cutover to the destination volume. This is the input
        by the upper layers. If the number of attempts is
        exhausted, the cutover-action input determines the next
        course of action for the move operation.
        <p>
        Attributes: non-creatable, modifiable
        """
        return self._cutover_attempts
    @cutover_attempts.setter
    def cutover_attempts(self, val):
        if val != None:
            self.validate('cutover_attempts', val)
        self._cutover_attempts = val
    
    _volume = None
    @property
    def volume(self):
        """
        This is the name of the vserver-scoped volume being
        moved.
        <p>
        Attributes: key, non-creatable, non-modifiable
        """
        return self._volume
    @volume.setter
    def volume(self, val):
        if val != None:
            self.validate('volume', val)
        self._volume = val
    
    _cutover_hard_deferred_count = None
    @property
    def cutover_hard_deferred_count(self):
        """
        Number of times cutover has been hard deferred during the
        move operation due to non-transient,
        intervention-necessary conditions. This is a diag only
        field.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._cutover_hard_deferred_count
    @cutover_hard_deferred_count.setter
    def cutover_hard_deferred_count(self, val):
        if val != None:
            self.validate('cutover_hard_deferred_count', val)
        self._cutover_hard_deferred_count = val
    
    _start_timestamp = None
    @property
    def start_timestamp(self):
        """
        The date and time in cluster timezone when the volume
        move started.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._start_timestamp
    @start_timestamp.setter
    def start_timestamp(self, val):
        if val != None:
            self.validate('start_timestamp', val)
        self._start_timestamp = val
    
    _destination_aggregate = None
    @property
    def destination_aggregate(self):
        """
        The name of the aggregate where the volume is being moved
        to.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._destination_aggregate
    @destination_aggregate.setter
    def destination_aggregate(self, val):
        if val != None:
            self.validate('destination_aggregate', val)
        self._destination_aggregate = val
    
    _phase = None
    @property
    def phase(self):
        """
        The phase of the move operation. The move operation can
        have the following phases: <ul>
        <li>Queued - Phase where the move operation is queued
        for execution by the cluster.
        <li>Initializing - Phase where the move operation is
        setting up resources and initializing them for moving the
        volume.
        <li>Replicating - Phase in which move operation is
        doing data copy from source volume to destination
        aggregate.
        <li>Cutover - Phase in which the move operation is
        attempting to switch over volume to the destination
        aggregate and ensuring client i/o and system operations
        go to the volume on the destination aggregate. In this
        phase client i/o and system operations are temporarily
        suspended while a final data copy is taking place from
        the current volume to the destination aggregate.
        <li>cutover_hard_deferred - Phase in which the move
        operation is deferring cutover due to some errors in the
        system during move. The move operation is waiting for
        corrective action from the admin or MEI tools to take
        place. The details field contains the reason for the
        error.
        <li>cutover_soft_deferred - Phase in which the move
        operation is deferring cutover due to some transient
        errors in the system during move. The move operation is
        replicating in the background and waiting for the
        transient error which is causing the soft deferral to
        clear up. If the move operation has not yet started the
        replication in the background, the 'Detailed Status'
        field will contain the reason for soft deferral.
        <li>Completed - The move operation has completed
        successfully and the volume is now on destination
        aggregate.
        <li>cleaning_up - The move operation aborted and is
        in the process of cleaning up. This is a transient
        condition that will eventually lead to Failed phase.
        <li>Failed - The move operation was not successful. The
        details field and the code indicates the reason for the
        failure.
        <li>Failed - The move operation did not complete
        successfully.
        <li>Restarting - The move operation is restarting.
        </ul>
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._phase
    @phase.setter
    def phase(self, val):
        if val != None:
            self.validate('phase', val)
        self._phase = val
    
    _bytes_sent = None
    @property
    def bytes_sent(self):
        """
        The number of bytes sent thus far as part of volume move.
        This is an approximate number and lags the current status
        by a few seconds while the volume move is in operation.
        The bytes-sent is applicable only for ongoing and
        successful volume moves. The bytes-sent counter is
        mononotonically increasing in most cases. It is stored in
        memory. As a result, any reboots or failover of the move
        operation can lead to resetting of this counter to a
        lesser value than reported earlier. The data inside the
        volume is considered to be much much larger than metadata
        of the volume, mostly stored outside the volume. This
        value most of the time will track data inside the volume
        sent at the time of retreiving status.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._bytes_sent
    @bytes_sent.setter
    def bytes_sent(self, val):
        if val != None:
            self.validate('bytes_sent', val)
        self._bytes_sent = val
    
    _internal_state = None
    @property
    def internal_state(self):
        """
        This is the actual internal state of the move job. This
        is used for debugging purposes only and is only available
        in diag mode.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._internal_state
    @internal_state.setter
    def internal_state(self, val):
        if val != None:
            self.validate('internal_state', val)
        self._internal_state = val
    
    _source_node = None
    @property
    def source_node(self):
        """
        The name of the node where the source aggregate is.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._source_node
    @source_node.setter
    def source_node(self, val):
        if val != None:
            self.validate('source_node', val)
        self._source_node = val
    
    _job_uuid = None
    @property
    def job_uuid(self):
        """
        The job uuid of the move job. This is available in diag
        mode only.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._job_uuid
    @job_uuid.setter
    def job_uuid(self, val):
        if val != None:
            self.validate('job_uuid', val)
        self._job_uuid = val
    
    _completion_code = None
    @property
    def completion_code(self):
        """
        The status code of the move operation. The status code
        will be 0 while the job is running or is successful. It
        will be non-zero if it is not successful. The code field
        will be the same as job show's 'status job' field. This
        field will be in diag mode of the UI.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._completion_code
    @completion_code.setter
    def completion_code(self, val):
        if val != None:
            self.validate('completion_code', val)
        self._completion_code = val
    
    _estimated_remaining_duration = None
    @property
    def estimated_remaining_duration(self):
        """
        The approximate amount of time in terms of days, hours,
        minutes and seconds remaining to complete the volume
        move. Note that this duration will not go down to zero
        when the move goes into Cutover-Deferrred mode. The
        duration displayed in the examples is not correct.
        cutover.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._estimated_remaining_duration
    @estimated_remaining_duration.setter
    def estimated_remaining_duration(self, val):
        if val != None:
            self.validate('estimated_remaining_duration', val)
        self._estimated_remaining_duration = val
    
    _prior_issues = None
    @property
    def prior_issues(self):
        """
        The list of issues or transient errors encountered
        causing the move operation to retry the data copy phase
        or the cutover phase. For RR.1, there will be only one
        transient error reported. For later releases, there can
        be many transient errors seperated by newlines reported,
        with the order being earliest at top and latest error at
        the bottom of the list. This is a diag only field.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._prior_issues
    @prior_issues.setter
    def prior_issues(self, val):
        if val != None:
            self.validate('prior_issues', val)
        self._prior_issues = val
    
    _cutover_trigger_timestamp = None
    @property
    def cutover_trigger_timestamp(self):
        """
        The time when move operation last accepted a trigger to
        initiate cutover. This is applicable when the move
        operation is waiting for a cutover to be triggered
        because of a hard cutover deferred state or because the
        cutover-action was wait.
        <p>
        Attributes: non-creatable, non-modifiable
        """
        return self._cutover_trigger_timestamp
    @cutover_trigger_timestamp.setter
    def cutover_trigger_timestamp(self, val):
        if val != None:
            self.validate('cutover_trigger_timestamp', val)
        self._cutover_trigger_timestamp = val
    
    @staticmethod
    def get_api_name():
          return "volume-move-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'replication-throughput',
            'cutover-attempted-count',
            'cutovers-soft-deferred-count',
            'source-aggregate',
            'last-cutover-trigger-timestamp',
            'cutover-window',
            'volume-instance-uuid',
            'actual-duration',
            'cutover-action',
            'destination-node',
            'vserver',
            'estimated-completion-time',
            'state',
            'actual-completion-timestamp',
            'percent-complete',
            'job-id',
            'execution-progress',
            'details',
            'managing-node',
            'completion-status',
            'bytes-remaining',
            'cutover-attempts',
            'volume',
            'cutover-hard-deferred-count',
            'start-timestamp',
            'destination-aggregate',
            'phase',
            'bytes-sent',
            'internal-state',
            'source-node',
            'job-uuid',
            'completion-code',
            'estimated-remaining-duration',
            'prior-issues',
            'cutover-trigger-timestamp',
        ]
    
    def describe_properties(self):
        return {
            'replication_throughput': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cutover_attempted_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cutovers_soft_deferred_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'source_aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'last_cutover_trigger_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cutover_window': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume_instance_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'actual_duration': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cutover_action': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'destination_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'vserver': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'estimated_completion_time': { 'class': int, 'is_list': False, 'required': 'optional' },
            'state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'actual_completion_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'percent_complete': { 'class': int, 'is_list': False, 'required': 'optional' },
            'job_id': { 'class': int, 'is_list': False, 'required': 'optional' },
            'execution_progress': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'details': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'managing_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'completion_status': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'bytes_remaining': { 'class': int, 'is_list': False, 'required': 'optional' },
            'cutover_attempts': { 'class': int, 'is_list': False, 'required': 'optional' },
            'volume': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cutover_hard_deferred_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'start_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
            'destination_aggregate': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'phase': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'bytes_sent': { 'class': int, 'is_list': False, 'required': 'optional' },
            'internal_state': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'source_node': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'job_uuid': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'completion_code': { 'class': int, 'is_list': False, 'required': 'optional' },
            'estimated_remaining_duration': { 'class': int, 'is_list': False, 'required': 'optional' },
            'prior_issues': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'cutover_trigger_timestamp': { 'class': int, 'is_list': False, 'required': 'optional' },
        }
