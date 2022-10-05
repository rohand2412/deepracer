class PARAMS:
    prev_progress = None
    prev_steps = None

def reward_function(params):
    if PARAMS.prev_steps is None or params['steps'] < PARAMS.prev_steps:
        PARAMS.prev_progress = params['progress']

    diff = params['progress'] - PARAMS.prev_progress
    reward = (10 ** (5 * min(diff, 0.3) + 1)) * diff

    PARAMS.prev_progress = params['progress']
    PARAMS.prev_steps = params['steps']
    return float(reward)
