#!/usr/bin/env python3
import os
import threading

threading.Thread(target=lambda: os.system("terminator -e 'python3 -m indexing_service.src.main'")).start()
threading.Thread(target=lambda: os.system("terminator -e 'python3 -m search_service.src.main'")).start()
threading.Thread(target=lambda: os.system("terminator -e 'python3 -m telegram_bot.src.main'")).start()
threading.Thread(target=lambda: os.system("terminator -e './web_backend/manage.py runserver'")).start()
threading.Thread(target=lambda: os.system("terminator -e 'cd web_frontend; npm start; bash'")).start()
threading.Thread(target=lambda: os.system("terminator -e 'ssh -R 80:localhost:8000 ssh.localhost.run'")).start()
