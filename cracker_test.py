import hashlib
from pathlib import Path
import pytest
from hash_cracker import crack_passwords

def md5(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()

def write_file(path: Path, lines):
    path.write_text("\n".join(lines) + "\n")

def test_crack_single_match(tmp_path):
    wordlist = ["apple", "banana", "secretpw", "123456"]
    hashes = [md5("secretpw")]

    wfile = tmp_path / "wordlist.txt"
    hfile = tmp_path / "hashes.txt"
    write_file(wfile, wordlist)
    write_file(hfile, hashes)

    matches = crack_passwords(str(hfile), str(wfile))
    assert len(matches) == 1
    assert matches[0][0] == "secretpw"
    assert matches[0][1] == md5("secretpw")

def test_crack_multiple_and_ignore_blank_lines(tmp_path):
    wordlist = ["pass1", "", "hello", "PaSsWoRd"]
    hashes = [md5("hello"), md5("PaSsWoRd")]

    wfile = tmp_path / "wordlist2.txt"
    hfile = tmp_path / "hashes2.txt"
    write_file(wfile, wordlist)
    write_file(hfile, hashes)

    matches = crack_passwords(str(hfile), str(wfile))
    found_pw = {pw for pw, _ in matches}
    assert found_pw == {"hello", "PaSsWoRd"}

def test_no_matches(tmp_path):
    wordlist = ["a","b","c"]
    hashes = [md5("notinthelist")]

    wfile = tmp_path / "w3.txt"
    hfile = tmp_path / "h3.txt"
    write_file(wfile, wordlist)
    write_file(hfile, hashes)

    matches = crack_passwords(str(hfile), str(wfile))
    assert matches == []
