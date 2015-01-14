class LunOsType(basestring):
    """
    The image type of the lun. This value determines
    the proper alignment settings for the desired
    host filesystem layout.
    Possible values:
    <ul>
    <li> "aix" The LUN will be used to store an AIX filesystem,
    <li> "hpux" The LUN will be used to store an HP-UX filesystem,
    <li> "hyper_v" The LUN will be used to store Hyper-V VHDs
    (Virtual Hard Disks),
    <li> "image" The default type indicating no assumptions will
    be made about the data stored in the LUN,
    <li> "linux" The LUN will be used to store a Linux filesystem
    with no partition table,
    <li> "netware" The LUN will be used to store a Netware filesystem,
    <li> "openvms" The LUN will be used to store an OpenVMS filesystem,
    <li> "solaris" The LUN will be used to store a Solaris filesystem,
    in a single slice partition,
    <li> "solaris_efi" The LUN will be used to store a Solaris filesystem
    with an EFI partition table,
    <li> "vmware" The LUN will be used to store a VMware Virtual
    Machine File System (VMFS) containing Virtual
    Machine Disk Files (VMDKs),
    <li> "windows" The LUN will be used to store a Windows filesystem
    with a Master Boot Record (MBR) partition table.
    <li> "windows_2008" The LUN will be used to store a Windows filesystem
    with a Master Boot Record (MBR) partition table on Windows
    2008 or later,
    <li> "windows_gpt" The LUN will be used to store a Windows filesystem
    with a GUID Partition Table (GPT).
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "lun-os-type"
    
