from netapp.connection import NaConnection
from cifs_lug_import_op_status import CifsLugImportOpStatus # 0 properties
from cifs_security_get_iter_key_td import CifsSecurityGetIterKeyTd # 1 properties
from cifs_shadowcopy_ems_get_iter_key_td import CifsShadowcopyEmsGetIterKeyTd # 3 properties
from cifs_options import CifsOptions # 18 properties
from cifs_home_directory_search_path_get_iter_key_td import CifsHomeDirectorySearchPathGetIterKeyTd # 3 properties
from cifs_domain_server_prefer_type import CifsDomainServerPreferType # 0 properties
from cifs_session_info import CifsSessionInfo # 8 properties
from cifs_share_access_control import CifsShareAccessControl # 5 properties
from cifs_server_get_iter_key_td import CifsServerGetIterKeyTd # 1 properties
from volumes_list_info import VolumesListInfo # 1 properties
from cifs_share_get_iter_key_td import CifsShareGetIterKeyTd # 2 properties
from cifs_domain_name_mapping_search import CifsDomainNameMappingSearch # 2 properties
from nbalias_name_info import NbaliasNameInfo # 0 properties
from cifs_filesystem_sector_size import CifsFilesystemSectorSize # 0 properties
from cifs_branchcache_get_iter_key_td import CifsBranchcacheGetIterKeyTd # 1 properties
from cifs_ca_protection import CifsCaProtection # 0 properties
from cifs_domain_discovered_server_status import CifsDomainDiscoveredServerStatus # 0 properties
from cifs_symlink_locality import CifsSymlinkLocality # 0 properties
from vscan_fileop_profile import VscanFileopProfile # 0 properties
from cifs_session import CifsSession # 16 properties
from cifs_privilege import CifsPrivilege # 3 properties
from cifs_name import CifsName # 0 properties
from homedir_path_info import HomedirPathInfo # 0 properties
from cifs_dialects import CifsDialects # 0 properties
from cifs_local_group_get_iter_key_td import CifsLocalGroupGetIterKeyTd # 3 properties
from cifs_setup_ou import CifsSetupOu # 0 properties
from cifs_domain_preferred_dc import CifsDomainPreferredDc # 3 properties
from cifs_local_group import CifsLocalGroup # 3 properties
from access_rights_info import AccessRightsInfo # 3 properties
from realm_name import RealmName # 0 properties
from cifs_domain_discovered_servers_get_iter_key_td import CifsDomainDiscoveredServersGetIterKeyTd # 5 properties
from cifs_share_symlink_properties import CifsShareSymlinkProperties # 0 properties
from cifs_domain_trusts import CifsDomainTrusts # 4 properties
from cifs_nbtstat import CifsNbtstat # 11 properties
from cifs_setup_site import CifsSetupSite # 0 properties
from cifs_branchcache import CifsBranchcache # 6 properties
from elapsed_time import ElapsedTime # 0 properties
from cifs_nbtstat_get_iter_key_td import CifsNbtstatGetIterKeyTd # 4 properties
from inet_address import InetAddress # 0 properties
from cifs_symlink_get_iter_key_td import CifsSymlinkGetIterKeyTd # 2 properties
from cifs_options_get_iter_key_td import CifsOptionsGetIterKeyTd # 1 properties
from cifs_domain_discovered_server_type import CifsDomainDiscoveredServerType # 0 properties
from windows_sid import WindowsSid # 0 properties
from cifs_home_directory_search_path import CifsHomeDirectorySearchPath # 3 properties
from domain_name import DomainName # 0 properties
from address_info import AddressInfo # 6 properties
from cifs_session_file_get_iter_key_td import CifsSessionFileGetIterKeyTd # 4 properties
from cifs_privilege_get_iter_key_td import CifsPrivilegeGetIterKeyTd # 3 properties
from path_error_info import PathErrorInfo # 2 properties
from cifs_domain_name_mapping_search_get_iter_key_td import CifsDomainNameMappingSearchGetIterKeyTd # 1 properties
from connection_info import ConnectionInfo # 4 properties
from cifs_local_user import CifsLocalUser # 5 properties
from cifs_share import CifsShare # 14 properties
from cifs_server_config import CifsServerConfig # 8 properties
from cifs_functional_level import CifsFunctionalLevel # 0 properties
from cifs_top_info import CifsTopInfo # 7 properties
from netbios_name import NetbiosName # 0 properties
from cifs_domain_discovered_servers import CifsDomainDiscoveredServers # 8 properties
from cifs_local_user_get_iter_key_td import CifsLocalUserGetIterKeyTd # 3 properties
from cifs_security import CifsSecurity # 7 properties
from cifs_session_get_iter_key_td import CifsSessionGetIterKeyTd # 3 properties
from cifs_share_access_control_get_iter_key_td import CifsShareAccessControlGetIterKeyTd # 3 properties
from auth_mechanism import AuthMechanism # 0 properties
from cifs_domain_trusts_get_iter_key_td import CifsDomainTrustsGetIterKeyTd # 2 properties
from cifs_share_info import CifsShareInfo # 17 properties
from cifs_file_type import CifsFileType # 0 properties
from cifs_domain_preferred_dc_get_iter_key_td import CifsDomainPreferredDcGetIterKeyTd # 3 properties
from cifs_symlink import CifsSymlink # 6 properties
from cifs_share_acl_info import CifsShareAclInfo # 2 properties
from cifs_access_perms import CifsAccessPerms # 0 properties
from wins_entry_info import WinsEntryInfo # 2 properties
from cifs_share_properties import CifsShareProperties # 0 properties
from cifs_local_group_members_get_iter_key_td import CifsLocalGroupMembersGetIterKeyTd # 4 properties
from uri import Uri # 0 properties
from cifs_local_group_members import CifsLocalGroupMembers # 3 properties
from cifs_bc_version_control import CifsBcVersionControl # 0 properties
from cifs_session_file import CifsSessionFile # 15 properties
from cifs_privilege_entries import CifsPrivilegeEntries # 0 properties
from cifs_local_user_membership import CifsLocalUserMembership # 3 properties
from cifs_local_user_membership_get_iter_key_td import CifsLocalUserMembershipGetIterKeyTd # 4 properties
from cifs_open_mode import CifsOpenMode # 0 properties
from cifs_auth_style import CifsAuthStyle # 0 properties

