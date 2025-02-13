# Copyright (c) 2025 Mike Chambers
# https://github.com/mikechambers/echo
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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