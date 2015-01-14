from netapp.connection import NaConnection
from fc_delegation_lock import FcDelegationLock # 2 properties
from lock_status_info import LockStatusInfo # 17 properties
from cifs_lock import CifsLock # 17 properties
from nlm_lock import NlmLock # 13 properties
from pfs_lock import PfsLock # 10 properties
from nfsv4_lock import Nfsv4Lock # 14 properties
from share_lock import ShareLock # 7 properties
from range_lock import RangeLock # 6 properties
from break_error import BreakError # 1 properties
from op_lock import OpLock # 3 properties

class LockConnection(NaConnection):
    
    def lock_status_iter_start(self, owner=None, host=None, protocol=None, file_name=None):
        """
        Gives information about one or more locks, the results of
        which are retrieved by using lock-status-iter-next.
        One or more of the defined inputs can be specified in tandem
        to get locks for specific cases. If none of the inputs are
        specified, then all the locks in the system are printed.
        If no protocol is specified but one or more of the other inputs
        are specified, then locks across all protocols, viz., CIFS, PFS,
        NLM (Nfsv2/Nfsv3), and NFSv4, are printed. In this case, it is
        possible for protocols that define syntax of specified input
        differently to generate input syntax errors. However, these
        errors do not stop scanning of locks for other protocols.
        
        :param owner: Name of the lock owner, viz., a username prefixed by an optional
                domain (and a backslash) for CIFS protocol ([domain\]username),
                IP address suffixed by a colon and a filesystem	ID of caching
                filer (IP:fsid) for PFS, and process-ID for NLM(Nfsv2/Nfsv3).
                The concept of an owner for NFSv4 is yet to be defined.
                If specified, then locks are printed for that owner only.
                If owner is not specified, locks across all owners are printed.<br><br>
                NOTE: Currently, only CIFS protocol filters lock output
                by owner name.
        
        :param host: Identity of a host. It is the NetBIOS name or IP address of a
                CIFS client, FQDN of a PFS client, IP address or FQDN of
                NLM (Nfsv2/Nfsv3) client, and IP address of NFSv4 client.
                If specified, then locks are printed for that host only.
                If not specified, then locks across all hosts are printed.<br><br>
                NOTE: Currently, only CIFS protocol filters lock output
                by host name.
        
        :param protocol: Name of the protocol (case-insensitive): "cifs" (CIFS),
                "nlm" (Nfsv2/Nfsv3), "nfsv4" (NFSv4), and "pfs"(PFS).
                If not specified, then all protocols are scanned for locks.
                If in that case, a host and/or owner were specified, then
                expect input syntax errors in "error" output field for
                protocols that define syntax of host or owner differently.
                However, scanning of locks is not aborted due to these syntax
                errors and instead all protocols are still scanned to
                completion.
        
        :param file_name: File name prefixed by "/vol/volX" style path. If not specified,
                then locks across all files are printed.
                Input syntax of file-name is the same for all protocols.
        """
        return self.request( "lock-status-iter-start", {
            'owner': [ owner, 'owner', [ basestring, 'None' ], False ],
            'host': [ host, 'host', [ basestring, 'None' ], False ],
            'protocol': [ protocol, 'protocol', [ basestring, 'None' ], False ],
            'file_name': [ file_name, 'file-name', [ basestring, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'tag': [ basestring, False ],
        } )
    
    def lock_break(self, owner=None, host=None, protocol=None, file_name=None):
        """
        Breaks all specified locks.
        At least one input argument needs to be specified.
        
        :param owner: Name of the lock owner, viz., a username prefixed by an optional
                domain (and a backslash) for CIFS protocol ([domain\]username),
                IP address of caching filer suffixed by a colon and a filesystem
                ID of origin filer (IP:fsid) for PFS, and process-ID for
                NLM(Nfsv2/Nfsv3).
                The concept of an owner for NFSv4 is yet to be defined.
                If specified, then locks are printed for that owner only.
                If owner is not specified, locks across all owners are printed.<br><br>
                NOTE: Currently, only CIFS protocol filters lock output
                by owner name.
        
        :param host: Identity of a host. It is the NetBIOS name or IP address of a
                CIFS cient, FQDN of a PFS client, IP address or FQDN of
                NLM (Nfsv2/Nfsv3) client, and IP address of NFSv4 client.
                If specified, then locks are printed for that host only.
                If not specified, then locks across all hosts are printed.<br><br>
                NOTE: Currently, only CIFS protocol filters lock output
                by host name.
        
        :param protocol: Name of the protocol (case-insensitive): "cifs" (CIFS),
                "nlm" (Nfsv2/Nfsv3), "nfsv4" (NFSv4), and "pfs"(PFS).
                If not specified, then all protocols are scanned for locks.
                If in that case, a host and/or owner were specified, then
                expect input syntax errors in "error" output field for
                protocols that define syntax of host or owner differently.
                However, scanning of locks is not aborted due to these syntax
                errors and instead all protocols are still scanned to
                completion.
        
        :param file_name: File name prefixed by "/vol/volX" style path.
                Input syntax of file-name is the same for all protocols.
                NOTE: Currently, breaking all locks of a file is not
                encouraged, as NFSv4 does not yet implement breaking of
                locks. If attempted, will lead to an inconsistent
                NFSv4 lock state. Specifying a protocol will prevent
                this by limiting the breaking of locks to that particular
                protocol. Also, breaking locks for proto "nfsv4" is explicitly
                disallowed.
        """
        return self.request( "lock-break", {
            'owner': [ owner, 'owner', [ basestring, 'None' ], False ],
            'host': [ host, 'host', [ basestring, 'None' ], False ],
            'protocol': [ protocol, 'protocol', [ basestring, 'None' ], False ],
            'file_name': [ file_name, 'file-name', [ basestring, 'None' ], False ],
        }, {
            'errors': [ BreakError, True ],
        } )
    
    def lock_status_iter_end(self, tag):
        """
        Terminate a list iteration and clean up any saved info.
        
        :param tag: Tag from a previous cifs-share-list-iter-start.
        """
        return self.request( "lock-status-iter-end", {
            'tag': tag,
        }, {
        } )
    
    def lock_status_iter_next(self, tag, maximum):
        """
        Returns items from a previous call to
        cifs-lock-status-iter-start. This API actually prints out
        the required locks.
        
        :param tag: Tag from a previous cifs-lock-status-iter-start.
        
        :param maximum: The maximum number of lock entries to retrieve.
        """
        return self.request( "lock-status-iter-next", {
            'tag': tag,
            'maximum': [ maximum, 'maximum', [ int, 'None' ], False ],
        }, {
            'records': [ int, False ],
            'lock-status': [ LockStatusInfo, True ],
        } )
