#!/usr/bin/env python3
import json
import sys
from datetime import datetime

LOG_FILE = "/var/log/suricata/eve.json"

def parse_alerts(log_file):
    alerts = []
    with open(log_file, "r") as f:
        for line in f:
            try:
                event = json.loads(line)
                if event.get("event_type") == "alert":
                    alerts.append({
                        "timestamp": event["timestamp"],
                        "signature": event["alert"]["signature"],
                        "severity": event["alert"]["severity"],
                        "src_ip": event["src_ip"],
                        "dest_ip": event["dest_ip"],
                        "proto": event["proto"]
                    })
            except json.JSONDecodeError:
                continue
    return alerts

def display_alerts(alerts):
    if not alerts:
        print("No alerts found.")
        return
    print(f"\n{'='*60}")
    print(f"SURICATA ALERT SUMMARY - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total alerts: {len(alerts)}")
    print(f"{'='*60}\n")
    for a in alerts:
        print(f"[{a['timestamp']}]")
        print(f"  Signature : {a['signature']}")
        print(f"  Severity  : {a['severity']}")
        print(f"  Traffic   : {a['src_ip']} -> {a['dest_ip']} ({a['proto']})")
        print()

if __name__ == "__main__":
    alerts = parse_alerts(LOG_FILE)
    display_alerts(alerts)
