
class PARAMS:
    prev_on_turn = None

on_turn = True

if on_turn and not PARAMS.prev_on_turn:
    print("Worked")