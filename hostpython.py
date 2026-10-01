"""One canonical interpreter, resolved by the standard library.

`PYTHON` overrides every consumer (Makefile, tests, MCP client configs).
`MINIMUM` is the floor the code requires. `CANDIDATES` lists the names probed,
in order, when no override is set.
"""

import os
import shutil
import sys

# Oldest CPython the code has been exercised on.
MINIMUM = (3, 10)

# Versioned names first, so an unrelated `python3` earlier on PATH cannot decide.
CANDIDATES = ("python3.14", "python3.13", "python3.12", "python3.11", "python3.10")


def host_interpreter():
    """The absolute path of the interpreter to use, or None when none qualifies.

    PYTHON wins when set and usable. Otherwise the first `CANDIDATES` name on
    PATH, falling back to `python3`.
    """
    override = os.environ.get("PYTHON")
    if override:
        resolved = shutil.which(override)
        if resolved is None and os.path.isfile(override):
            resolved = os.path.abspath(override)
        return resolved
    for name in CANDIDATES:
        resolved = shutil.which(name)
        if resolved:
            return resolved
    return shutil.which("python3")


def describe(interpreter):
    """`path (X.Y.Z)` for a resolved interpreter, for failure messages."""
    return f"{interpreter} ({sys.version.split()[0]})"


if __name__ == "__main__":
    resolved = host_interpreter()
    if resolved is None:
        print(f"No Python interpreter found (need CPython >= {'.'.join(map(str, MINIMUM))})",
              file=sys.stderr)
        raise SystemExit(1)
    if sys.version_info < MINIMUM:
        print(f"{sys.version.split()[0]} is below the required floor "
              f"{'.'.join(map(str, MINIMUM))}", file=sys.stderr)
        raise SystemExit(1)
    print(resolved)
