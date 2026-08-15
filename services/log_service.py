import os


def process_logs():

    log_file = "logs/hotel.log"

    if not os.path.exists(log_file):
        print("Log file not found")
        return

    info = 0
    warnings = 0
    errors = 0

    with open(log_file, "r") as file:

        for line in file:

            if "INFO" in line:
                info += 1

            elif "WARNING" in line:
                warnings += 1

            elif "ERROR" in line:
                errors += 1

    print("\n===== LOG SUMMARY =====")
    print(f"INFO: {info}")
    print(f"WARNING: {warnings}")
    print(f"ERROR: {errors}")

    print("\nLog processing completed.")

    if errors > 0:
        print("Historical errors detected in log.")

    if warnings > 0:
        print("Warnings detected in log.")

    print("System Status: CHECKED")