import sys
import math


"""
Soliton that get me to the gold 4000/7000
Easy and fast to write, good enough, but could better (solution2.py)
"""

distances = {
    "short1": 500,
    "short2": 650,
    "long": 5000,
}
MAX_THRUST = 100
BOOST = "BOOST"

STOP_ANGLE = 90
BOOST_ANGLE = 5
ACCELERATION_CONST = 3

x, y = 0, 0
while True:
    # read input data
    prev_x, prev_y = x, y
    (
        x,
        y,
        next_checkpoint_x,
        next_checkpoint_y,
        next_checkpoint_dist,
        next_checkpoint_angle,
    ) = [int(i) for i in input().split()]
    opponent_x, opponent_x = [int(i) for i in input().split()]

    # check distance
    if next_checkpoint_dist < distances["medium1"]:
        thrust = MAX_THRUST // 3
    elif next_checkpoint_dist < distances["short2"]:
        thrust = MAX_THRUST // 5
    else:
        thrust = MAX_THRUST

    # check angle
    if abs(next_checkpoint_angle) > STOP_ANGLE:
        thrust = 0

    # check for boost
    if (
        next_checkpoint_dist > distances["long"]
        and abs(next_checkpoint_angle) < BOOST_ANGLE
    ):
        thrust = BOOST

    # next_coord - 3*delta (logic1.png), in order to reduce accaleration the more closer car is to the target
    move_x = next_checkpoint_x - ACCELERATION_CONST * (x - prev_x)
    move_y = next_checkpoint_y - ACCELERATION_CONST * (y - prev_y)

    print(f"{move_x} {move_y} {thrust}")
    print(
        "Debug messages...",
        next_checkpoint_dist,
        next_checkpoint_angle,
        file=sys.stderr,
        flush=True,
    )
