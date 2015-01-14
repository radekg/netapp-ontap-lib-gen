from netapp.connection import NaConnection
from environment_sensors_info import EnvironmentSensorsInfo # 12 properties
from sensor_state_enum import SensorStateEnum # 0 properties
from sensor_type_enum import SensorTypeEnum # 0 properties
from environment_sensors_get_iter_key_td import EnvironmentSensorsGetIterKeyTd # 2 properties

class EnvironmentConnection(NaConnection):
    
    def environment_sensors_get_iter(self, sensor_type=None, desired_attributes=None, max_records=None, discrete_sensor_state=None, tag=None, query=None, threshold_sensor_state=None, sensor_name=None):
        """
        Returns the sensors information from the environmental
        subsystem.
        
        :param sensor_type: Type of the sensor.  See sensor-type-enum for possible values
        
        :param desired_attributes: Specify the attributes that should be returned.
                If not present, all attributes for which information is available
                will be returned.
                If present, only the desired attributes for which information is
                available will be returned.
        
        :param max_records: The maximum number of records to return in this call.
                Default: 300
        
        :param discrete_sensor_state: Discrete-valued sensor state
        
        :param tag: Specify the tag from the last call.
                It is usually not specified for the first call. For subsequent
                calls, copy values from the 'next-tag' obtained from the previous
                call.
        
        :param query: A query that specifies which objects to return.
                A query could be specified on any number of attributes in the
                environment object.
                All environment objects matching this query up to 'max-records'
                will be returned.
        
        :param threshold_sensor_state: Threshold-based sensor state
        
        :param sensor_name: Name of the sensor in the environmental subsystem. The maximum
                length of the sensor name is 32
        """
        return self.request( "environment-sensors-get-iter", {
            'sensor_type': [ sensor_type, 'sensor-type', [ basestring, 'sensor-type-enum' ], False ],
            'desired_attributes': [ desired_attributes, 'desired-attributes', [ EnvironmentSensorsInfo, 'None' ], False ],
            'max_records': max_records,
            'discrete_sensor_state': [ discrete_sensor_state, 'discrete-sensor-state', [ basestring, 'sensor-state-enum' ], False ],
            'tag': tag,
            'query': [ query, 'query', [ EnvironmentSensorsInfo, 'None' ], False ],
            'threshold_sensor_state': [ threshold_sensor_state, 'threshold-sensor-state', [ basestring, 'sensor-state-enum' ], False ],
            'sensor_name': [ sensor_name, 'sensor-name', [ basestring, 'None' ], False ],
        }, {
            'attributes-list': [ EnvironmentSensorsInfo, True ],
        } )
