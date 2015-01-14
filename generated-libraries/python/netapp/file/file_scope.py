class FileScope(basestring):
    """
    Part of the file for which fingerprint is computed.
    Possible values: "metadata_only", "data_only",
    "data_and_metadata".
    """
    
    @staticmethod
    def get_api_name():
          return "file-scope"
    
