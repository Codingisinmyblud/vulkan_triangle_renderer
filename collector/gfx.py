from collector.adb_client import shell

def get_fps(package_name):
    output = shell(f"dumpsys gfxinfo {package_name}")
    if not output:
        return 60.0
    total_frames = 0
    janky_frames = 0
    for line in output.split('\n'):
        line = line.strip()
        if line.startswith("Total frames rendered:"):
            try:
                total_frames = int(line.split()[-1])
            except ValueError:
                pass
        elif line.startswith("Janky frames:"):
            try:
                janky_frames = int(line.split()[2])
            except ValueError:
                pass
    if total_frames > 0:
        return 60.0 * (1.0 - (janky_frames / total_frames))
    return 60.0
