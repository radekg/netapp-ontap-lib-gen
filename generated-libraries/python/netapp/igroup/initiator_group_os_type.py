class InitiatorGroupOsType(basestring):
    """
    The operating system of the initiator group. This value
    modifies the finer details of SCSI protocol interaction for
    initiators in the group.
    Possible values:
    <ul>
    <li> "aix" The initiators belong to an AIX host,
    <li> "default" The initiators belong to an unknown host type,
    <li> "hpux" The initiators belong to an HP-UX host,
    <li> "hyper_v" The initiators belong to a Hyper-V parent host,
    <li> "linux" The initiators belong to a Linux host,
    <li> "netware" The initators belong to a NetWare host,
    <li> "openvms" The initiators belong to an OpenVMS host,
    <li> "solaris" The initiators belong to a Solaris host,
    <li> "vmware" The initiators belong to a VMware ESX host,
    <li> "windows" The initiators belong to a Windows host,
    <li> "xen" The initiators belong to a Xen hypervisor host.
    <ul>
    """
    
    @staticmethod
    def get_api_name():
          return "initiator-group-os-type"
    
