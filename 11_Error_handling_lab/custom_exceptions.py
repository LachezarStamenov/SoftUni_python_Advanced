
# class ValueTooSmallException(Exception):
#     pass
#
#
# value = int(input())
#
# if value < 10:
#     raise ValueTooSmallException(f'{value} should be equal or greater than 10')

class ValueCannotBeNegative(Exception):
    pass


values = [int(input()) for _ in range(5)]

for value in values:
    if value < 0:
        raise ValueCannotBeNegative