from netapp.connection import NaConnection
from job_history_get_iter_key_td import JobHistoryGetIterKeyTd # 5 properties
from job_private_resume_iter_key_td import JobPrivateResumeIterKeyTd # 3 properties
from job_schedule_consumer_get_iter_key_td import JobScheduleConsumerGetIterKeyTd # 5 properties
from job_type_by_category_get_iter_key_td import JobTypeByCategoryGetIterKeyTd # 2 properties
from cron_minute import CronMinute # 0 properties
from job_stop_iter_info import JobStopIterInfo # 3 properties
from job_history_vserver_name import JobHistoryVserverName # 0 properties
from job_queue_type import JobQueueType # 0 properties
from job_schedule_cron_destroy_iter_key_td import JobScheduleCronDestroyIterKeyTd # 1 properties
from job_schedule_info import JobScheduleInfo # 3 properties
from job_delete_iter_info import JobDeleteIterInfo # 3 properties
from job_private_completed_get_iter_key_td import JobPrivateCompletedGetIterKeyTd # 3 properties
from job_event_type import JobEventType # 0 properties
from job_resume_iter_key_td import JobResumeIterKeyTd # 2 properties
from job_soft_pause_iter_info import JobSoftPauseIterInfo # 3 properties
from job_state import JobState # 0 properties
from job_private_soft_pause_iter_key_td import JobPrivateSoftPauseIterKeyTd # 3 properties
from job_bad_info import JobBadInfo # 1 properties
from job_soft_pause_iter_key_td import JobSoftPauseIterKeyTd # 2 properties
from job_schedule_cron_get_iter_key_td import JobScheduleCronGetIterKeyTd # 1 properties
from job_init_state_get_iter_key_td import JobInitStateGetIterKeyTd # 2 properties
from job_by_node_get_iter_key_td import JobByNodeGetIterKeyTd # 3 properties
from job_type_get_iter_key_td import JobTypeGetIterKeyTd # 1 properties
from job_schedule_interval_info import JobScheduleIntervalInfo # 6 properties
from job_log_config_modify_iter_key_td import JobLogConfigModifyIterKeyTd # 1 properties
from job_private_pause_iter_key_td import JobPrivatePauseIterKeyTd # 3 properties
from job_queue_get_iter_key_td import JobQueueGetIterKeyTd # 2 properties
from job_log_config_info import JobLogConfigInfo # 2 properties
from job_pause_iter_info import JobPauseIterInfo # 3 properties
from cron_day_of_week import CronDayOfWeek # 0 properties
from job_schedule_interval_destroy_iter_key_td import JobScheduleIntervalDestroyIterKeyTd # 1 properties
from job_init_state_info import JobInitStateInfo # 13 properties
from job_private_delete_iter_info import JobPrivateDeleteIterInfo # 3 properties
from job_unclaim_iter_key_td import JobUnclaimIterKeyTd # 2 properties
from job_get_iter_key_td import JobGetIterKeyTd # 2 properties
from job_schedule_cron_destroy_iter_info import JobScheduleCronDestroyIterInfo # 3 properties
from cron_day_of_month import CronDayOfMonth # 0 properties
from job_affinity import JobAffinity # 0 properties
from job_schedule_get_iter_key_td import JobScheduleGetIterKeyTd # 1 properties
from job_type_info import JobTypeInfo # 16 properties
from job_history_info import JobHistoryInfo # 17 properties
from job_schedule_cron_info import JobScheduleCronInfo # 7 properties
from job_private_pause_iter_info import JobPrivatePauseIterInfo # 3 properties
from job_completed_get_iter_key_td import JobCompletedGetIterKeyTd # 2 properties
from job_log_config_get_iter_key_td import JobLogConfigGetIterKeyTd # 1 properties
from job_private_get_iter_key_td import JobPrivateGetIterKeyTd # 3 properties
from schedule_type import ScheduleType # 0 properties
from job_private_resume_iter_info import JobPrivateResumeIterInfo # 3 properties
from job_schedule_consumer_info import JobScheduleConsumerInfo # 5 properties
from cron_month import CronMonth # 0 properties
from job_pause_iter_key_td import JobPauseIterKeyTd # 2 properties
from job_info import JobInfo # 22 properties
from job_expunge_iter_key_td import JobExpungeIterKeyTd # 2 properties
from job_private_stop_iter_info import JobPrivateStopIterInfo # 3 properties
from job_log_level import JobLogLevel # 0 properties
from job_expunge_iter_info import JobExpungeIterInfo # 3 properties
from job_delete_iter_key_td import JobDeleteIterKeyTd # 2 properties
from job_private_soft_pause_iter_info import JobPrivateSoftPauseIterInfo # 3 properties
from job_stop_iter_key_td import JobStopIterKeyTd # 2 properties
from process_name import ProcessName # 0 properties
from cron_hour import CronHour # 0 properties
from job_private_stop_iter_key_td import JobPrivateStopIterKeyTd # 3 properties
from job_schedule_interval_destroy_iter_info import JobScheduleIntervalDestroyIterInfo # 3 properties
from job_private_delete_iter_key_td import JobPrivateDeleteIterKeyTd # 3 properties
from job_bad_get_iter_key_td import JobBadGetIterKeyTd # 1 properties
from job_schedule_interval_get_iter_key_td import JobScheduleIntervalGetIterKeyTd # 1 properties
from job_log_config_modify_iter_info import JobLogConfigModifyIterInfo # 3 properties
from job_priority import JobPriority # 0 properties
from job_resume_iter_info import JobResumeIterInfo # 3 properties
from job_unclaim_iter_info import JobUnclaimIterInfo # 3 properties
from job_queue_info import JobQueueInfo # 4 properties

