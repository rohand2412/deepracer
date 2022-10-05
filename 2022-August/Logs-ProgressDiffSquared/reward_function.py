class PARAMS:
    prev_progress = 0
    prev_steps = None

def reward_function(params):
    if PARAMS.prev_steps is None or params['steps'] < PARAMS.prev_steps:
        PARAMS.prev_progress = 0

    reward = (100 * (params['progress'] - PARAMS.prev_progress)) ** 2

    PARAMS.prev_progress = params['progress']
    PARAMS.prev_steps = params['steps']
    return float(reward)
