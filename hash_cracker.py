import hashlib
from typing import List, Tuple

def crack_passwords(hash_file_path: str, wordlist_path: str) -> List[Tuple[str, str]]:
    targets = set()
    with open(hash_file_path, "r", encoding="utf-8", errors="ignore") as hf:
        for line in hf:
            h = line.strip().lower()
            if h:
                targets.add(h)

    found = []
    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wf:
        for line in wf:
            pw = line.strip()
            if not pw:
                continue
            md5 = hashlib.md5(pw.encode()).hexdigest()
            if md5 in targets:
                found.append((pw, md5))
    return found

if __name__ == "__main__":
    hpath = input("Path to hash file: ").strip()
    wpath = input("Path to wordlist file: ").strip()
    matches = crack_passwords(hpath, wpath)
    if matches:
        print("These are the cracked hashes:")
        for pw, h in matches:
            print(f"{pw} = {h}")
    else:
        print("No matches found.")
