import requests
from typing import Optional
from dataclasses import dataclass

@dataclass
class UserPoints:
    total_points: int
    total_points_consumed: int
    total_points_earned: int

def get_user_points(config: dict) -> Optional[UserPoints]:
    url = "https://api-pass.levelinfinite.com/api/rewards/proxy/lipass/Points/GetUserTotalPoints"
    headers: dict[str, str] = {
        "Cookie": config["cookie"],
        "User-Agent": config["user_agent"]
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data['code'] == 0:
                points_data = data['data']
                return UserPoints(
                    total_points=points_data['total_points'],
                    total_points_consumed=points_data['total_points_consumed'],
                    total_points_earned=points_data['total_points_earned']
                )
            else:
                print(f"Error in response: {data['msg']}")
        else:
            print(f"HTTP Error: {response.status_code}")
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")

    return None