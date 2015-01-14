class CronDayOfMonth(int):
    """
    Job Manager cron scheduling day of month. -1 represents all days
    of a month from 1 to 31, and only supported for cron schedule
    create and modify.
    Range : [-1..31].
    """
    
    @staticmethod
    def get_api_name():
          return "cron-day-of-month"
    
