class AuditFormat(basestring):
    """
    xml|evtx
    Possible values:
    <ul>
    <li> "xml"      - Data ONTAP-Specific XML Log Format,
    <li> "evtx"     - Microsoft Windows EVTX Log Format
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "audit-format"
    
