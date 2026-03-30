# Class Activity 1 — System Calls in Practice

- Student Name: Chhi Layhorng
- Student ID: p20240050

---

## Task 1: File Creator & Reader

### Part A — File Creator

1. Flags:
O_WRONLY → write only  
O_CREAT → create file if not exist  
O_TRUNC → clear file content  

2. 0644:
Owner = read + write  
Group = read  
Others = read  

3. fopen() automatically opens file, handles buffering, and manages file pointer.

---

### Part B — File Reader

1. read() returns number of bytes read.  
fgets() reads line by line.

2. Loop is needed because read() reads small chunks.  
It stops when read() returns 0 (end of file).

---

## Task 2: Directory Listing

1. readdir() returns a struct dirent (contains file name, inode, etc.)

2. stat() provides:
- file size  
- permissions  
- last modified time  

3. write() only prints strings, so we use snprintf() to convert numbers to string.

---

## Task 3: strace Analysis

1. Library version uses more system calls than system call version.

2. Extra system calls:
- brk() → memory allocation  
- mmap() → load libraries  
- fstat() → file information  
- access() → permission check  

3. fprintf() may result in one or more write() calls due to buffering.

4. Difference:
System calls directly interact with the kernel.  
Library functions are wrappers that use system calls and add extra features.

---

## Task 4: OS Structure

1. /proc is a virtual filesystem created by the kernel. It is not stored on disk.

2. Linux uses a monolithic kernel.

3. Memory regions:
- heap  
- stack  
- shared libraries  

4. uname -a shows:
- kernel version  
- system architecture  
- OS information  

5. /proc shows that OS acts as intermediary between user programs and hardware.

---

## Reflection

I learned that system calls interact directly with the operating system kernel, while library functions provide a higher-level interface. I also learned how Linux exposes system information through /proc and how system calls work behind the scenes.
