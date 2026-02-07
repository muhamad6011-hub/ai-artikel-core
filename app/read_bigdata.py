from pathlib import Path

ARTIKEL_FOLDERS = [Path(f"artikel-0{i}") for i in range(1, 6)]

def read_bigdata():
    """Membaca semua artikel dan mengembalikan dict {folder: content}"""
    bigdata = {}
    for folder in ARTIKEL_FOLDERS:
        artikel_file = folder / "artikel.txt"
        if artikel_file.exists():
            content = artikel_file.read_text(encoding="utf-8")
            bigdata[folder.name] = content
    return bigdata
