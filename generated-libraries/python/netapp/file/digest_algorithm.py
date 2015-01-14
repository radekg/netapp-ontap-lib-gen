class DigestAlgorithm(basestring):
    """
    Digest algorithm used for fingerprint computation.
    Possible values: "sha-256" or "md5".
    """
    
    @staticmethod
    def get_api_name():
          return "digest-algorithm"
    
