import schedule
import time
import argparse
from datetime import datetime
import pytz
from modules.check_in import daily_check_in
from modules.user_points import get_user_points
from modules.game_login import check_play_games_task, reset_task_check, schedule_task_check
from config import CONFIG

def main() -> None:
    parser = argparse.ArgumentParser(description="Daily check-in script")
    parser.add_argument('-m', '--manual', action='store_true', help="Perform a manual check-in")
    args = parser.parse_args()

    if args.manual:
        print("Performing manual check-in...")
        daily_check_in(CONFIG)
        return

    print("Script started...")

    tz = pytz.timezone('Asia/Shanghai')
    now = datetime.now(tz)
    schedule_time = now.replace(hour=9, minute=0, second=0, microsecond=0)
    reset_time = now.replace(hour=9, minute=1, second=0, microsecond=0)

    schedule.every().day.at(schedule_time.strftime("%H:%M")).do(daily_check_in, CONFIG)
    print("Scheduled daily check-in at 09:00 AM GMT+8")

    schedule.every().day.at(reset_time.strftime("%H:%M")).do(reset_task_check)
    schedule_task_check(CONFIG)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
