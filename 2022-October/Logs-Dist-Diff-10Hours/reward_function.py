import numpy as np

class PARAMS:
    prev_progress = None
    prev_steps = None
    waypoints = np.array([
        [ 6.09499,  1.57587],	[ 6.04499,  1.5946 ],	[ 5.99467,  1.61304],	[ 5.94406,  1.63118],	[ 5.89315,  1.64904],
        [ 5.84197,  1.66661],	[ 5.79053,  1.6839 ],	[ 5.73884,  1.70091],	[ 5.68692,  1.71765],	[ 5.63477,  1.73413],
        [ 5.58242,  1.75035],	[ 5.52987,  1.7663 ],	[ 5.47714,  1.78203],	[ 5.42429,  1.79761],	[ 5.37134,  1.81313],
        [ 5.31835,  1.82871],	[ 5.26537,  1.84443],	[ 5.21243,  1.86038],	[ 5.15955,  1.87659],	[ 5.10672,  1.89302],
        [ 5.05395,  1.90963],	[ 5.00123,  1.92639],	[ 4.94855,  1.94326],	[ 4.89591,  1.96022],	[ 4.84331,  1.97726],
        [ 4.79075,  1.9944 ],	[ 4.73823,  2.01163],	[ 4.68575,  2.02897],	[ 4.63331,  2.04641],	[ 4.5809 ,  2.06395],
        [ 4.52853,  2.08158],	[ 4.4762 ,  2.09931],	[ 4.4239 ,  2.11713],	[ 4.37163,  2.13504],	[ 4.31939,  2.15302],
        [ 4.26719,  2.17108],	[ 4.21501,  2.18922],	[ 4.16287,  2.20744],	[ 4.11076,  2.22573],	[ 4.05867,  2.24409],
        [ 4.00661,  2.26253],	[ 3.95458,  2.28103],	[ 3.90258,  2.29961],	[ 3.85061,  2.31825],	[ 3.79865,  2.33696],
        [ 3.74673,  2.35573],	[ 3.69483,  2.37457],	[ 3.64296,  2.39347],	[ 3.59111,  2.41243],	[ 3.53928,  2.43145],
        [ 3.48748,  2.45054],	[ 3.43571,  2.46969],	[ 3.38396,  2.4889 ],	[ 3.33223,  2.50816],	[ 3.28052,  2.52748],
        [ 3.22884,  2.54686],	[ 3.17717,  2.56628],	[ 3.12553,  2.58576],	[ 3.07391,  2.60529],	[ 3.02231,  2.62488],
        [ 2.97073,  2.64451],	[ 2.91916,  2.66419],	[ 2.86762,  2.68392],	[ 2.8161 ,  2.7037 ],	[ 2.7646 ,  2.72353],
        [ 2.71312,  2.74341],	[ 2.66165,  2.76334],	[ 2.61021,  2.78331],	[ 2.55879,  2.80334],	[ 2.50738,  2.82341],
        [ 2.456  ,  2.84353],	[ 2.40463,  2.86371],	[ 2.35329,  2.88392],	[ 2.30196,  2.90419],	[ 2.25066,  2.9245 ],
        [ 2.19937,  2.94487],	[ 2.1481 ,  2.96528],	[ 2.09685,  2.98573],	[ 2.04563,  3.00624],	[ 1.99442,  3.02679],
        [ 1.94323,  3.0474 ],	[ 1.89206,  3.06805],	[ 1.84091,  3.08875],	[ 1.78978,  3.10949],	[ 1.73866,  3.13029],
        [ 1.68757,  3.15113],	[ 1.6365 ,  3.17203],	[ 1.58545,  3.19297],	[ 1.53442,  3.21396],	[ 1.48341,  3.235  ],
        [ 1.43242,  3.25609],	[ 1.38145,  3.27724],	[ 1.3305 ,  3.29843],	[ 1.27957,  3.31967],	[ 1.22866,  3.34096],
        [ 1.17777,  3.3623 ],	[ 1.1269 ,  3.38369],	[ 1.07606,  3.40513],	[ 1.02523,  3.42663],	[ 0.97443,  3.44817],
        [ 0.92364,  3.46977],	[ 0.87288,  3.49142],	[ 0.82214,  3.51311],	[ 0.77142,  3.53486],	[ 0.72072,  3.55666],
        [ 0.67004,  3.57852],	[ 0.61938,  3.60042],	[ 0.56874,  3.62238],	[ 0.51813,  3.64438],	[ 0.46754,  3.66644],
        [ 0.41696,  3.68855],	[ 0.36641,  3.71071],	[ 0.31588,  3.73292],	[ 0.26537,  3.75518],	[ 0.21488,  3.7775 ],
        [ 0.16441,  3.79986],	[ 0.11397,  3.82227],	[ 0.06354,  3.84473],	[ 0.01313,  3.86725],	[-0.03725,  3.88981],
        [-0.08762,  3.91242],	[-0.13796,  3.93508],	[-0.18829,  3.95779],	[-0.23859,  3.98055],	[-0.28888,  4.00335],
        [-0.33914,  4.0262 ],	[-0.38939,  4.0491 ],	[-0.43962,  4.07205],	[-0.48982,  4.09504],	[-0.54001,  4.11808],
        [-0.59018,  4.14116],	[-0.64033,  4.16429],	[-0.69046,  4.18746],	[-0.74058,  4.21068],	[-0.79067,  4.23394],
        [-0.84075,  4.25724],	[-0.89081,  4.28058],	[-0.94085,  4.30397],	[-0.99088,  4.3274 ],	[-1.04089,  4.35086],
        [-1.09088,  4.37437],	[-1.14085,  4.39792],	[-1.19081,  4.4215 ],	[-1.24076,  4.44512],	[-1.29068,  4.46878],
        [-1.3406 ,  4.49248],	[-1.39049,  4.51621],	[-1.44038,  4.53998],	[-1.49024,  4.56378],	[-1.5401 ,  4.58762],
        [-1.58994,  4.61149],	[-1.63976,  4.63539],	[-1.68958,  4.65933],	[-1.73937,  4.6833 ],	[-1.78916,  4.7073 ],
        [-1.83893,  4.73133],	[-1.88869,  4.7554 ],	[-1.93843,  4.77949],	[-1.98816,  4.80362],	[-2.03788,  4.82778],
        [-2.08758,  4.85197],	[-2.13727,  4.87619],	[-2.18695,  4.90044],	[-2.23662,  4.92472],	[-2.28627,  4.94904],
        [-2.3359 ,  4.97338],	[-2.38553,  4.99776],	[-2.43514,  5.02217],	[-2.48474,  5.04661],	[-2.53432,  5.07109],
        [-2.58389,  5.0956 ],	[-2.63344,  5.12014],	[-2.68298,  5.14471],	[-2.73251,  5.16932],	[-2.78202,  5.19397],
        [-2.83151,  5.21865],	[-2.88099,  5.24336],	[-2.93045,  5.26811],	[-2.9799 ,  5.29291],	[-3.02933,  5.31774],
        [-3.07874,  5.34261],	[-3.12814,  5.36752],	[-3.17752,  5.39247],	[-3.22688,  5.41746],	[-3.27622,  5.44249],
        [-3.32555,  5.46755],	[-3.37486,  5.49263],	[-3.42415,  5.51776],	[-3.47342,  5.54292],	[-3.52267,  5.56814],
        [-3.57191,  5.59343],	[-3.62113,  5.61879],	[-3.67034,  5.64423],	[-3.71952,  5.66972],	[-3.76868,  5.69524],
        [-3.81779,  5.72076],	[-3.86687,  5.74626],	[-3.91589,  5.77169],	[-3.96487,  5.79703],	[-4.01382,  5.8222 ],
        [-4.06274,  5.84716],	[-4.11166,  5.87184],	[-4.16058,  5.89618],	[-4.20951,  5.92013],	[-4.25845,  5.94364],
        [-4.30739,  5.96664],	[-4.35633,  5.98909],	[-4.40524,  6.01093],	[-4.45412,  6.03211],	[-4.50298,  6.05258],
        [-4.55179,  6.0723 ],	[-4.60055,  6.09122],	[-4.64926,  6.10931],	[-4.69791,  6.12653],	[-4.74648,  6.14282],
        [-4.79498,  6.15815],	[-4.84339,  6.17248],	[-4.8917 ,  6.18577],	[-4.9399 ,  6.19798],	[-4.98798,  6.20907],
        [-5.03592,  6.21901],	[-5.08372,  6.22778],	[-5.13136,  6.23536],	[-5.17884,  6.24173],	[-5.22613,  6.24687],
        [-5.27324,  6.25073],	[-5.32013,  6.25328],	[-5.3668 ,  6.25446],	[-5.41324,  6.25422],	[-5.45941,  6.25249],
        [-5.50531,  6.24923],	[-5.55088,  6.24431],	[-5.59606,  6.2376 ],	[-5.64079,  6.22897],	[-5.685  ,  6.21828],
        [-5.72862,  6.20539],	[-5.77163,  6.19031],	[-5.81406,  6.1732 ],	[-5.85594,  6.15426],	[-5.89729,  6.13368],
        [-5.93815,  6.11165],	[-5.97854,  6.08835],	[-6.01847,  6.06383],	[-6.05793,  6.0381 ],	[-6.09692,  6.01117],
        [-6.13545,  5.98306],	[-6.17351,  5.95378],	[-6.21109,  5.92335],	[-6.2482 ,  5.8918 ],	[-6.28484,  5.85917],
        [-6.32101,  5.8255 ],	[-6.35671,  5.79081],	[-6.39195,  5.75514],	[-6.42673,  5.71853],	[-6.46107,  5.68103],
        [-6.49499,  5.64268],	[-6.5285 ,  5.60352],	[-6.56161,  5.56359],	[-6.59433,  5.52291],	[-6.62661,  5.48148],
        [-6.65845,  5.43928],	[-6.68982,  5.39631],	[-6.72069,  5.35256],	[-6.75104,  5.30804],	[-6.78083,  5.26282],
        [-6.81001,  5.21698],	[-6.83853,  5.17059],	[-6.86637,  5.12375],	[-6.89346,  5.07651],	[-6.91979,  5.02894],
        [-6.94534,  4.98107],	[-6.97008,  4.93293],	[-6.994  ,  4.88455],	[-7.01709,  4.83597],	[-7.03932,  4.7872 ],
        [-7.06069,  4.73827],	[-7.0812 ,  4.6892 ],	[-7.10085,  4.64   ],	[-7.11964,  4.5907 ],	[-7.13756,  4.54131],
        [-7.15462,  4.49184],	[-7.17081,  4.4423 ],	[-7.18613,  4.39272],	[-7.20059,  4.34309],	[-7.21418,  4.29344],
        [-7.2269 ,  4.24378],	[-7.23875,  4.1941 ],	[-7.24974,  4.14444],	[-7.25985,  4.09478],	[-7.2691 ,  4.04515],
        [-7.27749,  3.99556],	[-7.285  ,  3.94601],	[-7.29165,  3.89651],	[-7.29742,  3.84706],	[-7.30232,  3.79769],
        [-7.30635,  3.74838],	[-7.3095 ,  3.69916],	[-7.31173,  3.65004],	[-7.31301,  3.60103],	[-7.31332,  3.55215],
        [-7.31261,  3.50341],	[-7.31087,  3.45482],	[-7.30807,  3.4064 ],	[-7.30419,  3.35816],	[-7.29922,  3.31011],
        [-7.29314,  3.26226],	[-7.28594,  3.21464],	[-7.27757,  3.16726],	[-7.26793,  3.12017],	[-7.25693,  3.07343],
        [-7.24449,  3.02707],	[-7.23052,  2.98115],	[-7.21494,  2.93572],	[-7.19782,  2.89076],	[-7.17925,  2.84628],
        [-7.15933,  2.80227],	[-7.13816,  2.75872],	[-7.11583,  2.71563],	[-7.0924 ,  2.673  ],	[-7.06789,  2.63082],
        [-7.04235,  2.58909],	[-7.01578,  2.54783],	[-6.98822,  2.50702],	[-6.9597 ,  2.46667],	[-6.93026,  2.42677],
        [-6.89994,  2.3873 ],	[-6.86879,  2.34826],	[-6.83685,  2.30963],	[-6.80416,  2.27141],	[-6.77076,  2.23358],
        [-6.73667,  2.19614],	[-6.70191,  2.15908],	[-6.6665 ,  2.1224 ],	[-6.63047,  2.08609],	[-6.59383,  2.05016],
        [-6.55662,  2.01457],	[-6.51884,  1.97933],	[-6.48053,  1.94442],	[-6.44171,  1.90983],	[-6.40239,  1.87555],
        [-6.36261,  1.84157],	[-6.3224 ,  1.80788],	[-6.28178,  1.77449],	[-6.24079,  1.74139],	[-6.19945,  1.70857],
        [-6.15777,  1.67602],	[-6.11578,  1.6437 ],	[-6.07346,  1.61156],	[-6.03082,  1.57955],	[-5.98785,  1.54764],
        [-5.94457,  1.51577],	[-5.90105,  1.48402],	[-5.85738,  1.45249],	[-5.81365,  1.42128],	[-5.76998,  1.3905 ],
        [-5.72645,  1.36026],	[-5.68315,  1.33055],	[-5.64014,  1.30121],	[-5.59748,  1.27204],	[-5.55523,  1.24285],
        [-5.51345,  1.21345],	[-5.47219,  1.18367],	[-5.43154,  1.15345],	[-5.3916 ,  1.12281],	[-5.35246,  1.09175],
        [-5.31421,  1.06026],	[-5.27694,  1.02836],	[-5.24074,  0.99604],	[-5.20568,  0.96325],	[-5.17183,  0.92996],
        [-5.13926,  0.89614],	[-5.10805,  0.86175],	[-5.07825,  0.82675],	[-5.04991,  0.79115],	[-5.02305,  0.75494],
        [-4.9977 ,  0.71811],	[-4.97388,  0.68066],	[-4.95161,  0.6426 ],	[-4.93102,  0.60389],	[-4.91229,  0.56451],
        [-4.89563,  0.52441],	[-4.88123,  0.48356],	[-4.86931,  0.44192],	[-4.85997,  0.39947],	[-4.85305,  0.35629],
        [-4.84832,  0.31247],	[-4.84551,  0.26812],	[-4.8444 ,  0.22333],	[-4.84474,  0.17819],	[-4.84644,  0.13276],
        [-4.84951,  0.08704],	[-4.85395,  0.04102],	[-4.85979, -0.00529],	[-4.86703, -0.05188],	[-4.87569, -0.09875],
        [-4.8857 , -0.14589],	[-4.89702, -0.19326],	[-4.90959, -0.24086],	[-4.92335, -0.28865],	[-4.93825, -0.33662],
        [-4.95424, -0.38476],	[-4.97126, -0.43305],	[-4.98927, -0.48147],	[-5.00821, -0.53003],	[-5.02803, -0.5787 ],
        [-5.04868, -0.62748],	[-5.07009, -0.67636],	[-5.09219, -0.72533],	[-5.11494, -0.77438],	[-5.13825, -0.8235 ],
        [-5.16206, -0.87269],	[-5.18632, -0.92193],	[-5.21095, -0.97121],	[-5.23589, -1.02052],	[-5.26108, -1.06984],
        [-5.28645, -1.11916],	[-5.31193, -1.16846],	[-5.33742, -1.21775],	[-5.36282, -1.26703],	[-5.38804, -1.31628],
        [-5.41298, -1.36551],	[-5.43755, -1.41471],	[-5.46168, -1.46389],	[-5.48535, -1.51304],	[-5.5085 , -1.56216],
        [-5.5311 , -1.61125],	[-5.55311, -1.6603 ],	[-5.57447, -1.70931],	[-5.59514, -1.75828],	[-5.61506, -1.80719],
        [-5.63416, -1.85603],	[-5.65241, -1.90481],	[-5.66973, -1.95351],	[-5.68611, -2.00212],	[-5.70148, -2.05063],
        [-5.71584, -2.09904],	[-5.72913, -2.14734],	[-5.74132, -2.19551],	[-5.75238, -2.24354],	[-5.76227, -2.29143],
        [-5.77093, -2.33915],	[-5.77834, -2.38669],	[-5.78445, -2.43403],	[-5.78922, -2.48116],	[-5.79264, -2.52807],
        [-5.79469, -2.57474],	[-5.79536, -2.62118],	[-5.79463, -2.66736],	[-5.7925 , -2.71328],	[-5.78887, -2.7589 ],
        [-5.78361, -2.80415],	[-5.77658, -2.84898],	[-5.76762, -2.89332],	[-5.7566 , -2.9371 ],	[-5.74343, -2.98028],
        [-5.72824, -3.02287],	[-5.71118, -3.06489],	[-5.69241, -3.10636],	[-5.67209, -3.14729],	[-5.65037, -3.18772],
        [-5.62734, -3.22763],	[-5.60301, -3.26703],	[-5.5774 , -3.30592],	[-5.55053, -3.34429],	[-5.52242, -3.38215],
        [-5.49309, -3.41949],	[-5.46258, -3.45631],	[-5.43092, -3.49261],	[-5.39816, -3.5284 ],	[-5.36432, -3.56369],
        [-5.32945, -3.59846],	[-5.29358, -3.63274],	[-5.25676, -3.66653],	[-5.21902, -3.69985],	[-5.18041, -3.73271],
        [-5.14096, -3.76511],	[-5.10072, -3.79707],	[-5.05972, -3.82861],	[-5.01798, -3.85972],	[-4.97555, -3.89043],
        [-4.93245, -3.92074],	[-4.88872, -3.95066],	[-4.84439, -3.98022],	[-4.79951, -4.00943],	[-4.75411, -4.03832],
        [-4.70824, -4.0669 ],	[-4.66195, -4.09519],	[-4.61526, -4.12322],	[-4.56822, -4.15101],	[-4.52086, -4.17858],
        [-4.47322, -4.20595],	[-4.42534, -4.23314],	[-4.37725, -4.26018],	[-4.32899, -4.28708],	[-4.2806 , -4.31388],
        [-4.23211, -4.34061],	[-4.18357, -4.36729],	[-4.13502, -4.39395],	[-4.08647, -4.42061],	[-4.03792, -4.44726],
        [-3.98937, -4.47391],	[-3.94083, -4.50057],	[-3.89228, -4.52722],	[-3.84373, -4.55387],	[-3.79519, -4.58052],
        [-3.74663, -4.60716],	[-3.69808, -4.63381],	[-3.64953, -4.66047],	[-3.60098, -4.68712],	[-3.55244, -4.71378],
        [-3.50389, -4.74043],	[-3.45534, -4.76709],	[-3.4068 , -4.79375],	[-3.35825, -4.8204 ],	[-3.3097 , -4.84706],
        [-3.26116, -4.87371],	[-3.21261, -4.90036],	[-3.16406, -4.92702],	[-3.11552, -4.95369],	[-3.06698, -4.98036],
        [-3.01844, -5.00704],	[-2.96991, -5.03373],	[-2.92138, -5.06041],	[-2.87285, -5.0871 ],	[-2.82433, -5.11379],
        [-2.77581, -5.14046],	[-2.72729, -5.16712],	[-2.67878, -5.19374],	[-2.63026, -5.22033],	[-2.58174, -5.24686],
        [-2.53321, -5.27333],	[-2.48468, -5.29973],	[-2.43614, -5.32603],	[-2.38758, -5.35224],	[-2.33902, -5.37833],
        [-2.29044, -5.4043 ],	[-2.24184, -5.43012],	[-2.19323, -5.4558 ],	[-2.1446 , -5.4813 ],	[-2.09595, -5.50664],
        [-2.04728, -5.53178],	[-1.99858, -5.55671],	[-1.94986, -5.58144],	[-1.90111, -5.60593],	[-1.85233, -5.63018],
        [-1.80353, -5.65418],	[-1.75469, -5.6779 ],	[-1.70583, -5.70135],	[-1.65693, -5.7245 ],	[-1.608  , -5.74734],
        [-1.55903, -5.76986],	[-1.51003, -5.79204],	[-1.46099, -5.81387],	[-1.41192, -5.83533],	[-1.36281, -5.85641],
        [-1.31366, -5.87709],	[-1.26447, -5.89735],	[-1.21524, -5.91718],	[-1.16596, -5.93657],	[-1.11665, -5.9555 ],
        [-1.0673 , -5.97394],	[-1.0179 , -5.99189],	[-0.96847, -6.00933],	[-0.91899, -6.02624],	[-0.86947, -6.04261],
        [-0.81991, -6.05841],	[-0.7703 , -6.07364],	[-0.72066, -6.08826],	[-0.67097, -6.10227],	[-0.62125, -6.11565],
        [-0.57148, -6.12836],	[-0.52168, -6.14038],	[-0.47184, -6.15168],	[-0.42196, -6.16224],	[-0.37205, -6.17203],
        [-0.3221 , -6.18102],	[-0.27212, -6.18919],	[-0.2221 , -6.1965 ],	[-0.17206, -6.20294],	[-0.12199, -6.20846],
        [-0.07189, -6.213  ],	[-0.02178, -6.21646],	[ 0.02835, -6.21876],	[ 0.07847, -6.21978],	[ 0.12858, -6.21943],
        [ 0.17868, -6.21766],	[ 0.22875, -6.21456],	[ 0.2788 , -6.21023],	[ 0.32881, -6.2048 ],	[ 0.37879, -6.19837],
        [ 0.42872, -6.19106],	[ 0.47861, -6.18291],	[ 0.52845, -6.17393],	[ 0.57824, -6.16414],	[ 0.62798, -6.15354],
        [ 0.67767, -6.14216],	[ 0.7273 , -6.13001],	[ 0.77688, -6.1171 ],	[ 0.8264 , -6.10348],	[ 0.87587, -6.08915],
        [ 0.92528, -6.07415],	[ 0.97463, -6.05851],	[ 1.02393, -6.04223],	[ 1.07316, -6.02535],	[ 1.12234, -6.00786],
        [ 1.17145, -5.98978],	[ 1.2205 , -5.97114],	[ 1.2695 , -5.95195],	[ 1.31843, -5.93222],	[ 1.3673 , -5.91198],
        [ 1.41611, -5.89125],	[ 1.46487, -5.87005],	[ 1.51356, -5.84841],	[ 1.5622 , -5.82633],	[ 1.61079, -5.80384],
        [ 1.65932, -5.78096],	[ 1.7078 , -5.75769],	[ 1.75622, -5.73406],	[ 1.80459, -5.71008],	[ 1.85292, -5.68577],
        [ 1.90119, -5.66113],	[ 1.94942, -5.63619],	[ 1.9976 , -5.61096],	[ 2.04573, -5.58545],	[ 2.09382, -5.55968],
        [ 2.14187, -5.53366],	[ 2.18988, -5.5074 ],	[ 2.23785, -5.48092],	[ 2.28579, -5.45422],	[ 2.33369, -5.42733],
        [ 2.38156, -5.40024],	[ 2.42938, -5.37296],	[ 2.47715, -5.3455 ],	[ 2.52486, -5.31784],	[ 2.57251, -5.29001],
        [ 2.62009, -5.26201],	[ 2.66759, -5.23385],	[ 2.71501, -5.20554],	[ 2.76232, -5.17707],	[ 2.80952, -5.14848],
        [ 2.85661, -5.11975],	[ 2.90359, -5.0909 ],	[ 2.95046, -5.06192],	[ 2.99722, -5.03283],	[ 3.04386, -5.00362],
        [ 3.0904 , -4.97429],	[ 3.13683, -4.94485],	[ 3.18315, -4.9153 ],	[ 3.22935, -4.88564],	[ 3.27545, -4.85587],
        [ 3.32143, -4.826  ],	[ 3.3673 , -4.79602],	[ 3.41305, -4.76594],	[ 3.45869, -4.73575],	[ 3.50422, -4.70547],
        [ 3.54963, -4.67508],	[ 3.59492, -4.64459],	[ 3.64011, -4.614  ],	[ 3.68517, -4.58331],	[ 3.73013, -4.55252],
        [ 3.77497, -4.52164],	[ 3.81969, -4.49066],	[ 3.86429, -4.45958],	[ 3.90879, -4.42841],	[ 3.95316, -4.39714],
        [ 3.99742, -4.36578],	[ 4.04156, -4.33432],	[ 4.08558, -4.30277],	[ 4.12948, -4.27112],	[ 4.17327, -4.23938],
        [ 4.21693, -4.20755],	[ 4.26048, -4.17563],	[ 4.30392, -4.14361],	[ 4.34723, -4.11151],	[ 4.39043, -4.07931],
        [ 4.4335 , -4.04701],	[ 4.47644, -4.01463],	[ 4.51926, -3.98214],	[ 4.56195, -3.94956],	[ 4.6045 , -3.91688],
        [ 4.64693, -3.88411],	[ 4.68921, -3.85123],	[ 4.73136, -3.81825],	[ 4.77337, -3.78517],	[ 4.81523, -3.75199],
        [ 4.85695, -3.7187 ],	[ 4.89851, -3.68531],	[ 4.93992, -3.6518 ],	[ 4.98117, -3.61819],	[ 5.02226, -3.58446],
        [ 5.06319, -3.55062],	[ 5.10394, -3.51666],	[ 5.14451, -3.48258],	[ 5.1849 , -3.44838],	[ 5.2251 , -3.41405],
        [ 5.26511, -3.3796 ],	[ 5.30492, -3.34501],	[ 5.34451, -3.31029],	[ 5.38389, -3.27542],	[ 5.42304, -3.24041],
        [ 5.46195, -3.20526],	[ 5.50062, -3.16995],	[ 5.53904, -3.13448],	[ 5.57718, -3.09885],	[ 5.61505, -3.06306],
        [ 5.65264, -3.0271 ],	[ 5.68992, -2.99096],	[ 5.7269 , -2.95464],	[ 5.76355, -2.91814],	[ 5.79987, -2.88145],
        [ 5.83584, -2.84457],	[ 5.87145, -2.80749],	[ 5.90665, -2.77019],	[ 5.94141, -2.73267],	[ 5.9757 , -2.69492],
        [ 6.00949, -2.65692],	[ 6.04276, -2.61867],	[ 6.07554, -2.5802 ],	[ 6.10789, -2.54152],	[ 6.13985, -2.50267],
        [ 6.17147, -2.46367],	[ 6.20279, -2.42454],	[ 6.23382, -2.38529],	[ 6.26454, -2.34591],	[ 6.29495, -2.30641],
        [ 6.32504, -2.26677],	[ 6.3548 , -2.227  ],	[ 6.38421, -2.18709],	[ 6.41328, -2.14704],	[ 6.44202, -2.10686],
        [ 6.47043, -2.06656],	[ 6.49852, -2.02613],	[ 6.52628, -1.98558],	[ 6.55371, -1.94492],	[ 6.58083, -1.90413],
        [ 6.60761, -1.86323],	[ 6.63406, -1.82221],	[ 6.66019, -1.78107],	[ 6.68598, -1.73982],	[ 6.71143, -1.69846],
        [ 6.73656, -1.65698],	[ 6.76135, -1.61539],	[ 6.7858 , -1.5737 ],	[ 6.80992, -1.53189],	[ 6.8337 , -1.48998],
        [ 6.85714, -1.44796],	[ 6.88022, -1.40584],	[ 6.90295, -1.3636 ],	[ 6.92531, -1.32126],	[ 6.94729, -1.2788 ],
        [ 6.9689 , -1.23623],	[ 6.99011, -1.19356],	[ 7.01092, -1.15077],	[ 7.03132, -1.10786],	[ 7.0513 , -1.06485],
        [ 7.07084, -1.02172],	[ 7.08995, -0.97847],	[ 7.10861, -0.93511],	[ 7.12682, -0.89163],	[ 7.14456, -0.84804],
        [ 7.16183, -0.80434],	[ 7.1786 , -0.76052],	[ 7.19485, -0.71657],	[ 7.21056, -0.67251],	[ 7.22572, -0.62832],
        [ 7.24029, -0.58401],	[ 7.25426, -0.53957],	[ 7.26761, -0.495  ],	[ 7.28032, -0.45031],	[ 7.29237, -0.4055 ],
        [ 7.30373, -0.36055],	[ 7.31438, -0.31549],	[ 7.32431, -0.2703 ],	[ 7.33347, -0.22499],	[ 7.34185, -0.17957],
        [ 7.34941, -0.13403],	[ 7.35613, -0.08838],	[ 7.36194, -0.04262],	[ 7.3668 ,  0.00324],	[ 7.37065,  0.04919],
        [ 7.37343,  0.09522],	[ 7.37508,  0.14133],	[ 7.37555,  0.1875 ],	[ 7.37477,  0.23367],	[ 7.37266,  0.2798 ],
        [ 7.36919,  0.32585],	[ 7.36426,  0.37178],	[ 7.35784,  0.41753],	[ 7.3499 ,  0.46306],	[ 7.34039,  0.50829],
        [ 7.3293 ,  0.55316],	[ 7.31659,  0.59762],	[ 7.30223,  0.6416 ],	[ 7.2861 ,  0.68493],	[ 7.26801,  0.72743],
        [ 7.24782,  0.76889],	[ 7.22533,  0.80913],	[ 7.2004 ,  0.84794],	[ 7.17302,  0.88525],	[ 7.14348,  0.92121],
        [ 7.11211,  0.95599],	[ 7.07923,  0.98974],	[ 7.04518,  1.02264],	[ 7.01025,  1.05483],	[ 6.9745 ,  1.08634],
        [ 6.93789,  1.11715],	[ 6.90039,  1.14724],	[ 6.86197,  1.17658],	[ 6.82261,  1.20515],	[ 6.78229,  1.23294],
        [ 6.74108,  1.26   ],	[ 6.69904,  1.28635],	[ 6.65622,  1.31203],	[ 6.61268,  1.33707],	[ 6.56848,  1.3615 ],
        [ 6.52363,  1.38534],	[ 6.47818,  1.40861],	[ 6.43213,  1.43131],	[ 6.38551,  1.45348],	[ 6.33834,  1.47511],
        [ 6.29064,  1.49623],	[ 6.24243,  1.51685],	[ 6.19374,  1.53699],	[ 6.14459,  1.55665],
    ])
    progress_diffs = np.array([
        0.12014, 0.134  , 0.09199, 0.13875, 0.10012, 0.13046, 0.12158, 0.10433, 0.13215, 0.12364, 0.11535, 0.11232, 0.13861, 0.11285, 0.13933, 0.12401, 0.09786, 
        0.12753, 0.12916, 0.1195 , 0.13179, 0.11978, 0.11006, 0.12521, 0.1314 , 0.11036, 0.12546, 0.12022, 0.13056, 0.12094, 0.11426, 0.13652, 0.1152 , 0.10769, 
        0.13882, 0.10224, 0.13714, 0.13219, 0.1039 , 0.121  , 0.1268 , 0.12422, 0.13137, 0.10181, 0.12381, 0.14388, 0.12524, 0.10832, 0.12033, 0.1213 , 0.13455, 
        0.10258, 0.11572, 0.12494, 0.12766, 0.11405, 0.12618, 0.13414, 0.109  , 0.11496, 0.12714, 0.13903, 0.09969, 0.13477, 0.09761, 0.16643, 0.10784, 0.10827, 
        0.12516, 0.13235, 0.09443, 0.1382 , 0.12433, 0.1257 , 0.11422, 0.10625, 0.15203, 0.13213, 0.11198, 0.1231 , 0.12884, 0.11723, 0.13184, 0.11858, 0.13226, 
        0.11598, 0.137  , 0.12237, 0.12575, 0.12503, 0.11525, 0.11415, 0.13187, 0.11353, 0.11265, 0.15534, 0.09484, 0.13283, 0.11352, 0.13265, 0.11488, 0.13228, 
        0.11787, 0.12471, 0.1115 , 0.138  , 0.12017, 0.11542, 0.1241 , 0.11781, 0.1233 , 0.13304, 0.12527, 0.11948, 0.10946, 0.13816, 0.12871, 0.1016 , 0.128  , 
        0.12966, 0.10149, 0.13838, 0.13123, 0.11208, 0.11301, 0.13663, 0.11626, 0.12879, 0.11904, 0.12181, 0.11402, 0.13916, 0.11004, 0.12998, 0.11537, 0.10514, 
        0.1405 , 0.11146, 0.12464, 0.12726, 0.12026, 0.12255, 0.11247, 0.13336, 0.12562, 0.11324, 0.12393, 0.12201, 0.12034, 0.11555, 0.13963, 0.11874, 0.10903, 
        0.11929, 0.13597, 0.10642, 0.13882, 0.11019, 0.12933, 0.11428, 0.13886, 0.10387, 0.1231 , 0.13652, 0.1139 , 0.11672, 0.12437, 0.13403, 0.12301, 0.11502, 
        0.12845, 0.11854, 0.1188 , 0.12139, 0.11534, 0.12103, 0.13285, 0.10536, 0.13203, 0.1161 , 0.12264, 0.13873, 0.09893, 0.12572, 0.13201, 0.11865, 0.12159, 
        0.12868, 0.10282, 0.13919, 0.12254, 0.13008, 0.11433, 0.11787, 0.11222, 0.14037, 0.10778, 0.12403, 0.14902, 0.11015, 0.11678, 0.10349, 0.13318, 0.12216, 
        0.12063, 0.11599, 0.12419, 0.11421, 0.10886, 0.10783, 0.1297 , 0.09621, 0.12236, 0.11564, 0.11379, 0.11818, 0.09228, 0.10321, 0.11751, 0.10892, 0.10108, 
        0.09907, 0.11122, 0.08578, 0.10647, 0.15902, 0.09846, 0.09085, 0.10199, 0.08787, 0.09374, 0.3193 , 0.11894, 0.08041, 0.52591, 0.07985, 0.11199, 0.0977 , 
        0.33564, 0.09509, 0.09653, 0.09324, 0.09339, 0.13393, 0.08233, 0.11359, 0.11637, 0.08782, 0.10245, 0.10529, 0.10766, 0.12227, 0.11035, 0.09546, 0.10957, 
        0.10766, 0.13067, 0.12215, 0.12382, 0.07552, 0.14246, 0.12039, 0.09159, 0.13566, 0.12404, 0.12635, 0.11464, 0.12817, 0.12809, 0.10492, 0.12571, 0.11387, 
        0.1249 , 0.10257, 0.12316, 0.10522, 0.11878, 0.10948, 0.12549, 0.11359, 0.11234, 0.1226 , 0.11389, 0.10354, 0.11875, 0.12373, 0.10618, 0.11772, 0.08766, 
        0.12253, 0.16574, 0.07997, 0.12173, 0.09328, 0.11412, 0.10365, 0.20283, 0.09974, 0.1005 , 0.11773, 0.09377, 0.22807, 0.10565, 0.11529, 0.1095 , 0.09834, 
        0.27793, 0.12379, 0.08929, 0.11122, 0.28967, 0.11295, 0.09251, 0.12113, 0.09678, 0.25098, 0.09536, 0.10765, 0.11015, 0.10461, 0.21215, 0.10138, 0.10796, 
        0.10675, 0.11997, 0.09244, 0.18368, 0.0938 , 0.10387, 0.1301 , 0.11514, 0.121  , 0.13338, 0.08715, 0.13597, 0.09653, 0.11486, 0.13965, 0.10851, 0.11058, 
        0.10738, 0.1181 , 0.12314, 0.10448, 0.12829, 0.09815, 0.13252, 0.11002, 0.13987, 0.09187, 0.14375, 0.10741, 0.10178, 0.1254 , 0.1318 , 0.08858, 0.12301, 
        0.1063 , 0.11868, 0.1106 , 0.10905, 0.11667, 0.1096 , 0.09315, 0.11018, 0.10712, 0.12101, 0.0954 , 0.1069 , 0.09964, 0.08701, 0.10625, 0.08264, 0.12084, 
        0.09158, 0.07554, 0.08924, 0.0844 , 0.07036, 0.37836, 0.10381, 0.68084, 0.072  , 0.12091, 0.28889, 0.078  , 0.09369, 0.06725, 0.11653, 0.08931, 0.08828, 
        0.11458, 0.10683, 0.05705, 0.07509, 0.13632, 0.09282, 0.14064, 0.12378, 0.109  , 0.07839, 0.09506, 0.15362, 0.07844, 0.14705, 0.11715, 0.09798, 0.15563, 
        0.08005, 0.11446, 0.14954, 0.11247, 0.12133, 0.11403, 0.12598, 0.15057, 0.09463, 0.12862, 0.1319 , 0.11595, 0.12249, 0.09469, 0.13735, 0.13332, 0.09733, 
        0.13983, 0.09969, 0.13715, 0.12466, 0.10107, 0.11355, 0.13657, 0.07167, 0.11001, 0.11639, 0.11697, 0.09891, 0.11459, 0.10537, 0.08968, 0.09772, 0.1115 , 
        0.08241, 0.09682, 0.12255, 0.10831, 0.08611, 0.11206, 0.07824, 0.38593, 0.08411, 0.10461, 0.46985, 0.07276, 0.11936, 0.09369, 0.33081, 0.08828, 0.1191 , 
        0.08312, 0.10442, 0.1799 , 0.09489, 0.09064, 0.10578, 0.11211, 0.10819, 0.08576, 0.14137, 0.12297, 0.06408, 0.13014, 0.09746, 0.10012, 0.12546, 0.13137, 
        0.126  , 0.11558, 0.08416, 0.12344, 0.11201, 0.05471, 0.17639, 0.13987, 0.11924, 0.09725, 0.14506, 0.09503, 0.13348, 0.10021, 0.13902, 0.12316, 0.12403, 
        0.1134 , 0.12198, 0.12426, 0.12203, 0.12911, 0.11283, 0.13826, 0.10609, 0.13632, 0.11852, 0.10155, 0.10723, 0.13462, 0.14471, 0.11129, 0.13732, 0.10445, 
        0.144  , 0.09313, 0.13254, 0.11012, 0.14037, 0.10725, 0.14431, 0.09554, 0.15148, 0.10374, 0.13564, 0.11536, 0.12143, 0.14081, 0.08982, 0.14571, 0.0895 , 
        0.13273, 0.13371, 0.12001, 0.10823, 0.14059, 0.13407, 0.08269, 0.14634, 0.12903, 0.12117, 0.10534, 0.12444, 0.1271 , 0.12584, 0.1162 , 0.10999, 0.13815, 
        0.10877, 0.11122, 0.15349, 0.09769, 0.10561, 0.133  , 0.11223, 0.13917, 0.10178, 0.1173 , 0.10356, 0.12431, 0.1163 , 0.1024 , 0.0997 , 0.15311, 0.08611, 
        0.11672, 0.14974, 0.10562, 0.09666, 0.12112, 0.10571, 0.13464, 0.10284, 0.11456, 0.11123, 0.09533, 0.14339, 0.08521, 0.1667 , 0.11909, 0.12594, 0.08769, 
        0.12954, 0.25536, 0.10456, 0.09312, 0.12146, 0.3448 , 0.09911, 0.10049, 0.14346, 0.09246, 0.29713, 0.12239, 0.09452, 0.09663, 0.09565, 0.20925, 0.09024, 
        0.1298 , 0.09669, 0.10496, 0.09646, 0.13378, 0.1081 , 0.10143, 0.12496, 0.11893, 0.106  , 0.12605, 0.0934 , 0.12933, 0.11246, 0.11318, 0.10232, 0.14351, 
        0.09835, 0.12907, 0.1081 , 0.1457 , 0.08866, 0.12495, 0.1213 , 0.12056, 0.12066, 0.10998, 0.14813, 0.09733, 0.12561, 0.09069, 0.16101, 0.10914, 0.12979, 
        0.11481, 0.12345, 0.1105 , 0.1434 , 0.10815, 0.12406, 0.09054, 0.14314, 0.12415, 0.13748, 0.109  , 0.13079, 0.10293, 0.14179, 0.1014 , 0.13116, 0.1327 , 
        0.10499, 0.11956, 0.14874, 0.08566, 0.13898, 0.12438, 0.11276, 0.11172, 0.12745, 0.11964, 0.1198 , 0.1144 , 0.12774, 0.11597, 0.10856, 0.13877, 0.12984, 
        0.10199, 0.10477, 0.13222, 0.13116, 0.10289, 0.13077, 0.12788, 0.11847, 0.10225, 0.1137 , 0.11973, 0.14268, 0.10727, 0.1111 , 0.11307, 0.12588, 0.11797, 
        0.12115, 0.09463, 0.1508 , 0.11018, 0.1118 , 0.10197, 0.13323, 0.11455, 0.11498, 0.12961, 0.10486, 0.11574, 0.12023, 0.0985 , 0.13964, 0.11598, 0.10412, 
        0.13229, 0.09678, 0.10563, 0.1652 , 0.1213 , 0.09327, 0.1408 , 0.10629, 0.18795, 0.1042 , 0.14361, 0.10199, 0.13383, 0.17436, 0.10948, 0.10611, 0.10333, 
        0.142  , 0.18781, 0.09522, 0.14192, 0.08261, 0.09708, 0.21639, 0.07409, 0.12375, 0.09919, 0.10743, 0.11857, 0.13081, 0.08665, 0.13286, 0.09578, 0.09126, 
        0.12794, 0.09807, 0.11666, 0.09916, 0.10523, 0.10853, 0.11059, 0.11325, 0.09374, 0.10473, 0.12941, 0.09199, 0.11204, 0.08416, 0.15262, 0.09537, 0.09568, 
        0.09661, 0.1222 , 0.09048, 0.21626, 0.09728, 0.10732, 0.10078, 0.10973, 0.13576, 0.09843, 0.07884, 0.1175 , 0.10365, 0.09907, 0.10736, 0.13425, 0.10109, 
        0.11149, 0.08654, 0.09452, 0.12445, 0.12139, 0.09183, 0.10574, 0.11056, 0.08619, 0.11573, 0.11694, 0.10131, 0.11316, 0.09829, 0.1152 , 0.08701, 0.16352, 
        0.09444, 0.10562, 0.08637, 0.11795, 0.10282, 0.19943, 0.08477, 0.09623, 0.08524, 0.13441, 0.08058, 0.28117, 0.09868, 0.10861, 0.09684, 0.45461, 0.07742, 
        0.11201, 0.43664, 0.09769, 0.07893, 0.11901, 0.09787, 0.09811, 0.10153, 0.09924, 0.10324, 0.11169, 0.08817, 0.11065, 0.10969, 0.09786, 0.12746, 0.11893, 
        0.09223, 0.11861, 0.13107, 0.11414, 0.12641, 0.09184, 0.12704, 0.10451
    ])
    interpolation_points = [5, 5, 1.75, 3.35, 0, 0]

