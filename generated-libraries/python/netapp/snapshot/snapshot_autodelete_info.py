from netapp.netapp_object import NetAppObject

class SnapshotAutodeleteInfo(NetAppObject):
    """
    Option name and value.
    """
    
    _option_value = None
    @property
    def option_value(self):
        """
        Option value.
        """
        return self._option_value
    @option_value.setter
    def option_value(self, val):
        if val != None:
            self.validate('option_value', val)
        self._option_value = val
    
    _option_name = None
    @property
    def option_name(self):
        """
        Option key.
        Possible values:
        "state" (value: "on" | "off")
        "commitment" (value: "try" | "disrupt")
        "trigger" (value: "volume" | "snap_reserve" | "space_reserve")
        "target_free_space" (value: &lt; number &gt;)
        "delete_order" (value: newest_first | oldest_first)
        "defer_delete" (value: scheduled | user_created | prefix | none)
        destroy_list" (value: &lt; user-defined &gt;)
        "prefix" (value: &lt; string &gt;)
        """
        return self._option_name
    @option_name.setter
    def option_name(self, val):
        if val != None:
            self.validate('option_name', val)
        self._option_name = val
    
    @staticmethod
    def get_api_name():
          return "snapshot-autodelete-info"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'option-value',
            'option-name',
        ]
    
    def describe_properties(self):
        return {
            'option_value': { 'class': basestring, 'is_list': False, 'required': 'required' },
            'option_name': { 'class': basestring, 'is_list': False, 'required': 'required' },
        }
