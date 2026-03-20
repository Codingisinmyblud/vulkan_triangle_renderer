def analyze_metrics(cpu_usage, memory_mb, fps):
    warnings = []
    suggestions = []
    
    if cpu_usage > 70.0:
        warnings.append("High CPU usage")
    
    if memory_mb > 400.0:
        warnings.append("High Memory usage")
        suggestions.append("Check bitmap allocations")
        
    return warnings, suggestions
