from netapp.ntdtest.output_typedef_2 import OutputTypedef2
from netapp.netapp_object import NetAppObject

class OutputTypedef1(NetAppObject):
    """
    Output
    """
    
    _zfield1 = None
    @property
    def zfield1(self):
        """
        Generic/Dummy Field 1
        Attributes: key, required-for-create, non-modifiable
        """
        return self._zfield1
    @zfield1.setter
    def zfield1(self, val):
        if val != None:
            self.validate('zfield1', val)
        self._zfield1 = val
    
    _output_td_2 = None
    @property
    def output_td_2(self):
        """
        Output
        """
        return self._output_td_2
    @output_td_2.setter
    def output_td_2(self, val):
        if val != None:
            self.validate('output_td_2', val)
        self._output_td_2 = val
    
    @staticmethod
    def get_api_name():
          return "output-typedef-1"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'zfield1',
            'output-td-2',
        ]
    
    def describe_properties(self):
        return {
            'zfield1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
            'output_td_2': { 'class': OutputTypedef2, 'is_list': True, 'required': 'optional' },
        }
