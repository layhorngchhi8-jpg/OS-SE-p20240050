Student name: Chhi Layhorng
Student ID: p20240050
Server username: se-chhi-layhorng
Exam scenario value (COMPANY / PRODUCT): OrbitWorks / Relay Pass
Date & start time: 2026-06-30, [FILL IN START TIME]
AI assistant used (name/none): Claude (Anthropic)

---

## Part A — Threads, Kernel Mapping & Signals

- thread_demo.c: spawns 3 worker threads, each computes a value, main joins all and prints summary.
- Screenshot: images/a1_thread_run.png
- thread_map.txt: captured shared PID, distinct thread/LWP ids while process was alive.
- signal_demo.c: handles SIGINT and SIGTERM, prints cleanup message, exits cleanly.
- Screenshot: images/a2_signal_catch.png

Written: A worker thread shares the same address space and memory as the main thread, so when it returns a value via pthread_join, the main thread reads it directly from shared memory. A forked child gets its own separate copy of the process's memory (copy-on-write), so any value it computes lives only in its own address space and is not visible to the parent unless explicitly sent back via IPC (pipes, shared memory, exit status, etc).

## Part B — Files, Permissions & Special Bits

- perm_report.txt: ls -l / ls -ld / stat output for private file (600) and shared directory.
- setuid_demo.c: prints real and effective UID. Setuid bit set, but since the binary is owned by se-chhi-layhorng (not root), the effective UID can only become se-chhi-layhorng's own UID when run by another user -- it cannot escalate to root.
- Screenshot: images/b1_special_bits.png

Written: 600 -> rw-------

## Part C — Bash Scripting, PATH & Safe File Scanning

- scripts/greeter: prints current user, logged-in user count, uptime, and a random message from an array. Runs by name via PATH.
- path_report.txt: PATH contents + `which greeter` / `type greeter` resolved location.
- scripts/collector: loops over candidate files, checks -e and -r before reading, writes consolidated report, skips missing/unreadable files without crashing.
- Screenshot: images/c1_collector_run.png

Written (C1): greeter failed to run by name before adding ~/bin to PATH because the shell only resolves bare command names by searching directories listed in PATH; ~/bin was not in that list, so only the explicit ./greeter form (bypassing PATH lookup) worked.

Written (C2): Checking -e and -r before calling cat avoids the script crashing on "No such file" or "Permission denied" errors; instead it logs a clean [SKIP] reason and continues to the next file in the array.

## Part D — Concurrency, Race Condition & File Locking

- scripts/buy_relay_pass: validates buyer/quantity input, reads stock file (init 150), decrements stock, logs sale with student id p20240050. Patched with `flock -x` exclusive advisory lock around the read-modify-write critical section.
- scripts/swarm: launches 40 concurrent purchases in background, waits, reports final stock.
- observations.txt: patched swarm runs all landed at the correct final stock of 110 (150 - 40). Unpatched baseline not separately captured before patching (noted honestly per exam allowance); TOCTOU reasoning given for why unpatched runs would lose updates.
- Screenshot: images/d2_patched.png

Written: With unpatched read-modify-write split into 3 non-atomic steps, multiple buyer processes can read the same stock value before any of them writes back. Each computes its own decrement from that stale read, and whichever writes last overwrites earlier writes, silently discarding other buyers' decrements (a lost update). Fewer decrements survive than purchases logged, so final stock ends up higher than the correct 110.

## Part E — Backups, Archiving & cron Automation

- scripts/backup_project: timestamped compressed tar.gz of sample_project, retains newest 2 archives, prunes older ones. Verified exactly 2 archives remain after repeated runs.
- Screenshot: images/e1_backup_retention.png
- scripts/timed_job: appends timestamped line to a given output file.
- Per-user crontab: recurring (every 1 min) -> logs/cron_recurring.log; one-shot at 14:35 today -> logs/cron_oneshot.log. Both confirmed firing (see cron_report.txt).
- scripts/backup_exam: tars final-exam/ folder to ~/exam-backups/final-exam-<timestamp>.tar.gz (outside repo). Crontab: short interval (every 2 min) + one-shot at 16:00 today.
- cron_report.txt: crontab -l output + log contents + exam-backups listing.

Written: tar alone only archives/bundles files together with header metadata -- it does not reduce total bytes. The -z flag pipes the tar stream through gzip, which is what actually shrinks the byte count by exploiting redundancy in the data. Compression, not archiving, is what reduced the size.

## Notes / Incomplete items

- [List anything not finished, e.g. 16:00 backup_exam one-shot still pending at submission time, live curveballs pending/completed]
