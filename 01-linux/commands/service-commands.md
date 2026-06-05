# Linux Service and Logging Commands

## systemctl status

Purpose:

Display service status information.

Example:

systemctl status cron

Shows:

- Service state
- PID
- Memory usage
- CPU usage
- Recent logs

---

## systemctl start

Purpose:

Start a service.

Example:

sudo systemctl start cron

---

## systemctl stop

Purpose:

Stop a service.

Example:

sudo systemctl stop cron

---

## systemctl restart

Purpose:

Restart a service.

Example:

sudo systemctl restart cron

---

## systemctl enable

Purpose:

Configure a service to automatically start after system boot.

Example:

sudo systemctl enable cron

---

## journalctl

Purpose:

Display system logs collected by systemd.

Example:

journalctl

---

## journalctl -n 20

Purpose:

Display the most recent 20 log entries.

Example:

journalctl -n 20

---

## journalctl -u service

Purpose:

Display logs for a specific service.

Example:

journalctl -u cron

---

## ls /var/log

Purpose:

Display available Linux log files.

Example:

ls /var/log
