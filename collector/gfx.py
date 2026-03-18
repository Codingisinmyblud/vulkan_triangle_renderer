from collector.adb_client import shell

def get_fps(package_name):
    output = shell(f"dumpsys gfxinfo {package_name}")
    if not output:
        return 60.0
    total = 0
    jank = 0
    for line in output.split('\n'):
        line = line.strip()
        if line.startswith("Total frames rendered:"):
            total = int(line.split()[-1])
        elif line.startswith("Janky frames:"):
            jank = int(line.split()[2])
    if total > 0:
        return 60.0 * (1.0 - (jank / total))
    return 60.0
