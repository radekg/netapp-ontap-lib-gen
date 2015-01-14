from netapp.netapp_object import NetAppObject

class AggregationData(NetAppObject):
    """
    Information related to aggregation that was done.
    """
    
    _constituent_count = None
    @property
    def constituent_count(self):
        """
        Number of constituents used to aggregate this instance.
        """
        return self._constituent_count
    @constituent_count.setter
    def constituent_count(self, val):
        if val != None:
            self.validate('constituent_count', val)
        self._constituent_count = val
    
    _result = None
    @property
    def result(self):
        """
        Each counter for an instance can be part of an aggregation set. Each counter can
        either have a strict or permissive aggregation. (Basically whether an aggregation
        with missing data samples in the aggregation set can be considered valid.)
        <br>Possible values: "complete_aggregation", "partial_aggregation"
        <ul>
        <li>If aggregation is 'strict', and we have all of the data samples,
        we return: complete_aggregation
        <li>If aggregation is 'strict' and we DON'T have all of the data samples,
        we return: partial_aggregation
        <li>If aggregation is 'strict' and we only have one instance (such as a flex vole)
        we return: complete_aggregation
        <li>If aggregation is 'permissive', we always return: complete_aggregation
        (since the results are always valid)
        </ul>
        NOTE: Since a given node DOES NOT have enough information to determine all of the
        members of the set, we have to assume if we can't contact a given node/process that
        may contain a piece to be aggregated, the aggregation is incomplete. (For example,
        if we're trying to aggregate 'volume' stats, and we can't contact the local dblade
        or a remote node, we'll mark it as incomplete.)
        """
        return self._result
    @result.setter
    def result(self, val):
        if val != None:
            self.validate('result', val)
        self._result = val
    
    @staticmethod
    def get_api_name():
          return "aggregation-data"
    
    @staticmethod
    def get_desired_attrs():
        return [
            'constituent-count',
            'result',
        ]
    
    def describe_properties(self):
        return {
            'constituent_count': { 'class': int, 'is_list': False, 'required': 'optional' },
            'result': { 'class': basestring, 'is_list': False, 'required': 'optional' },
        }
