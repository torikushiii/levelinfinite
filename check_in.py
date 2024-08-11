import requests
from config import CONFIG

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
        response_data = response.json()

        if response_data.get('code') == 1001009:
            print(f"Check-in failed: {response_data.get('msg')}")
        elif response_data.get('code') == 0 and response_data.get('msg') == 'ok':
            print("Check-in successful!")
        else:
            print(f"Unexpected response: {response_data}")
    except requests.exceptions.RequestException as e:
        print(f"Check-in failed: {e}")
