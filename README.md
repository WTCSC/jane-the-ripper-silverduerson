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

```bash
python crack_md5.py
