import os


def string():
    try:
        with open(os.path.dirname(__file__) + "/VERSION", "r", encoding="utf-8") as fd:
            version = fd.read().strip()
            if version:
                return version
    except Exception:
        return "unknown (git checkout)"
