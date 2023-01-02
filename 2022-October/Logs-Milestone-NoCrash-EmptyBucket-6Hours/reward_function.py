class PARAMS:
    prev_progress = None
    prev_steps = None
    last_milestone = 0
    last_steps = 0
    reward_bucket = 0

def reward_function(params):
    if PARAMS.prev_steps is None or params['steps'] < PARAMS.prev_steps:
        PARAMS.prev_progress = params['progress']
        PARAMS.last_milestone = 0
        PARAMS.last_steps = 0
        PARAMS.reward_bucket = 0

    reward = 0
    pi = int(params['progress'] // 2)
    if pi > PARAMS.last_milestone:
        reward += 30 - (params['steps'] - PARAMS.last_steps)
        PARAMS.last_milestone = pi
        PARAMS.last_steps = params['steps']

    if params['progress'] != 100 and (not params['all_wheels_on_track'] or params['is_offtrack'] or params['is_crashed']):
        PARAMS.reward_bucket += reward
        reward = 0
    else:
        reward += PARAMS.reward_bucket
        PARAMS.reward_bucket = 0

    PARAMS.prev_progress = params['progress']
    PARAMS.prev_steps = params['steps']
    return float(reward)

