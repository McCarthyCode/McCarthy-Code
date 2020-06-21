# To-Do

- Titles
- Footer date
- margin-bottom: 1rem to h1-h3
- SSH keys
- Data transfer
    pg_dumpall | gzip > db.sql.gz
    scp db.sql.gz matt@mccarthywebdesign.com:~
    psql -f db.sql postgres
    rm db.sql
- Set timezone on production
    sudo timedatectl set-timezone America/Chicago