class JobConnection(NaConnection):
    
    def job_private_pause_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Pause a collection of private jobs.
        
        :param query: If operating on a specific private job, this input element must
                specify all keys.
                If operating on private job objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching private job
                even when the operation on a previous matching private job fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of private job objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of private job
                objects (just keys) that were successfully operated on.
                If set to false, the list of private job objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple private job objects
                match a given query.
                If set to true, the API will continue with the next matching
                private job even when the operation fails for the private job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of private job
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of private job objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "job-private-pause-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobPrivatePauseIterInfo, True ],
            'failure-list': [ JobPrivatePauseIterInfo, True ],
        } )
    
    def job_stop(self, job_id):
        """
        Stop a job. A job must be of a type that has
        job-type-is-quittable set to true before it may be stopped.
        job-stop attempts to stop a job that's currently running. If the
        job allows itself to stop it completes its current run. If the
        job has a recurring schedule it will transition to the Queued
        state; otherwise it will transition into either the Success or
        Failure state.
        
        :param job_id: The job id.
        """
        return self.request( "job-stop", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_resume(self, job_id):
        """
        Resume a job from the paused state.
        
        :param job_id: The job id.
        """
        return self.request( "job-resume", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_schedule_interval_get(self, job_schedule_name, desired_attributes=None):
        """
        Get a single interval job schedule entry.
        
        :param job_schedule_name: The name of the job schedule.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-schedule-interval-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobScheduleIntervalInfo, 'None' ], False ],
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ JobScheduleIntervalInfo, False ],
        } )
    
    def job_soft_pause_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Soft pause a collection of jobs.
        
        :param query: If operating on a specific job, this input element must specify
                all keys.
                If operating on job objects based on query, this input element
                must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching job even
                when the operation on a previous matching job fails, and do so
                until the total number of objects failed to be operated on
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job objects to be operated in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of job objects (just
                keys) that were successfully operated on.
                If set to false, the list of job objects operated on will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job objects match a
                given query.
                If set to true, the API will continue with the next matching job
                even when the operation fails for the job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job objects (just
                keys) that were not operated on due to some error.
                If set to false, the list of job objects not operated on will not
                be returned.
                Default: true
        """
        return self.request( "job-soft-pause-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobSoftPauseIterInfo, True ],
            'failure-list': [ JobSoftPauseIterInfo, True ],
        } )
    
    def job_log_config_modify_iter(self, query, attributes, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Modify multiple job-manager-logging configuration records.
        
        :param query: If modifying a specific job-log-config, this input element must
                specify all keys.
                If modifying job-log-config objects based on query, this input
                element must specify a query.
        
        :param attributes: Specify at least one modifiable element.
                Do not specify any other element.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed modify operations before the server gives up and returns.
                If set, the API will continue modifying the next matching
                job-log-config even when the modification of a previous matching
                job-log-config fails, and do so until the total number of objects
                failed to be modified reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed modify operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of objects to be modified in this call.
                Default: 100
        
        :param return_success_list: If set to true, the API will return the list of job-log-config
                objects (just keys) that were successfully updated.
                If set to false, the list of job-log-config objects modified will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job-log-config objects
                match a given query.
                If set to true, the API will continue modifying the next matching
                job-log-config even when modification of a previous
                job-log-config fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job-log-config
                objects (just keys) that were not modified due to some error.
                If set to false, the list of job-log-config objects not modified
                will not be returned.
                Default: true
        """
        return self.request( "job-log-config-modify-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobLogConfigInfo, 'None' ], False ],
            'attributes': [ attributes, 'attributes', [ JobLogConfigInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobLogConfigModifyIterInfo, True ],
            'failure-list': [ JobLogConfigModifyIterInfo, True ],
        } )
    
    def job_private_watch_progress(self, job_node, job_id, interval=None):
        """
        auto generated : Watch the progress of a job
        
        :param job_node: Node
        
        :param job_id: Job ID
        
        :param interval: Refresh Interval (seconds)
        """
        return self.request( "job-private-watch-progress", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
            'interval': [ interval, 'interval', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_private_delete(self, job_node, job_id):
        """
        Delete a private job.
        
        :param job_node: Node
        
        :param job_id: Job ID
        """
        return self.request( "job-private-delete", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_private_get(self, job_node, job_id, desired_attributes=None):
        """
        Get a single private job entry.
        
        :param job_node: Node
        
        :param job_id: Job ID
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-private-get", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes': [ JobInfo, False ],
        } )
    
    def job_queue_get(self, job_queue, job_uuid, desired_attributes=None):
        """
        Get a single job queue entry.
        
        :param job_queue: Job queue name.
                Possible values:
                <ul>
                <li> "queued"              ,
                <li> "runnable"            ,
                <li> "cluster_queued"      ,
                <li> "cluster_runnable"    ,
                <li> "pending"             ,
                <li> "paused"              ,
                <li> "cleanup"             ,
                <li> "startup"             ,
                <li> "shutdown"
                </ul>
        
        :param job_uuid: Job's universally unique identifier (UUID).
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-queue-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobQueueInfo, 'None' ], False ],
            'job_queue': [ job_queue, 'job-queue', [ basestring, 'job-queue-type' ], False ],
            'job_uuid': [ job_uuid, 'job-uuid', [ basestring, 'uuid' ], False ],
        }, {
            'attributes': [ JobQueueInfo, False ],
        } )
    
    def job_private_completed_get(self, job_node, job_id, desired_attributes=None):
        """
        Get a single completed, private job entry.  This is just a
        performance optimization for job-private-get.
        
        :param job_node: Node
        
        :param job_id: Job ID
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-private-completed-get", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes': [ JobInfo, False ],
        } )
    
    def job_type_by_category_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job types.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-type-by-category object.
                All job-type-by-category objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-type-by-category-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobTypeInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobTypeInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobTypeInfo, True ],
        } )
    
    def job_schedule_cron_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete multiple cron job schedule entries. The entries must not
        be in use.
        
        :param query: If deleting a specific job-schedule-cron, this input element must
                specify all keys.
                If deleting multiple job-schedule-cron objects based on query,
                this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                job-schedule-cron even when the deletion of a previous matching
                job-schedule-cron fails, and do so until the total number of
                objects failed to be deleted reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job-schedule-cron objects to delete in this
                call.
                Default: 100
        
        :param return_success_list: If set to true, the API will return the list of job-schedule-cron
                objects (just keys) that were successfully deleted.
                If set to false, the list of job-schedule-cron objects deleted
                will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job-schedule-cron
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                job-schedule-cron even when the deletion of a previous
                job-schedule-cron fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job-schedule-cron
                objects (just keys) that were not deleted due to some error.
                If set to false, the list of job-schedule-cron objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "job-schedule-cron-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobScheduleCronInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobScheduleCronDestroyIterInfo, True ],
            'failure-list': [ JobScheduleCronDestroyIterInfo, True ],
        } )
    
    def job_unclaim(self, job_id):
        """
        Detach a cluster job from the owning node. The job may
        subsequently be reclaimed.
        
        :param job_id: The job id.
        """
        return self.request( "job-unclaim", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_private_soft_pause_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Soft pause a collection of private jobs.
        
        :param query: If operating on a specific private job, this input element must
                specify all keys.
                If operating on private job objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching private job
                even when the operation on a previous matching private job fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of private job objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of private job
                objects (just keys) that were successfully operated on.
                If set to false, the list of private job objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple private job objects
                match a given query.
                If set to true, the API will continue with the next matching
                private job even when the operation fails for the private job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of private job
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of private job objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "job-private-soft-pause-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobPrivateSoftPauseIterInfo, True ],
            'failure-list': [ JobPrivateSoftPauseIterInfo, True ],
        } )
    
    def job_schedule_cron_modify(self, job_schedule_name, job_schedule_cron_day=None, job_schedule_cron_minute=None, job_schedule_cron_month=None, job_schedule_cron_hour=None, job_schedule_cron_day_of_week=None):
        """
        Modify an existing cron job schedule entry.
        
        :param job_schedule_name: The name of the job schedule.
        
        :param job_schedule_cron_day: The day(s) of the month when the job should be run.
        
        :param job_schedule_cron_minute: The minute(s) of each hour when the job should be run.
        
        :param job_schedule_cron_month: The month(s) when the job should be run.
        
        :param job_schedule_cron_hour: The hour(s) of the day when the job should be run.
        
        :param job_schedule_cron_day_of_week: The day(s) in the week when the job should be run.
        """
        return self.request( "job-schedule-cron-modify", {
            'job_schedule_cron_day': [ job_schedule_cron_day, 'job-schedule-cron-day', [ int, 'cron-day-of-month' ], True ],
            'job_schedule_cron_minute': [ job_schedule_cron_minute, 'job-schedule-cron-minute', [ int, 'cron-minute' ], True ],
            'job_schedule_cron_month': [ job_schedule_cron_month, 'job-schedule-cron-month', [ int, 'cron-month' ], True ],
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
            'job_schedule_cron_hour': [ job_schedule_cron_hour, 'job-schedule-cron-hour', [ int, 'cron-hour' ], True ],
            'job_schedule_cron_day_of_week': [ job_schedule_cron_day_of_week, 'job-schedule-cron-day-of-week', [ int, 'cron-day-of-week' ], True ],
        }, {
        } )
    
    def job_completed_get(self, job_id, desired_attributes=None):
        """
        Get a single completed job entry.  This is just a performance
        optimization for job-get.
        
        :param job_id: Job ID
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-completed-get", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes': [ JobInfo, False ],
        } )
    
    def job_bad_erase(self, job_uuid):
        """
        auto generated : Erase a bad job
        
        :param job_uuid: Job's universally unique identifier (UUID).
        """
        return self.request( "job-bad-erase", {
            'job_uuid': [ job_uuid, 'job-uuid', [ basestring, 'uuid' ], False ],
        }, {
        } )
    
    def job_schedule_cron_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple cron job schedule entries.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-schedule-cron object.
                All job-schedule-cron objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-schedule-cron-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobScheduleCronInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobScheduleCronInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobScheduleCronInfo, True ],
        } )
    
    def job_delete(self, job_id):
        """
        Delete a job. A job must be of a type that has
        job-type-is-deletable set to true before it may be deleted. It
        may be deleted from any state. No job history will be written for
        the job.
        
        :param job_id: The job id.
        """
        return self.request( "job-delete", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_log_config_get(self, job_log_module, desired_attributes=None):
        """
        Get a single job-manager-logging configuration entry.
        
        :param job_log_module: The module being logged.  These are pre-defined in the system
                binaries. To get an up-to-date list call job-log-config-get-iter
                without a query.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-log-config-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobLogConfigInfo, 'None' ], False ],
            'job_log_module': [ job_log_module, 'job-log-module', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ JobLogConfigInfo, False ],
        } )
    
    def job_schedule_interval_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple interval job schedule entries.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-schedule-interval object.
                All job-schedule-interval objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-schedule-interval-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobScheduleIntervalInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobScheduleIntervalInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobScheduleIntervalInfo, True ],
        } )
    
    def job_expunge_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Force a removal of a collection of jobs.
        
        :param query: If operating on a specific job, this input element must specify
                all keys.
                If operating on job objects based on query, this input element
                must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching job even
                when the operation on a previous matching job fails, and do so
                until the total number of objects failed to be operated on
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job objects to be operated in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of job objects (just
                keys) that were successfully operated on.
                If set to false, the list of job objects operated on will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job objects match a
                given query.
                If set to true, the API will continue with the next matching job
                even when the operation fails for the job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job objects (just
                keys) that were not operated on due to some error.
                If set to false, the list of job objects not operated on will not
                be returned.
                Default: true
        """
        return self.request( "job-expunge-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobExpungeIterInfo, True ],
            'failure-list': [ JobExpungeIterInfo, True ],
        } )
    
    def job_expunge(self, job_id):
        """
        Force a removal of a job. Expunge removes entries for the job
        from RDB. No attempt is made to notify the job if it is running.
        
        :param job_id: The job id.
        """
        return self.request( "job-expunge", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_kick(self, job_uuid):
        """
        Immediately schedule a pending job.
        
        :param job_uuid: Job Id.
        """
        return self.request( "job-kick", {
            'job_uuid': [ job_uuid, 'job-uuid', [ basestring, 'uuid' ], False ],
        }, {
        } )
    
    def job_by_node_get(self, job_node, job_id, desired_attributes=None):
        """
        Get a single job entry.  This is just a performance optimization
        for job-get that only searches for the job among the ones
        currently owned by the given node.
        
        :param job_node: The name of the node where the job is run.
        
        :param job_id: The job id.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-by-node-get", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes': [ JobInfo, False ],
        } )
    
    def job_schedule_interval_modify(self, job_schedule_name, job_schedule_interval_hours=None, job_schedule_interval_days=None, job_schedule_interval_seconds=None, job_schedule_interval_minutes=None):
        """
        Modify an existing interval job schedule entry.
        
        :param job_schedule_name: The name of the job schedule.
        
        :param job_schedule_interval_hours: The number of hours between jobs.
        
        :param job_schedule_interval_days: The number of days between jobs.
        
        :param job_schedule_interval_seconds: The number of seconds between jobs.
        
        :param job_schedule_interval_minutes: The number of minutes between jobs.
        """
        return self.request( "job-schedule-interval-modify", {
            'job_schedule_interval_hours': [ job_schedule_interval_hours, 'job-schedule-interval-hours', [ int, 'None' ], False ],
            'job_schedule_interval_days': [ job_schedule_interval_days, 'job-schedule-interval-days', [ int, 'None' ], False ],
            'job_schedule_interval_seconds': [ job_schedule_interval_seconds, 'job-schedule-interval-seconds', [ int, 'None' ], False ],
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
            'job_schedule_interval_minutes': [ job_schedule_interval_minutes, 'job-schedule-interval-minutes', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_schedule_cron_destroy(self, job_schedule_name):
        """
        Delete a single cron job schedule entry. The entry must not be in
        use.
        
        :param job_schedule_name: The name of the job schedule.
        """
        return self.request( "job-schedule-cron-destroy", {
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def job_completed_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple completed job records.  This is just a performance
        optimization for job-get-iter.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the job
                completed object.
                All job completed objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-completed-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobInfo, True ],
        } )
    
    def job_pause(self, job_id):
        """
        Pause a job. A job must be of a type that has
        job-type-is-pausible set to true before it may be paused. Once
        notified of a pause request, a job should stop performing work
        until it is subsequently resumed.
        
        :param job_id: The job id.
        """
        return self.request( "job-pause", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_private_soft_pause(self, job_node, job_id):
        """
        Soft pause a private job.
        
        :param job_node: Node
        
        :param job_id: Job ID
        """
        return self.request( "job-private-soft-pause", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_private_resume_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Resume a collection of jobs.
        
        :param query: If operating on a specific private job, this input element must
                specify all keys.
                If operating on private job objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching private job
                even when the operation on a previous matching private job fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of private job objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of private job
                objects (just keys) that were successfully operated on.
                If set to false, the list of private job objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple private job objects
                match a given query.
                If set to true, the API will continue with the next matching
                private job even when the operation fails for the private job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of private job
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of private job objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "job-private-resume-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobPrivateResumeIterInfo, True ],
            'failure-list': [ JobPrivateResumeIterInfo, True ],
        } )
    
    def job_by_node_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job records organized by node. This is just a
        performance optimization for job-get-iter that only searches for
        the job among the ones currently owned by the given node.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-by-node entry object.
                All job-by-node entry objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-by-node-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobInfo, True ],
        } )
    
    def job_type_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job types.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-type object.
                All job-type objects matching this query up to 'max-records' will
                be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-type-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobTypeInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobTypeInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobTypeInfo, True ],
        } )
    
    def job_private_completed_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple completed, private job records.  This is just a
        performance optimization for job-private-get-iter.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                private job completion entry object.
                All private job completion entry objects matching this query up
                to 'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-private-completed-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobInfo, True ],
        } )
    
    def job_schedule_interval_destroy(self, job_schedule_name):
        """
        Delete a single interval job schedule entry. The entry must not
        be in use.
        
        :param job_schedule_name: The name of the job schedule.
        """
        return self.request( "job-schedule-interval-destroy", {
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def job_schedule_cron_create(self, job_schedule_cron_minute, job_schedule_name, job_schedule_cron_day=None, job_schedule_cron_month=None, return_record=None, job_schedule_cron_hour=None, job_schedule_cron_day_of_week=None):
        """
        Create a new cron job schedule entry.
        
        :param job_schedule_cron_minute: The minute(s) of each hour when the job should be run.
        
        :param job_schedule_name: The name of the job schedule.
        
        :param job_schedule_cron_day: The day(s) of the month when the job should be run.
        
        :param job_schedule_cron_month: The month(s) when the job should be run.
        
        :param return_record: If set to true, returns the job-schedule-cron on successful
                creation.
                Default: false
        
        :param job_schedule_cron_hour: The hour(s) of the day when the job should be run.
        
        :param job_schedule_cron_day_of_week: The day(s) in the week when the job should be run.
        """
        return self.request( "job-schedule-cron-create", {
            'job_schedule_cron_day': [ job_schedule_cron_day, 'job-schedule-cron-day', [ int, 'cron-day-of-month' ], True ],
            'job_schedule_cron_minute': [ job_schedule_cron_minute, 'job-schedule-cron-minute', [ int, 'cron-minute' ], True ],
            'job_schedule_cron_month': [ job_schedule_cron_month, 'job-schedule-cron-month', [ int, 'cron-month' ], True ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
            'job_schedule_cron_hour': [ job_schedule_cron_hour, 'job-schedule-cron-hour', [ int, 'cron-hour' ], True ],
            'job_schedule_cron_day_of_week': [ job_schedule_cron_day_of_week, 'job-schedule-cron-day-of-week', [ int, 'cron-day-of-week' ], True ],
        }, {
            'result': [ JobScheduleCronInfo, False ],
        } )
    
    def job_pause_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Pause a collection of jobs.
        
        :param query: If operating on a specific job, this input element must specify
                all keys.
                If operating on job objects based on query, this input element
                must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching job even
                when the operation on a previous matching job fails, and do so
                until the total number of objects failed to be operated on
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job objects to be operated in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of job objects (just
                keys) that were successfully operated on.
                If set to false, the list of job objects operated on will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job objects match a
                given query.
                If set to true, the API will continue with the next matching job
                even when the operation fails for the job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job objects (just
                keys) that were not operated on due to some error.
                If set to false, the list of job objects not operated on will not
                be returned.
                Default: true
        """
        return self.request( "job-pause-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobPauseIterInfo, True ],
            'failure-list': [ JobPauseIterInfo, True ],
        } )
    
    def job_private_stop_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Stop a collection of jobs.
        
        :param query: If operating on a specific private job, this input element must
                specify all keys.
                If operating on private job objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching private job
                even when the operation on a previous matching private job fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of private job objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of private job
                objects (just keys) that were successfully operated on.
                If set to false, the list of private job objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple private job objects
                match a given query.
                If set to true, the API will continue with the next matching
                private job even when the operation fails for the private job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of private job
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of private job objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "job-private-stop-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobPrivateStopIterInfo, True ],
            'failure-list': [ JobPrivateStopIterInfo, True ],
        } )
    
    def job_resume_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Resume a collection of jobs.
        
        :param query: If operating on a specific job, this input element must specify
                all keys.
                If operating on job objects based on query, this input element
                must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching job even
                when the operation on a previous matching job fails, and do so
                until the total number of objects failed to be operated on
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job objects to be operated in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of job objects (just
                keys) that were successfully operated on.
                If set to false, the list of job objects operated on will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job objects match a
                given query.
                If set to true, the API will continue with the next matching job
                even when the operation fails for the job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job objects (just
                keys) that were not operated on due to some error.
                If set to false, the list of job objects not operated on will not
                be returned.
                Default: true
        """
        return self.request( "job-resume-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobResumeIterInfo, True ],
            'failure-list': [ JobResumeIterInfo, True ],
        } )
    
    def job_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job records.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the job
                object.
                All job objects matching this query up to 'max-records' will be
                returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobInfo, True ],
        } )
    
    def job_private_resume(self, job_node, job_id):
        """
        Resume a job.
        
        :param job_node: Node
        
        :param job_id: Job ID
        """
        return self.request( "job-private-resume", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_private_pause(self, job_node, job_id):
        """
        Pause a private job.
        
        :param job_node: Node
        
        :param job_id: Job ID
        """
        return self.request( "job-private-pause", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_schedule_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job schedule entries.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-schedule object.
                All job-schedule objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-schedule-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobScheduleInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobScheduleInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobScheduleInfo, True ],
        } )
    
    def job_schedule_get(self, job_schedule_name, desired_attributes=None):
        """
        Get a single job schedule entry.
        
        :param job_schedule_name: The name of the job schedule.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-schedule-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobScheduleInfo, 'None' ], False ],
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ JobScheduleInfo, False ],
        } )
    
    def job_type_get(self, job_type, desired_attributes=None):
        """
        Get a single job type.
        
        :param job_type: Job type. For example, 'AggrCreate', 'VOL_CREATE'.  These are
                pre-defined in the system binaries. You can get an up-to-date
                list call job-type-get-iter without a query.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-type-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobTypeInfo, 'None' ], False ],
            'job_type': [ job_type, 'job-type', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ JobTypeInfo, False ],
        } )
    
    def job_schedule_consumer_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job schedule entries.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-schedule-consumer object.
                All job-schedule-consumer objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-schedule-consumer-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobScheduleConsumerInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobScheduleConsumerInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobScheduleConsumerInfo, True ],
        } )
    
    def job_get(self, job_id, desired_attributes=None):
        """
        Get a single job entry.
        
        :param job_id: The job id.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-get", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes': [ JobInfo, False ],
        } )
    
    def job_schedule_interval_destroy_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete multiple interval job schedule entries. The entries must
        not be in use.
        
        :param query: If deleting a specific job-schedule-interval, this input element
                must specify all keys.
                If deleting multiple job-schedule-interval objects based on
                query, this input element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed deletions before the server gives up and returns.
                If set, the API will continue deleting the next matching
                job-schedule-interval even when the deletion of a previous
                matching job-schedule-interval fails, and do so until the total
                number of objects failed to be deleted reaches the maximum
                specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed deletions.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job-schedule-interval objects to delete in
                this call.
                Default: 100
        
        :param return_success_list: If set to true, the API will return the list of
                job-schedule-interval objects (just keys) that were successfully
                deleted.
                If set to false, the list of job-schedule-interval objects
                deleted will not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job-schedule-interval
                objects match a given query.
                If set to true, the API will continue deleting the next matching
                job-schedule-interval even when the deletion of a previous
                job-schedule-interval fails.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of
                job-schedule-interval objects (just keys) that were not deleted
                due to some error.
                If set to false, the list of job-schedule-interval objects not
                deleted will not be returned.
                Default: true
        """
        return self.request( "job-schedule-interval-destroy-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobScheduleIntervalInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobScheduleIntervalDestroyIterInfo, True ],
            'failure-list': [ JobScheduleIntervalDestroyIterInfo, True ],
        } )
    
    def job_init_state_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple Job Manager initialization state records.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-init-state object.
                All job-init-state objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-init-state-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobInitStateInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInitStateInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobInitStateInfo, True ],
        } )
    
    def job_init_state_get(self, job_mgr_node, job_mgr_process, desired_attributes=None):
        """
        Get the Job Manager initialization state entry.
        
        :param job_mgr_node: The name of the node hosting a job manager instance.
        
        :param job_mgr_process: Process using Job Manager
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-init-state-get", {
            'job_mgr_node': [ job_mgr_node, 'job-mgr-node', [ basestring, 'node-name' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInitStateInfo, 'None' ], False ],
            'job_mgr_process': [ job_mgr_process, 'job-mgr-process', [ basestring, 'process-name' ], False ],
        }, {
            'attributes': [ JobInitStateInfo, False ],
        } )
    
    def job_bad_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get the ids of jobs marked as bad by the Job Manager because they
        are invalid: they may not be deserializable, have an unknown type
        or an unknown schedule or may otherwise be invalid.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-bad object.
                All job-bad objects matching this query up to 'max-records' will
                be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-bad-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobBadInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobBadInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobBadInfo, True ],
        } )
    
    def job_history_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job history records.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the job
                history event object.
                All job history event objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-history-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobHistoryInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobHistoryInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobHistoryInfo, True ],
        } )
    
    def job_soft_pause(self, job_id):
        """
        Soft pause a job. Indicates to the job that a soft pause has been
        initiated. It is up to the job to do what it needs to do for a
        soft pause. As a result of this command the job may request to be
        moved into the runnnable queue to perform further processing of
        the soft pause.
        
        :param job_id: The job id.
        """
        return self.request( "job-soft-pause", {
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def job_type_by_category_get(self, job_category, job_type, desired_attributes=None):
        """
        Get a single job type.
        
        :param job_category: Job category. For example, 'Aggregate', 'VOPL'.
        
        :param job_type: Job type. For example, 'AggrCreate', 'VOL_CREATE'.  These are
                pre-defined in the system binaries. You can get an up-to-date
                list call job-type-get-iter without a query.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-type-by-category-get", {
            'job_category': [ job_category, 'job-category', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobTypeInfo, 'None' ], False ],
            'job_type': [ job_type, 'job-type', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ JobTypeInfo, False ],
        } )
    
    def job_delete_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete a collection of jobs.
        
        :param query: If operating on a specific job, this input element must specify
                all keys.
                If operating on job objects based on query, this input element
                must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching job even
                when the operation on a previous matching job fails, and do so
                until the total number of objects failed to be operated on
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job objects to be operated in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of job objects (just
                keys) that were successfully operated on.
                If set to false, the list of job objects operated on will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job objects match a
                given query.
                If set to true, the API will continue with the next matching job
                even when the operation fails for the job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job objects (just
                keys) that were not operated on due to some error.
                If set to false, the list of job objects not operated on will not
                be returned.
                Default: true
        """
        return self.request( "job-delete-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobDeleteIterInfo, True ],
            'failure-list': [ JobDeleteIterInfo, True ],
        } )
    
    def job_log_config_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job-manager-logging configuration records.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-log-config object.
                All job-log-config objects matching this query up to
                'max-records' will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-log-config-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobLogConfigInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobLogConfigInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobLogConfigInfo, True ],
        } )
    
    def job_schedule_consumer_get(self, job_name, job_consumer_owner, job_schedule_name, job_id, job_consumer_affinity, desired_attributes=None):
        """
        Get a single job schedule entry.
        
        :param job_name: Name of the job.
        
        :param job_consumer_owner: The node where the job is scheduled.
        
        :param job_schedule_name: The name of the job schedule.
        
        :param job_id: The job id.
        
        :param job_consumer_affinity: The scheduling affinity of the job.  Affinity is used to indicate
                whether scheduling is independent (cluster) or specific (node) to
                a specific compute location in the cluster.
                Possible values:
                <ul>
                <li> "cluster"   - Cluster Affinity,
                <li> "node"      - Node Affinity
                </ul>
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-schedule-consumer-get", {
            'job_name': [ job_name, 'job-name', [ basestring, 'None' ], False ],
            'job_consumer_owner': [ job_consumer_owner, 'job-consumer-owner', [ basestring, 'None' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobScheduleConsumerInfo, 'None' ], False ],
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
            'job_consumer_affinity': [ job_consumer_affinity, 'job-consumer-affinity', [ basestring, 'job-affinity' ], False ],
        }, {
            'attributes': [ JobScheduleConsumerInfo, False ],
        } )
    
    def job_stop_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Stop a collection of jobs.
        
        :param query: If operating on a specific job, this input element must specify
                all keys.
                If operating on job objects based on query, this input element
                must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching job even
                when the operation on a previous matching job fails, and do so
                until the total number of objects failed to be operated on
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job objects to be operated in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of job objects (just
                keys) that were successfully operated on.
                If set to false, the list of job objects operated on will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job objects match a
                given query.
                If set to true, the API will continue with the next matching job
                even when the operation fails for the job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job objects (just
                keys) that were not operated on due to some error.
                If set to false, the list of job objects not operated on will not
                be returned.
                Default: true
        """
        return self.request( "job-stop-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobStopIterInfo, True ],
            'failure-list': [ JobStopIterInfo, True ],
        } )
    
    def job_private_delete_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Delete a collection of private jobs.
        
        :param query: If operating on a specific private job, this input element must
                specify all keys.
                If operating on private job objects based on query, this input
                element must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching private job
                even when the operation on a previous matching private job fails,
                and do so until the total number of objects failed to be operated
                on reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of private job objects to be operated in this
                call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of private job
                objects (just keys) that were successfully operated on.
                If set to false, the list of private job objects operated on will
                not be returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple private job objects
                match a given query.
                If set to true, the API will continue with the next matching
                private job even when the operation fails for the private job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of private job
                objects (just keys) that were not operated on due to some error.
                If set to false, the list of private job objects not operated on
                will not be returned.
                Default: true
        """
        return self.request( "job-private-delete-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobPrivateDeleteIterInfo, True ],
            'failure-list': [ JobPrivateDeleteIterInfo, True ],
        } )
    
    def job_schedule_cron_get(self, job_schedule_name, desired_attributes=None):
        """
        Get a single cron job schedule entry.
        
        :param job_schedule_name: The name of the job schedule.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-schedule-cron-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobScheduleCronInfo, 'None' ], False ],
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
        }, {
            'attributes': [ JobScheduleCronInfo, False ],
        } )
    
    def job_history_get(self, job_node, log_id, desired_attributes=None):
        """
        Get a single job history event.
        
        :param job_node: The name of the node where the job ran, or the node that changed
                the job's state.
        
        :param log_id: The internal identifier of this job history event.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-history-get", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobHistoryInfo, 'None' ], False ],
            'log_id': [ log_id, 'log-id', [ int, 'None' ], False ],
        }, {
            'attributes': [ JobHistoryInfo, False ],
        } )
    
    def job_unclaim_iter(self, query, max_failure_count=None, max_records=None, return_success_list=None, tag=None, continue_on_failure=None, return_failure_list=None):
        """
        Detach a collection of cluster jobs from their owning nodes.
        
        :param query: If operating on a specific job, this input element must specify
                all keys.
                If operating on job objects based on query, this input element
                must specify a query.
        
        :param max_failure_count: When allowing failures ('continue-on-failure' is set to true),
                then this input element may be provided to limit the number of
                failed operations before the server gives up and returns.
                If set, the API will continue with the next matching job even
                when the operation on a previous matching job fails, and do so
                until the total number of objects failed to be operated on
                reaches the maximum specified.
                If set to the maximum or not provided, then there will be no
                limit on the number of failed operations.
                Only applicable if 'continue-on-failure' is set to true.
                Default: 2^32-1
        
        :param max_records: The maximum number of job objects to be operated in this call.
                Default: 20
        
        :param return_success_list: If set to true, the API will return the list of job objects (just
                keys) that were successfully operated on.
                If set to false, the list of job objects operated on will not be
                returned.
                Default: true
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the next-tag obtained from the previous
                call.
        
        :param continue_on_failure: This input element is useful when multiple job objects match a
                given query.
                If set to true, the API will continue with the next matching job
                even when the operation fails for the job.
                If set to false, the API will return on the first failure.
                Default: false
        
        :param return_failure_list: If set to true, the API will return the list of job objects (just
                keys) that were not operated on due to some error.
                If set to false, the list of job objects not operated on will not
                be returned.
                Default: true
        """
        return self.request( "job-unclaim-iter", {
            'max_failure_count': [ max_failure_count, 'max-failure-count', [ int, 'None' ], False ],
            'max_records': max_records,
            'return_success_list': [ return_success_list, 'return-success-list', [ bool, 'None' ], False ],
            'tag': tag,
            'continue_on_failure': [ continue_on_failure, 'continue-on-failure', [ bool, 'None' ], False ],
            'return_failure_list': [ return_failure_list, 'return-failure-list', [ bool, 'None' ], False ],
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
        }, {
            'num-succeeded': [ int, False ],
            'num-failed': [ int, False ],
            'success-list': [ JobUnclaimIterInfo, True ],
            'failure-list': [ JobUnclaimIterInfo, True ],
        } )
    
    def job_queue_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple job queue records.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 100
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                job-queue object.
                All job-queue objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-queue-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobQueueInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobQueueInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobQueueInfo, True ],
        } )
    
    def job_private_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Get multiple private job records.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                private job object.
                All private job objects matching this query up to 'max-records'
                will be returned.
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "job-private-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ JobInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ JobInfo, 'None' ], False ],
        }, {
            'attributes-list': [ JobInfo, True ],
        } )
    
    def job_log_config_modify(self, job_log_module, job_log_level=None):
        """
        Modify a single job-manager-logging configuration entry.
        
        :param job_log_module: The module being logged.  These are pre-defined in the system
                binaries. To get an up-to-date list call job-log-config-get-iter
                without a query.
        
        :param job_log_level: The verbosity of logging enabled in the given module.
                Possible values:
                <ul>
                <li> "emerg"     ,
                <li> "alert"     ,
                <li> "crit"      ,
                <li> "err"       ,
                <li> "warning"   ,
                <li> "notice"    ,
                <li> "info"      ,
                <li> "debug"
                </ul>
        """
        return self.request( "job-log-config-modify", {
            'job_log_level': [ job_log_level, 'job-log-level', [ basestring, 'job-log-level' ], False ],
            'job_log_module': [ job_log_module, 'job-log-module', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def job_schedule_interval_create(self, job_schedule_name, job_schedule_interval_minutes=None, job_schedule_interval_seconds=None, return_record=None, job_schedule_interval_hours=None, job_schedule_interval_days=None):
        """
        Create a new interval job schedule entry.
        
        :param job_schedule_name: The name of the job schedule.
        
        :param job_schedule_interval_minutes: The number of minutes between jobs.
        
        :param job_schedule_interval_seconds: The number of seconds between jobs.
        
        :param return_record: If set to true, returns the job-schedule-interval on successful
                creation.
                Default: false
        
        :param job_schedule_interval_hours: The number of hours between jobs.
        
        :param job_schedule_interval_days: The number of days between jobs.
        """
        return self.request( "job-schedule-interval-create", {
            'job_schedule_interval_minutes': [ job_schedule_interval_minutes, 'job-schedule-interval-minutes', [ int, 'None' ], False ],
            'job_schedule_interval_seconds': [ job_schedule_interval_seconds, 'job-schedule-interval-seconds', [ int, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'job_schedule_interval_hours': [ job_schedule_interval_hours, 'job-schedule-interval-hours', [ int, 'None' ], False ],
            'job_schedule_interval_days': [ job_schedule_interval_days, 'job-schedule-interval-days', [ int, 'None' ], False ],
            'job_schedule_name': [ job_schedule_name, 'job-schedule-name', [ basestring, 'None' ], False ],
        }, {
            'result': [ JobScheduleIntervalInfo, False ],
        } )
    
    def job_private_stop(self, job_node, job_id):
        """
        Stop a job.
        
        :param job_node: Node
        
        :param job_id: Job ID
        """
        return self.request( "job-private-stop", {
            'job_node': [ job_node, 'job-node', [ basestring, 'node-name' ], False ],
            'job_id': [ job_id, 'job-id', [ int, 'None' ], False ],
        }, {
        } )
