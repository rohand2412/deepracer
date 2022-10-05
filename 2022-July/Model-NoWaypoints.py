import math

def get_norm_dist(x, dist_data):
    return dist_data['scalar'] * (math.e ** (-0.5 * ((x - dist_data['mean'])/dist_data['std']) ** 2)) / (dist_data['std'] * math.sqrt(2 * math.pi))

def reward_function(params):

    reward = 2.0

    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    steering_angle = params['steering_angle']

    center_dist_percent = distance_from_center / track_width

    center_reward_dist = {
        'mean': 0,
        'std': 0.75 / math.sqrt(2 * math.pi),
        'scalar': 1.5
    }

    reward += get_norm_dist(center_dist_percent, center_reward_dist)

    center_speed_dist = {
        'mean': 0,
        'std': 0.75 / math.sqrt(2 * math.pi),
        'scalar': 1.125
    }

    speed_reward_dist = {
        'mean': 0,
        'std': 0.25 / math.sqrt(2 * math.pi),
        'scalar': 0.5
    }

    speed_diff = abs(get_norm_dist(center_dist_percent, center_speed_dist) - speed)
    reward += get_norm_dist(speed_diff, speed_reward_dist)

    SPEED_THRESHOLD = 0.75 #m/s
    DISTANCE_THRESHOLD = 0.50 #percent
    STEERING_FAST_CLOSE_THRESHOLD = 5
    STEERING_SLOW_FAR_THRESHOLD = 15

    if speed >= SPEED_THRESHOLD \
        and center_dist_percent < DISTANCE_THRESHOLD \
        and steering_angle <= STEERING_FAST_CLOSE_THRESHOLD:
        reward += 2.0
    elif speed < SPEED_THRESHOLD \
        and center_dist_percent >= DISTANCE_THRESHOLD \
        and steering_angle <= STEERING_SLOW_FAR_THRESHOLD:
        reward += 2.0

    return float(reward)
