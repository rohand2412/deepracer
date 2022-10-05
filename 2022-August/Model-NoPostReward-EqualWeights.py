import math
import numpy as np
from shapely.geometry import Polygon, Point

class PARAMS:
    prev_speed = None
    prev_steering_angle = None
    prev_steps = None
    prev_direction_diff = None
    prev_normalized_distance_from_route = None
    waypoints = np.array([
        [-4.31327952, -2.04071418],
        [-4.06795844, -2.16668643],
        [-3.80669807, -2.27737184],
        [-3.53358327, -2.37577653],
        [-3.25155585, -2.46428961],
        [-2.96357725, -2.54581438],
        [-2.67207001, -2.62310862],
        [-2.37902213, -2.69833984],
        [-2.08606587, -2.77097213],
        [-1.79315222, -2.84090317],
        [-1.50030383, -2.90792766],
        [-1.20755823, -2.97172899],
        [-0.91496136, -3.03197736],
        [-0.62256728, -3.08833296],
        [-0.33043993, -3.14043626],
        [-0.03866012, -3.18783927],
        [ 0.25263228, -3.2296237 ],
        [ 0.54325204, -3.26481766],
        [ 0.83292118, -3.29210657],
        [ 1.12124516, -3.30991819],
        [ 1.40756526, -3.31587219],
        [ 1.69093638, -3.30732206],
        [ 1.96989124, -3.28085106],
        [ 2.24236648, -3.23272507],
        [ 2.50529396, -3.158263  ],
        [ 2.7542722 , -3.05193234],
        [ 2.98231934, -2.90612896],
        [ 3.19593577, -2.73640985],
        [ 3.3966184 , -2.54654967],
        [ 3.5860592 , -2.34003794],
        [ 3.76542647, -2.11926719],
        [ 3.93581873, -1.88637212],
        [ 4.09842007, -1.6434862 ],
        [ 4.25400823, -1.3922682 ],
        [ 4.40169788, -1.13502133],
        [ 4.53739015, -0.87974949],
        [ 4.65847336, -0.63272075],
        [ 4.76645561, -0.39180738],
        [ 4.86303361, -0.1532521 ],
        [ 4.9490177 ,  0.08593569],
        [ 5.02438561,  0.3276919 ],
        [ 5.08805344,  0.57316438],
        [ 5.13832907,  0.82266337],
        [ 5.17246294,  1.07570383],
        [ 5.18753145,  1.33074808],
        [ 5.17882651,  1.58514187],
        [ 5.14167809,  1.83472654],
        [ 5.07065419,  2.07377242],
        [ 4.9579921 ,  2.29350076],
        [ 4.79560446,  2.48049653],
        [ 4.60226418,  2.64145946],
        [ 4.38393536,  2.77831744],
        [ 4.1449537 ,  2.89273122],
        [ 3.88905791,  2.98653584],
        [ 3.61883313,  3.06071772],
        [ 3.33666325,  3.11627896],
        [ 3.04463867,  3.15393833],
        [ 2.74417353,  3.17217004],
        [ 2.44752232,  3.16856386],
        [ 2.16183996,  3.14198067],
        [ 1.89180323,  3.08995128],
        [ 1.64199647,  3.01133883],
        [ 1.41682656,  2.90614641],
        [ 1.22064236,  2.77522728],
        [ 1.05744977,  2.62039916],
        [ 0.93498911,  2.44241852],
        [ 0.86168907,  2.24435441],
        [ 0.8549989 ,  2.03193624],
        [ 0.90570959,  1.81850983],
        [ 1.00176426,  1.61112746],
        [ 1.13320118,  1.41241506],
        [ 1.28966602,  1.22192358],
        [ 1.46166597,  1.03746343],
        [ 1.63105909,  0.86418892],
        [ 1.77849047,  0.68022595],
        [ 1.88375092,  0.47746333],
        [ 1.91939809,  0.25511079],
        [ 1.89560837,  0.0303444 ],
        [ 1.82077643, -0.18567285],
        [ 1.70367263, -0.38635034],
        [ 1.55038338, -0.56736403],
        [ 1.36601707, -0.72564678],
        [ 1.15486554, -0.85864709],
        [ 0.92115361, -0.96436247],
        [ 0.66938364, -1.04137563],
        [ 0.40452379, -1.08887775],
        [ 0.13202843, -1.10661603],
        [-0.14238439, -1.09493436],
        [-0.41331924, -1.05519369],
        [-0.6762242 , -0.98903932],
        [-0.9272613 , -0.89782601],
        [-1.16231287, -0.78162374],
        [-1.37678451, -0.64000028],
        [-1.56507446, -0.47184381],
        [-1.72060165, -0.2758385 ],
        [-1.82900981, -0.04712233],
        [-1.9009658 ,  0.20230248],
        [-1.94382956,  0.46599558],
        [-1.96689978,  0.73844074],
        [-1.97966289,  1.01520142],
        [-1.9952704 ,  1.29359696],
        [-2.01940482,  1.56817372],
        [-2.05762176,  1.83597287],
        [-2.11460748,  2.09375127],
        [-2.19441824,  2.33758797],
        [-2.30042209,  2.56256535],
        [-2.43472208,  2.76284759],
        [-2.5985635 ,  2.93075806],
        [-2.79225102,  3.05396425],
        [-3.00953123,  3.11594247],
        [-3.23425893,  3.12595762],
        [-3.45793856,  3.09009506],
        [-3.6752395 ,  3.01414432],
        [-3.88094745,  2.89824872],
        [-4.07303428,  2.74948118],
        [-4.2503002 ,  2.57218004],
        [-4.41224846,  2.37012132],
        [-4.55897307,  2.14686166],
        [-4.69064717,  1.90533559],
        [-4.8082028 ,  1.64877838],
        [-4.91275064,  1.37999624],
        [-5.00528902,  1.10125509],
        [-5.08592238,  0.81404577],
        [-5.15390594,  0.52061767],
        [-5.20728837,  0.22939995],
        [-5.24458374, -0.05736732],
        [-5.26184875, -0.33783374],
        [-5.25572644, -0.61000387],
        [-5.22255961, -0.87139849],
        [-5.15872075, -1.11905582],
        [-5.05928611, -1.3486818 ],
        [-4.91715615, -1.5532803 ],
        [-4.7416481 , -1.73545052],
        [-4.53895739, -1.89740818]
    ])
    optimal_speed = np.array([
        1.        , 1.        , 1.        , 1.        , 1.        ,
        1.        , 1.        , 1.        , 1.        , 1.        ,
        1.        , 1.        , 1.        , 1.        , 1.        ,
        1.        , 1.        , 1.        , 1.        , 0.89952803,
        0.7889049 , 0.7889049 , 0.7889049 , 0.7889049 , 0.7889049 ,
        1.        , 1.        , 1.        , 1.        , 1.        ,
        1.        , 1.        , 1.        , 1.        , 1.        ,
        1.        , 1.        , 1.        , 1.        , 1.        ,
        0.9205331 , 0.82183582, 0.71399127, 0.62436711, 0.62436711,
        0.62436711, 0.62436711, 0.62436711, 0.76637612, 0.84837381,
        0.93529028, 1.        , 1.        , 1.        , 1.        ,
        0.94330378, 0.85632779, 0.77943286, 0.71622234, 0.63325145,
        0.57219781, 0.5       , 0.5       , 0.5       , 0.5       ,
        0.5       , 0.5571372 , 0.65161901, 0.76717606, 0.66956772,
        0.51983698, 0.51983698, 0.51983698, 0.51983698, 0.51983698,
        0.56983416, 0.6157059 , 0.67065767, 0.71511716, 0.75803079,
        0.79680671, 0.83654013, 0.87826155, 0.92007723, 0.95664455,
        0.95305017, 0.88990272, 0.81579469, 0.74711446, 0.64768663,
        0.64768663, 0.64768663, 0.64768663, 0.64768663, 0.77589726,
        0.91393876, 1.        , 1.        , 1.        , 0.87953521,
        0.78654953, 0.70386555, 0.61797057, 0.54809662, 0.54809662,
        0.54809662, 0.54809662, 0.54809662, 0.60619708, 0.64933459,
        0.69962337, 0.70780007, 0.78960694, 0.86073108, 0.93932578,
        1.        , 1.        , 1.        , 1.        , 1.        ,
        1.        , 1.        , 0.99016641, 0.88428464, 0.7839294 ,
        0.69143954, 0.69143954, 0.69143954, 0.69143954, 0.69143954,
        0.7729101 , 0.86552158, 0.96047409, 1.        
    ])
    waypoints_poly = Polygon(waypoints)
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
    turn_points = np.array([
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0.
    ])
    last_milestone = 0

