class CronMonth(int):
    """
    Job Manager cron scheduling month. -1 represents all months and
    only supported for cron schedule create and modify.
    Range : [-1..11].
    """
    
    @staticmethod
    def get_api_name():
          return "cron-month"
    
