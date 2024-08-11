import schedule
import time
import argparse
from modules.check_in import daily_check_in

def main() -> None:
    parser = argparse.ArgumentParser(description="Daily check-in script")
    parser.add_argument('--manual', action='store_true', help="Perform a manual check-in")
    args = parser.parse_args()

    if args.manual:
        print("Performing manual check-in...")
        daily_check_in()
        return

    print("Script started...")

    schedule.every().day.at("09:00").do(daily_check_in)
    print("Scheduled daily check-in at 09:00 AM")

    while True:
        schedule.run_pending()
        print("Script is running...")
        time.sleep(60)

if __name__ == "__main__":
    main()
