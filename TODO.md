# To-Do

- Separate dev/prod heads
- SSH keys
- Data transfer
    pg_dumpall | gzip > db.sql.gz
    scp db.sql.gz matt@mccarthywebdesign.com:~
    psql -f db.sql postgres
    rm db.sql
- Set timezone on production
    sudo timedatectl set-timezone America/Chicago
- Separate dev/prod heads
