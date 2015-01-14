from netapp.netapp_object import NetAppObject

class IscsiSesssionCmdListEntryInfo(NetAppObject):
    """
    information about a particular command
    """
    
    _cmd_state = None
    @property
    def cmd_state(self):
        """
        State of iSCSI command.
        Possible values:
        <ul>
        <li> "FREE" - Free,
        <li> "Logout_Begin" - Logout - Begin,
        <li> "Logout_Wait_For_Other_Conn" - Logout - Wait For Other Conn,
        <li> "Logout_Build_and_Send_Resp" - Logout - Build and Send Resp,
        <li> "Logout_Waiting_StatSN_ACK" - Logout - Waiting StatSN ACK,
        <li> "Logout_Done" - Logout - Done,
        <li> "Nopout_Begin" - Nopout - Begin,
        <li> "Nopout_Build_And_Send_Resp" - Nopout - Build And Send Resp,
        <li> "Nopout_Waiting_Resp_Sockio_Comp" - Nopout - Waiting Resp Sockio Comp,
        <li> "Nopout_Resp_Sockio_Comp" - Nopout - Resp Sockio Comp,
        <li> "Nopout_Waiting_StatSN_ACK" - Nopout - Waiting StatSN ACK,
        <li> "Nopout_Done" - Nopout - Done,
        <li> "Taskmgmt_Begin" - Taskmgmt - Begin,
        <li> "Taskmgmt_Waiting_FFPCmds_Rcvd" - Taskmgmt - Waiting FFPCmds Rcvd,
        <li> "Taskmgmt_FFPCmds_Rcvd" - Taskmgmt - FFPCmds Rcvd,
        <li> "Taskmgmt_Waiting_FFPCmds_Complete" - Taskmgmt - Waiting FFPCmds Complete,
        <li> "Taskmgmt_Build_And_Send_Resp" - Taskmgmt - Build And Send Resp,
        <li> "Taskmgmt_Waiting_StatSN_ACK" - Taskmgmt - Waiting StatSN ACK,
        <li> "Taskmgmt_Done" - Taskmgmt - Done,
        <li> "Text_Begin" - Text - Begin,
        <li> "Text_Waiting_Portal_List_Notify" - Text - Waiting Portal List Notify,
        <li> "Text_Build_And_Send_Resp" - Text - Build And Send Resp,
        <li> "Text_Waiting_Resp_Sockio_Comp" - Text - Waiting Resp Sockio Comp,
        <li> "Text_Resp_Sockio_Comp" - Text - Resp Sockio Comp,
        <li> "Text_Waiting_StatSN_ACK" - Text - Waiting StatSN ACK,
        <li> "Text_Done" - Text - Done,
        <li> "Scsicdb_Begin" - Scsicdb - Begin,
        <li> "Scsicdb_Claim_Early_Udata" - Scsicdb - Claim Early Udata,
        <li> "Scsicdb_Waiting_Udata_Rcvd" - Scsicdb - Waiting Udata Rcvd,
        <li> "Scsicdb_Udata_Rcvd" - Scsicdb - Udata Rcvd,
        <li> "Scsicdb_Ready_For_STSubmit" - Scsicdb - Ready For STSubmit,
        <li> "Scsicdb_Udata_Not_Rcvd" - Scsicdb - Udata Not Rcvd,
        <li> "Scsicdb_Udata_Waiting_Task_Reassignment" - Scsicdb - Udata Waiting Task Reassignment,
        <li> "Scsicdb_Udata_Task_Reassigned" - Scsicdb - Udata Task Reassigned,
        <li> "Scsicdb_Waiting_STLayer" - Scsicdb - Waiting STLayer,
        <li> "Scsicdb_RD_STLayer_Called" - Scsicdb - RD STLayer Called,
        <li> "Scsicdb_RD_Build_And_Send_R2T" - Scsicdb - RD Build And Send R2T,
        <li> "Scsicdb_RD_Waiting_Burst" - Scsicdb - RD Waiting Burst,
        <li> "Scsicdb_RD_Burst_Rcvd" - Scsicdb - RD Burst Rcvd,
        <li> "Scsicdb_RD_Done" - Scsicdb - RD Done,
        <li> "Scsicdb_RD_Burst_Not_Rcvd" - Scsicdb - RD Burst Not Rcvd,
        <li> "Scsicdb_RD_Waiting_Task_Reassignment" - Scsicdb - RD Waiting Task Reassignment,
        <li> "Scsicdb_RD_Task_Reassigned" - Scsicdb - RD Task Reassigned,
        <li> "Scsicdb_SD_STLayer_Called" - Scsicdb - SD STLayer Called,
        <li> "Scsicdb_SD_XDI_Done" - Scsicdb - SD XDI Done,
        <li> "Scsicdb_SD_Waiting_DataSN_ACK" - Scsicdb - SD Waiting DataSN ACK,
        <li> "Scsicdb_SD_Done" - Scsicdb - SD Done,
        <li> "Scsicdb_SD_SNACK_Rcvd" - Scsicdb - SD SNACK Rcvd,
        <li> "Scsicdb_SD_Task_Reassigned" - Scsicdb - SD Task Reassigned,
        <li> "Scsicdb_SR_STLayer_Called" - Scsicdb - SR STLayer Called,
        <li> "Scsicdb_SR_Build_And_Send_Resp" - Scsicdb - SR Build And Send Resp,
        <li> "Scsicdb_SR_Waiting_StatSN_ACK" - Scsicdb - SR Waiting StatSN ACK,
        <li> "Scsicdb_SR_Done" - Scsicdb - SR Done,
        <li> "Scsicdb_SR_SNACK_Rcvd" - Scsicdb - SR SNACK Rcvd,
        <li> "Scsicdb_SR_Task_Reassigned" - Scsicdb - SR Task Reassigned,
        <li> "Scsicdb_SR_XDI_Done" - Scsicdb - SR XDI Done,
        <li> "Scsicdb_SDR_STLayer_Called" - Scsicdb - SDR STLayer Called,
        <li> "Scsicdb_SDR_XDI_Done" - Scsicdb - SDR XDI Done,
        <li> "Scsicdb_SDR_Waiting_StatSN_ACK" - Scsicdb - SDR Waiting StatSN ACK,
        <li> "Scsicdb_SDR_Done" - Scsicdb - SDR Done,
        <li> "Scsicdb_SDR_SNACK_Rcvd" - Scsicdb - SDR SNACK Rcvd,
        <li> "Scsicdb_SDR_Task_Reassigned" - Scsicdb - SDR Task Reassigned,
        <li> "Scsicdb_Abort_Begin" - Scsicdb - Abort Begin,
        <li> "Scsicdb_Abort_Build_And_Send_Resp" - Scsicdb - Abort Build And Send Resp,
        <li> "Scsicdb_Abort_Waiting_StatSN_ACK" - Scsicdb - Abort Waiting StatSN ACK,
        <li> "Scsicdb_Abort_Done" - Scsicdb - Abort Done,
        <li> "Scsicdb_Abort_SNACK_Rcvd" - Scsicdb - Abort SNACK Rcvd,
        <li> "Scsicdb_Abort_Task_Reassigned" - Scsicdb - Abort Task Reassigned,
        <li> "Scsicdb_Abort_XDI_Done" - Scsicdb - Abort XDI Done,
        <li> "Scsicdb_QFull_Begin" - Scsicdb - QFull Begin,
        <li> "Scsicdb_QFull_Build_And_Send_Resp" - Scsicdb - QFull Build And Send Resp,
        <li> "Scsicdb_QFull_Waiting_StatSN_ACK" - Scsicdb - QFull Waiting StatSN ACK,
        <li> "Scsicdb_QFull_Done" - Scsicdb - QFull Done,
        <li> "Scsicdb_XDI_Start" - Scsicdb - XDI Start,
        <li> "Scsicdb_XDI_Waiting_Data_In_Sockio_Comp" - Scsicdb - XDI Waiting Data In Sockio Comp,
        <li> "Scsicdb_Waiting_Scsitgt_Abort" - Scsicdb - Waiting Scsitgt Abort,
        <li> "Done" - Done.
        </ul>
        """
        return self._cmd_state
    @cmd_state.setter
    def cmd_state(self, val):
        if val != None:
            self.validate('cmd_state', val)
        self._cmd_state = val
    
    _cmd_type = None
    @property
    def cmd_type(self):
        """
        Type of command being executed.
        Possible values:
        <ul>
        <li> "Seq",
        <li> "ITM",
        <li> "Oth",
        <li> "UNK".
        </ul>
        """
        return self._cmd_type
    @cmd_type.setter
    def cmd_type(self, val):
        if val != None:
            self.validate('cmd_type', val)
        self._cmd_type = val
    
    _cmd_sub_id = None
    @property
    def cmd_sub_id(self):
        """
        Variety specific sub-id.
        """
        return self._cmd_sub_id
    @cmd_sub_id.setter
    def cmd_sub_id(self, val):
        if val != None:
            self.validate('cmd_sub_id', val)
        self._cmd_sub_id = val
    
    @staticmethod
    def get_api_name():
          return "iscsi-sesssion-cmd-list-entry-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'cmd-state',
            'cmd-type',
            'cmd-sub-id',
        ]
    
    def describe_properties(self):
        return {
            'cmd_state': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'cmd_type': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'cmd_sub_id': { 'class': int, 'is_list': False, 'required': 'required' },
        }
