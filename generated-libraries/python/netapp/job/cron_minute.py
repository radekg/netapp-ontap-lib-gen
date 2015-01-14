class CronMinute(int):
    """
    Job Manager cron scheduling minute. -1 represents all minutes and
    only supported for cron schedule create and modify.
    Range : [-1..59].
    """
    
    @staticmethod
    def get_api_name():
          return "cron-minute"
    
