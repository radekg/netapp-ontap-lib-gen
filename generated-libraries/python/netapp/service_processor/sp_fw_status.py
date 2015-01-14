class SpFwStatus(basestring):
    """
    Possible states the firmware of a SP/RLM device can be in
    Possible values:
    <ul>
    <li> "installed"     - Firmware installed and in normal
    state,
    <li> "corrupt"       - Firmware is corrupt,
    <li> "updating"      - Firmware is undergoing a manual
    update,
    <li> "auto_updating" - Firmware is undergoing an automatic
    update,
    <li> "none"          - Firmware status not known
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sp-fw-status"
    
