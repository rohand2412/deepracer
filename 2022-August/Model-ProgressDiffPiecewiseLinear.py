class PARAMS:
    prev_progress = None
    prev_steps = None
    prev_x = None
    prev_y = None

def reward_function(params):
    if PARAMS.prev_steps is None or params['steps'] < PARAMS.prev_steps:
        PARAMS.prev_progress = params['progress']

    diff = params['progress'] - PARAMS.prev_progress
    if diff > 0.2:
        reward = 100 * diff
    else:
        reward = 10 * diff

    PARAMS.prev_progress = params['progress']
    PARAMS.prev_steps = params['steps']
    return float(reward)