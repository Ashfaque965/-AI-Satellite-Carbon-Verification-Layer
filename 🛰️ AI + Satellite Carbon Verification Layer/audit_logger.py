import time
import json


class AuditLogger:
    def __init__(self, file="audit_log.jsonl"):
        self.file = file

    def log(self, event_type, data):
        record = {
            "timestamp": time.time(),
            "event": event_type,
            "data": data
        }

        with open(self.file, "a") as f:
            f.write(json.dumps(record) + "\n")