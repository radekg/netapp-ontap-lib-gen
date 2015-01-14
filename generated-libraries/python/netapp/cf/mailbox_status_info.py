from netapp.netapp_object import NetAppObject

class MailboxStatusInfo(NetAppObject):
    """
    Mailbox status info.
    """
    
    _mailbox_status = None
    @property
    def mailbox_status(self):
        """
        representation of mailbox status bit.
        Possible values:
        mbx_status_nodisks
        mbx_status_uncertain
        mbx_status_stale
        mbx_status_conflicted
        mbx_status_old_version
        mbx_status_not_found
        mbx_status_wrong_state
        mbx_status_backup
        """
        return self._mailbox_status
    @mailbox_status.setter
    def mailbox_status(self, val):
        if val != None:
            self.validate('mailbox_status', val)
        self._mailbox_status = val
    
    @staticmethod
    def get_api_name():
          return "mailbox-status-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'mailbox-status',
        ]
    
    def describe_properties(self):
        return {
            'mailbox_status': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
