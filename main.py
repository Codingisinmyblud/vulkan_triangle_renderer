import sys
import time
from core.monitor import EmulatorMonitor
from ui.cli import display_metrics

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <package_name>")
        sys.exit(1)

    package_name = sys.argv[1]
    monitor = EmulatorMonitor(package_name)

    try:
        while True:
            host_metrics = monitor.get_host_metrics()
            emulator_metrics = monitor.get_emulator_metrics()
            warnings, suggestions = monitor.analyze(emulator_metrics)
            
            display_metrics(package_name, host_metrics, emulator_metrics, warnings, suggestions)
            
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting monitor...")

if __name__ == "__main__":
    main()
