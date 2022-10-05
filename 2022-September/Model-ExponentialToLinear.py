class PARAMS:
    prev_progress = None
    prev_steps = None

def reward_function(params):
    if PARAMS.prev_steps is None or params['steps'] < PARAMS.prev_steps:
        PARAMS.prev_progress = params['progress']

    diff = params['progress'] - PARAMS.prev_progress

    threshold = 0.125
    constant_slope = 1.75
    base = 2
    shrink = 5

    if diff <= threshold:
        reward = (base ** (shrink * diff)) * diff
    else:
        reward = constant_slope * (diff - threshold) + ((base ** (shrink * threshold)) * threshold)

    PARAMS.prev_progress = params['progress']
    PARAMS.prev_steps = params['steps']
    return float(reward)