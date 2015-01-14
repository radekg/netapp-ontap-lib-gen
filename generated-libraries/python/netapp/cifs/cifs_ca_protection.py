class CifsCaProtection(basestring):
    """
    The list of possible protection levels.
    Open files are "Continuously Available" if they are opened from an SMB 3
    client through a share with the "continuously_available" property set.
    These open files are capable of non-disruptively recovering from takeover
    and giveback as well as general aggregate relocation between partners in a
    high-availability relationship. This is in addition to the traditional SMB 2
    capability allowing clients to recover from LIF migration and other brief
    network interruptions.
    Note:
    The CA protection levels depicts the continuous availability at the connection
    level so it might not be accurate for a session if the connection has multiple
    sessions.
    Streams opened through a continuously available share are permitted,
    but are not currently made continuously available. Directories may be opened
    through a continuously available share, but will not appear continuously
    available as clients do not open them that way by design. These protection
    levels are applicable to the sessions/files on read/write volumes on SFO aggregates.
    Possible values:
    <ul>
    <li> "No"            - The open file is not continuously available.
    For sessions, it contains one or more open files
    but none of them are continuously available.
    <li> "Yes"           - The open file is continuously available.
    For sessions, it contains one or more open files and
    all of them are continuously available.
    <li> "Partial"       - This value is used for sessions only. It contains
    at least one continuously available open file but
    other open files that are not.
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "cifs-ca-protection"
    
