from datetime import datetime
import atexit
from application.salary import calculate_salary
from application.db.people import get_employeers
import asyncio

@atexit.register
def print_time():
    print(datetime.now())

async def main():
    task1 = asyncio.create_task(calculate_salary())
    task2 = asyncio.create_task(get_employeers())
    await asyncio.gather(task1,task2)
    
if __name__ == '__main__':
    asyncio.run(main())
