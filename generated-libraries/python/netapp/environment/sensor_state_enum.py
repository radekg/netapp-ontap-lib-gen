class SensorStateEnum(basestring):
    """
    The operating states of the sensors. Depends on the hardware
    architecture, the environmental subsystem is implemented in two
    different approaches: one for service processor (SP) based
    platforms and one for non SP based (RLM, BMC) platforms. Some of
    the following states are available for one type of filers but
    not the other.
    Possible values:
    <ul>
    <li> "normal"        - The device is normal,
    <li> "warn_low"      - The device state is lower than the
    warning low threshold and higher than the critical low threshold,
    <li> "warn_high"     - The device state is higher than the
    warning high threshold and lower than the critical high
    threshold,
    <li> "crit_low"      - The device state is lower than the
    critical low threshold,
    <li> "crit_high"     - The device state is higher than the
    critical higher threshold,
    <li> "disabled"      - The sensor is disabled, only available
    for SP-based filers,
    <li> "uninitialized" - The sensor is not yet initialized, only
    available for SP-based filers,
    <li> "init_failed"   - The sensor failed to initialize, only
    available for SP-based filers,
    <li> "not_available" - The sensor is temporarily not able to
    report status, only available for SP-based filers,
    <li> "invalid"       - The status returned from the sensor is
    not valid, only available for SP-based filers,
    <li> "retry"         - The sensor is in the rety state, only
    available for non SP-based filers,
    <li> "bad"           - The device is bad, only available for
    non SP-based filers,
    <li> "not_present"   - The device is not present, only
    available for non SP-based filers,
    <li> "failed"        - The sensor failed to report status,
    <li> "ignored"       - The sensor state is ignored, only
    available for SP-based filers,
    <li> "unknown"       - The sensor state is uknown
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sensor-state-enum"
    
