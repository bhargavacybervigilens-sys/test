from __future__ import annotations

import os


def basename_windows(path: str | None) -> str | None:
    if not path:
        return None
    return os.path.basename(path.replace("\\", "/"))
