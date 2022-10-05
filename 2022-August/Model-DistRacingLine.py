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
    inner_border = np.array([
        [-4.29747677, -1.65810001],
        [-4.00641012, -1.73277295],
        [-3.71360302, -1.80763102],
        [-3.42076397, -1.88219702],
        [-3.12779689, -1.95648301],
        [-2.83473992, -2.03055596],
        [-2.54145098, -2.10441494],
        [-2.24755597, -2.17839408],
        [-1.95340002, -2.25288796],
        [-1.65966499, -2.32768703],
        [-1.36542797, -2.40267396],
        [-1.06569695, -2.48015404],
        [-0.7642709 , -2.56529093],
        [-0.4705922 , -2.65364408],
        [-0.18616679, -2.7386179 ],
        [ 0.09208944, -2.81577206],
        [ 0.36414421, -2.88187194],
        [ 0.62917483, -2.93166494],
        [ 0.9005872 , -2.96256208],
        [ 1.18027794, -2.98351002],
        [ 1.463184  , -2.9922049 ],
        [ 1.75200498, -2.99245811],
        [ 2.0427959 , -2.98633409],
        [ 2.3398571 , -2.97338295],
        [ 2.57211494, -2.96855807],
        [ 2.70825195, -2.92793894],
        [ 2.83194709, -2.83090997],
        [ 2.96616292, -2.6750071 ],
        [ 3.09371996, -2.47420597],
        [ 3.22101998, -2.2259841 ],
        [ 3.36291909, -1.953897  ],
        [ 3.50812507, -1.68267703],
        [ 3.65431595, -1.41456401],
        [ 3.79998708, -1.14891398],
        [ 3.94390106, -0.88560808],
        [ 4.08381081, -0.62438953],
        [ 4.21845579, -0.3634052 ],
        [ 4.34909296, -0.09823533],
        [ 4.47902298,  0.17099179],
        [ 4.47902298,  0.17099179],
        [ 4.60422707,  0.43421629],
        [ 4.71485519,  0.69019729],
        [ 4.80896997,  0.9442777 ],
        [ 4.8842988 ,  1.19755805],
        [ 4.93762207,  1.445737  ],
        [ 4.96322584,  1.68151999],
        [ 4.95684481,  1.89569604],
        [ 4.91621208,  2.07930803],
        [ 4.84203482,  2.2297461 ],
        [ 4.73189783,  2.35211992],
        [ 4.58130407,  2.4516499 ],
        [ 4.39322281,  2.52670598],
        [ 4.18015718,  2.57315397],
        [ 3.92518091,  2.58906603],
        [ 3.62969804,  2.60085106],
        [ 3.32659698,  2.61349106],
        [ 3.02391911,  2.62636304],
        [ 2.72119594,  2.63926506],
        [ 2.41839099,  2.65247107],
        [ 2.11695004,  2.66575694],
        [ 1.82789898,  2.67744589],
        [ 1.57345796,  2.676862  ],
        [ 1.38167298,  2.65432   ],
        [ 1.24726605,  2.59625006],
        [ 1.13373005,  2.49377108],
        [ 1.04116797,  2.35788894],
        [ 0.98872489,  2.20658898],
        [ 0.97523272,  2.08275604],
        [ 1.01772594,  1.97520494],
        [ 1.12251306,  1.83783305],
        [ 1.25443101,  1.71249902],
        [ 1.40521502,  1.63385606],
        [ 1.63203502,  1.57785296],
        [ 1.94975197,  1.50339603],
        [ 2.40722299,  1.31294   ],
        [ 2.74998903,  0.8357473 ],
        [ 2.81346893,  0.2945078 ],
        [ 2.69292808, -0.1087581 ],
        [ 2.58838511, -0.4068518 ],
        [ 2.45365191, -0.74767178],
        [ 2.22419   , -1.09895396],
        [ 1.91649103, -1.39155495],
        [ 1.55870402, -1.60363305],
        [ 1.18255997, -1.73445797],
        [ 0.80922687, -1.800336  ],
        [ 0.42550781, -1.81645596],
        [ 0.08083374, -1.77241695],
        [-0.2181896 , -1.73526502],
        [-0.52531707, -1.69572699],
        [-0.84186   , -1.64788306],
        [-1.16914499, -1.58358204],
        [-1.50888598, -1.49066901],
        [-1.86468303, -1.34711802],
        [-2.22787809, -1.10967898],
        [-2.53568506, -0.73475218],
        [-2.6868639 , -0.26692459],
        [-2.68373394,  0.14654119],
        [-2.64695692,  0.4762345 ],
        [-2.60432601,  0.794379  ],
        [-2.54579806,  1.11420596],
        [-2.47801495,  1.421929  ],
        [-2.4134531 ,  1.698686  ],
        [-2.3756609 ,  1.95163906],
        [-2.3618319 ,  2.17323709],
        [-2.38615799,  2.34421992],
        [-2.47196794,  2.52016807],
        [-2.58647895,  2.70764494],
        [-2.70887089,  2.84369302],
        [-2.84514594,  2.9312849 ],
        [-3.00704408,  2.98027611],
        [-3.19704008,  2.99241996],
        [-3.39837503,  2.96825194],
        [-3.5928421 ,  2.9073329 ],
        [-3.77149796,  2.81245303],
        [-3.92842698,  2.68569803],
        [-4.05974913,  2.53115201],
        [-4.16075516,  2.35378695],
        [-4.233459  ,  2.14126205],
        [-4.29420996,  1.87411499],
        [-4.36275721,  1.57883203],
        [-4.43124485,  1.28382504],
        [-4.4998498 ,  0.98902023],
        [-4.56826496,  0.69420582],
        [-4.6368289 ,  0.3992776 ],
        [-4.70546293,  0.1039506 ],
        [-4.77486181, -0.19209699],
        [-4.84466696, -0.48561981],
        [-4.91022587, -0.76972657],
        [-4.95892906, -1.00931501],
        [-4.96316481, -1.19013298],
        [-4.92915106, -1.32592797],
        [-4.85743284, -1.42987895],
        [-4.73682594, -1.51772201],
        [-4.55269289, -1.59191895]
    ])
    outer_border = np.array([
        [-4.56644011, -2.69043803],
        [-4.27108383, -2.76621795],
        [-3.97734189, -2.84131598],
        [-3.68348598, -2.91614103],
        [-3.38961005, -2.99065709],
        [-3.09571099, -3.06494188],
        [-2.80191588, -3.13893008],
        [-2.50870895, -3.21273494],
        [-2.21597695, -3.2868681 ],
        [-1.92302096, -3.36146903],
        [-1.63059497, -3.43599391],
        [-1.34416401, -3.509969  ],
        [-1.06299102, -3.58941388],
        [-0.77693582, -3.67551303],
        [-0.48126879, -3.76378894],
        [-0.1761108 , -3.84830809],
        [ 0.1401484 , -3.924891  ],
        [ 0.4700965 , -3.98653698],
        [ 0.79999149, -4.02460814],
        [ 1.12395501, -4.04882193],
        [ 1.44615102, -4.05886889],
        [ 1.76272202, -4.0592041 ],
        [ 2.07720304, -4.05257893],
        [ 2.3849709 , -4.03922892],
        [ 2.75730109, -4.01916218],
        [ 3.194309  , -3.87757611],
        [ 3.55547905, -3.61485195],
        [ 3.81924701, -3.31556201],
        [ 4.01801205, -3.0068841 ],
        [ 4.16808796, -2.71702909],
        [ 4.30612898, -2.45231295],
        [ 4.44668007, -2.18980289],
        [ 4.59031916, -1.92638505],
        [ 4.73574018, -1.66119301],
        [ 4.88217592, -1.39325094],
        [ 5.02809   , -1.12077701],
        [ 5.17100477, -0.84373021],
        [ 5.30795288, -0.5658356 ],
        [ 5.44116211, -0.2898246 ],
        [ 5.44116211, -0.2898246 ],
        [ 5.57584715, -0.00625765],
        [ 5.7051692 ,  0.2935372 ],
        [ 5.82110882,  0.60717648],
        [ 5.91806698,  0.93414509],
        [ 5.99112892,  1.27785099],
        [ 6.02935696,  1.64376104],
        [ 6.01464415,  2.03398705],
        [ 5.92038822,  2.43943691],
        [ 5.7245822 ,  2.82905698],
        [ 5.43234921,  3.15675092],
        [ 5.08137417,  3.39398408],
        [ 4.70898914,  3.54570293],
        [ 4.33134317,  3.62918591],
        [ 3.9827199 ,  3.65431309],
        [ 3.67327309,  3.66676092],
        [ 3.37148404,  3.67934704],
        [ 3.06929398,  3.69219708],
        [ 2.76715112,  3.70507503],
        [ 2.46511602,  3.71824694],
        [ 2.16172791,  3.73161697],
        [ 1.84586   ,  3.74409509],
        [ 1.496773  ,  3.74090195],
        [ 1.09045804,  3.68060303],
        [ 0.67302489,  3.49531007],
        [ 0.33354449,  3.199296  ],
        [ 0.08720905,  2.83540893],
        [-0.05733318,  2.41593289],
        [-0.08165254,  1.93764997],
        [ 0.07332603,  1.47904897],
        [ 0.32561421,  1.12859797],
        [ 0.6367833 ,  0.84268677],
        [ 1.01761699,  0.63995922],
        [ 1.37616897,  0.54219192],
        [ 1.64825296,  0.48008791],
        [ 1.75099504,  0.4614822 ],
        [ 1.758165  ,  0.46630821],
        [ 1.75257897,  0.4066371 ],
        [ 1.68308401,  0.23515721],
        [ 1.58735394, -0.0380725 ],
        [ 1.50387597, -0.26188669],
        [ 1.40411496, -0.41664869],
        [ 1.27384305, -0.54004651],
        [ 1.11130404, -0.6351831 ],
        [ 0.91589218, -0.70152551],
        [ 0.69332713, -0.73985022],
        [ 0.47271031, -0.75070089],
        [ 0.217408  , -0.71439499],
        [-0.08436234, -0.67689198],
        [-0.37769809, -0.63919002],
        [-0.65977353, -0.59673798],
        [-0.92655033, -0.54473191],
        [-1.17082798, -0.47884899],
        [-1.37692201, -0.39835539],
        [-1.52210999, -0.30970809],
        [-1.60006201, -0.22223639],
        [-1.63073206, -0.1164376 ],
        [-1.61941803,  0.07378387],
        [-1.58817697,  0.34567189],
        [-1.55064797,  0.62757069],
        [-1.50008094,  0.90316892],
        [-1.43748498,  1.18664396],
        [-1.36538196,  1.49966896],
        [-1.31418204,  1.845227  ],
        [-1.29642904,  2.22782111],
        [-1.36500204,  2.65293193],
        [-1.53251195,  3.02562189],
        [-1.73671198,  3.3525939 ],
        [-2.023211  ,  3.66096497],
        [-2.39549804,  3.89869404],
        [-2.81023097,  4.02876377],
        [-3.22313809,  4.05890083],
        [-3.62210608,  4.01132679],
        [-4.00456619,  3.89148092],
        [-4.35964394,  3.70247889],
        [-4.67313099,  3.44955611],
        [-4.93334818,  3.1434319 ],
        [-5.13175201,  2.79563189],
        [-5.25835419,  2.43732405],
        [-5.3335681 ,  2.11452389],
        [-5.40192223,  1.82007396],
        [-5.47034502,  1.52534902],
        [-5.53896093,  1.23049498],
        [-5.6074028 ,  0.93556571],
        [-5.67592812,  0.64080471],
        [-5.74433994,  0.34643191],
        [-5.81311417,  0.05304696],
        [-5.88337517, -0.2424169 ],
        [-5.95378494, -0.54825741],
        [-6.02038717, -0.90269059],
        [-6.02128792, -1.32591605],
        [-5.89809704, -1.77225196],
        [-5.62984896, -2.16570306],
        [-5.26951981, -2.44200492],
        [-4.89646482, -2.60181093]
    ])

