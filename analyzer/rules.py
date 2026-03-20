def analyze_metrics(cpu_usage, memory_mb, fps):
    warnings = []
    suggestions = []
    
    if cpu_usage > 70.0:
        warnings.append("High CPU usage")
    
    if memory_mb > 400.0:
        warnings.append("High Memory usage")
        suggestions.append("Check bitmap allocations")
    
    if fps < 55.0:
        warnings.append("Jank detected")
    
    if cpu_usage > 80.0 and fps < 30.0:
        suggestions.append("Reduce main thread work")
        
    return warnings, suggestions
