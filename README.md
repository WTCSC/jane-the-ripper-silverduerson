# Hash Cracker

A small, easy-to-read Python script that tries to match MD5 hashes using a wordlist.  

---

## Quick Summary

- **Input:** a file with MD5 hashes (one per line) and a wordlist (one password per line).  
- **Output:** prints any found `password = hash` pairs.  
- **Dependencies:** None, uses Python standard library.

---
## Decision Tree
Start                                                
 │                                                
 ▼                                                                    
Read hash file (line-by-line)                                                    
 │                                                        
 ├─ Is line empty? ── Yes ──> Skip line                                            
 │                     No                                      
 │                                                  
 ▼                                                    
Add hash to target set                                        
 │                                                                
 ▼                                                        
Read wordlist (line-by-line)                                          
 │                                                    
 ├─ Is line empty? ── Yes ──> Skip line                            
 │                     No                                          
 │                                      
 ▼                                      
Compute MD5(candidate)                                                  
 │                                      
 ├─ Is MD5 in target set? ── No ──> Continue with next word                          
 │                           Yes                                  
 │                                                                                                          
 ▼                                              
Store match (password, hash)                                            
 │                                            
 ▼                                                  
All words processed?                                      
 │                                                
 ├─ No ──> Continue reading words                                      
 │                                                              
 └─ Yes ──> Print results (matches or "No matches found")
 │                                  
 ▼                                    
End                                        

---

## Requirements

- Python 3.8+  
- Two text files:  
  - `hashes.txt` — one MD5 hash per line (hex)  
  - `wordlist.txt` — one candidate password per line

---

## How to Run (Interactive)

bash
`python crack_md5.py`

## Testing the Hash Cracker

This project includes **automated tests** using `pytest` to ensure the `crack_passwords` function works correctly.  

### Test Overview

1. **`test_crack_single_match`**  
   - Checks that a single password in the wordlist correctly matches its MD5 hash.  

2. **`test_crack_multiple_and_ignore_blank_lines`**  
   - Checks multiple passwords, including ignoring blank lines in the wordlist.  

3. **`test_no_matches`**  
   - Ensures that no matches are returned when the hashes do not appear in the wordlist.

### Test Utilities

- `md5(s: str) -> str` — helper function to compute MD5 hashes of strings.  
- `write_file(path: Path, lines)` — helper to write test wordlists and hash files.

### Running the Tests

Make sure `pytest` is installed:

```bash
pip install pytest

Run all tests from the project root:

pytest

Example output if all tests pass:

============================= test session starts =============================
platform linux -- Python 3.x.x, pytest-x.x.x
collected 3 items

test_hash_cracker.py ...                                               [100%]

============================== 3 passed in 0.05s ==============================

File Structure for Tests

.
├─ hash_cracker.py      # main script
├─ test_hash_cracker.py # pytest test file
├─ README.md
└─ ...
