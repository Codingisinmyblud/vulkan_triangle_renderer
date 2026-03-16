from collector.adb_client import shell

def get_app_cpu(package_name):
    output = shell("dumpsys cpuinfo")
    if not output:
        return 0.0
    for line in output.split('\n'):
        if package_name in line:
            parts = line.strip().split()
            if parts and parts[0].endswith('%'):
                try:
                    return float(parts[0].replace('%', ''))
                except ValueError:
                    return 0.0
    return 0.0
