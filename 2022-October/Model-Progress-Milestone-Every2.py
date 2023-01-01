class PARAMS:
    prev_progress = None
    prev_steps = None
    last_milestone = 0
    last_steps = 0

def reward_function(params):
    if PARAMS.prev_steps is None or params['steps'] < PARAMS.prev_steps:
        PARAMS.prev_progress = params['progress']
        PARAMS.last_milestone = 0
        PARAMS.last_steps = 0

    reward = 0
    pi = int(params['progress'] // 2)
    if pi > PARAMS.last_milestone:
        reward += 50 - (params['steps'] - PARAMS.last_steps)
        PARAMS.last_milestone = pi
        PARAMS.last_steps = params['steps']

    PARAMS.prev_progress = params['progress']
    PARAMS.prev_steps = params['steps']
    return float(reward)
