import math
import numpy as np

class PARAMS:
    waypoints = np.array([
        [-4.34030972, -2.06504005],
        [-4.08804741, -2.18648419],
        [-3.82060876, -2.29226565],
        [-3.54208166, -2.38558323],
        [-3.25597406, -2.46969921],
        [-2.96524402, -2.54780915],
        [-2.67207001, -2.62310862],
        [-2.37904922, -2.69767043],
        [-2.08600993, -2.77113446],
        [-1.79294083, -2.84303647],
        [-1.4998361 , -2.91289114],
        [-1.20669947, -2.98018996],
        [-0.91354779, -3.04439527],
        [-0.62041474, -3.1049302 ],
        [-0.32735469, -3.16117177],
        [-0.0344466 , -3.21248494],
        [ 0.25820535, -3.25824412],
        [ 0.55041772, -3.29714782],
        [ 0.84191597, -3.32776958],
        [ 1.13227359, -3.34828137],
        [ 1.42085561, -3.35655033],
        [ 1.70671915, -3.35003786],
        [ 1.98846089, -3.32564904],
        [ 2.26398754, -3.27956519],
        [ 2.52971556, -3.20599164],
        [ 2.78061835, -3.09887937],
        [ 3.00908263, -2.95046072],
        [ 3.22256882, -2.77784095],
        [ 3.42215545, -2.5841176 ],
        [ 3.60908277, -2.37219658],
        [ 3.78478808, -2.14496442],
        [ 3.95099377, -1.90543374],
        [ 4.10930971, -1.65624553],
        [ 4.26093974, -1.39947113],
        [ 4.40651781, -1.13761609],
        [ 4.54150309, -0.87932112],
        [ 4.66188545, -0.63288224],
        [ 4.77032246, -0.39324692],
        [ 4.86877427, -0.1556539 ],
        [ 4.95797709,  0.0830843 ],
        [ 5.03755424,  0.32510068],
        [ 5.10652784,  0.57167067],
        [ 5.16309692,  0.82334028],
        [ 5.20411027,  1.07994021],
        [ 5.22514771,  1.33999865],
        [ 5.22195157,  1.60039722],
        [ 5.18809168,  1.85629639],
        [ 5.11721918,  2.10086555],
        [ 5.00270744,  2.3250695 ],
        [ 4.83533613,  2.51359422],
        [ 4.6357221 ,  2.67370234],
        [ 4.41095592,  2.8081027 ],
        [ 4.16566414,  2.91870485],
        [ 3.90334487,  3.0069462 ],
        [ 3.62757792,  3.07509978],
        [ 3.34119739,  3.12511958],
        [ 3.04605789,  3.15755552],
        [ 2.74417353,  3.17217004],
        [ 2.44822214,  3.16692867],
        [ 2.16199089,  3.14122729],
        [ 1.88888252,  3.09291914],
        [ 1.63305989,  3.0197203 ],
        [ 1.39892194,  2.92034727],
        [ 1.1920107 ,  2.79368364],
        [ 1.01854   ,  2.63984513],
        [ 0.88651586,  2.45985659],
        [ 0.80905356,  2.2558749 ],
        [ 0.79645568,  2.03671581],
        [ 0.85120523,  1.81637471],
        [ 0.95903797,  1.60544229],
        [ 1.10789913,  1.40793591],
        [ 1.2841623 ,  1.2224364 ],
        [ 1.47568552,  1.04468307],
        [ 1.65857727,  0.87797664],
        [ 1.81851093,  0.69844827],
        [ 1.93466089,  0.49613759],
        [ 1.97969271,  0.26789137],
        [ 1.960916  ,  0.03239036],
        [ 1.88701971, -0.19618867],
        [ 1.76580053, -0.40816404],
        [ 1.60504306, -0.59751979],
        [ 1.41195633, -0.7611979 ],
        [ 1.19231834, -0.8975834 ],
        [ 0.95061528, -1.00535565],
        [ 0.69102389, -1.08359068],
        [ 0.41801197, -1.13198955],
        [ 0.13656304, -1.15083599],
        [-0.14787843, -1.14125039],
        [-0.42968585, -1.10333497],
        [-0.70346833, -1.03837381],
        [-0.9637212 , -0.9461807 ],
        [-1.20569414, -0.82749152],
        [-1.42405833, -0.68172006],
        [-1.61348562, -0.50839666],
        [-1.76690893, -0.3060533 ],
        [-1.87344295, -0.07249981],
        [-1.94087116,  0.18225779],
        [-1.97694446,  0.45127556],
        [-1.99022075,  0.72930962],
        [-1.9911871 ,  1.01181347],
        [-1.99749598,  1.29451247],
        [-2.01420008,  1.57308338],
        [-2.04624727,  1.84501797],
        [-2.09804755,  2.10741572],
        [-2.17383454,  2.35651698],
        [-2.27679275,  2.58779978],
        [-2.40906452,  2.79582396],
        [-2.57360063,  2.97168863],
        [-2.77110225,  3.10287168],
        [-2.99620893,  3.16891568],
        [-3.22960451,  3.1804594 ],
        [-3.46184896,  3.14531688],
        [-3.68701986,  3.0682451 ],
        [-3.89917414,  2.94953146],
        [-4.09461464,  2.79432295],
        [-4.27281644,  2.60959886],
        [-4.43351512,  2.39970418],
        [-4.57733351,  2.16885141],
        [-4.70539077,  1.92082431],
        [-4.81882117,  1.65868942],
        [-4.91932251,  1.3854576 ],
        [-5.00810639,  1.10327902],
        [-5.0866913 ,  0.81423784],
        [-5.15637851,  0.52004115],
        [-5.21592182,  0.22710922],
        [-5.26173563, -0.06257134],
        [-5.28824963, -0.34698401],
        [-5.29067083, -0.6237953 ],
        [-5.26477108, -0.89031942],
        [-5.2053026 , -1.14277599],
        [-5.10699238, -1.37630699],
        [-4.96299945, -1.58335898],
        [-4.78294238, -1.76582192],
        [-4.5734119 , -1.92553715]
    ])

def reward_function(params):
    # Read input parameters
    vehicle_x = params['x']
    vehicle_y = params['y']

    distances_from_route_points = np.hypot(PARAMS.waypoints[:, 0] - vehicle_x, PARAMS.waypoints[:, 1] - vehicle_y)
    closest_route_point = np.argmin(distances_from_route_points)
    normalized_distance_from_route = distances_from_route_points[closest_route_point] / (params['track_width'] * 0.5)

    MAX_REWARD = 10
    MIN_REWARD = 0

    b = -1
    a = -MAX_REWARD * b * (1.4 - b) / 1.4
    c = -a / (1.4 - b)
    reward = (a / (normalized_distance_from_route - b)) + c

    if reward > MAX_REWARD or reward < MIN_REWARD:
        reward = 0

    return float(reward)