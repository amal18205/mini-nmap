import json
from datetime import datetime


def save_report(target, results):

    filename = "reports/scan_report.txt"

    with open(filename, "w") as file:

        file.write("Mini-Nmap Scan Report\n")
        file.write("=====================\n\n")

        file.write(f"Target: {target}\n")
        file.write(f"Date: {datetime.now()}\n\n")


        file.write("Results:\n")
        file.write("---------------------\n")


        for result in results:

            file.write(
                f"Port: {result['port']} | "
                f"State: {result['state']} | "
                f"Banner: {result['banner']}\n"
            )


    return filename

def save_json_report(target, results):

    filename = "reports/scan_report.json"

    report = {
        "target": target,
        "results": results
    }

    with open(filename, "w") as file:

        json.dump(
            report,
            file,
            indent=4
        )

    return filename
