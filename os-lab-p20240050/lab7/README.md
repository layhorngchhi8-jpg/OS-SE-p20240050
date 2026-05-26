**Student ID:** p20240050  
**Name:** se-chhi-layhorng

## Task 1 - Warm-Up Script
Created `warmup` script in `~/bin`, made it executable with `chmod +x`.

## Task 2 - Custom Command Center
Added `export PATH="$HOME/bin:$PATH"` to `.bashrc` so scripts run by name.

## Task 3 - Doorstep Login Message
Added dynamic welcome message to `.bashrc` showing username, users online, uptime, and random quote.

## Task 4 - Secure Mailbox
Created `~/public_inbox` with `chmod 733` — classmates can drop files but cannot list contents.

## Task 5 - Broadcaster
Created `broadcaster` script that writes a random secret word and timestamp to `~/public_outbox/secret.txt`.

## Task 6 - VIP Guestbook
Compiled `sign_book.c` with SUID bit (`chmod 4755`) so classmates can sign guestbook without direct file access.

## Task 7 - Data Harvester
`harvester` script loops through `/home/*`, reads readable `secret.txt` files, and saves to `harvest_report.txt`.

## Task 8 - Mailman Bot
`mailman` script reads `harvest_report.txt` and sends automated messages to classmates' inboxes.

## Answers
1. `warmup` failed before execute permission because Linux requires `+x` bit to run a file as a program.
2. Adding `~/bin` to PATH allows running scripts by name from any directory without `./`.
3. `chmod 733` allows write/execute but not read, so others can drop files but cannot list the directory.
4. Linux ignores SUID on shell scripts for security; compiled C programs respect SUID.
5. `>` overwrites a file; `>>` appends to it.
6. Harvester used `[ -f "$target_file" ] && [ -r "$target_file" ]` to check existence and readability.
7. Some classmates needed `chmod 755 ~/public_outbox` and `chmod 711 $HOME` for access.
