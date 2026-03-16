from collector.adb_client import shell

def get_app_memory(package_name):
    output = shell(f"dumpsys meminfo {package_name}")
    if not output or "No process found" in output:
        return 0.0
    for line in output.split('\n'):
        if "TOTAL" in line and ":" not in line:
            parts = line.strip().split()
            if len(parts) > 1:
                try:
                    return float(parts[1]) / 1024.0
                except ValueError:
                    pass
    return 0.0
