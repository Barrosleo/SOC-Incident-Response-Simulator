import pandas as pd
import random
import datetime

def generate_logs(num_records=100):
    logs = []
    event_types = ["auth", "network", "cloud"]
    statuses = ["success", "failure"]
    users = ["alice", "bob", "charlie", "dave"]

    for _ in range(num_records):
        log_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "event_type": random.choice(event_types),
            "user": random.choice(users),
            "status": random.choice(statuses)
        }
        logs.append(log_entry)
    df = pd.DataFrame(logs)
    return df

if __name__ == '__main__':
    df = generate_logs(200)
    df.to_csv("data/synthetic_logs.csv", index=False)
    print("Synthetic logs generated and saved to data/synthetic_logs.csv")
