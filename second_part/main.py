from datetime import datetime, timedelta

from infrastructure.queries import *


def check_users():
    users = get_distinct_users()
    for user in users:
        datastr = get_datastr_for_user(user=user)
        datastr = [data[:6] for data in datastr]
        missing_record = False
        for i in range(7):
            current_date = (datetime.now() - timedelta(days=i)).strftime('%y%m%d')
            if current_date not in datastr:
                missing_record = True
                break
        if missing_record:
            continue
        else:
            insert_message(user=user, message="есть запись")


if __name__ == "__main__":
    create_db()
    insert_values_in_users()
    check_users()
