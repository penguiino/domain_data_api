import json
from functools import lru_cache
from pathlib import Path

_file_mtime_cache = {}

@lru_cache(maxsize=None)
def load_json(path: str, auto_reload: bool = True):
    """
    Load JSON file with caching and optional auto-reload.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"{path} does not exist.")

    if auto_reload:
        mtime = file_path.stat().st_mtime
        last_mtime = _file_mtime_cache.get(path)
        if last_mtime is None or mtime > last_mtime:
            load_json.cache_clear()
            _file_mtime_cache[path] = mtime

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
