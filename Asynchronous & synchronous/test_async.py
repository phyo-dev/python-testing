import asyncio

async def main():
    task = asyncio.create_task(otherFunction())
    print("A")
    await asyncio.sleep(1)
    print("B")
    await task

async def otherFunction():
    print("1")
    await asyncio.sleep(2)
    print("2")

asyncio.run(main())

# output -
# A
# 1
# B
# 2