class CifsConnection(NaConnection):
    
    def cifs_setup_site_list_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to
        cifs-setup-site-list-iter-start
        
        :param tag: Tag from a previous cifs-setup-site-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "cifs-setup-site-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'default-site': [ basestring, False ],
            'cifs-setup-sites': [ basestring, True ],
        } )
    
    def cifs_domain_trusts_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of discovered trusted domains.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-domain-trusts object.
                All cifs-domain-trusts objects matching this query up to
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
        return self.request( "cifs-domain-trusts-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsDomainTrusts, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsDomainTrusts, 'None' ], False ],
        }, {
            'attributes-list': [ CifsDomainTrusts, True ],
        } )
    
    def cifs_privilege_add_privilege(self, privileges, user_or_group_name):
        """
        Add privileges to a local or Active Directory user or group
        
        :param privileges: Privileges
        
        :param user_or_group_name: User or Group Name
        """
        return self.request( "cifs-privilege-add-privilege", {
            'privileges': [ privileges, 'privileges', [ basestring, 'cifs-privilege-entries' ], True ],
            'user_or_group_name': [ user_or_group_name, 'user-or-group-name', [ basestring, 'cifs-name' ], False ],
        }, {
        } )
    
    def cifs_branchcache_modify(self, flush_hashes=None, operating_mode=None, versions=None, hash_store_path=None, server_key=None, hash_store_max_size=None):
        """
        Modify the CIFS BranchCache service settings
        
        :param flush_hashes: Delete Existing Hashes
        
        :param operating_mode: CIFS BranchCache Operating Modes
        
        :param versions: Supported BranchCache Versions
        
        :param hash_store_path: Path to Hash Store
        
        :param server_key: Encryption Key Used to Secure the Hashes
        
        :param hash_store_max_size: Maximum Size of the Hash Store
        """
        return self.request( "cifs-branchcache-modify", {
            'flush_hashes': [ flush_hashes, 'flush-hashes', [ bool, 'None' ], False ],
            'operating_mode': [ operating_mode, 'operating-mode', [ basestring, 'None' ], False ],
            'versions': [ versions, 'versions', [ basestring, 'cifs-bc-version-control' ], True ],
            'hash_store_path': [ hash_store_path, 'hash-store-path', [ basestring, 'None' ], False ],
            'server_key': [ server_key, 'server-key', [ basestring, 'None' ], False ],
            'hash_store_max_size': [ hash_store_max_size, 'hash-store-max-size', [ int, 'size' ], False ],
        }, {
        } )
    
    def cifs_session_list_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous cifs-session-list-iter-start.
        """
        return self.request( "cifs-session-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def cifs_domain_discovered_servers_reset(self):
        """
        Command to trigger re-discovery of servers.
        """
        return self.request( "cifs-domain-discovered-servers-reset", {
        }, {
        } )
    
    def cifs_symlink_modify(self, unix_path, share_name=None, cifs_path=None, cifs_server=None, locality=None):
        """
        Modify a CIFS symbolic link path mapping parameters.
        
        :param unix_path: This field specifies the UNIX path prefix to be matched for the
                mapping. If the prefix of the target path in the symbolic link
                matches against this field, this entry of symbolic link path
                mapping would be used. The path is a UTF-8 string and supports
                localization. The path must start and end with a forward slash
                ('/'). For example '/usr/local/'.
        
        :param share_name: This field specifies the CIFS share name on the destination CIFS
                server to which the symbolic link is mapped. This is a UTF-8
                string and supports localization.
        
        :param cifs_path: This field specifies the CIFS path on the destination to which
                the symbolic link maps. The final path is generated by
                concatenating the CIFS server name, the share name, the cifs-path
                and the remaining path in the symbolic link left after the prefix
                match. This value is specified by using a UNIX-style path name.
                The trailing forward slash is required for the full path name to
                be properly interpreted. This is a UTF-8 string and supports
                localization.
        
        :param cifs_server: This field specifies the destination CIFS server name for the
                mapping to which the symbolic link is mapped. The default is the
                local CIFS server. The field needs to be specified if the
                locality of the symbolic link is 'widelink'. This can be either a
                DNS name, NetBIOS name or an IP address. If a DNS name or a
                NetBIOS name are specified, the CIFS client configuration should
                be such that it is capable of resolving the CIFS server name to
                the correct IP address.
        
        :param locality: This field specifies whether the CIFS symbolic link is a local
                link or wide link. A local symbolic link maps to the local CIFS
                share, whereas a wide symbolic link maps to any CIFS share on the
                network. If the CIFS server matches the VServer's NetBIOS name
                then the default value is local otherwise widelink.
                Possible values:
                <ul>
                <li> "local"     - Share On This VServer,
                <li> "widelink"  - Share On Another CIFS Server
                </ul>
        """
        return self.request( "cifs-symlink-modify", {
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
            'cifs_path': [ cifs_path, 'cifs-path', [ basestring, 'None' ], False ],
            'unix_path': [ unix_path, 'unix-path', [ basestring, 'None' ], False ],
            'cifs_server': [ cifs_server, 'cifs-server', [ basestring, 'None' ], False ],
            'locality': [ locality, 'locality', [ basestring, 'cifs-symlink-locality' ], False ],
        }, {
        } )
    
    def cifs_server_create(self, domain, cifs_server, admin_username, admin_password, default_site=None, force_account_overwrite=None, administrative_status=None, organizational_unit=None):
        """
        Configure and setup CIFS services on a Vserver.
        
        :param domain: The fully qualified domain name of the Windows Active Directory
                this CIFS server belongs to.
        
        :param cifs_server: The NetBIOS name of the CIFS server.
        
        :param admin_username: The username of the account used to add this CIFS server to the
                Active Directory.
        
        :param admin_password: The password for the account used to add this CIFS server to the
                Active Directory.
        
        :param default_site: The default site used by LIFs that do not have a site
                membership.
        
        :param force_account_overwrite: If this is set and a machine account with the same name as
                specified in 'cifs-server' exists in the Active Directory, it
                will be overwritten and reused. The default value for this field
                is false.
        
        :param administrative_status: CIFS Server Administrative Status
                Possible values:
                <ul>
                <li> "down" ,
                <li> "up"
                </ul>
        
        :param organizational_unit: The Organizational Unit (OU) within the Windows Active Directory
                this CIFS server belongs to.
        """
        return self.request( "cifs-server-create", {
            'domain': [ domain, 'domain', [ basestring, 'None' ], False ],
            'cifs_server': [ cifs_server, 'cifs-server', [ basestring, 'netbios-name' ], False ],
            'default_site': [ default_site, 'default-site', [ basestring, 'None' ], False ],
            'force_account_overwrite': [ force_account_overwrite, 'force-account-overwrite', [ bool, 'None' ], False ],
            'admin_username': [ admin_username, 'admin-username', [ basestring, 'None' ], False ],
            'administrative_status': [ administrative_status, 'administrative-status', [ basestring, 'service-state' ], False ],
            'organizational_unit': [ organizational_unit, 'organizational-unit', [ basestring, 'None' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_homedir_path_get_for_user(self, user_name):
        """
        Return path to the user's CIFS home directory if it exists.
        
        :param user_name: Name of the user. If the filer is using the "mapped" CIFS
                home directory naming style, then a mapped Unix name is
                provided. For the domain naming style, a domain/user is
                provided. Otherwise the filer will expect the NT name for
                the user.
                The filer's CIFS home directory naming style can be obtained
                with the "options-get" api, using input parameter "name
                cifs.home_dir_namestyle".
        """
        return self.request( "cifs-homedir-path-get-for-user", {
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
        }, {
            'homedir-path-user': [ basestring, False ],
        } )
    
    def cifs_local_group_members_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of local group members
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-local-group-members object.
                All cifs-local-group-members objects matching this query up to
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
        return self.request( "cifs-local-group-members-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsLocalGroupMembers, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsLocalGroupMembers, 'None' ], False ],
        }, {
            'attributes-list': [ CifsLocalGroupMembers, True ],
        } )
    
    def cifs_share_modify(self, share_name, comment=None, dir_umask=None, offline_files_mode=None, share_properties=None, symlink_properties=None, path=None, attribute_cache_ttl=None, file_umask=None, vscan_fileop_profile=None):
        """
        Modifies settings of a CIFS share, even if the shares are in
        use.
        
        :param share_name: The name of the CIFS share. The CIFS share name is a UTF-8 string
                with the following characters being illegal: control characters
                from 0x00 to 0x1F, both inclusive, 0x22 (double quotes) and the
                characters \/[]:|<>+=;,?"*
        
        :param comment: This string gives a description of the CIFS share. CIFS clients
                see this description when browsing the Vserver's CIFS shares.
        
        :param dir_umask: The value of this field controls the file mode creation mask for
                the CIFS share in qtrees with UNIX or Mixed security styles. The
                mask restricts the initial permissions setting of a newly created
                directory. The input value is a numeric mode comprising of one to
                three octal digits (0-7), derived by adding up the bits with
                values 4, 2, and 1. The first digit selects permissions for the
                user who owns the file: read (4), write (2), and execute (1); the
                second selects permissions for other users in the file's group,
                with the same values; and the third for other users not in the
                file's group, with the same values.
        
        :param offline_files_mode: Mode of the offline file for the CIFS share. The default value
                is manual.
                Possible values:
                <ul>
                <li> "none"      - Clients are not permitted to cache files for
                offline access.,
                <li> "manual"    - Clients may cache files that are explicitly
                selected by the user for offline use.,
                <li> "documents" - Clients may automatically cache files that
                are used by the user for offline access.,
                <li> "programs"  - Clients may automatically cache files that
                are used by the user for offline access and may use those files
                in an offline mode even if the share is available.
                </ul>
        
        :param share_properties: The list of properties for this CIFS share.
                Possible values:
                <ul>
                <li> "oplocks"        - This specifies that opportunistic locks
                (client-side caching) are enabled on this share.,
                <li> "browsable"      - This specifies that the share can be
                browsed by Windows clients.,
                <li> "showsnapshot"   - This specifies that Snapshots can be
                viewed and traversed by clients.,
                <li> "changenotify"   - This specifies that CIFS clients can
                request for change notifications for directories on this share.,
                <li> "homedirectory"  - This specifies that the share is added
                and enabled as part of the CIFS home directory feature. The
                configuration of this share should be done using CIFS home
                directory feature interface. This property cannot be added or
                removed from existing share.
                <li> "attributecache" - This specifies that connections through
                this share are caching attributes for a short time to improve
                performance.
                <li> "branchcache" - This specifies that clients connecting to
                this share can make requests using BranchCache technology that
                allows them to cache the content in an attempt to reduce WAN
                utilization from a remote office.
                <li> "continuously_available" - This specifies that clients
                connecting to this share can open files in a persistent manner.
                Files opened this way are protected from disruptive events, such
                as failover and giveback.
                <li> "shadowcopy" - This specifies that the share is pointing
                to a shadow copy. This attribute cannot be added nor removed from
                a share.
                <li> "access_based_enumeration" - This specifies that Access
                Based Enumeration is enabled on this share. ABE-filtered shared
                folders are visible to a user based on that individual user's
                access rights, preventing the display of folders or other shared
                resources that the user does not have rights to access.
                </ul>
        
        :param symlink_properties: This flag controls whether the symlinks under this shared
                directory are hidden (option 'hide'), accessible (option
                'enable') or are accessible as read-only (option 'read-only'
                along with option 'enable').
                Possible values:
                <ul>
                <li> "enable"    ,
                <li> "hide"      ,
                <li> "read_only"
                </ul>
        
        :param path: The file system path that is shared through this CIFS share.
        
        :param attribute_cache_ttl: The lifetime of an entry in the file attribute cache, in seconds.
                This value is used if the share has the 'attributecache' property
                set, which improves the performance of certain metadata
                operations in common workloads. The default is 10 seconds.
                Raising this value may improve performance, but the likelihood
                that stale metadata will be served increases as well. The value
                of this field must be in the range of 1 to 86400.
        
        :param file_umask: The value of this field controls the file mode creation mask for
                the CIFS share in qtrees with UNIX or Mixed security styles. The
                mask restricts the initial permissions setting of a newly created
                file. The input value is a numeric mode comprising of one to
                three octal digits (0-7), derived by adding up the bits with
                values 4, 2, and 1. The first digit selects permissions for the
                user who owns the file: read (4), write (2), and execute (1); the
                second selects permissions for other users in the file's group,
                with the same values; and the third for other users not in the
                file's group, with the same values.
        
        :param vscan_fileop_profile: Profile-set of file-ops to which Vscan On-Access scanning
                is applicable.
                Possible values:
                <ul>
                <li> "no_scan"     - Virus scans are never triggered for
                accesses to this share,
                <li> "standard"    - Virus scans can be triggered by open,
                close, and rename operations,
                <li> "strict"      - Virus scans can be triggered by open,
                read, close, and rename operations,
                <li> "writes_only" - Virus scans can be triggered only when
                a file that has been modified is closed.
                </ul>
        """
        return self.request( "cifs-share-modify", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'dir_umask': [ dir_umask, 'dir-umask', [ int, 'None' ], False ],
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
            'offline_files_mode': [ offline_files_mode, 'offline-files-mode', [ basestring, 'None' ], False ],
            'share_properties': [ share_properties, 'share-properties', [ basestring, 'cifs-share-properties' ], True ],
            'symlink_properties': [ symlink_properties, 'symlink-properties', [ basestring, 'cifs-share-symlink-properties' ], True ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'attribute_cache_ttl': [ attribute_cache_ttl, 'attribute-cache-ttl', [ int, 'None' ], False ],
            'file_umask': [ file_umask, 'file-umask', [ int, 'None' ], False ],
            'vscan_fileop_profile': [ vscan_fileop_profile, 'vscan-fileop-profile', [ basestring, 'vscan-fileop-profile' ], False ],
        }, {
        } )
    
    def cifs_top_iter_start(self, maxclients=None, sortgroup=None, avgtype=None):
        """
        Display CIFS client statistics
        
        :param maxclients: Specifies the maximum number of top clients to display
                (the default is 20).
        
        :param sortgroup: If specified, the client statistics are sorted by the
                value of the string:
                "ops":		Sort by the number of operations per second of any type.
                "reads":	Sort by kbytes/sec of data in response to read requests.
                "writes":	Sort by kbytes/sec of data written to the filer.
                "ios":		Sort by the combined total of reads plus writes for
                each client.
                "suspicious":	Sort by the number of "suspicious" events per
                second by each client.
        
        :param avgtype: Specifies how the client statistics are to be averaged
                for display:
                "smooth":	Use a smoothed average which is weighted towards
                recent behavior but takes into account previous history
                of the client.
                "now":		Use a one-second sample taken immediately and
                no history is taken into account.
                "total":	Use the total count of each statistic divided by
                the total time since sampling started. If the
                is-verbose option is also set, the totals are
                given without dividing by the sample time.
        """
        return self.request( "cifs-top-iter-start", {
            'maxclients': [ maxclients, 'maxclients', [ int, 'None' ], False ],
            'sortgroup': [ sortgroup, 'sortgroup', [ basestring, 'None' ], False ],
            'avgtype': [ avgtype, 'avgtype', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def cifs_session_file_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of the opened CIFS files.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-session-file object.
                All cifs-session-file objects matching this query up to
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
        return self.request( "cifs-session-file-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsSessionFile, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsSessionFile, 'None' ], False ],
        }, {
            'attributes-list': [ CifsSessionFile, True ],
        } )
    
    def cifs_stop_on_target(self, target_name, target_type):
        """
        Stops the CIFS service for all users on specified target
        (volume or aggregate) across all vfilers with shares on
        the specified target. Appropriate warning should be
        given to connected clients before calling this API, as it
        will immediately terminate those sessions regardless of
        their current state.
        
        :param target_name: Name of the target on which CIFS service should be stopped.
                The target should be a volume or an aggregate name. The type
                must be specified with target-type parameter.
        
        :param target_type: Type of the target specified in target-name parameter, on which
                CIFS service should be stopped.
                Possible values: "volume", "aggregate".
        """
        return self.request( "cifs-stop-on-target", {
            'target_name': [ target_name, 'target-name', [ basestring, 'None' ], False ],
            'target_type': [ target_type, 'target-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_session_list_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to
        cifs-session-list-iter-start.
        
        :param tag: Tag from a previous cifs-session-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "cifs-session-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'cifs-sessions': [ CifsSessionInfo, True ],
            'records': [ int, False ],
        } )
    
    def cifs_local_user_delete(self, user_name):
        """
        Delete a single local user
        
        :param user_name: The name of the local user
        """
        return self.request( "cifs-local-user-delete", {
            'user_name': [ user_name, 'user-name', [ basestring, 'cifs-name' ], False ],
        }, {
        } )
    
    def cifs_shadowcopy_ems_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Return Shadow Copy EMS messages. This ZAPI is identical to the
        ems-message-get-iter except that it only returns
        cifs.shadowcopy.failure messages. Note that it is a stop gap and
        should only be used by SDW.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-shadowcopy-ems object.
                All cifs-shadowcopy-ems objects matching this query up to
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
        return self.request( "cifs-shadowcopy-ems-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ EmsMessageInfo, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EmsMessageInfo, 'None' ], False ],
        }, {
            'attributes-list': [ EmsMessageInfo, True ],
        } )
    
    def cifs_local_group_rename(self, group_name, new_group_name):
        """
        Rename a local group
        
        :param group_name: The name of the local group
        
        :param new_group_name: New Group Name
        """
        return self.request( "cifs-local-group-rename", {
            'group_name': [ group_name, 'group-name', [ basestring, 'cifs-name' ], False ],
            'new_group_name': [ new_group_name, 'new-group-name', [ basestring, 'cifs-name' ], False ],
        }, {
        } )
    
    def cifs_setup_verify_name(self, server_name, auth_type, domain_name, pdc_ip_address=None, login_user=None, login_password=None):
        """
        Determines whether or not a particular CIFS server name
        is already in use on the network and a specified domain.
        
        :param server_name: The NetBIOS CIFS server name that will be verified.
                Example: cifsserver
        
        :param auth_type: The authentication style that will be used in a
                subsequent call to cifs-setup. These styles are
                subject to change in a future release.
                Possible values: ad, nt4, workgroup, passwd
                Note: The domain-name, login-user and login-password
                fields are optional unless the auth-type is ad.
        
        :param domain_name: The name of the domain that the CIFS server will join.
                Examples: cifsdomain, cifs.domain.com
        
        :param pdc_ip_address: If this value is defined, CIFS will attempt to
                communicate with the domain controller directly using
                this address.
                Note: This information is only used when the auth-type
                is 'nt4'.
        
        :param login_user: The name of a domain user that has the ability to add
                the CIFS server to the domain given in domain-name.
                Examples: username (assumes domain-name is the
                user's domain), cifsdomain\username,
                cifs.domain.com\username
        
        :param login_password: The password for login-user.
        """
        return self.request( "cifs-setup-verify-name", {
            'pdc_ip_address': [ pdc_ip_address, 'pdc-ip-address', [ basestring, 'ip-address' ], False ],
            'server_name': [ server_name, 'server-name', [ basestring, 'None' ], False ],
            'login_user': [ login_user, 'login-user', [ basestring, 'None' ], False ],
            'login_password': [ login_password, 'login-password', [ basestring, 'None' ], False ],
            'auth_type': [ auth_type, 'auth-type', [ basestring, 'None' ], False ],
            'domain_name': [ domain_name, 'domain-name', [ basestring, 'None' ], False ],
        }, {
            'is-in-domain': [ bool, False ],
            'is-in-use': [ bool, False ],
        } )
    
    def cifs_share_ace_delete(self, share_name, user_name=None, is_unixgroup=None, unix_group_name=None):
        """
        Deletes the access control entry of the given share
        or the unix group. This API is equivalent to
        "cifs access <share> [-g] <user|group>" CLI.
        
        :param share_name: CIFS share name. It specifies name of the share of which the
                access rights have to be deleted. This is a case insensitive
                field. The maximum size of the share name is 256 characters.
        
        :param user_name: Name of the user. This API deletes the access rights of the
                specified user. This is a case sensitive field. The format of
                the field is <user-name>. If specified user does not exist,
                It fails with the reason "Unknown user <username>".
        
        :param is_unixgroup: This filter is used to tell that the access rights of the unix
                group have to be  deleted. If its value is true, uinx-group-name
                needs to be provided. Otherwise it fails with the reason
                "group-name missing". The default value of this is false.
        
        :param unix_group_name: Name of the unix group. This field specifies the unix group of
                which the access rights to be deleted. The format of this
                field <group-name>. This is a case sensitive field. If the
                specified group name does not exist, it fails with the reason
                "Unknown Unix group <group-name>"
        """
        return self.request( "cifs-share-ace-delete", {
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'is_unixgroup': [ is_unixgroup, 'is-unixgroup', [ bool, 'None' ], False ],
            'unix_group_name': [ unix_group_name, 'unix-group-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_domain_preferred_dc_add(self, domain, preferred_dc):
        """
        Add to a list of preferred domain controllers
        
        :param domain: The fully qualified domain name of the Active Directory domain to
                which the domain controllers in the list belong.
        
        :param preferred_dc: Preferred Domain Controllers
        """
        return self.request( "cifs-domain-preferred-dc-add", {
            'domain': [ domain, 'domain', [ basestring, 'None' ], False ],
            'preferred_dc': [ preferred_dc, 'preferred-dc', [ basestring, 'None' ], True ],
        }, {
        } )
    
    def cifs_options_modify(self, file_system_sector_size=None, is_copy_offload_enabled=None, is_smb3_enabled=None, shadowcopy_dir_depth=None, is_referral_enabled=None, is_local_users_and_groups_enabled=None, is_shadowcopy_enabled=None, is_use_junctions_as_reparse_points_enabled=None, is_trusted_domain_enum_search_enabled=None, is_exportpolicy_enabled=None, wins_servers=None, is_local_auth_enabled=None, is_smb2_enabled=None, max_mpx=None, read_grants_execute=None, default_unix_group=None, default_unix_user=None):
        """
        Modify the attributes of cifs-options object.
        
        :param file_system_sector_size: This optional parameter specifies the size of file system sector
                in bytes reported to SMB Clients.
                Possible values:
                <ul>
                <li> "512"  - Reported file system sector size to SMB clients
                is 512 bytes,
                <li> "4096" - Reported file system sector size to SMB clients
                is 4096 bytes
                </ul>
        
        :param is_copy_offload_enabled: This optional parameter specifies whether the CIFS server is
                capable of performing copy offload operation. The default value
                for this parameter is true.
        
        :param is_smb3_enabled: This optional parameter specifies whether the CIFS server
                negotiates the SMB3 version of the CIFS protocol. The default
                value for this parameter is true.
        
        :param shadowcopy_dir_depth: This optional parameter specifies the maximum depth of
                directories to shadow copy.
        
        :param is_referral_enabled: This optional parameter specifies whether the CIFS server refers
                clients to more optimal data access paths (LIFs). The default
                value for this parameter is false.
        
        :param is_local_users_and_groups_enabled: This optional parameter specifies whether the CIFS local users
                and groups feature is enabled on the cluster.
        
        :param is_shadowcopy_enabled: This optional parameter specifies whether the CIFS server is
                capable of performing shadow copy operations.
        
        :param is_use_junctions_as_reparse_points_enabled: This optional parameter specifies whether the CIFS server exposes
                junction points as reparse points to Windows clients.
        
        :param is_trusted_domain_enum_search_enabled: This optional parameter specifies whether the CIFS server is
                capable of performing enumeration of trusted domains and search
                to map a UNIX user to a Windows user.
        
        :param is_exportpolicy_enabled: This optional parameter specifies whether the CIFS server uses
                export policies to control client access. The default value for
                this parameter is false.
        
        :param wins_servers: List of Windows Internet Name Service (WINS) IP addresses. The
                Vserver will send NetBIOS name resolution requests to these
                addresses.
        
        :param is_local_auth_enabled: This optional parameter specifies whether CIFS local users can
                authenticate.
        
        :param is_smb2_enabled: This optional parameter specifies whether the CIFS server
                negotiates the SMB2 versions of the CIFS protocol. The default
                value for this parameter is true.
        
        :param max_mpx: This option controls maximum simultaneous operations the CIFS
                server reports it can process per TCP connection. The default
                value for this option is 255.
        
        :param read_grants_execute: On a file with UNIX Style security effective on it, if the file
                has read permission on it, a CIFS user would be allowed to
                execute permissions if this option is enabled.
        
        :param default_unix_group: The default UNIX group used if the identity of a CIFS group
                cannot be mapped using normal group mapping rules.
        
        :param default_unix_user: The default UNIX user used if the identity of a CIFS user cannot
                be mapped using normal user mapping rules.
        """
        return self.request( "cifs-options-modify", {
            'file_system_sector_size': [ file_system_sector_size, 'file-system-sector-size', [ basestring, 'cifs-filesystem-sector-size' ], False ],
            'is_copy_offload_enabled': [ is_copy_offload_enabled, 'is-copy-offload-enabled', [ bool, 'None' ], False ],
            'is_smb3_enabled': [ is_smb3_enabled, 'is-smb3-enabled', [ bool, 'None' ], False ],
            'shadowcopy_dir_depth': [ shadowcopy_dir_depth, 'shadowcopy-dir-depth', [ int, 'None' ], False ],
            'is_referral_enabled': [ is_referral_enabled, 'is-referral-enabled', [ bool, 'None' ], False ],
            'is_local_users_and_groups_enabled': [ is_local_users_and_groups_enabled, 'is-local-users-and-groups-enabled', [ bool, 'None' ], False ],
            'is_shadowcopy_enabled': [ is_shadowcopy_enabled, 'is-shadowcopy-enabled', [ bool, 'None' ], False ],
            'is_use_junctions_as_reparse_points_enabled': [ is_use_junctions_as_reparse_points_enabled, 'is-use-junctions-as-reparse-points-enabled', [ bool, 'None' ], False ],
            'is_trusted_domain_enum_search_enabled': [ is_trusted_domain_enum_search_enabled, 'is-trusted-domain-enum-search-enabled', [ bool, 'None' ], False ],
            'is_exportpolicy_enabled': [ is_exportpolicy_enabled, 'is-exportpolicy-enabled', [ bool, 'None' ], False ],
            'wins_servers': [ wins_servers, 'wins-servers', [ basestring, 'inet-address' ], True ],
            'is_local_auth_enabled': [ is_local_auth_enabled, 'is-local-auth-enabled', [ bool, 'None' ], False ],
            'is_smb2_enabled': [ is_smb2_enabled, 'is-smb2-enabled', [ bool, 'None' ], False ],
            'max_mpx': [ max_mpx, 'max-mpx', [ int, 'None' ], False ],
            'read_grants_execute': [ read_grants_execute, 'read-grants-execute', [ basestring, 'enable' ], False ],
            'default_unix_group': [ default_unix_group, 'default-unix-group', [ basestring, 'None' ], False ],
            'default_unix_user': [ default_unix_user, 'default-unix-user', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_home_directory_search_path_add(self, path):
        """
        Add a path to the list of paths that will be searched to find a
        CIFS user's home directory.
        
        :param path: The file system path that will be searched for finding a CIFS
                user's home directory.
        """
        return self.request( "cifs-home-directory-search-path-add", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_domain_name_mapping_search_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of trusted domains for name-mapping search.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-domain-name-mapping-search object.
                All cifs-domain-name-mapping-search objects matching this query
                up to 'max-records' will be returned.
        
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
        return self.request( "cifs-domain-name-mapping-search-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsDomainNameMappingSearch, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsDomainNameMappingSearch, 'None' ], False ],
        }, {
            'attributes-list': [ CifsDomainNameMappingSearch, True ],
        } )
    
    def cifs_status(self):
        """
        Returns the running state of the CIFS service.
        """
        return self.request( "cifs-status", {
        }, {
            'status': [ basestring, False ],
        } )
    
    def cifs_symlink_delete(self, unix_path):
        """
        Delete a CIFS symbolic link path mapping.
        
        :param unix_path: This field specifies the UNIX path prefix to be matched for the
                mapping. If the prefix of the target path in the symbolic link
                matches against this field, this entry of symbolic link path
                mapping would be used. The path is a UTF-8 string and supports
                localization. The path must start and end with a forward slash
                ('/'). For example '/usr/local/'.
        """
        return self.request( "cifs-symlink-delete", {
            'unix_path': [ unix_path, 'unix-path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_domain_name_mapping_search_remove(self, trusted_domains=None):
        """
        Remove from the list of trusted domains for name-mapping search
        
        :param trusted_domains: Trusted Domains
        """
        return self.request( "cifs-domain-name-mapping-search-remove", {
            'trusted_domains': [ trusted_domains, 'trusted-domains', [ basestring, 'realm-name' ], True ],
        }, {
        } )
    
    def cifs_setup_ou_list_iter_start(self, domain_name, login_user, login_password):
        """
        Gathers a list of joinable sites and organizational units
        from Active Directory for the login-user specified, which
        is retrieved by using cifs-setup-ou-list-iter-next.
        For more information regarding Active Directory
        organizational units and their use, please reference
        Microsoft's Active Directory documentation.
        
        :param domain_name: The name of the domain that the CIFS server will join.
                Examples: cifsdomain, cifs.domain.com
        
        :param login_user: The name of a domain user that has the ability to add
                the CIFS server to the domain given in domain-name.
                Examples: username (assumes domain-name is the
                user's domain), cifsdomain\username,
                cifs.domain.com\username
        
        :param login_password: The password for login-user.
        """
        return self.request( "cifs-setup-ou-list-iter-start", {
            'domain_name': [ domain_name, 'domain-name', [ basestring, 'None' ], False ],
            'login_user': [ login_user, 'login-user', [ basestring, 'None' ], False ],
            'login_password': [ login_password, 'login-password', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def cifs_start(self):
        """
        Starts the CIFS service, usually after a previous call to
        cifs-stop as the CIFS service starts automatically when
        cifs-setup completes successfully or the system reboots.
        """
        return self.request( "cifs-start", {
        }, {
        } )
    
    def cifs_local_user_rename(self, user_name, new_user_name):
        """
        Rename a local user
        
        :param user_name: The name of the local user
        
        :param new_user_name: New User Name
        """
        return self.request( "cifs-local-user-rename", {
            'user_name': [ user_name, 'user-name', [ basestring, 'cifs-name' ], False ],
            'new_user_name': [ new_user_name, 'new-user-name', [ basestring, 'cifs-name' ], False ],
        }, {
        } )
    
    def cifs_branchcache_create(self, hash_store_path, versions=None, server_key=None, return_record=None, operating_mode=None, hash_store_max_size=None):
        """
        Create and setup the BranchCache service.
        
        :param hash_store_path: Path to the directory where hash files are stored.
        
        :param versions: Versions of the BranchCache protocol that are supported.
        
        :param server_key: BranchCache server key.
        
        :param return_record: If set to true, returns the cifs-branchcache on successful
                creation.
                Default: false
        
        :param operating_mode: The mode in which the BranchCache service will operate.
        
        :param hash_store_max_size: Maximum size the hash store can grow to.
        """
        return self.request( "cifs-branchcache-create", {
            'versions': [ versions, 'versions', [ basestring, 'cifs-bc-version-control' ], True ],
            'server_key': [ server_key, 'server-key', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'hash_store_path': [ hash_store_path, 'hash-store-path', [ basestring, 'None' ], False ],
            'operating_mode': [ operating_mode, 'operating-mode', [ basestring, 'None' ], False ],
            'hash_store_max_size': [ hash_store_max_size, 'hash-store-max-size', [ int, 'size' ], False ],
        }, {
            'result': [ CifsBranchcache, False ],
        } )
    
    def cifs_domain_name_mapping_search_modify(self, trusted_domains):
        """
        Modify the list of trusted domains for name-mapping search
        
        :param trusted_domains: Trusted Domains
        """
        return self.request( "cifs-domain-name-mapping-search-modify", {
            'trusted_domains': [ trusted_domains, 'trusted-domains', [ basestring, 'realm-name' ], True ],
        }, {
        } )
    
    def cifs_nbalias_names_get(self):
        """
        Return the current list of NetBIOS alias names for the filer
        """
        return self.request( "cifs-nbalias-names-get", {
        }, {
            'nbalias-names': [ basestring, True ],
        } )
    
    def cifs_branchcache_flush(self):
        """
        Flush (delete) all the BranchCache hashes that have been
        generated for a Vserver.
        """
        return self.request( "cifs-branchcache-flush", {
        }, {
        } )
    
    def cifs_local_group_modify(self, group_name, description=None):
        """
        Modify a description of a single local group
        
        :param group_name: The name of the local group
        
        :param description: The description of the local group
        """
        return self.request( "cifs-local-group-modify", {
            'group_name': [ group_name, 'group-name', [ basestring, 'cifs-name' ], False ],
            'description': [ description, 'description', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_share_access_control_modify(self, share, user_or_group, permission=None):
        """
        Modify the permissions for a user or group on a defined CIFS
        share.
        
        :param share: The CIFS share for which the permissions are defined.
        
        :param user_or_group: The user or group name for which the permissions are listed.
        
        :param permission: The access rights that the user or group has on the defined CIFS
                share.
                Possible values:
                <ul>
                <li> "no_access"      - No access,
                <li> "read"           - Read,
                <li> "change"         - Change,
                <li> "full_control"   - Full Control
                </ul>
        """
        return self.request( "cifs-share-access-control-modify", {
            'share': [ share, 'share', [ basestring, 'None' ], False ],
            'user_or_group': [ user_or_group, 'user-or-group', [ basestring, 'None' ], False ],
            'permission': [ permission, 'permission', [ basestring, 'cifs-access-perms' ], False ],
        }, {
        } )
    
    def cifs_users_and_groups_load_from_uri(self, file_password, uri, uri_password=None, uri_username=None):
        """
        Import CIFS local users, local groups, and memberships from URI.
        The file available from the URI needs to be generated from the
        Transition Tool which will ensure a proper internal formatting
        acceptable to this API. The import job, referenced by the ID
        returned via the output parameter, can be administered via the
        job interface.
        
        :param file_password: The password for decrypting the file. The password can only
                contain alphanumeric characters
        
        :param uri: The URI destination of the file to download
        
        :param uri_password: The password for the URI provided, if any
        
        :param uri_username: The username for the URI provided, if any
        """
        return self.request( "cifs-users-and-groups-load-from-uri", {
            'file_password': [ file_password, 'file-password', [ basestring, 'None' ], False ],
            'uri_password': [ uri_password, 'uri-password', [ basestring, 'None' ], False ],
            'uri': [ uri, 'uri', [ basestring, 'uri' ], False ],
            'uri_username': [ uri_username, 'uri-username', [ basestring, 'None' ], False ],
        }, {
            'job-identifier': [ int, False ],
        } )
    
    def cifs_share_ace_set(self, share_name, access_rights, user_name=None, is_unixgroup=None, unix_group_name=None):
        """
        Sets the ace to the share for the given user or unix group.
        This API is equivalent to
        "cifs access <share> [-g] <user|group> <rights>" CLI.
        
        :param share_name: CIFS share name. It specifies name of the share to which the
                access rights have to be set. This is a case insensitive field.
                The maximum size of the share name is 256 characters.
        
        :param access_rights: Access rights to be set to the above share and user.
                The format of the rights can be Unix-style combinations of
                r w x - or NT-style "No Access", "Read", "Change", and
                "Full Control"
        
        :param user_name: Name of the user. This API sets the access rights to the
                specified user. This is a case sensitive field. The format of
                the field <user-name>. If specified user does not exist, It
                fails with the reason "Unknown user: <username>".
        
        :param is_unixgroup: This filter is used to tell that the access rights are
                to be set to the unix group. If its value is true, unix-group-name
                needs to be provided. Otherwise API fails with the reason
                "group-name missing". The default value of this is false.
        
        :param unix_group_name: Name of the unix group. This field specifies the unix group to
                which the access rights are to be set. The format of this field
                <unix-group-name>. This is a case sensitive field. If the
                specified group name does not exist, it fails with the reason
                "Unknown Unix group : <groupname>".
        """
        return self.request( "cifs-share-ace-set", {
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'None' ], False ],
            'access_rights': [ access_rights, 'access-rights', [ basestring, 'None' ], False ],
            'is_unixgroup': [ is_unixgroup, 'is-unixgroup', [ bool, 'None' ], False ],
            'unix_group_name': [ unix_group_name, 'unix-group-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_domain_name_mapping_search_add(self, trusted_domains):
        """
        Add to the list of trusted domains for name-mapping search
        
        :param trusted_domains: Trusted Domains
        """
        return self.request( "cifs-domain-name-mapping-search-add", {
            'trusted_domains': [ trusted_domains, 'trusted-domains', [ basestring, 'realm-name' ], True ],
        }, {
        } )
    
    def cifs_server_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of CIFS servers on the cluster and their basic
        configurations.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-server object.
                All cifs-server objects matching this query up to 'max-records'
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
        return self.request( "cifs-server-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsServerConfig, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsServerConfig, 'None' ], False ],
        }, {
            'attributes-list': [ CifsServerConfig, True ],
        } )
    
    def cifs_setup_create_group_file(self):
        """
        Creates a basic /etc/group file.
        Note: This will overwrite an existing /etc/group file.
        See cifs-setup-verify-passwd-and-group for more information.
        """
        return self.request( "cifs-setup-create-group-file", {
        }, {
        } )
    
    def cifs_password_change(self):
        """
        Generate a new password for the CIFS server's machine account and
        change it in the Windows Active Directory domain.
        """
        return self.request( "cifs-password-change", {
        }, {
        } )
    
    def cifs_local_user_membership_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve local users' membership information
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-local-user-membership object.
                All cifs-local-user-membership objects matching this query up to
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
        return self.request( "cifs-local-user-membership-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsLocalUserMembership, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsLocalUserMembership, 'None' ], False ],
        }, {
            'attributes-list': [ CifsLocalUserMembership, True ],
        } )
    
    def cifs_setup_ou_list_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to
        cifs-setup-ou-list-iter-start
        
        :param tag: Tag from a previous cifs-setup-ou-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "cifs-setup-ou-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'cifs-setup-ous': [ basestring, True ],
        } )
    
    def cifs_branchcache_set_key(self, server_secret):
        """
        Sets the server secret for BranchCache.
        
        :param server_secret: A binary string that provides cryptographic data used by the
                BranchCache content server to generate hashes. Content servers
                that are serving the same data and are expected to provide the
                same hash values must use the same key. After changing this
                value, any existing cached content will be identified as stale
                and retrieved from the content server again.
        """
        return self.request( "cifs-branchcache-set-key", {
            'server_secret': [ server_secret, 'server-secret', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_security_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of cifs-security objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-security object.
                All cifs-security objects matching this query up to 'max-records'
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
        return self.request( "cifs-security-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsSecurity, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsSecurity, 'None' ], False ],
        }, {
            'attributes-list': [ CifsSecurity, True ],
        } )
    
    def cifs_start_on_target(self, target_name, target_type):
        """
        Starts the CIFS service on target (volume or aggregate),
        usually after a previous call to
        cifs-stop-on-target-on-target. CIFS service should be already
        enabled. If CIFS service is not running, cifs-start should be
        used.
        
        :param target_name: Name of the object on which CIFS service should be started.
        
        :param target_type: Type of the object on which CIFS service should be started.
                Possible values: "volume", "aggregate".
        """
        return self.request( "cifs-start-on-target", {
            'target_name': [ target_name, 'target-name', [ basestring, 'None' ], False ],
            'target_type': [ target_type, 'target-type', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_password_reset(self, admin_username, admin_password):
        """
        Reset the CIFS server's machine account password in the Windows
        Active Directory domain. This may be required if the password
        stored along with the machine account in the Windows Active
        Directory domain is changed or reset without the Vserver's
        knowledge. This operation requires the credentials for a user
        with permission to reset the password in the organizational unit
        (OU) that the machine account is a member of.
        
        :param admin_username: Username of a user with permission to reset the password in the
                organizational unit (OU) that the machine account is a member of.
                This user is expected to be part of the same Windows Active
                Directory domain as the CIFS server. If the specified username is
                not part of the same domain but part of a domain that has a trust
                relationship with the CIFS server's domain, the username can be
                specified as '<username> @ <FQDN>' where FQDN is the fully
                qualified domain name of the domain of which the user is a
                member.
        
        :param admin_password: Account password for the admin-username.
        """
        return self.request( "cifs-password-reset", {
            'admin_username': [ admin_username, 'admin-username', [ basestring, 'None' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_nbtstat_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the NetBIOS Name Service statistics for Vservers in
        cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                NetBIOS statistics object.
                All NetBIOS statistics objects matching this query up to
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
        return self.request( "cifs-nbtstat-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsNbtstat, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsNbtstat, 'None' ], False ],
        }, {
            'attributes-list': [ CifsNbtstat, True ],
        } )
    
    def cifs_nbalias_names_set(self):
        """
        Provides a list of NetBIOS alias names for the filer.
        The filer replaces the current list of aliases with
        with this list.
        Note that supplying an empty name list causes the filer
        to delete all current entries.
        """
        return self.request( "cifs-nbalias-names-set", {
        }, {
            'nbalias-names': [ basestring, True ],
        } )
    
    def cifs_server_start(self):
        """
        Start a CIFS server on the specified Vserver. The CIFS server
        must already exist. To create a CIFS server, use
        cifs-server-create.
        """
        return self.request( "cifs-server-start", {
        }, {
        } )
    
    def cifs_server_modify(self, domain=None, default_site=None, force_account_overwrite=None, admin_username=None, administrative_status=None, admin_password=None):
        """
        Modify the basic configurations of a CIFS server.
        
        :param domain: The fully qualified domain name of the Windows Active Directory
                this CIFS server belongs to. If this input is not specified, it
                is not modified.
        
        :param default_site: The default site used by LIFs that do not have a site
                membership.
        
        :param force_account_overwrite: If this is set and the domain is being modified, and a machine
                account with the same name as the current Vserver's CIFS server
                name exists in the Active Directory, it will be overwritten and
                reused. The default value for this field is false.
        
        :param admin_username: The username of the account used to add this CIFS server to the
                Active Directory. This part of the credential only needs to be
                supplied if the domain is being modified.
        
        :param administrative_status: CIFS Server Administrative Status.
                Possible values:
                <ul>
                <li> "down" ,
                <li> "up"
                </ul>
        
        :param admin_password: The password for the account used to add this CIFS server to the
                Active Directory. This part of the credential only needs to be
                supplied if the domain is being modified.
        """
        return self.request( "cifs-server-modify", {
            'domain': [ domain, 'domain', [ basestring, 'None' ], False ],
            'default_site': [ default_site, 'default-site', [ basestring, 'None' ], False ],
            'force_account_overwrite': [ force_account_overwrite, 'force-account-overwrite', [ bool, 'None' ], False ],
            'admin_username': [ admin_username, 'admin-username', [ basestring, 'None' ], False ],
            'administrative_status': [ administrative_status, 'administrative-status', [ basestring, 'service-state' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_setup(self, server_name, security_style, auth_type, pdc_ip_address=None, ou_name=None, site_name=None, login_user=None, login_password=None, domain_name=None):
        """
        Configures the filer's CIFS service. The CIFS service will
        start automatically once this call completes successfully.
        
        :param server_name: The resulting CIFS server name.
        
        :param security_style: The security style determines whether or not the CIFS
                service will support multiprotocol access. These styles
                are subject to change in a future release.
                Possible values: ntfs, multiprotocol
        
        :param auth_type: The authentication style that determines the method by
                which clients will be authenticated when connecting to
                this CIFS server. These styles are subject to change
                in a future release.
                Possible values: ad, nt4, workgroup, passwd
                Note: The domain-name, login-user and login-password
                fields are optional unless the auth-type is ad.
        
        :param pdc_ip_address: If this value is defined, CIFS will attempt to
                communicate with the domain controller directly using
                this address.
                Note: This information is only used when the auth-type
                is 'nt4'.
        
        :param ou_name: The distinguished name of the organizational unit that
                the CIFS service will become a member of. This value
                must be one of the cifs-setup-ous retrieved from a
                call to the cifs-setup-container-list-iter APIs.
                By default, the filer will join the 'CN=Computers'
                organizational unit.
                Note: This information is only used when the auth-type
                is 'ad'.
        
        :param site_name: The name of the site that the CIFS service will become
                a member of. This value must be one of the
                cifs-setup-sites retrieved from a call to the
                cifs-setup-container-list-iter APIs. If a default-site
                was returned, it is the recommended choice. Sites will
                be ignored if this value is left blank.
                Note: This information is only used when the auth-type
                is 'ad'.
        
        :param login_user: The name of a domain user that has the ability to add
                the CIFS server to the domain given in domain-name.
                Examples: username (assumes domain-name is the
                user's domain), cifsdomain\username,
                cifs.domain.com\username
        
        :param login_password: The password for login-user.
        
        :param domain_name: The name of the domain that the CIFS server will join.
                This can be the NetBIOS or fully qualified domain name.
                Examples: cifsdomain, cifs.domain.com
        """
        return self.request( "cifs-setup", {
            'pdc_ip_address': [ pdc_ip_address, 'pdc-ip-address', [ basestring, 'ip-address' ], False ],
            'ou_name': [ ou_name, 'ou-name', [ basestring, 'None' ], False ],
            'server_name': [ server_name, 'server-name', [ basestring, 'None' ], False ],
            'site_name': [ site_name, 'site-name', [ basestring, 'None' ], False ],
            'login_user': [ login_user, 'login-user', [ basestring, 'None' ], False ],
            'login_password': [ login_password, 'login-password', [ basestring, 'None' ], False ],
            'security_style': [ security_style, 'security-style', [ basestring, 'None' ], False ],
            'auth_type': [ auth_type, 'auth-type', [ basestring, 'None' ], False ],
            'domain_name': [ domain_name, 'domain-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_share_list_iter_start(self, share_name=None):
        """
        Gives information about one or more shares, the results of
        which are retrieved by using cifs-share-list-iter-next.
        
        :param share_name: Cifs share name. If share-name is specified, only information
                about that share is returned. If share-name is not specified,
                then information about all the shares is returned.
                If the name contains the wildcard characters * or ?,
                then all the shares matching the specified name are listed.
        """
        return self.request( "cifs-share-list-iter-start", {
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def cifs_shadowcopy_keep_snapshot(self, storage_shadow_copy_set_id):
        """
        Request the storage system to keep the snapshots taken as part of
        the shadow copy set creation.
        
        :param storage_shadow_copy_set_id: The universally-unique identifier of the storage's shadow copy
                set.
        """
        return self.request( "cifs-shadowcopy-keep-snapshot", {
            'storage_shadow_copy_set_id': [ storage_shadow_copy_set_id, 'storage-shadow-copy-set-id', [ basestring, 'uuid' ], False ],
        }, {
        } )
    
    def cifs_share_acl_list_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to
        cifs-share-acl-list-iter-start.
        
        :param tag: Tag from the previous cifs-share-acl-list-iter-start
        
        :param maximum: The maximum number of entries to retrieve.
                Range:[0..2^32-1]
        """
        return self.request( "cifs-share-acl-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'cifs-share-acls': [ CifsShareAclInfo, True ],
        } )
    
    def cifs_top_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous cifs-top-iter-start.
        """
        return self.request( "cifs-top-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def cifs_options_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of cifs-options objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-options object.
                All cifs-options objects matching this query up to 'max-records'
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
        return self.request( "cifs-options-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsOptions, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsOptions, 'None' ], False ],
        }, {
            'attributes-list': [ CifsOptions, True ],
        } )
    
    def cifs_local_group_members_remove_members(self, group_name, member_names):
        """
        Remove local users or Active Directory users or groups from a
        local group
        
        :param group_name: The name of the local group
        
        :param member_names: Names of Users or Active Directory Groups to be Removed
        """
        return self.request( "cifs-local-group-members-remove-members", {
            'group_name': [ group_name, 'group-name', [ basestring, 'cifs-name' ], False ],
            'member_names': [ member_names, 'member-names', [ basestring, 'cifs-name' ], True ],
        }, {
        } )
    
    def cifs_share_access_control_create(self, share, user_or_group, permission, return_record=None):
        """
        Add permissions for a user or group for a defined CIFS share.
        
        :param share: The CIFS share for which the permissions are defined.
        
        :param user_or_group: The user or group name for which the permissions are listed.
        
        :param permission: The access rights that the user or group has on the defined CIFS
                share.
                Possible values:
                <ul>
                <li> "no_access"      - No access,
                <li> "read"           - Read,
                <li> "change"         - Change,
                <li> "full_control"   - Full Control
                </ul>
        
        :param return_record: If set to true, returns the cifs-share-access-control on
                successful creation.
                Default: false
        """
        return self.request( "cifs-share-access-control-create", {
            'share': [ share, 'share', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'user_or_group': [ user_or_group, 'user-or-group', [ basestring, 'None' ], False ],
            'permission': [ permission, 'permission', [ basestring, 'cifs-access-perms' ], False ],
        }, {
            'result': [ CifsShareAccessControl, False ],
        } )
    
    def cifs_local_group_create(self, group_name, description=None, return_record=None):
        """
        Create a single local group
        
        :param group_name: The name of the local group
        
        :param description: The description of the local group
        
        :param return_record: If set to true, returns the cifs-local-group on successful
                creation.
                Default: false
        """
        return self.request( "cifs-local-group-create", {
            'group_name': [ group_name, 'group-name', [ basestring, 'cifs-name' ], False ],
            'description': [ description, 'description', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ CifsLocalGroup, False ],
        } )
    
    def cifs_symlink_create(self, unix_path, share_name, cifs_path, cifs_server=None, locality=None, return_record=None):
        """
        Create a new CIFS symbolic link path mapping from a UNIX symlink
        to a target CIFS path. This symbolic link path mapping will be
        effective on symbolic links that have a prefix match with the
        value of 'unix-path'. e.g.: if the value of 'unix-path' is
        '/usr/local/' and there exists a symbolic link on the file system
        at '/home/user/link' which points to '/usr/local/share/dest'. If
        a CIFS client accesses the symbolic link 'link', this entry of
        path mapping would have a prefix match '/usr/local/'. The CIFS
        client would be redirected to the location pointed to by this
        path mapping's 'cifs-server', 'share-name' and 'cifs-path'
        fields.
        
        :param unix_path: This field specifies the UNIX path prefix to be matched for the
                mapping. If the prefix of the target path in the symbolic link
                matches against this field, this entry of symbolic link path
                mapping would be used. The path is a UTF-8 string and supports
                localization. The path must start and end with a forward slash
                ('/'). For example '/usr/local/'.
        
        :param share_name: This field specifies the CIFS share name on the destination CIFS
                server to which the symbolic link is mapped. This is a UTF-8
                string and supports localization.
        
        :param cifs_path: This field specifies the CIFS path on the destination to which
                the symbolic link maps. The final path is generated by
                concatenating the CIFS server name, the share name, the cifs-path
                and the remaining path in the symbolic link left after the prefix
                match. This value is specified by using a UNIX-style path name.
                The trailing forward slash is required for the full path name to
                be properly interpreted. This is a UTF-8 string and supports
                localization.
        
        :param cifs_server: This field specifies the destination CIFS server name for the
                mapping to which the symbolic link is mapped. The default is the
                local CIFS server. The field needs to be specified if the
                locality of the symbolic link is 'widelink'. This can be either a
                DNS name, NetBIOS name or an IP address. If a DNS name or a
                NetBIOS name are specified, the CIFS client configuration should
                be such that it is capable of resolving the CIFS server name to
                the correct IP address.
        
        :param locality: This field specifies whether the CIFS symbolic link is a local
                link or wide link. A local symbolic link maps to the local CIFS
                share, whereas a wide symbolic link maps to any CIFS share on the
                network. If the CIFS server matches the VServer's NetBIOS name
                then the default value is local otherwise widelink.
                Possible values:
                <ul>
                <li> "local"     - Share On This VServer,
                <li> "widelink"  - Share On Another CIFS Server
                </ul>
        
        :param return_record: If set to true, returns the cifs-symlink on successful creation.
                Default: false
        """
        return self.request( "cifs-symlink-create", {
            'unix_path': [ unix_path, 'unix-path', [ basestring, 'None' ], False ],
            'cifs_server': [ cifs_server, 'cifs-server', [ basestring, 'None' ], False ],
            'locality': [ locality, 'locality', [ basestring, 'cifs-symlink-locality' ], False ],
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
            'cifs_path': [ cifs_path, 'cifs-path', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
        }, {
            'result': [ CifsSymlink, False ],
        } )
    
    def cifs_branchcache_hash_stat(self, include_filesize_stats=None, include_flush_stats=None):
        """
        Display the CIFS BranchCache statistics
        
        :param include_filesize_stats: If true, it shows BranchCache hash stats of file sizes for which
                hashes were requested for. File sizes are <10K, 11K-100K, 101K-250K,
                251K-1M, 1.1M-10M, 11M-100M, >100M. The default value of this
                is false.
        
        :param include_flush_stats: If true, returns BranchCache hash stats like how many hashes were
                flushed in multiples of BranchCache hash timeout duration. The
                default value of this field is false.
        """
        return self.request( "cifs-branchcache-hash-stat", {
            'include_filesize_stats': [ include_filesize_stats, 'include-filesize-stats', [ bool, 'None' ], False ],
            'include_flush_stats': [ include_flush_stats, 'include-flush-stats', [ bool, 'None' ], False ],
        }, {
            'hashes-flashed-post-fourth-timeout': [ int, False ],
            'hashes-flashed-post-first-timeout': [ int, False ],
            'filesize-range-10kb-to-100kb': [ int, False ],
            'hashes-flashed-post-third-timeout': [ int, False ],
            'hashes-flashed-post-second-timeout': [ int, False ],
            'hashes-flashed-post-fifth-timeout': [ int, False ],
            'filesize-range-1mb-to-10mb': [ int, False ],
            'filesize-more-than-100mb': [ int, False ],
            'filesize-range-0kb-to-10kb': [ int, False ],
            'filesize-range-100kb-to-250kb': [ int, False ],
            'filesize-range-250kb-to-1mb': [ int, False ],
            'filesize-range-10mb-to-100mb': [ int, False ],
        } )
    
    def cifs_home_directory_search_path_remove(self, path):
        """
        Remove a home directory search path.
        
        :param path: The file system path that will be searched for finding a CIFS
                user's home directory.
        """
        return self.request( "cifs-home-directory-search-path-remove", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_home_directory_search_path_delete(self, path):
        """
        Delete a home directory search path. This API is deprecated in
        Data ONTAP 8.2 and later but retained for backwards
        compatibility. Use cifs-home-directory-search-path-remove instead
        of cifs-home-directory-search-path-delete.
        
        :param path: The file system path that will be searched for finding a CIFS
                user's home directory.
        """
        return self.request( "cifs-home-directory-search-path-delete", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_share_add(self, share_name, path, comment=None, is_symlink_strict_security=None, forcegroup=None, dir_umask=None, is_namespace_caching_allowed=None, is_vscanread=None, umask=None, is_browse=None, is_vscan=None, caching=None, maxusers=None, is_widelink=None, is_access_based_enum=None, file_umask=None):
        """
        Creates a new CIFS share rooted at the specified path.
        
        :param share_name: Name of the share to be added. The name cannot exceed 12
                characters for DOS-style shares and 256 characters for others.
        
        :param path: Full path name of the directory on the filer corresponding to
                the root of the new share.
        
        :param comment: If specified, gives description of the new share. CIFS clients
                see this description when browsing the filer's shares.
                If not specified, the description is blank.
        
        :param is_symlink_strict_security: If true or not specified, strict symlink security is enabled.
                If false, allows clients to follow symbolic links to
                destinations on this filer but outside of the current share.
                It is not checked if the client is authenticated to the
                symbolic link's	destination.
        
        :param forcegroup: If specified, provides name of the group to which files to be
                created in the share belong. The groupname is the name of a
                group in the UNIX group database.
                If it is an empty string or else not specified, then files to be
                created in the share do not belong to a particular UNIX group.
                That is, each file belongs to the same group as the owner of the
                file.
        
        :param dir_umask: If specified, sets file mode creation mask for a share in qtrees
                with Unix or mixed security styles. The mask restricts the
                initial permissions setting of a newly created directory. For
                directories, this mask overrides one set with "umask".
        
        :param is_namespace_caching_allowed: If true, namespace caching is enabled on the share.
                If namespace caching is enabled on a share, clients are allowed
                to cache the directory enumeration results for better performance.
        
        :param is_vscanread: If true or not specified, virus scan is done when clients open
                files on this share for read access, else no virus scan is done
                for read access on this share.
        
        :param umask: If specified, sets file mode creation mask for a share in qtrees
                with Unix or mixed security styles. The mask restricts the
                initial permissions setting of a newly created file or directory.
                If not specified, the file mode creation mask of the share is 0.
                This field is ignored when both dir-umask and file-umask are present.
        
        :param is_browse: If true or not specified, shares are visible to browsing clients
                and can be enumerated (e.g. "net view", SrvMgr, AD).
        
        :param is_vscan: If true or not specified, virus scan is done when clients open
                files on this share, else no virus scan is done.
        
        :param caching: If specified, the following is done based on the value of the
                string:
                "no_caching": disallow Windows clients from caching any files on
                this share. This is the default value.
                "auto_document_caching": allow Windows clients to cache user
                documents on this share.
                "auto_program_caching": allow Windows clients to cache programs
                on this share. The actual caching
                behavior depends on the Windows client.
                "branchcache":	clients connecting to this share can make requests
                using BranchCache technology that allows them to
                cache the content in an attempt to reduce WAN
                utilization from a remote office.
        
        :param maxusers: If specified, gives the maximum number of simultaneous
                connections to the new share. It must be a positive number.
                If not specified, the filer does not impose a limit on the
                number of connections to the share.
        
        :param is_widelink: If true, allows clients to follow absolute symbolic links
                outside of this share, subject to NT security. This feature
                requires an entry in the /etc/symlink.translations file and it
                requires that the client supports  Microsoft's Distributed File
                System (DFS).
                If false or not specified, widelinks in the share are disabled.
        
        :param is_access_based_enum: If true Access Based Enumeration (ABE) is enabled, else
                it is disabled. ABE filtered shared folders are
                visible to a user based on that individual user's
                access rights, preventing the display of folders or
                other shared resources that the user does not have
                rights to access.
        
        :param file_umask: If specified, sets file mode creation mask for a share in qtrees
                with Unix or mixed security styles. The mask restricts the
                initial permissions setting of a newly created file. For files,
                this mask overrides one set with "umask".
        """
        return self.request( "cifs-share-add", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'is_symlink_strict_security': [ is_symlink_strict_security, 'is-symlink-strict-security', [ bool, 'None' ], False ],
            'forcegroup': [ forcegroup, 'forcegroup', [ basestring, 'None' ], False ],
            'dir_umask': [ dir_umask, 'dir-umask', [ int, 'None' ], False ],
            'is_namespace_caching_allowed': [ is_namespace_caching_allowed, 'is-namespace-caching-allowed', [ bool, 'None' ], False ],
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
            'is_vscanread': [ is_vscanread, 'is-vscanread', [ bool, 'None' ], False ],
            'umask': [ umask, 'umask', [ int, 'None' ], False ],
            'is_browse': [ is_browse, 'is-browse', [ bool, 'None' ], False ],
            'is_vscan': [ is_vscan, 'is-vscan', [ bool, 'None' ], False ],
            'caching': [ caching, 'caching', [ basestring, 'None' ], False ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'maxusers': [ maxusers, 'maxusers', [ int, 'None' ], False ],
            'is_widelink': [ is_widelink, 'is-widelink', [ bool, 'None' ], False ],
            'is_access_based_enum': [ is_access_based_enum, 'is-access-based-enum', [ bool, 'None' ], False ],
            'file_umask': [ file_umask, 'file-umask', [ int, 'None' ], False ],
        }, {
        } )
    
    def cifs_local_user_set_password(self, user_password, user_name):
        """
        Set password for a local user
        
        :param user_password: The Password for a Local User
        
        :param user_name: The name of the local user
        """
        return self.request( "cifs-local-user-set-password", {
            'user_password': [ user_password, 'user-password', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'cifs-name' ], False ],
        }, {
        } )
    
    def cifs_share_acl_list_iter_end(self, tag):
        """
        Terminates a list iteration and cleans up any saved info.
        
        :param tag: Tag from the previous cifs-share-acl-list-iter-start
        """
        return self.request( "cifs-share-acl-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def cifs_local_user_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of local users
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-local-user object.
                All cifs-local-user objects matching this query up to
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
        return self.request( "cifs-local-user-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsLocalUser, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsLocalUser, 'None' ], False ],
        }, {
            'attributes-list': [ CifsLocalUser, True ],
        } )
    
    def cifs_domain_preferred_dc_remove(self, domain, preferred_dc=None):
        """
        Remove from a list of preferred domain controllers
        
        :param domain: The fully qualified domain name of the Active Directory domain to
                which the domain controllers in the list belong.
        
        :param preferred_dc: Preferred Domain Controllers
        """
        return self.request( "cifs-domain-preferred-dc-remove", {
            'domain': [ domain, 'domain', [ basestring, 'None' ], False ],
            'preferred_dc': [ preferred_dc, 'preferred-dc', [ basestring, 'None' ], True ],
        }, {
        } )
    
    def cifs_server_delete(self, admin_username=None, admin_password=None):
        """
        Delete a CIFS server. If the admin-username and admin-password
        are not specified, the CIFS server's machine account will not be
        deleted from the Windows Active Directory domain. The deletion of
        the CIFS server will also delete the CIFS shares associated with
        it.
        
        :param admin_username: A user account name that has sufficient privileges in the Windows
                Active Directory domain to delete the CIFS server's machine
                account.
        
        :param admin_password: Account password for the admin-username.
        """
        return self.request( "cifs-server-delete", {
            'admin_username': [ admin_username, 'admin-username', [ basestring, 'None' ], False ],
            'admin_password': [ admin_password, 'admin-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_local_group_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of local groups
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-local-group object.
                All cifs-local-group objects matching this query up to
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
        return self.request( "cifs-local-group-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsLocalGroup, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsLocalGroup, 'None' ], False ],
        }, {
            'attributes-list': [ CifsLocalGroup, True ],
        } )
    
    def cifs_home_directory_search_path_reorder(self, path, to_position):
        """
        Change the position of this path in the list of paths that will
        be searched to find a CIFS user's home directory.
        
        :param path: The file system path that will be searched for finding a CIFS
                user's home directory.
        
        :param to_position: The target position this entry should be moved to, in the list of
                CIFS home directory search paths.
        """
        return self.request( "cifs-home-directory-search-path-reorder", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'to_position': [ to_position, 'to-position', [ int, 'None' ], False ],
        }, {
        } )
    
    def cifs_setup_site_list_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous cifs-setup-site-list-iter-start.
        """
        return self.request( "cifs-setup-site-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def cifs_share_change(self, share_name, comment=None, is_symlink_strict_security=None, forcegroup=None, dir_umask=None, is_namespace_caching_allowed=None, is_vscanread=None, umask=None, is_browse=None, is_vscan=None, caching=None, maxusers=None, is_widelink=None, is_access_based_enum=None, file_umask=None):
        """
        Changes settings of one or more CIFS shares at any time,
        even if the shares are in use.
        
        :param share_name: If fully specified, it's the name of the existing share to be
                changed. If the name contains the wildcard characters * or ?,
                then all the shares matching the specified name are to be
                changed.
        
        :param comment: If specified, changes description of the share. CIFS clients
                see this description when browsing the filer's shares.
                Specifying an empty string clears the previous description.
        
        :param is_symlink_strict_security: If true, strict symlink security is enabled.
                If false, allows clients to follow symbolic links to
                destinations on this filer but outside of the current share.
                It is not checked if the client is authenticated to the
                symbolic link's	destination.
        
        :param forcegroup: If specified, changes name of the group to which files to be
                created in the share belong. The groupname is the name of a
                group in the UNIX group database. If the string is empty, files
                to be created in the share do not belong to a particular UNIX
                group. That is, each file belongs to the same group as the owner
                of the file.
        
        :param dir_umask: If specified, changes file mode creation mask for a share in
                qtrees with Unix or mixed security styles. The mask restricts the
                initial permissions setting of a newly created directory. For
                directories, this mask overrides one set with "umask".
                Specifying an empty string resets (removes) this dir-umask.
        
        :param is_namespace_caching_allowed: If true, namespace caching is enabled on the share.
                If false, namespace caching is disabled on the share.
                If namespace caching is enabled on a share, clients are allowed
                to cache the directory enumeration results for better performance.
        
        :param is_vscanread: If true, virus scan is done when clients open files on this
                share for read access, else virus scan is not done for read
                access.
        
        :param umask: If specified, changes file mode creation mask for a share in
                qtrees with Unix or mixed security styles. The mask restricts
                the initial permissions setting of a newly created file or
                directory. Specifying a zero value resets (removes) the file
                mode creation mask.  This field is ignored when both dir-umask
                and file-umask are present.
        
        :param is_browse: If true or undefined, share is visible to browsers and can be
                enumerated.
        
        :param is_vscan: If true, virus scan is done when clients open files on this
                share, else virus scan is not done.
        
        :param caching: If specified, the following is done based on the value of the
                string:
                "no_caching": disallow Windows clients from caching any files on
                this share. This is the default value.
                "auto_document_caching": allow Windows clients to cache user
                documents on this share.
                "auto_program_caching": allow Windows clients to cache programs
                on this share. The actual caching
                behavior depends on the Windows client.
                "manual_caching": allow users on Windows clients to manually
                select files to be cached.
                "branchcache":	clients connecting to this share can make requests
                using BranchCache technology that allows them to
                cache the content in an attempt to reduce WAN
                utilization from a remote office.
        
        :param maxusers: If specified, changes the maximum number of simultaneous
                connections to the new share. It must be a positive number or
                else zero, in which case no limit is imposed on the number of
                connections to the share.
        
        :param is_widelink: If true, allows clients to follow absolute symbolic links
                outside of this share, subject to NT security. This feature
                requires an entry in the /etc/symlink.translations file and it
                requires that the client supports  Microsoft's Distributed File
                System (DFS). If false, widelinks in the share are disabled.
        
        :param is_access_based_enum: If true Access Based Enumeration (ABE) is enabled, if
                false it is disabled. ABE filtered shared folders are
                visible to a user based on that individual user's
                access rights, preventing the display of folders or
                other shared resources that the user does not have
                rights to access.
        
        :param file_umask: If specified, changes file mode creation mask for a share in
                qtrees with Unix or mixed security styles. The mask restricts the
                initial permissions setting of a newly created file. For
                files, this mask overrides one set with "umask".
                Specifying an empty string resets (removes) this file-umask.
        """
        return self.request( "cifs-share-change", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'is_symlink_strict_security': [ is_symlink_strict_security, 'is-symlink-strict-security', [ bool, 'None' ], False ],
            'forcegroup': [ forcegroup, 'forcegroup', [ basestring, 'None' ], False ],
            'dir_umask': [ dir_umask, 'dir-umask', [ int, 'None' ], False ],
            'is_namespace_caching_allowed': [ is_namespace_caching_allowed, 'is-namespace-caching-allowed', [ bool, 'None' ], False ],
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
            'is_vscanread': [ is_vscanread, 'is-vscanread', [ bool, 'None' ], False ],
            'umask': [ umask, 'umask', [ int, 'None' ], False ],
            'is_browse': [ is_browse, 'is-browse', [ bool, 'None' ], False ],
            'is_vscan': [ is_vscan, 'is-vscan', [ bool, 'None' ], False ],
            'caching': [ caching, 'caching', [ basestring, 'None' ], False ],
            'maxusers': [ maxusers, 'maxusers', [ int, 'None' ], False ],
            'is_widelink': [ is_widelink, 'is-widelink', [ bool, 'None' ], False ],
            'is_access_based_enum': [ is_access_based_enum, 'is-access-based-enum', [ bool, 'None' ], False ],
            'file_umask': [ file_umask, 'file-umask', [ int, 'None' ], False ],
        }, {
        } )
    
    def cifs_domain_discovered_servers_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of servers discovered by the cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-domain-discovered-servers object.
                All cifs-domain-discovered-servers objects matching this query up
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
        return self.request( "cifs-domain-discovered-servers-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsDomainDiscoveredServers, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsDomainDiscoveredServers, 'None' ], False ],
        }, {
            'attributes-list': [ CifsDomainDiscoveredServers, True ],
        } )
    
    def cifs_users_and_groups_get_import_status(self, uri_password=None, uri=None, uri_username=None):
        """
        Obtains the status of the previous import operation done in
        cifs-users-and-groups-load-from-uri and if some entries were
        ignored places the status at the specified URI
        
        :param uri_password: The password for the URI provided, if any
        
        :param uri: The URI destination to upload the file
        
        :param uri_username: The username for the URI provided, if any
        """
        return self.request( "cifs-users-and-groups-get-import-status", {
            'uri_password': [ uri_password, 'uri-password', [ basestring, 'None' ], False ],
            'uri': [ uri, 'uri', [ basestring, 'uri' ], False ],
            'uri_username': [ uri_username, 'uri-username', [ basestring, 'None' ], False ],
        }, {
            'error-line-num': [ int, False ],
            'operation-status': [ basestring, False ],
            'num-elements-ok': [ int, False ],
            'error-catalog-num': [ int, False ],
            'error-code': [ int, False ],
            'detailed-operation-status': [ basestring, False ],
            'num-elements-ignored': [ int, False ],
            'job-identifier': [ int, False ],
        } )
    
    def cifs_share_access_control_delete(self, share, user_or_group):
        """
        Remove permissions for a user or group on a defined CIFS share.
        
        :param share: The CIFS share for which the permissions are defined.
        
        :param user_or_group: The user or group name for which the permissions are listed.
        """
        return self.request( "cifs-share-access-control-delete", {
            'share': [ share, 'share', [ basestring, 'None' ], False ],
            'user_or_group': [ user_or_group, 'user-or-group', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_branchcache_hash(self, path, recurse=None):
        """
        Force the generation of BranchCache hashes for a file or path.
        
        :param path: Path of File or Directory to Hash
        
        :param recurse: If set to 'true', hashes will be recursively computed for all
                files in the directory
        """
        return self.request( "cifs-branchcache-hash", {
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'recurse': [ recurse, 'recurse', [ bool, 'None' ], False ],
        }, {
        } )
    
    def cifs_privilege_reset_privilege(self, user_or_group_name):
        """
        Reset privileges for a local or Active Directory user or group
        
        :param user_or_group_name: User or Group Name
        """
        return self.request( "cifs-privilege-reset-privilege", {
            'user_or_group_name': [ user_or_group_name, 'user-or-group-name', [ basestring, 'cifs-name' ], False ],
        }, {
        } )
    
    def cifs_share_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Gives information about one or more CIFS shares.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-share object.
                All cifs-share objects matching this query up to 'max-records'
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
        return self.request( "cifs-share-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsShare, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsShare, 'None' ], False ],
        }, {
            'attributes-list': [ CifsShare, True ],
        } )
    
    def cifs_local_group_members_add_members(self, group_name, member_names):
        """
        Add local users or Active Directory users or groups to a local
        group
        
        :param group_name: The name of the local group
        
        :param member_names: Names of Users or Active Directory Groups to be Added
        """
        return self.request( "cifs-local-group-members-add-members", {
            'group_name': [ group_name, 'group-name', [ basestring, 'cifs-name' ], False ],
            'member_names': [ member_names, 'member-names', [ basestring, 'cifs-name' ], True ],
        }, {
        } )
    
    def cifs_share_list_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous cifs-share-list-iter-start.
        """
        return self.request( "cifs-share-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def cifs_security_modify(self, kerberos_renew_age=None, use_start_tls_for_ad_ldap=None, kerberos_ticket_age=None, is_signing_required=None, is_password_complexity_required=None, kerberos_clock_skew=None):
        """
        Modify the attributes of cifs-security object.
        
        :param kerberos_renew_age: This option determines the maximum amount of time in days for
                which a ticket can be renewed.
        
        :param use_start_tls_for_ad_ldap: This option determines whether to use start-tls for AD LDAP
                connections. By default this option is false.
        
        :param kerberos_ticket_age: This option determines the maximum amount of time in hours that a
                user's ticket may be used for the purpose of Kerberos
                authentication.
        
        :param is_signing_required: This option determines whether signing is required for incoming
                CIFS traffic. By default this option is false.
        
        :param is_password_complexity_required: This option determines whether password complexity is required
                for local users. By default this option is true.
        
        :param kerberos_clock_skew: The clock skew in minutes is the tolerance for accepting tickets
                with time stamps that do not exactly match the host's system
                clock.
        """
        return self.request( "cifs-security-modify", {
            'kerberos_renew_age': [ kerberos_renew_age, 'kerberos-renew-age', [ int, 'None' ], False ],
            'use_start_tls_for_ad_ldap': [ use_start_tls_for_ad_ldap, 'use-start-tls-for-ad-ldap', [ bool, 'None' ], False ],
            'kerberos_ticket_age': [ kerberos_ticket_age, 'kerberos-ticket-age', [ int, 'None' ], False ],
            'is_signing_required': [ is_signing_required, 'is-signing-required', [ bool, 'None' ], False ],
            'is_password_complexity_required': [ is_password_complexity_required, 'is-password-complexity-required', [ bool, 'None' ], False ],
            'kerberos_clock_skew': [ kerberos_clock_skew, 'kerberos-clock-skew', [ int, 'None' ], False ],
        }, {
        } )
    
    def cifs_share_list_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to
        cifs-share-list-iter-start
        
        :param tag: Tag from a previous cifs-share-list-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "cifs-share-list-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'cifs-shares': [ CifsShareInfo, True ],
        } )
    
    def cifs_setup_site_list_iter_start(self, domain_name, login_user, login_password):
        """
        Gathers a list of joinable sites and organizational units
        from Active Directory for the login-user specified, which
        is retrieved by using cifs-setup-site-list-iter-next.
        For more information regarding Active Directory sites and
        their use, please reference Microsoft's Active Directory
        documentation.
        
        :param domain_name: The name of the domain that the CIFS server will join.
                Examples: cifsdomain, cifs.domain.com
        
        :param login_user: The name of a domain user that has the ability to add
                the CIFS server to the domain given in domain-name.
                Examples: username (assumes domain-name is the
                user's domain), cifsdomain\username,
                cifs.domain.com\username
        
        :param login_password: The password for login-user.
        """
        return self.request( "cifs-setup-site-list-iter-start", {
            'domain_name': [ domain_name, 'domain-name', [ basestring, 'None' ], False ],
            'login_user': [ login_user, 'login-user', [ basestring, 'None' ], False ],
            'login_password': [ login_password, 'login-password', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
            'default-site': [ basestring, False ],
        } )
    
    def cifs_stop(self, workstation=None):
        """
        Stops the CIFS service for all users or a particular
        workstation, if specified. Appropriate warning should be
        given to connected clients before calling this API, as it
        will immediately terminate those sessions regardless of
        their current state. See the cifs-sessions API for the
        list of clients that are currently connected.
        
        :param workstation: The name or IP address of a workstation that will be
                disconnected from the CIFS service. Note that the CIFS
                service does not stop if this value is specified, it
                simply disconnects related sessions.
        """
        return self.request( "cifs-stop", {
            'workstation': [ workstation, 'workstation', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_share_delete(self, share_name):
        """
        Deletes the specified CIFS share.
        
        :param share_name: The name of the CIFS share. The CIFS share name is a UTF-8 string
                with the following characters being illegal: control characters
                from 0x00 to 0x1F, both inclusive, 0x22 (double quotes) and the
                characters \/[]:|<>+=;,?"*
        """
        return self.request( "cifs-share-delete", {
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_local_user_modify(self, user_name, full_name=None, is_account_disabled=None, description=None):
        """
        Modify a single local user
        
        :param user_name: The name of the local user
        
        :param full_name: Full name of the local user
        
        :param is_account_disabled: The user account is disabled
        
        :param description: The description of the local user
        """
        return self.request( "cifs-local-user-modify", {
            'full_name': [ full_name, 'full-name', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'cifs-name' ], False ],
            'is_account_disabled': [ is_account_disabled, 'is-account-disabled', [ bool, 'None' ], False ],
            'description': [ description, 'description', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_branchcache_get(self, desired_attributes=None):
        """
        Retrieve information about the BranchCache service.
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        """
        return self.request( "cifs-branchcache-get", {
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsBranchcache, 'None' ], False ],
        }, {
            'attributes': [ CifsBranchcache, False ],
        } )
    
    def cifs_share_access_control_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of permissions on defined CIFS shares.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-share-access-control object.
                All cifs-share-access-control objects matching this query up to
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
        return self.request( "cifs-share-access-control-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsShareAccessControl, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsShareAccessControl, 'None' ], False ],
        }, {
            'attributes-list': [ CifsShareAccessControl, True ],
        } )
    
    def cifs_local_group_delete(self, group_name):
        """
        Delete a single local group
        
        :param group_name: The name of the local group
        """
        return self.request( "cifs-local-group-delete", {
            'group_name': [ group_name, 'group-name', [ basestring, 'cifs-name' ], False ],
        }, {
        } )
    
    def cifs_top_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to cifs-top-iter-start.
        
        :param tag: Tag from a previous cifs-top-iter-start.
        
        :param maximum: The maximum number of entries to retrieve.
        """
        return self.request( "cifs-top-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'cifs-top': [ CifsTopInfo, True ],
        } )
    
    def cifs_session_list_iter_start(self, host=None, protocol=None, user=None):
        """
        Gives information on current CIFS activity. Without arguments,
        it returns a summary of information about the filer and lists
        the users who are connected to the filer.
        
        :param host: IP address/machine name of the user's client machine.
        
        :param protocol: Filters the information on the basis of protocol version
                specified. When 'smb' is specified as the argument, this
                API retrieves information about only SMB 1.0 sessions.
                When 'smb2' is specified as the argument, this API retrieves
                information about only SMB 2.0 sessions. If this option is
                not specified, then information about both SMB 1.0 and SMB 2.0
                sessions is retrieved.
        
        :param user: User name. If user is specified , this api returns information
                about the specified user, along with the names and access
                level of files that the user has opened. This api returns
                information about all the users, if the user is specified
                as '*' or is not specified.
        """
        return self.request( "cifs-session-list-iter-start", {
            'host': [ host, 'host', [ basestring, 'None' ], False ],
            'protocol': [ protocol, 'protocol', [ basestring, 'None' ], False ],
            'user': [ user, 'user', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def cifs_share_acl_list_iter_start(self, share_name=None):
        """
        Gives information about one or more shares acl.
        
        :param share_name: Cifs share name. If share-name is specified, only information
                about that share is returned. If share-name is not specified,
                then information about all the shares is returned.
                If the name contains the wildcard characters * or ?,
                then all the shares matching the specified pattern are listed.
        """
        return self.request( "cifs-share-acl-list-iter-start", {
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def cifs_home_directory_search_path_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Iterate over a list of cifs-home-directory-search-path objects.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-home-directory-search-path object.
                All cifs-home-directory-search-path objects matching this query
                up to 'max-records' will be returned.
        
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
        return self.request( "cifs-home-directory-search-path-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsHomeDirectorySearchPath, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsHomeDirectorySearchPath, 'None' ], False ],
        }, {
            'attributes-list': [ CifsHomeDirectorySearchPath, True ],
        } )
    
    def cifs_local_user_create(self, user_password, user_name, full_name=None, is_account_disabled=None, description=None):
        """
        Configure and create a local user, associated with a Vserver
        
        :param user_password: The password for the local user
        
        :param user_name: The name of the local user
        
        :param full_name: The full name of the local user
        
        :param is_account_disabled: The local user account is disabled
        
        :param description: The description of the local user
        """
        return self.request( "cifs-local-user-create", {
            'full_name': [ full_name, 'full-name', [ basestring, 'None' ], False ],
            'user_password': [ user_password, 'user-password', [ basestring, 'None' ], False ],
            'user_name': [ user_name, 'user-name', [ basestring, 'cifs-name' ], False ],
            'is_account_disabled': [ is_account_disabled, 'is-account-disabled', [ bool, 'None' ], False ],
            'description': [ description, 'description', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_setup_verify_passwd_and_group(self):
        """
        Determines whether or not the /etc/passwd and /etc/group
        files exist, which would be used in the event that the
        configured CIFS authentication method fails.
        """
        return self.request( "cifs-setup-verify-passwd-and-group", {
        }, {
            'group-file-exists': [ bool, False ],
            'required': [ bool, False ],
            'passwd-file-exists': [ bool, False ],
        } )
    
    def cifs_shadowcopy_add_files(self, files, client_shadow_copy_id):
        """
        Provide the storage system with the list of files to shadow copy
        in a particular share.
        
        :param files: The list of files to shadow copy in the share. The path is in
                UTF8 and uses forward slash as directory separator. The path is
                relative to the root of the share.
        
        :param client_shadow_copy_id: The universally-unique identifier of the client's shadow copy.
        """
        return self.request( "cifs-shadowcopy-add-files", {
            'files': [ files, 'files', [ basestring, 'None' ], True ],
            'client_shadow_copy_id': [ client_shadow_copy_id, 'client-shadow-copy-id', [ basestring, 'uuid' ], False ],
        }, {
            'storage-shadow-copy-id': [ basestring, False ],
            'storage-shadow-copy-set-id': [ basestring, False ],
        } )
    
    def cifs_privilege_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of local groups
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-privilege object.
                All cifs-privilege objects matching this query up to
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
        return self.request( "cifs-privilege-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsPrivilege, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsPrivilege, 'None' ], False ],
        }, {
            'attributes-list': [ CifsPrivilege, True ],
        } )
    
    def cifs_domain_trusts_rediscover(self):
        """
        Command to trigger re-discovery of trusted domains.
        """
        return self.request( "cifs-domain-trusts-rediscover", {
        }, {
        } )
    
    def cifs_homedir_paths_get(self):
        """
        Return the current list of paths to users' cifs home
        directories, if any.
        """
        return self.request( "cifs-homedir-paths-get", {
        }, {
            'homedir-paths': [ basestring, True ],
        } )
    
    def cifs_list_config(self):
        """
        This ZAPI is used to display the CIFS configuration.
        """
        return self.request( "cifs-list-config", {
        }, {
            'forest-functionality': [ basestring, False ],
            'DNS-domainname': [ basestring, False ],
            'security-style': [ basestring, False ],
            'domain-functionality': [ basestring, False ],
            'auth-type': [ basestring, False ],
            'Windows-type': [ basestring, False ],
            'DC-connection': [ ConnectionInfo, True ],
            'AD-site': [ basestring, False ],
            'NetBIOS-servername': [ basestring, False ],
            'NetBIOS-domainname': [ basestring, False ],
            'LDAP-connection': [ ConnectionInfo, True ],
            'domain-controller-functionality': [ basestring, False ],
        } )
    
    def cifs_server_stop(self):
        """
        Stop a CIFS server on the specified Vserver. Note that
        established sessions will be terminated and their open files
        closed. Workstations with cached data will not be able to save
        those changes, which could result in data loss.
        """
        return self.request( "cifs-server-stop", {
        }, {
        } )
    
    def cifs_symlink_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of CIFS symbolic link path mappings.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-symlink object.
                All cifs-symlink objects matching this query up to 'max-records'
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
        return self.request( "cifs-symlink-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsSymlink, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsSymlink, 'None' ], False ],
        }, {
            'attributes-list': [ CifsSymlink, True ],
        } )
    
    def cifs_branchcache_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the per-Vserver BranchCache configurations for the
        cluster.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-branchcache object.
                All cifs-branchcache objects matching this query up to
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
        return self.request( "cifs-branchcache-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsBranchcache, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsBranchcache, 'None' ], False ],
        }, {
            'attributes-list': [ CifsBranchcache, True ],
        } )
    
    def cifs_privilege_remove_privilege(self, privileges, user_or_group_name):
        """
        Remove privileges from a local or Active Directory user or group
        
        :param privileges: Privileges
        
        :param user_or_group_name: User or Group Name
        """
        return self.request( "cifs-privilege-remove-privilege", {
            'privileges': [ privileges, 'privileges', [ basestring, 'cifs-privilege-entries' ], True ],
            'user_or_group_name': [ user_or_group_name, 'user-or-group-name', [ basestring, 'cifs-name' ], False ],
        }, {
        } )
    
    def cifs_session_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of the established CIFS sessions.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-session object.
                All cifs-session objects matching this query up to 'max-records'
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
        return self.request( "cifs-session-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsSession, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsSession, 'None' ], False ],
        }, {
            'attributes-list': [ CifsSession, True ],
        } )
    
    def cifs_setup_ou_list_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous cifs-setup-ou-list-iter-start.
        """
        return self.request( "cifs-setup-ou-list-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def cifs_shadowcopy_restore_dir(self, volume, with_content, dst_dir, src_dir):
        """
        Request the storage system to restore a directory.
        
        :param volume: The name of the volume where the source and destination
                directories reside.
        
        :param with_content: Specifies what needs to be restored. False specifies the
                directory only. True indicates the directory and its content.
        
        :param dst_dir: The path of the destination directory. The path is in UTF8 and
                uses forward slash as directory separator. The path is relative
                to the root of the volume.
        
        :param src_dir: The path of the source directory. The path is in UTF8 and uses
                forward slash as directory separator. The path is relative to the
                root of the volume.
        """
        return self.request( "cifs-shadowcopy-restore-dir", {
            'volume': [ volume, 'volume', [ basestring, 'volume-name' ], False ],
            'with_content': [ with_content, 'with-content', [ bool, 'None' ], False ],
            'dst_dir': [ dst_dir, 'dst-dir', [ basestring, 'None' ], False ],
            'src_dir': [ src_dir, 'src-dir', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_branchcache_remove(self, flush_hashes):
        """
        Remove the BranchCache service
        
        :param flush_hashes: Delete Existing Hashes
        """
        return self.request( "cifs-branchcache-remove", {
            'flush_hashes': [ flush_hashes, 'flush-hashes', [ bool, 'None' ], False ],
        }, {
        } )
    
    def cifs_setup_create_passwd_file(self, default_root_password):
        """
        Creates a basic /etc/passwd file including a root user
        with the specified password.
        Note: This will overwrite an existing /etc/passwd file.
        See cifs-setup-verify-passwd-and-group for more information.
        
        :param default_root_password: The password given to a locally defined root user which
                may be used in the event that other authentication
                services are unavailable. This will be defined in the
                filer's local /etc/passwd file.
        """
        return self.request( "cifs-setup-create-passwd-file", {
            'default_root_password': [ default_root_password, 'default-root-password', [ basestring, 'None' ], False ],
        }, {
        } )
    
    def cifs_domain_preferred_dc_get_iter(self, max_records=None, query=None, tag=None, desired_attributes=None):
        """
        Retrieve the list of preferred domain controllers associated with
        Active Directory domains.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 20
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                cifs-domain-preferred-dc object.
                All cifs-domain-preferred-dc objects matching this query up to
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
        return self.request( "cifs-domain-preferred-dc-get-iter", {
            'max_records': max_records,
            'query': [ query, 'query', [ CifsDomainPreferredDc, 'None' ], False ],
            'tag': tag,
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ CifsDomainPreferredDc, 'None' ], False ],
        }, {
            'attributes-list': [ CifsDomainPreferredDc, True ],
        } )
    
    def cifs_share_create(self, share_name, path, comment=None, dir_umask=None, return_record=None, offline_files_mode=None, share_properties=None, symlink_properties=None, attribute_cache_ttl=None, file_umask=None, vscan_fileop_profile=None):
        """
        Creates a new CIFS share rooted at the specified path.
        
        :param share_name: The name of the CIFS share. The CIFS share name is a UTF-8 string
                with the following characters being illegal: control characters
                from 0x00 to 0x1F, both inclusive, 0x22 (double quotes) and the
                characters \/[]:|<>+=;,?"*
        
        :param path: The file system path that is shared through this CIFS share.
        
        :param comment: This string gives a description of the CIFS share. CIFS clients
                see this description when browsing the Vserver's CIFS shares.
        
        :param dir_umask: The value of this field controls the file mode creation mask for
                the CIFS share in qtrees with UNIX or Mixed security styles. The
                mask restricts the initial permissions setting of a newly created
                directory. The input value is a numeric mode comprising of one to
                three octal digits (0-7), derived by adding up the bits with
                values 4, 2, and 1. The first digit selects permissions for the
                user who owns the file: read (4), write (2), and execute (1); the
                second selects permissions for other users in the file's group,
                with the same values; and the third for other users not in the
                file's group, with the same values.
        
        :param return_record: If set to true, returns the cifs-share on successful creation.
                Default: false
        
        :param offline_files_mode: Mode of the offline file for the CIFS share. The default value
                is manual.
                Possible values:
                <ul>
                <li> "none"      - Clients are not permitted to cache files for
                offline access.,
                <li> "manual"    - Clients may cache files that are explicitly
                selected by the user for offline use.,
                <li> "documents" - Clients may automatically cache files that
                are used by the user for offline access.,
                <li> "programs"  - Clients may automatically cache files that
                are used by the user for offline access and may use those files
                in an offline mode even if the share is available.
                </ul>
        
        :param share_properties: The list of properties for this CIFS share.
                Possible values:
                <ul>
                <li> "oplocks"        - This specifies that opportunistic locks
                (client-side caching) are enabled on this share.,
                <li> "browsable"      - This specifies that the share can be
                browsed by Windows clients.,
                <li> "showsnapshot"   - This specifies that Snapshots can be
                viewed and traversed by clients.,
                <li> "changenotify"   - This specifies that CIFS clients can
                request for change notifications for directories on this share.,
                <li> "homedirectory"  - This specifies that the share is added
                and enabled as part of the CIFS home directory feature. The
                configuration of this share should be done using CIFS home
                directory feature interface. This property can only be set
                during the create process and cannot be altered later.
                <li> "attributecache" - This specifies that connections through
                this share are caching attributes for a short time to improve
                performance.
                <li> "branchcache" - This specifies that clients connecting to
                this share can make requests using BranchCache technology that
                allows them to cache the content in an attempt to reduce WAN
                utilization from a remote office.
                <li> "continuously_available" - This specifies that clients
                connecting to this share can open files in a persistent manner.
                Files opened this way are protected from disruptive events, such
                as failover and giveback.
                <li> "shadowcopy" - This specifies that the share is pointing
                to a shadow copy. This attribute cannot be added nor removed from
                a share.
                <li> "access_based_enumeration" - This specifies that Access
                Based Enumeration is enabled on this share. ABE-filtered shared
                folders are visible to a user based on that individual user's
                access rights, preventing the display of folders or other shared
                resources that the user does not have rights to access.
                </ul>
        
        :param symlink_properties: This flag controls whether the symlinks under this shared
                directory are hidden (option 'hide'), accessible (option
                'enable') or are accessible as read-only (option 'read-only'
                along with option 'enable').
                Possible values:
                <ul>
                <li> "enable"    ,
                <li> "hide"      ,
                <li> "read_only"
                </ul>
        
        :param attribute_cache_ttl: The lifetime of an entry in the file attribute cache, in seconds.
                This value is used if the share has the 'attributecache' property
                set, which improves the performance of certain metadata
                operations in common workloads. The default is 10 seconds.
                Raising this value may improve performance, but the likelihood
                that stale metadata will be served increases as well. The value
                of this field must be in the range of 1 to 86400.
        
        :param file_umask: The value of this field controls the file mode creation mask for
                the CIFS share in qtrees with UNIX or Mixed security styles. The
                mask restricts the initial permissions setting of a newly created
                file. The input value is a numeric mode comprising of one to
                three octal digits (0-7), derived by adding up the bits with
                values 4, 2, and 1. The first digit selects permissions for the
                user who owns the file: read (4), write (2), and execute (1); the
                second selects permissions for other users in the file's group,
                with the same values; and the third for other users not in the
                file's group, with the same values.
        
        :param vscan_fileop_profile: Profile-set of file-ops to which Vscan On-Access scanning
                is applicable. The default value is standard.
                Possible values:
                <ul>
                <li> "no_scan"     - Virus scans are never triggered for
                accesses to this share,
                <li> "standard"    - Virus scans can be triggered by open,
                close, and rename operations,
                <li> "strict"      - Virus scans can be triggered by open,
                read, close, and rename operations,
                <li> "writes_only" - Virus scans can be triggered only when
                a file that has been modified is closed.
                </ul>
        """
        return self.request( "cifs-share-create", {
            'comment': [ comment, 'comment', [ basestring, 'None' ], False ],
            'dir_umask': [ dir_umask, 'dir-umask', [ int, 'None' ], False ],
            'share_name': [ share_name, 'share-name', [ basestring, 'None' ], False ],
            'return_record': [ return_record, 'return-record', [ bool, 'None' ], False ],
            'offline_files_mode': [ offline_files_mode, 'offline-files-mode', [ basestring, 'None' ], False ],
            'share_properties': [ share_properties, 'share-properties', [ basestring, 'cifs-share-properties' ], True ],
            'symlink_properties': [ symlink_properties, 'symlink-properties', [ basestring, 'cifs-share-symlink-properties' ], True ],
            'path': [ path, 'path', [ basestring, 'None' ], False ],
            'attribute_cache_ttl': [ attribute_cache_ttl, 'attribute-cache-ttl', [ int, 'None' ], False ],
            'file_umask': [ file_umask, 'file-umask', [ int, 'None' ], False ],
            'vscan_fileop_profile': [ vscan_fileop_profile, 'vscan-fileop-profile', [ basestring, 'vscan-fileop-profile' ], False ],
        }, {
            'result': [ CifsShare, False ],
        } )
    
    def cifs_homedir_paths_set(self, force=None, homedir_paths=None):
        """
        Provides a list of CIFS home directory paths for the filer.
        Replaces the current list of paths in use by the filer.
        Note that supplying an empty path list causes the filer
        to delete any current entries.
        
        :param force: If true, the new set of homedir paths will be put into use
                even if some user homedir connections will be broken. This
                can cause users with open files in their home directories to
                lose access to the files. A user can lose data if there
                are updates not yet committed to disk.
        
        :param homedir_paths: An array, one entry per each cifs home directory path.
                note: homedir-path-info defined above
        """
        return self.request( "cifs-homedir-paths-set", {
            'force': [ force, 'force', [ bool, 'None' ], False ],
            'homedir_paths': [ homedir_paths, 'homedir-paths', [ basestring, 'homedir-path-info' ], True ],
        }, {
            'path-error': [ PathErrorInfo, True ],
        } )