def reward_function(params):
    # Read input parameters
    heading = params['heading']
    steering_angle = params['steering_angle']
    vehicle_x = params['x']
    vehicle_y = params['y']

    distances_from_route_points = np.hypot(PARAMS.waypoints[:, 0] - vehicle_x, PARAMS.waypoints[:, 1] - vehicle_y)
    closest_route_point = np.argmin(distances_from_route_points)
    normalized_distance_from_route = distances_from_route_points[closest_route_point] / (params['track_width'] * 0.5)

    npoints = len(PARAMS.waypoints)

    LOOKAHEAD = 5
    next_route_point_x = PARAMS.waypoints[(closest_route_point + LOOKAHEAD) % npoints, 0]
    next_route_point_y = PARAMS.waypoints[(closest_route_point + LOOKAHEAD) % npoints, 1]

    def direction_diff_to_point(x, y):
        # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians between target and current vehicle position
        direction = math.atan2(y - vehicle_y, x - vehicle_x)
        # Convert to degree
        direction = math.degrees(direction)
        # Calculate the difference between the direction and the heading direction of the car
        direction_diff = direction - heading
        #Check that the direction_diff is in valid range
        if direction_diff < -180:
            direction_diff += 360
        elif direction_diff > 180:
            direction_diff -= 360
        return direction_diff

    direction_diff = direction_diff_to_point(next_route_point_x, next_route_point_y)

    next_inner_route_point_x = PARAMS.inner_border[(closest_route_point + LOOKAHEAD) % npoints, 0]
    next_inner_route_point_y = PARAMS.inner_border[(closest_route_point + LOOKAHEAD) % npoints, 1]
    inner_direction_diff = direction_diff_to_point(next_inner_route_point_x, next_inner_route_point_y)
    next_outer_route_point_x = PARAMS.outer_border[(closest_route_point + LOOKAHEAD) % npoints, 0]
    next_outer_route_point_y = PARAMS.outer_border[(closest_route_point + LOOKAHEAD) % npoints, 1]
    outer_direction_diff = direction_diff_to_point(next_outer_route_point_x, next_outer_route_point_y)

    #Heading is pointing inside the cone formed by car and the lookahead waypoint on the inner and outer track borders
    is_heading_in_right_direction = inner_direction_diff >= 0 and outer_direction_diff <= 0

    def unpardonable_action_taken():
        if params['distance_from_center'] > (params['track_width'] * 0.5):
            return True
        if abs(direction_diff) > 30:
            return True
        if not is_heading_in_right_direction:
            return True
        if abs(steering_angle) > (abs(direction_diff) + 2):
            return True
        if direction_diff < 0 and steering_angle > 0:
            return True
        if direction_diff > 0 and steering_angle < 0:
            return True
        return False

    reward = -(10 / 1.2) * normalized_distance_from_route + 10

    #If an unpardonable action is taken, then the immediate reward is 0
    if unpardonable_action_taken():
        reward = 0

    return float(reward)