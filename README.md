# Pro104-Auto-Puncher
Automatically punch in and out for 104企業大師 system

## Get started
1. Please create `.env` and provide environment variables in it. For `PUNCH_MINUTE`, `PUNCH_HOUR`, `PUNCH_DAY_OF_WEEK`, and `TIMEZONE`, please refer to [`celery`](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html) for the setting.
```
ACUD=
ACCOUNT=
PASSWORD=
PUNCH_MINUTE=
PUNCH_HOUR=
PUNCH_DAY_OF_WEEK=
TIMEZONE=
```
For example:
```
ACUD=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
ACCOUNT=XXXXX@example.com
PASSWORD=XXXXXXXXXX
PUNCH_MINUTE="0"
PUNCH_HOUR="9,18"
PUNCH_DAY_OF_WEEK="mon,tue,wed,thu,fri"
TIMEZONE="Asia/Taipei"
```
2. For the `ACUD`, please log in [https://bsignin.104.com.tw/login](https://bsignin.104.com.tw/login) to get the `ACUD` from cookies.
3. Make sure you have `docker-compose`, then:
```bash
docker-compose up --build -d
```
4. Everything is done!

## Troubleshooting
Reomve the comment in the `docker-compose.yml`. Then you can see the login and punch process at `http://localhost:7900`.
```yml
version: "3"
services:
  chrome-puncher:
    image: selenium/standalone-chrome:119.0-chromedriver-119.0
    container_name: pro-puncher-chrome
    privileged: true
    shm_size: 16gb
    ports:
      - "4444:4444"  # monitor panel
      - "7900:7900"  # to check the process with the browser
    environment:
      - SE_VNC_NO_PASSWORD=1  # the password setting for the viewer
    stdin_open: true
    tty: true
```
