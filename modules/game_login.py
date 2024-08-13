import requests
import schedule
import time
from typing import Optional
from datetime import datetime
import pytz

task_check_scheduled = False
play_games_task_completed = False

def get_task_list_with_status(config: dict) -> Optional[dict]:
    url = "https://api-pass.levelinfinite.com/api/rewards/proxy/lipass/Points/GetTaskListWithStatus"
    headers = {
        "Cookie": config["cookie"],
        "User-Agent": config["user_agent"]
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:
            return data['data']
        else:
            print(f"Error in response: {data['msg']}")
    else:
        print(f"HTTP Error: {response.status_code}")

    return None

def check_play_games_task(config: dict) -> None:
    global play_games_task_completed
    if play_games_task_completed:
        return

    task_data = get_task_list_with_status(config)
    if task_data:
        tasks = task_data.get('tasks', [])
        for task in tasks:
            if task['task_name'] == "Play Games":
                if task['is_completed']:
                    print("Play Games task is completed.")
                    play_games_task_completed = True
                else:
                    print("Play Games task is not completed yet.")
                return

def reset_task_check():
    global task_check_scheduled, play_games_task_completed
    task_check_scheduled = False
    play_games_task_completed = False
    print("Resetting task check after daily check-in.")

def schedule_task_check(config: dict):
    global task_check_scheduled
    if not task_check_scheduled:
        schedule.every(2).minutes.do(check_play_games_task, config)
        task_check_scheduled = True
        print("Scheduled task check every 2 minutes.")

if __name__ == "__main__":
    from config import CONFIG

    tz = pytz.timezone('Asia/Shanghai')
    now = datetime.now(tz)
    reset_time = now.replace(hour=9, minute=1, second=0, microsecond=0)

    task_check_scheduled = False

    schedule.every().day.at(reset_time.strftime("%H:%M")).do(reset_task_check)

    while True:
        current_time = datetime.now(tz).strftime("%H:%M")
        if current_time >= "09:00" and not task_check_scheduled:
            schedule_task_check(CONFIG)
        
        schedule.run_pending()
        time.sleep(60)
