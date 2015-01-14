class SensorTypeEnum(basestring):
    """
    Type of the sensors the system can manage
    Possible values:
    <ul>
    <li> "fan"      - FAN RPM sensors,
    <li> "thermal"  - Temerature sensors,
    <li> "voltage"  - Voltage measurement sensors,
    <li> "current"  - Current measurement sensors,
    <li> "battlife" - Sensors report battery life,
    <li> "discrete" - Discrete sensors,
    <li> "fru"      - FRU sensors,
    <li> "nvmem"    - Sensors on the NVMEM module,
    <li> "counter"  - Sensors report in counters,
    <li> "minutes"  - Sensors report by minutes,
    <li> "percent"  - Sensors report in percentage,
    <li> "agent"    - Sensors on or throught the Agent device,
    <li> "unknown"  - Unknown sensors
    </ul>
    """
    
    @staticmethod
    def get_api_name():
          return "sensor-type-enum"
    
