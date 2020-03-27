#!/usr/bin/env python3
import os
import threading

start_commands = [
    "terminator -e 'python3 -m indexing_service.src.main'",
    "terminator -e 'python3 -m search_service.src.main'",
    "terminator -e 'python3 -m telegram_bot.src.main'",
    "terminator -e './web_backend/manage.py runserver'",
    "terminator -e 'cd web_frontend; npm start; bash'",
    "terminator -e 'ssh -R 80:localhost:8000 ssh.localhost.run'"
]
for command in start_commands:
    threading.Thread(target=lambda: os.system(command)).start()
