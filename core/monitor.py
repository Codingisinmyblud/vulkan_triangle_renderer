import psutil

class EmulatorMonitor:
    def __init__(self, package_name):
        self.package_name = package_name

    def get_host_metrics(self):
        return {
            "cpu": psutil.cpu_percent(interval=None),
            "memory": psutil.virtual_memory().percent
        }
