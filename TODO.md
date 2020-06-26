# To-Do

- Change color of first panel chevron on homepage
- Data transfer
  - Staging

    ```sh
    sudo -u postgres pg_dumpall | gzip > /tmp/db.sql.gz
    ```

  - Local

    ```sh
    scp matt@staging.mccarthywebdesign.com:~/db.sql.gz /tmp
    scp /tmp/db.sql.gz matt@mccarthywebdesign.com:~
    ```

  - Production

    ```sh
    psql -f /tmp/db.sql postgres
    ```
