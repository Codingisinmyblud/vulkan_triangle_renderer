import psutil
from collector.cpu import get_app_cpu
from collector.memory import get_app_memory
from collector.gfx import get_fps
from analyzer.rules import analyze_metrics

class EmulatorMonitor:
    def __init__(self, package_name):
        self.package_name = package_name

    def get_host_metrics(self):
        return {
            "cpu": psutil.cpu_percent(interval=None),
            "memory": psutil.virtual_memory().percent
        }

    def get_emulator_metrics(self):
        cpu = get_app_cpu(self.package_name)
        mem = get_app_memory(self.package_name)
        fps = get_fps(self.package_name)
        return {"cpu": cpu, "memory": mem, "fps": fps}

    def analyze(self, metrics):
        return analyze_metrics(metrics["cpu"], metrics["memory"], metrics["fps"])