def reward_function(params):
    def minimum(arr):
        # LOW = None
        # for val in arr:
        #     if LOW is None:
        #         LOW = val
        #     else:
        #         LOW = min(LOW, val)
        # return LOW
        return np.amin(arr)

    def maximum(arr):
        # HIGH = None
        # for val in arr:
        #     if HIGH is None:
        #         HIGH = val
        #     else:
        #         HIGH = max(HIGH, val)
        # return HIGH
        return np.amax(arr)
    
    # Read input parameters
    heading = params['heading']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    steering_angle = params['steering_angle']
    speed = params['speed']
    vehicle_x = params['x']
    vehicle_y = params['y']

    distances_from_route_points = np.hypot(PARAMS.waypoints[:, 0] - vehicle_x, PARAMS.waypoints[:, 1] - vehicle_y)
    closest_route_point = np.argmin(distances_from_route_points)
    normalized_distance_from_route = distances_from_route_points[closest_route_point] / (params['track_width'] * 0.5)

    npoints = len(PARAMS.waypoints)

    bearing = "left" if Point((vehicle_x, vehicle_y)).within(PARAMS.waypoints_poly) else "right"

    # Reinitialize previous parameters if it is a new episode
    if PARAMS.prev_steps is None or steps < PARAMS.prev_steps:
        PARAMS.prev_speed = None
        PARAMS.prev_steering_angle = None
        PARAMS.prev_direction_diff = None
        PARAMS.prev_normalized_distance_from_route = None
        PARAMS.last_milestone = 0

    #Calculate the speed reward
    MIN_SPEED = 0.5
    MAX_SPEED = 1.0
    optimal_speed = 0

    #chosen such that 6 standard deviations covers the entire range
    sigma_speed = abs(MAX_SPEED - MIN_SPEED)/6.0
    optimal_speed = PARAMS.optimal_speed[closest_route_point]

    speed_reward = math.exp(-0.5*abs(speed-optimal_speed)**2 / sigma_speed**2)

    #distance reward is value of the standard normal scaled back to 1. #Hence the 1/2*pi*sigma term is cancelled out
    distance_reward = 0
    if normalized_distance_from_route <= 0.1: #i.e. on the route line
        distance_from_route = 0
        distance_reward = 1
    elif bearing == "left": #i.e. on left side of the route line
        distances_from_inner_border_points = np.hypot(PARAMS.inner_border[:, 0] - vehicle_x, PARAMS.inner_border[:, 1] - vehicle_y)
        normalized_route_distance_from_inner_border = minimum(distances_from_inner_border_points) / (params['track_width'] * 0.5)
        sigma=abs(normalized_route_distance_from_inner_border / 4)
        distance_reward = math.exp(-0.5*abs(normalized_distance_from_route)**2/sigma**2)
    elif bearing == "right": #i.e. on right side of the route line
        distances_from_outer_border_points = np.hypot(PARAMS.outer_border[:, 0] - vehicle_x, PARAMS.outer_border[:, 1] - vehicle_y)
        normalized_route_distance_from_outer_border = minimum(distances_from_outer_border_points) / (params['track_width'] * 0.5)
        sigma=abs(normalized_route_distance_from_outer_border / 4)
        distance_reward = math.exp(-0.5*abs(normalized_distance_from_route)**2/sigma**2)

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

    #Then compute the heading reward
    heading_reward = math.cos( abs(direction_diff ) * ( math.pi / 180 ) ) ** 10
    if abs(direction_diff) <= 20:
        heading_reward = math.cos( abs(direction_diff ) * ( math.pi / 180 ) ) ** 4

    #Check if the speed has dropped
    has_speed_dropped = False
    if PARAMS.prev_speed is not None:
        if PARAMS.prev_speed > speed:
            has_speed_dropped = True

    on_turn = PARAMS.turn_points[closest_route_point]
    on_straight = not PARAMS.turn_points[closest_route_point]

    #Penalize slowing down without good reason on straight portions
    speed_maintain_bonus = 1
    if has_speed_dropped and not on_turn:
        speed_maintain_bonus = min( speed / PARAMS.prev_speed, 1 )

    next_inner_route_point_x = PARAMS.inner_border[(closest_route_point + LOOKAHEAD) % npoints, 0]
    next_inner_route_point_y = PARAMS.inner_border[(closest_route_point + LOOKAHEAD) % npoints, 1]
    inner_direction_diff = direction_diff_to_point(next_inner_route_point_x, next_inner_route_point_y)
    next_outer_route_point_x = PARAMS.outer_border[(closest_route_point + LOOKAHEAD) % npoints, 0]
    next_outer_route_point_y = PARAMS.outer_border[(closest_route_point + LOOKAHEAD) % npoints, 1]
    outer_direction_diff = direction_diff_to_point(next_outer_route_point_x, next_outer_route_point_y)

    #Heading is pointing inside the cone formed by car and the lookahead waypoint on the inner and outer track borders
    is_heading_in_right_direction = inner_direction_diff >= 0 and outer_direction_diff <= 0

    #has the steering angle been maintained
    has_steering_angle_maintained = True
    if PARAMS.prev_steering_angle is not None:
        has_steering_angle_maintained = abs(PARAMS.prev_steering_angle - steering_angle) <= 1

    steering_angle_maintain_bonus = 1 
    #Maintaining the steering angle is a good thing if heading in the right direction
    if is_heading_in_right_direction and has_steering_angle_maintained:
        if abs(direction_diff) < 10:
            steering_angle_maintain_bonus *= 2
        if abs(direction_diff) < 5:
            steering_angle_maintain_bonus *= 2
        if PARAMS.prev_direction_diff is not None and abs(PARAMS.prev_direction_diff) > abs(direction_diff):
            steering_angle_maintain_bonus *= 2

    #Reward reducing distance to the race line
    distance_reduction_bonus = 1
    if PARAMS.prev_normalized_distance_from_route is not None and PARAMS.prev_normalized_distance_from_route > normalized_distance_from_route:
        if abs(normalized_distance_from_route) > 0:
            distance_reduction_bonus = min( abs( PARAMS.prev_normalized_distance_from_route / normalized_distance_from_route ), 2)

    # Reward for making steady progress
    progress_reward = 10 * params['progress'] / params['steps']
    if steps <= 5:
        progress_reward = 1 #ignore progress in the first 5 steps

    # Bonus that the agent gets for completing every 10 percent of track
    # Is exponential in the progress / steps. 
    # exponent increases with an increase in fraction of lap completed

    intermediate_progress_bonus = 0
    pi = int(params['progress'] // 10)
    if pi > PARAMS.last_milestone:
        if pi==10: # 100% track completion
            intermediate_progress_bonus = progress_reward ** 14
        else:
            intermediate_progress_bonus = progress_reward ** (5+0.75*pi)
        PARAMS.last_milestone = pi

    # Before returning reward, update the variables
    PARAMS.prev_speed = speed
    PARAMS.prev_steering_angle = steering_angle
    PARAMS.prev_direction_diff = direction_diff
    PARAMS.prev_steps = steps
    PARAMS.prev_normalized_distance_from_route = normalized_distance_from_route

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
        if on_turn and speed >= (PARAMS.optimal_speed[closest_route_point] + 1):
            return True
        if not on_turn and speed <= (PARAMS.optimal_speed[closest_route_point] - 1.5):
            return True
        return False

    #heading component of reward
    HC = ( 10 * heading_reward * steering_angle_maintain_bonus )
    #distance component of reward
    DC = ( 10 * distance_reward * distance_reduction_bonus )
    #speed component of reward
    SC = ( 10 * speed_reward * speed_maintain_bonus )
    #Immediate component of reward
    IC = ( HC + DC + SC ) ** 2 + ( HC * DC * SC )

    #If an unpardonable action is taken, then the immediate reward is 0
    if unpardonable_action_taken():
        IC = 1e-3
        intermediate_progress_bonus = 0

    #Long term component of reward
    LC = ( intermediate_progress_bonus )

    return max(IC + LC,1e-3)