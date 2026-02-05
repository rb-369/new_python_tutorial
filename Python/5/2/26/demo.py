from collections import defaultdict
from typing import List, Tuple, Dict, Set


def process_user_activity(
    records: List[Tuple[int, str, List[str]]]
) -> Dict[str, object]:
    """
    Processes user activity records and returns aggregated information.
    """

    unique_users: Set[str] = set()
    activity_count: Dict[str, int] = defaultdict(int)
    user_activity_map: Dict[str, Set[str]] = defaultdict(set)
    user_total_activity: Dict[str, int] = defaultdict(int)

    for _, username, activities in records:
        unique_users.add(username)

        for activity in activities:
            activity_count[activity] += 1
            user_activity_map[username].add(activity)
            user_total_activity[username] += 1

    # Sort activities per user
    sorted_user_activity_map = {
        user: sorted(activities)
        for user, activities in user_activity_map.items()
    }

    # Determine most active user (lexicographically smallest in case of tie)
    max_activity = max(user_total_activity.values())
    most_active_user = min(
        user
        for user, count in user_total_activity.items()
        if count == max_activity
    )

    return {
        "unique_users": unique_users,
        "activity_count": dict(activity_count),
        "user_activity_map": sorted_user_activity_map,
        "most_active_user": most_active_user
    }


def main() -> None:
    records = [
        (1, "alice", ["login", "view", "logout"]),
        (2, "bob", ["login", "view"]),
        (3, "alice", ["login", "purchase"]),
        (4, "david", ["login", "view", "purchase", "logout"]),
    ]

    result = process_user_activity(records)
    print(result)


if __name__ == "__main__":
    main()
