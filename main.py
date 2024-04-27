from snowflake import Snowflake
from base62_converter import to_base62

# Example usage:
snowflake = Snowflake(worker_id=1)
for _ in range(10):
    val = snowflake.generate_id()
    # print(to_base62(val))
    print(val)