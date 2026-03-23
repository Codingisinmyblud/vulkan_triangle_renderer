from rich.console import Console

console = Console()

def display_metrics(package_name, host_metrics, emulator_metrics, warnings, suggestions):
    console.clear()
    console.print(f"[bold blue]App:[/bold blue] {package_name}\n")
    
    cpu_color = "red" if "High CPU usage" in warnings else "green"
    cpu_warn = "⚠ High" if "High CPU usage" in warnings else "OK"
    
    mem_color = "red" if "High Memory usage" in warnings else "green"
    mem_warn = "⚠ High" if "High Memory usage" in warnings else "OK"
    
    fps_color = "red" if "Jank detected" in warnings else "green"
    fps_warn = "⚠ Jank detected" if "Jank detected" in warnings else "OK"

    console.print(f"CPU Usage: [{cpu_color}]{emulator_metrics['cpu']:.1f}%[/{cpu_color}]\t{cpu_warn}")
    console.print(f"Memory:    [{mem_color}]{emulator_metrics['memory']:.1f}MB[/{mem_color}]\t{mem_warn}")
    console.print(f"FPS:       [{fps_color}]{emulator_metrics['fps']:.1f}[/{fps_color}]\t{fps_warn}\n")

    if suggestions:
        console.print("[bold yellow]Suggestions:[/bold yellow]")
        for s in suggestions:
            console.print(f"- {s}")
    
    console.print(f"\n[dim]Host CPU: {host_metrics['cpu']}% | Host RAM: {host_metrics['memory']}%[/dim]")
