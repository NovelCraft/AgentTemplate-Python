import asyncio

import novelcraft.sdk as sdk


async def main():
    await sdk.initialize()
    sdk.get_logger().info('Hello, world!')
    await asyncio.sleep(30)
    await sdk.finalize()
    sdk.get_logger().info('Goodbye, world!')

if __name__ == '__main__':
    asyncio.run(main())
