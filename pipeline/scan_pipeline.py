import time

from pipeline.port_stage import discover_ports
from pipeline.service_stage import detect_services
from pipeline.report_stage import save_report, save_json_report


def run_scan(target, start_port, end_port, threads):

    start_time = time.time()

    # Stage 1: Find open ports
    open_ports = discover_ports(
        target,
        start_port,
        end_port,
        threads
    )

    # Stage 2: Identify services
    results = detect_services(open_ports)

    end_time = time.time()

    scan_duration = end_time - start_time

    open_ports_count = len(results)

    report_file = save_report(target, results)
    json_file = save_json_report(target, results)

    return results, open_ports_count, scan_duration, report_file, json_file
