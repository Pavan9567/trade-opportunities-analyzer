from datetime import datetime

sessions = {}

def track_request(user_id: str):
    if user_id not in sessions:
        sessions[user_id] = {
            "count": 0,
            "last_request": None
        }

    sessions[user_id]["count"] += 1
    sessions[user_id]["last_request"] = datetime.utcnow()

def get_session(user_id: str):
    return sessions.get(user_id, {})