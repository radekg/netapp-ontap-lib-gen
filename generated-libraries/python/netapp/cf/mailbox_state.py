class MailboxState(basestring):
    """
    State of mailbox disks owned by the node.
    Possible values are:
    <ul>
    <li>mbx_status_nodisks</li>
    <li>mbx_status_uncertain</li>
    <li>mbx_status_stale</li>
    <li>mbx_status_conflicted</li>
    <li>mbx_status_old_version</li>
    <li>mbx_status_not_found</li>
    <li>mbx_status_wrong_state</li>
    <li>mbx_status_backup</li>
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "mailbox-state"
    
