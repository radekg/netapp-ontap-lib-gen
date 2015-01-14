class PartitionScheme(basestring):
    """
    mbr|gpt|unknown
    Possible values:
    <ul>
    <li> "mbr"      - Master Boot Record Partition Table Scheme.,
    <li> "gpt"      - GUID Partition Table Scheme.,
    <li> "unknown"  - Partition Scheme other than MBR or GPT or an
    unformatted LUN.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "partition-scheme"
    
