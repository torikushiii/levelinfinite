import schedule
import time
import argparse
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

    schedule.every().day.at("09:00").do(daily_check_in, CONFIG)
    print("Scheduled daily check-in at 09:00 AM")

    schedule.every().day.at("09:01").do(reset_task_check)
    schedule_task_check(CONFIG)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
