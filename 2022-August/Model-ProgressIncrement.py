class PARAMS:
    prev_progress = None
    prev_steps = None
    last_milestone = 0

def reward_function(params):
    if PARAMS.prev_steps is None or params['steps'] < PARAMS.prev_steps:
        PARAMS.prev_progress = params['progress']
        PARAMS.last_milestone = 0

    diff = params['progress'] - PARAMS.prev_progress
    if diff >= 0:
        reward = 18 * (diff ** 2)
    else:
        reward = -18 * (diff ** 2)

    pi = int(params['progress'] // 10)
    if pi > PARAMS.last_milestone:
        reward += (10 * params['progress'] / params['steps']) ** (pi)
        PARAMS.last_milestone = pi

    PARAMS.prev_progress = params['progress']
    PARAMS.prev_steps = params['steps']
    return float(reward)