def inverse_interpolation(x: float, h: float, g: float, i: float, j: float, k: float, l: float) -> float:
    b = (g*h*i-g*h*k+j*i*k+l*k*h-l*k*i-i*j*h) / (l*h-j*h-i*l+g*i-g*k+j*k)
    c = (g*h-g*b+j*b-j*i)/(h-i)
    a = (i-b)*(j-c)

    return (a / (x - b)) + c

def reward_function(params):
    if PARAMS.prev_steps is None or params['steps'] < PARAMS.prev_steps:
        PARAMS.prev_progress = params['progress']

    distances_to_waypoints = np.hypot(PARAMS.waypoints[:, 0] - params['x'], PARAMS.waypoints[:, 1] - params['y'])
    closest_waypoint, second_closest_waypoint = np.argpartition(distances_to_waypoints, 2)[:2]

    reward = 25

    #Distance reward
    normalized_distance_from_route = distances_to_waypoints[closest_waypoint] / (params['track_width'] * 0.5)
    reward -= min(normalized_distance_from_route * 25, 25)

    #Diff reward
    front_waypoint = None
    behind_waypoint = None
    max_waypoint = max(closest_waypoint, second_closest_waypoint)
    min_waypoint = min(closest_waypoint, second_closest_waypoint)
    if max_waypoint - min_waypoint < len(PARAMS.waypoints) / 2:
        front_waypoint = max_waypoint
        behind_waypoint = min_waypoint
    else:
        front_waypoint = min_waypoint
        behind_waypoint = max_waypoint
    if abs((max_waypoint - min_waypoint + 1) % len(PARAMS.waypoints) - 1) != 1 and closest_waypoint == front_waypoint:
        print("caught")
        behind_waypoint = (front_waypoint - 1) % len(PARAMS.waypoints)

    predicted_steps = params['steps'] * 100 / params['progress']
    diff = params['progress'] - PARAMS.prev_progress
    diff_ratio = diff / PARAMS.progress_diffs[behind_waypoint]
    reward *= max(inverse_interpolation(diff_ratio, *PARAMS.interpolation_points), 0) * 1000 / predicted_steps

    PARAMS.prev_progress = params['progress']
    PARAMS.prev_steps = params['steps']
    return float(reward)

