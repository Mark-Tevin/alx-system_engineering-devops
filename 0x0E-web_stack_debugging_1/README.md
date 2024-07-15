# Web stack debugging #1

> we create a symbolic link between configuration files located at
```
> /etc/nginx/sites-available/default
and
/etc/nginx/sites-enabled/default
The sites-available directory contains the available configuration files,
while the sites-enabled directory contains the enabled or active configuration files.
By creating a symbolic link, any changes made to the default file in the sites-available directory
will be reflected in the default file in the
sites-enabled directory.
```
> kill "$(pgrep 'nginx' | head -1)"
This command finds the process ID(PID) on the first Nginx process by using'the pgrep command and then
> sends a termination signal (SIGTERM) to that process using the kill command
