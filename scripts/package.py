from __future__ import annotations

import hashlib
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "theme.tar.gz"
INCLUDE = [ROOT / "dist", ROOT / "theme.json", ROOT / "preview.png", ROOT / "THIRD_PARTY_NOTICES.txt"]

with tarfile.open(ARCHIVE, "w:gz", format=tarfile.PAX_FORMAT) as archive:
    for source in INCLUDE:
        entries = [source]
        if source.is_dir():
            entries.extend(sorted(source.rglob("*")))
        for path in entries:
            arcname = path.relative_to(ROOT).as_posix()
            info = archive.gettarinfo(str(path), arcname)
            info.uid = info.gid = 0
            info.uname = info.gname = "root"
            info.mode = 0o755 if path.is_dir() else 0o644
            if path.is_file():
                with path.open("rb") as file:
                    archive.addfile(info, file)
            else:
                archive.addfile(info)

digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
(ROOT / "theme.tar.gz.sha256").write_text(f"{digest}  theme.tar.gz\n", encoding="ascii")
print(f"built {ARCHIVE.name} ({ARCHIVE.stat().st_size} bytes) sha256={digest}")
