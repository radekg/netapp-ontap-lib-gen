class AutosupportCmdTgt(basestring):
    """
    Execution domain of AutoSupport content
    Possible values:
    <ul>
    <li> "bsd"           - Command executed by BSD,
    <li> "smf_table"     - Command selects SMF table,
    <li> "file"          - Command indicates file to collect,
    <li> "dblade"        - Collect from dbladecli,
    <li> "dblade_file"   - Collect a file from dblade. Could be
    partner file,
    <li> "zapi_xml"      - Response in XML format,
    <li> "custom_fx"     - Collect custom function output file
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "autosupport-cmd-tgt"
    
