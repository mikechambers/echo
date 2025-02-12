from datetime import timedelta

def format_elapsed_time(elapsed_seconds):
    elapsed = timedelta(seconds=elapsed_seconds)
    parts = []

    hours, remainder = divmod(elapsed.total_seconds(), 3600)
    if hours:
        parts.append(f"{int(hours)} hour{'s' if hours > 1 else ''}")

    minutes, seconds = divmod(remainder, 60)
    if minutes:
        parts.append(f"{int(minutes)} minute{'s' if minutes > 1 else ''}")

    if seconds or not parts:
        parts.append(f"{int(seconds)} second{'s' if seconds > 1 else ''}")

    return ", ".join(parts)