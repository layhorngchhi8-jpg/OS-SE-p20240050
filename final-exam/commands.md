# Commands Log — Final Exam (p20240050)

## Part A
gcc -pthread thread_demo.c -o thread_demo
./thread_demo
ps -eLf | grep thread_demo
gcc signal_demo.c -o signal_demo
./signal_demo
(Ctrl+C sent to trigger SIGINT handler)

## Part B
mkdir -p ~/permtest/shared
touch ~/permtest/private.txt
chmod 600 ~/permtest/private.txt
chmod 711 ~/permtest/shared
ls -l ~/permtest/private.txt
ls -ld ~/permtest/shared
stat ~/permtest/private.txt
chmod g+s ~/permtest/shared
chmod +t ~/permtest/shared
gcc setuid_demo.c -o setuid_demo
chmod u+s setuid_demo
./setuid_demo

## Part C
cat > ~/bin/greeter << 'GEOF'
... (script content)
GEOF
chmod +x ~/bin/greeter
export PATH="$HOME/bin:$PATH"
greeter
which greeter
type greeter

cat > ~/bin/collector << 'CEOF'
... (script content)
CEOF
chmod +x ~/bin/collector
mkdir -p ~/collector_test/dir1 ~/collector_test/dir2 ~/collector_test/dir3
chmod 000 ~/collector_test/dir3/private.txt
collector

## Part D
cat > ~/bin/buy_relay_pass << 'DEOF'
... (script content, unpatched then patched with flock -x)
DEOF
chmod +x ~/bin/buy_relay_pass

cat > ~/bin/swarm << 'SEOF'
... (script content)
SEOF
chmod +x ~/bin/swarm
swarm
swarm
swarm

## Part E
cat > ~/bin/backup_project << 'BEOF'
... (script content)
BEOF
chmod +x ~/bin/backup_project
backup_project
backup_project
backup_project
backup_project

cat > ~/bin/timed_job << 'TEOF'
... (script content)
TEOF
chmod +x ~/bin/timed_job

cat > ~/bin/backup_exam << 'AEOF'
... (script content)
AEOF
chmod +x ~/bin/backup_exam
backup_exam

crontab -e
# added:
# * * * * * timed_job -> cron_recurring.log
# 35 14 30 6 * timed_job -> cron_oneshot.log
# */2 * * * * backup_exam -> backup_exam_recurring.log
# 0 16 30 6 * backup_exam -> backup_exam_oneshot.log
crontab -l
