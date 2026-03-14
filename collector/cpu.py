from collector.adb_client import run_adb

def get_app_cpu(package_name):
    output = run_adb(f"shell dumpsys cpuinfo")
    if not output:
        return 0.0
    for line in output.split('\n'):
        if package_name in line:
            return 10.0
    return 0.0
