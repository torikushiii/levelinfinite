import requests
from typing import Optional
from config import CONFIG
from modules.user_points import get_user_points, UserPoints

def daily_check_in(task_id: str = "15") -> None:
    """Performs the daily check-in request."""
    url: str = "https://api-pass.levelinfinite.com/api/rewards/proxy/lipass/Points/DailyCheckIn"
    headers: dict[str, str] = {
        "Cookie": CONFIG["cookie"],
        "User-Agent": CONFIG["user_agent"]
    }
    data: dict[str, str] = {"task_id": task_id}

    try:
        response: requests.Response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_data: dict = response.json()

        if response_data.get('code') == 1001009:
            print("You have already checked in today.")
            user_points: Optional[UserPoints] = get_user_points()
            if user_points:
                print(f"Total Points: {user_points.total_points} (Consumed: {user_points.total_points_consumed}, Earned: {user_points.total_points_earned})")
        elif response_data.get('code') == 0 and response_data.get('msg') == 'ok':
            print("Check-in successful!")
            user_points: Optional[UserPoints] = get_user_points()
            if user_points:
                print(f"Total Points: {user_points.total_points} (Consumed: {user_points.total_points_consumed}, Earned: {user_points.total_points_earned})")
        else:
            print(f"Unexpected response: {response_data}")
    except requests.exceptions.RequestException as e:
        print(f"Check-in failed: {e}")
