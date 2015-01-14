class CronHour(int):
    """
    Job Manager cron scheduling hour. -1 represents all hours and
    only supported for cron schedule create and modify.
    Range : [-1..23].
    """
    
    @staticmethod
    def get_api_name():
          return "cron-hour"
    
