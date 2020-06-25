# To-Do

- Data transfer
    pg_dumpall | gzip > db.sql.gz
    scp db.sql.gz matt@mccarthywebdesign.com:~
    psql -f db.sql postgres
    rm db.sql
