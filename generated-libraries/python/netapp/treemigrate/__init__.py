from netapp.connection import NaConnection
from treemigrate_migrations import TreemigrateMigrations # 3 properties
from treemigrate_status_info import TreemigrateStatusInfo # 15 properties
from treemigrate_fh_map_memory import TreemigrateFhMapMemory # 3 properties
from treemigrate_files_estimate import TreemigrateFilesEstimate # 3 properties

class TreemigrateConnection(NaConnection):
    
    def treemigrate_abort(self, migration_id):
        """
        Abort an in-progress data migration identified by the
        migration-id passed in. Only migrations that are in the
        Initialization or Copy state can be aborted. If the migration
        is in the Copy State and has not yet cut over file service for
        the migrated data to the destination system then the migration
        will be stopped and any files copied to the destination will be
        removed. If the migration is not in the Initialization or Copy
        State then by default the command will return without aborting
        the migration.
        An aborted migration cannot be restarted. If it is required to
        stop a migration that is in the Proxy state then reduce the
        proxy inactivity timeout using the treemigrate-modify API.
        
        :param migration_id: The migration identifier of the migration to abort.
        """
        return self.request( "treemigrate-abort", {
            'migration_id': [ migration_id, 'migration-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def treemigrate_list_info_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous treemigrate-list-info-iter-start.
        """
        return self.request( "treemigrate-list-info-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def treemigrate_start(self, destination_path, source_path, leave_source=None, proxy_inactivity_timeout=None, leave_destination=None, expected_files_number=None, priority_level=None, test_run=None):
        """
        Start the data migration process. The source path
        and destination path must be specified. The migrated data
        on the source storage system is removed during the Proxy Cleanup State.
        The treemigrate-start API runs in the background copying the
        data from the source to the destination system, doing the
        cut over, and then proxying client requests from the source
        system to the destination system for the migrated data. The
        proxy will continue to run until proxy-inactivity-timeout
        minutes after there are no client requests to proxy from
        the source to the destination system.
        
        :param destination_path: The destination system and path to a directory or file where
                the data specified in the source-path will be migrated to.
                The destination system and path argument should be separated
                by a colon. Both of these arguments together are referred to
                as the destination. If the last component of the destination
                path name exists on the destination system then it must be a
                directory and must be exported for use by the root user
                account on the source system. The data to be migrated from
                the source system to the destination system will be placed
                inside this directory on the destination system. The source
                system will mount this directory from the destination system.
                If the last component of the destination path name does not
                exist on the destination system then the directory or file
                being migrated as specified with the source path name will
                assume the name of the last component of the destination path
                name. For this case then the parent directory of the last
                component of the destination path name must be exported for
                use by the root user account on the source system. The source
                system will mount the parent directory of the last component
                of the destination path name from the destination system.
                Ex: toaster:/vol/vol162/dir10/subdir19
        
        :param source_path: The path to a directory or file that will be migrated to
                the destination. Paths are specified by their fully-qualified
                path. The directory or file must exist on the source
                system, that is the system running the treemigrate-start command.
        
        :param leave_source: When set it will make the treemigrate-start call leave the
                files on the source after the migration is complete. Otherwise
                the files that were migrated will be removed from the source.
                The default value is false.
        
        :param proxy_inactivity_timeout: The number of minutes after which no requests have been
                proxied then the migration moves from the Proxy state to the
                Proxy Cleanup state.
                A timeout value of 0 indicates that the migration should
                go to the Proxy Cleanup state immediately.
                The default value is 30 minutes.
        
        :param leave_destination: When set files already copied on the dstination will not be
                cleared if the treemigration fails due to any reason.
                The default value is false.
        
        :param expected_files_number: Expected number of files which will be migrated.
                Memory allocation for File Handle map will be done for
                this number of files before starting the data copy.
                Default value is 0.
        
        :param priority_level: The priority level of the copy phase of the migration.
                Possible values are: "fast", "medium", or "slow".
                The default priority level is "medium".
        
        :param test_run: When set it will make the treemigrate-start call a test run;
                that is, it will run all the pre-migration checks, but will
                not migrate the data. Use the treemigrate status APIs to
                get the status of the test run and find out how many
                directories, files, and bytes would be migrated had this
                call been performed without this flag set.
                The default value is false.
        """
        return self.request( "treemigrate-start", {
            'leave_source': [ leave_source, 'leave-source', [ bool, 'None' ], False ],
            'proxy_inactivity_timeout': [ proxy_inactivity_timeout, 'proxy-inactivity-timeout', [ int, 'None' ], False ],
            'leave_destination': [ leave_destination, 'leave-destination', [ bool, 'None' ], False ],
            'destination_path': [ destination_path, 'destination-path', [ basestring, 'None' ], False ],
            'expected_files_number': [ expected_files_number, 'expected-files-number', [ int, 'None' ], False ],
            'priority_level': [ priority_level, 'priority-level', [ basestring, 'None' ], False ],
            'test_run': [ test_run, 'test-run', [ bool, 'None' ], False ],
            'source_path': [ source_path, 'source-path', [ basestring, 'None' ], False ],
        }, {
            'migration-id': [ int, False ],
        } )
    
    def treemigrate_limits(self):
        """
        Display limits for treemigrations
        """
        return self.request( "treemigrate-limits", {
        }, {
            'treemigrate-fh-map-memory': [ TreemigrateFhMapMemory, False ],
            'treemigrate-migrations': [ TreemigrateMigrations, False ],
            'treemigrate-files-estimate': [ TreemigrateFilesEstimate, False ],
        } )
    
    def treemigrate_list_info_iter_start(self, active=None, migration_id=None):
        """
        Reports the status of one or more data migrations that are
        currently in progress or have recently completed. If a
        migration-id is specified then only the status of that data
        migration is reported.
        
        :param active: When set will limit the results to only returning
                information on active migrations, that is migrations
                that are in the Copy or Proxy state. This flag is
                ignored if the migrate-id is specified.
                The default value false.
        
        :param migration_id: When the migration identifier is specified then only
                information on that migration will be returned.
        """
        return self.request( "treemigrate-list-info-iter-start", {
            'active': [ active, 'active', [ bool, 'None' ], False ],
            'migration_id': [ migration_id, 'migration-id', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def treemigrate_status_clear(self, migration_id=None):
        """
        Clear completed migrations from the system so that the
        migration does not show up when the migration status is
        listed. If a migration-id is specified then only that
        entry is cleared provided the migration is complete.
        A migration is considered complete if it is in the
        "Migration Complete", "Migration Aborted", or
        "Migration Failed" state.
        
        :param migration_id: When the migration identifier is specified then only
                that migration will be cleared.
        """
        return self.request( "treemigrate-status-clear", {
            'migration_id': [ migration_id, 'migration-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def treemigrate_modify(self, migration_id, proxy_inactivity_timeout=None):
        """
        Modify the parameters of a migration that is in the Copy
        or Proxy state.
        
        :param migration_id: The migration identifier of the migration to modify.
        
        :param proxy_inactivity_timeout: The number of minutes after which no requests have been
                proxied then the migration moves from the Proxy state to the
                Proxy Cleanup state.
                A timeout value of 0 indicates that the migration should
                go to the Proxy Cleanup state immediately.
                The default value is 30 minutes.
        """
        return self.request( "treemigrate-modify", {
            'proxy_inactivity_timeout': [ proxy_inactivity_timeout, 'proxy-inactivity-timeout', [ int, 'None' ], False ],
            'migration_id': [ migration_id, 'migration-id', [ int, 'None' ], False ],
        }, {
        } )
    
    def treemigrate_list_info_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to
        treemigrate-list-info-iter-start.
        
        :param tag: Tag from a previous treemigrate-list-info-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "treemigrate-list-info-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'treemigrate-status': [ TreemigrateStatusInfo, True ],
        } )
