import os
import sys
import datetime

def update_tracker(account_id, stage, status="Success"):
    tracker_path = "MASTER_TASK_TRACKER.md"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    line = f"| {now} | {account_id} | {stage} | {status} |\n"
    
    file_exists = os.path.isfile(tracker_path)
    
    with open(tracker_path, "a") as f:
        if not file_exists:
            f.write("# Clara Pipeline - Task Tracker\n\n")
            f.write("| Timestamp | Account ID | Stage | Status |\n")
            f.write("|---'|---|---|---|\n")
        f.write(line)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python update_tracker.py <account_id> <stage> [status]")
        sys.exit(1)
        
    acc_id = sys.argv[1]
    stage = sys.argv[2]
    status = sys.argv[3] if len(sys.argv) > 3 else "Success"
    
    update_tracker(acc_id, stage, status)
    print(f"Logged {stage} for {acc_id} in MASTER_TASK_TRACKER.md")
