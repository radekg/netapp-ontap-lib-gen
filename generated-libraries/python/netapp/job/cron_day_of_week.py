class CronDayOfWeek(int):
    """
    Job Manager cron scheduling day of week. Zero represents Sunday.
    -1 represents all days of a week and only supported for cron
    schedule create and modify.
    Range : [-1..6].
    """
    
    @staticmethod
    def get_api_name():
          return "cron-day-of-week"
    
