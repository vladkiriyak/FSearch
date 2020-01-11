async def put_log_in_file(message: str, path_file: str = "/home/vlad/FSearch/telegram_bot/log/log_file.txt"):
    import time
    import aiofiles as aiof

    if not path_file:
        print(f"{time.ctime(time.time())} {message}")
    else:
        async with aiof.open(path_file, mode='a') as log_file:
            await log_file.write(f"{time.ctime(time.time())} {message}\n")
            await log_file.flush()
