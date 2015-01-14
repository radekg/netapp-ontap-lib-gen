class DataProtocol(basestring):
    """
    nfs|cifs|iscsi|fcp|fcache|none
    Possible values:
    <ul>
    <li> "nfs"      - Used for NFS connections,
    <li> "cifs"     - Used for CIFS connections,
    <li> "iscsi"    - Used for iSCSI connections,
    <li> "fcp"      - Used for Fibre Channel connections,
    <li> "fcache"   - Used for FlexCache connections,
    <li> "none"     - Used for management. Does not serve any file
    protocols.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "data-protocol"
    
