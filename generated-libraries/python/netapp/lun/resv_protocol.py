class ResvProtocol(basestring):
    """
    fcp|iscsi
    Possible values:
    <ul>
    <li> "fcp"      ,
    <li> "iscsi"
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "resv-protocol"
    
