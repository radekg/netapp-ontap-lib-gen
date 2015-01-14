from netapp.ntdtest.output_typedef_4 import OutputTypedef4
from netapp.netapp_object import NetAppObject

class OutputTypedef3(NetAppObject):
    """
    Output
    """
    
    _output_td_4 = None
    @property
    def output_td_4(self):
        """
        Output
        """
        return self._output_td_4
    @output_td_4.setter
    def output_td_4(self, val):
        if val != None:
            self.validate('output_td_4', val)
        self._output_td_4 = val
    
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
    
    @staticmethod
    def get_api_name():
          return "output-typedef-3"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'output-td-4',
            'zfield1',
        ]
    
    def describe_properties(self):
        return {
            'output_td_4': { 'class': OutputTypedef4, 'is_list': True, 'required': 'optional' },
            'zfield1': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
