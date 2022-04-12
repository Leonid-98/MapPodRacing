import sys
import math

"""
Soliton that get me to the gold 900/7000
"""
distances = {
    "medium1": 1050,
    "medium2": 1200,
    "medium3": 1500,
    "long": 4000,
}
MAX_THRUST = 100
BOOST = "BOOST"
SHIELD = "SHIELD"


laps = int(input())
checkpoint_count = int(input())
checkpoints = []
for _ in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoints.append((checkpoint_x, checkpoint_y))

INGAME_INPUTS = 2
while True:
    for _ in range(INGAME_INPUTS):
        # read input data
        x, y, vx, vy, rotation_angle, next_check_point_id = [
            int(j) for j in input().split()
        ]
        next_checkpoint_x = checkpoints[next_check_point_id][0]
        next_checkpoint_y = checkpoints[next_check_point_id][1]
        next_checkpoint_dist = math.hypot(
            abs(x - next_checkpoint_x), abs(y - next_checkpoint_y)
        )

        # check distance
        if next_checkpoint_dist < distances["medium3"]:
            thrust = MAX_THRUST // 3
        elif next_checkpoint_dist < distances["medium1"]:
            thrust = MAX_THRUST // 5
        elif next_checkpoint_dist > distances["long"]:
            thrust = BOOST
        else:
            thrust = MAX_THRUST

    coord_enemies = []
    for _ in range(INGAME_INPUTS):

        pod_x, pod_y, pod_vx, pod_vy, pod_rotation_angle, pod_next_check_point_id = [
            int(j) for j in input().split()
        ]
        coord_enemies.append((pod_x, pod_y))

        enemy_x = coord_enemies[0][0]
        enemy_y = coord_enemies[0][1]

        dist_between_enemy = math.hypot(abs(x - pod_x), abs(y - pod_y))
        if dist_between_enemy < distances["medium2"]:
            thurst = SHIELD

    enemy_x = enemy_x - 3 * vx
    enemy_y = enemy_y - 3 * vy
    print(f"{enemy_x} {enemy_y} {thrust}")

    move_x = next_checkpoint_x - 3 * vx
    move_y = next_checkpoint_y - 3 * vy
    print(f"{move_x} {move_y} {thrust}")
