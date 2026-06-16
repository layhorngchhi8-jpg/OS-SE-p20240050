# Lab 10 - Backups, Archiving, Scheduling & cron Automation

**Student ID:** p20240050  
**Username:** se-chhi-layhorng

## Screenshots
- Level 0: ![level0](images/level0_warmup.png)
- Level 1: ![level1](images/level1_archive.png)
- Level 2: ![level2](images/level2_backup.png)
- Level 3: ![level3](images/level3_cron_basics.png)
- Level 4: ![level4](images/level4_session_job.png)
- Level 5: ![level5](images/level5_schedule.png)
- Level 6: ![level6](images/level6_maintenance.png)
- Level 7: ![level7](images/level7_own_job.png)
- Level 8: ![level8](images/level8_teardown.png)

## Lab Questions

1. **Archiving vs Compression:** `tar` combines many files into one without shrinking. `gzip` shrinks bytes. Only `gzip` reduces file size.

2. **Size difference:** The `.tar.gz` was much smaller than `.tar` because text files with repeated numbers compress very well.

3. **Absolute path in cron:** cron runs with a minimal environment and does not know about `~/bin`, so full paths like `/home/se-chhi-layhorng/bin/` are required.

4. **% sign and redirection:** `%` has special meaning in crontab (newline), so it must be escaped as `\%`. `>> logfile 2>&1` appends both stdout and stderr to the log file.

5. **Retention logic:** `ls -1t` lists archives newest-first, `tail -n +4` skips the 3 newest and returns the rest for deletion. Keeping only 3 prevents disk from filling up.

6. **Cron line for deadline job:** `30 14 22 6 * /home/se-chhi-layhorng/bin/deadline_job`. Minute=30, Hour=14, Day=22, Month=6 were filled in; day-of-week stayed `*`.

7. **Teardown filter vs crontab -r:** `crontab -r` deletes ALL jobs including the graded deadline job. The filter keeps only the GRADED jobs we still need.

8. **Health check usefulness:** Automated alerts catch disk full or high load before they cause outages, which is critical in real operations.

9. **Level 7 job:** My script logs free disk space every minute. Schedule: `*/1 * * * *` means every 1 minute, any hour, any day, any month, any weekday.
