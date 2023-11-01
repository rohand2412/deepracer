import numpy as np
from shapely.geometry import Polygon, Point

class PARAMS:
    waypoints = np.array([
        [ 6.03198,  1.51865],	[ 5.98548,  1.5402 ],	[ 5.93854,  1.56134],	[ 5.8912 ,  1.58211],	[ 5.84346,  1.60251],
        [ 5.79535,  1.62258],	[ 5.74689,  1.64234],	[ 5.6981 ,  1.6618 ],	[ 5.64899,  1.68099],	[ 5.59958,  1.69993],
        [ 5.5499 ,  1.71864],	[ 5.49997,  1.73715],	[ 5.4498 ,  1.75547],	[ 5.39943,  1.77361],	[ 5.3489 ,  1.79157],
        [ 5.29826,  1.80935],	[ 5.24752,  1.82697],	[ 5.19674,  1.84442],	[ 5.14589,  1.86176],	[ 5.09493,  1.87905],
        [ 5.04381,  1.89636],	[ 4.99249,  1.91377],	[ 4.94091,  1.93135],	[ 4.88907,  1.94913],	[ 4.83703,  1.9671 ],
        [ 4.78485,  1.9852 ],	[ 4.7326 ,  2.00341],	[ 4.68036,  2.02167],	[ 4.6282 ,  2.03996],	[ 4.57613,  2.05826],
        [ 4.52412,  2.07658],	[ 4.47215,  2.09494],	[ 4.42022,  2.11334],	[ 4.36829,  2.13178],	[ 4.31635,  2.15028],
        [ 4.26442,  2.16884],	[ 4.21249,  2.18744],	[ 4.16057,  2.20609],	[ 4.10867,  2.22478],	[ 4.05678,  2.2435 ],
        [ 4.00491,  2.26227],	[ 3.95306,  2.28108],	[ 3.90123,  2.29993],	[ 3.84941,  2.31882],	[ 3.79761,  2.33775],
        [ 3.74582,  2.35672],	[ 3.69404,  2.37573],	[ 3.64228,  2.39478],	[ 3.59053,  2.41388],	[ 3.5388 ,  2.43301],
        [ 3.48708,  2.45218],	[ 3.43537,  2.47139],	[ 3.38368,  2.49064],	[ 3.33201,  2.50993],	[ 3.28035,  2.52926],
        [ 3.2287 ,  2.54863],	[ 3.17707,  2.56804],	[ 3.12545,  2.58749],	[ 3.07385,  2.60698],	[ 3.02226,  2.62651],
        [ 2.97069,  2.64608],	[ 2.91914,  2.6657 ],	[ 2.8676 ,  2.68535],	[ 2.81607,  2.70505],	[ 2.76457,  2.72479],
        [ 2.71307,  2.74458],	[ 2.6616 ,  2.7644 ],	[ 2.61014,  2.78427],	[ 2.5587 ,  2.80419],	[ 2.50727,  2.82415],
        [ 2.45586,  2.84415],	[ 2.40447,  2.8642 ],	[ 2.3531 ,  2.8843 ],	[ 2.30174,  2.90444],	[ 2.25041,  2.92463],
        [ 2.19909,  2.94487],	[ 2.14779,  2.96515],	[ 2.09651,  2.98548],	[ 2.04524,  3.00586],	[ 1.994  ,  3.02629],
        [ 1.94278,  3.04678],	[ 1.89157,  3.06731],	[ 1.84039,  3.08789],	[ 1.78922,  3.10852],	[ 1.73808,  3.1292 ],
        [ 1.68695,  3.14994],	[ 1.63585,  3.17073],	[ 1.58476,  3.19157],	[ 1.5337 ,  3.21246],	[ 1.48266,  3.2334 ],
        [ 1.43164,  3.2544 ],	[ 1.38063,  3.27545],	[ 1.32966,  3.29655],	[ 1.2787 ,  3.31771],	[ 1.22776,  3.33892],
        [ 1.17684,  3.36018],	[ 1.12595,  3.38149],	[ 1.07508,  3.40286],	[ 1.02422,  3.42429],	[ 0.97339,  3.44576],
        [ 0.92258,  3.46729],	[ 0.8718 ,  3.48887],	[ 0.82103,  3.51051],	[ 0.77028,  3.5322 ],	[ 0.71956,  3.55394],
        [ 0.66886,  3.57573],	[ 0.61818,  3.59758],	[ 0.56752,  3.61948],	[ 0.51688,  3.64143],	[ 0.46626,  3.66343],
        [ 0.41566,  3.68548],	[ 0.36509,  3.70759],	[ 0.31453,  3.72975],	[ 0.264  ,  3.75195],	[ 0.21349,  3.77421],
        [ 0.16299,  3.79652],	[ 0.11252,  3.81888],	[ 0.06207,  3.84129],	[ 0.01164,  3.86375],	[-0.03877,  3.88626],
        [-0.08916,  3.90882],	[-0.13953,  3.93142],	[-0.18988,  3.95408],	[-0.24021,  3.97678],	[-0.29052,  3.99953],
        [-0.34082,  4.02233],	[-0.39109,  4.04517],	[-0.44134,  4.06806],	[-0.49158,  4.091  ],	[-0.54179,  4.11398],
        [-0.59199,  4.137  ],	[-0.64217,  4.16008],	[-0.69233,  4.18319],	[-0.74247,  4.20635],	[-0.79259,  4.22955],
        [-0.8427 ,  4.25279],	[-0.89279,  4.27607],	[-0.94286,  4.2994 ],	[-0.99292,  4.32276],	[-1.04296,  4.34617],
        [-1.09298,  4.36961],	[-1.14299,  4.39309],	[-1.19298,  4.41661],	[-1.24295,  4.44017],	[-1.29292,  4.46376],
        [-1.34286,  4.48738],	[-1.39279,  4.51104],	[-1.44271,  4.53474],	[-1.49262,  4.55846],	[-1.54251,  4.58222],
        [-1.59239,  4.60601],	[-1.64225,  4.62982],	[-1.69211,  4.65367],	[-1.74195,  4.67754],	[-1.79178,  4.70145],
        [-1.8416 ,  4.72537],	[-1.89141,  4.74933],	[-1.94121,  4.77331],	[-1.99099,  4.79731],	[-2.04077,  4.82134],
        [-2.09053,  4.84539],	[-2.14029,  4.86946],	[-2.19004,  4.89356],	[-2.23978,  4.91769],	[-2.28951,  4.94184],
        [-2.33923,  4.96601],	[-2.38895,  4.99021],	[-2.43865,  5.01443],	[-2.48833,  5.03867],	[-2.53799,  5.06293],
        [-2.58763,  5.08721],	[-2.63725,  5.11152],	[-2.68688,  5.13585],	[-2.73651,  5.16022],	[-2.78617,  5.18462],
        [-2.83587,  5.20906],	[-2.88559,  5.23353],	[-2.93529,  5.25803],	[-2.98491,  5.28254],	[-3.03441,  5.30705],
        [-3.08374,  5.33156],	[-3.13285,  5.35603],	[-3.18178,  5.38047],	[-3.23058,  5.40485],	[-3.27929,  5.42914],
        [-3.32798,  5.45333],	[-3.37668,  5.47741],	[-3.42543,  5.50134],	[-3.4742 ,  5.5251 ],	[-3.52298,  5.54867],
        [-3.57174,  5.57201],	[-3.62048,  5.59511],	[-3.66919,  5.61794],	[-3.71784,  5.64047],	[-3.76646,  5.66269],
        [-3.81504,  5.68458],	[-3.86358,  5.70611],	[-3.91209,  5.72727],	[-3.96055,  5.74802],	[-4.00898,  5.76836],
        [-4.05735,  5.78826],	[-4.10568,  5.8077 ],	[-4.15394,  5.82665],	[-4.20215,  5.8451 ],	[-4.25029,  5.86302],
        [-4.29837,  5.88038],	[-4.34637,  5.89717],	[-4.3943 ,  5.91337],	[-4.44214,  5.92894],	[-4.4899 ,  5.94388],
        [-4.53757,  5.95815],	[-4.58514,  5.97173],	[-4.63261,  5.98461],	[-4.67998,  5.99675],	[-4.72723,  6.00815],
        [-4.77436,  6.01877],	[-4.82137,  6.02859],	[-4.86825,  6.0376 ],	[-4.91499,  6.04576],	[-4.96158,  6.05306],
        [-5.00802,  6.05946],	[-5.0543 ,  6.06494],	[-5.1004 ,  6.06946],	[-5.14631,  6.07299],	[-5.19203,  6.0755 ],
        [-5.23755,  6.07695],	[-5.28285,  6.07732],	[-5.32792,  6.0766 ],	[-5.37277,  6.07474],	[-5.41737,  6.07174],
        [-5.46171,  6.06755],	[-5.50577,  6.06209],	[-5.5495 ,  6.05525],	[-5.59286,  6.04691],	[-5.63581,  6.03696],
        [-5.67831,  6.02529],	[-5.72034,  6.01187],	[-5.76192,  5.99683],	[-5.80306,  5.98028],	[-5.84379,  5.96235],
        [-5.88413,  5.94316],	[-5.9241 ,  5.92281],	[-5.96369,  5.90134],	[-6.00289,  5.87875],	[-6.04169,  5.85502],
        [-6.08007,  5.83016],	[-6.11804,  5.80416],	[-6.15557,  5.77703],	[-6.19265,  5.7488 ],	[-6.22925,  5.71949],
        [-6.26538,  5.68912],	[-6.30099,  5.65772],	[-6.33609,  5.62532],	[-6.37064,  5.59195],	[-6.40461,  5.55764],
        [-6.43797,  5.52243],	[-6.47069,  5.48636],	[-6.50275,  5.44945],	[-6.53411,  5.41175],	[-6.56477,  5.3733 ],
        [-6.59472,  5.33416],	[-6.62392,  5.29436],	[-6.65237,  5.25395],	[-6.68005,  5.21298],	[-6.70696,  5.17147],
        [-6.73309,  5.12947],	[-6.75843,  5.08701],	[-6.78297,  5.04412],	[-6.80671,  5.00083],	[-6.82965,  4.95718],
        [-6.85176,  4.91318],	[-6.87306,  4.86886],	[-6.89353,  4.82425],	[-6.91316,  4.77937],	[-6.93196,  4.73425],
        [-6.94992,  4.68891],	[-6.96704,  4.64336],	[-6.98334,  4.59763],	[-6.9988 ,  4.55174],	[-7.01343,  4.50571],
        [-7.02724,  4.45955],	[-7.04023,  4.41328],	[-7.0524 ,  4.36692],	[-7.06376,  4.32047],	[-7.07432,  4.27396],
        [-7.08407,  4.22739],	[-7.09303,  4.18078],	[-7.10119,  4.13414],	[-7.10854,  4.08748],	[-7.1151 ,  4.04081],
        [-7.12086,  3.99414],	[-7.12582,  3.94748],	[-7.12999,  3.90084],	[-7.13335,  3.85423],	[-7.13592,  3.80766],
        [-7.13769,  3.76113],	[-7.13865,  3.71467],	[-7.1388 ,  3.66826],	[-7.13812,  3.62194],	[-7.1366 ,  3.57571],
        [-7.13423,  3.52958],	[-7.13099,  3.48355],	[-7.12688,  3.43765],	[-7.1219 ,  3.39186],	[-7.11607,  3.34621],
        [-7.10936,  3.3007 ],	[-7.1018 ,  3.25533],	[-7.09334,  3.21012],	[-7.08391,  3.1651 ],	[-7.07344,  3.12031],
        [-7.06185,  3.07576],	[-7.04906,  3.03149],	[-7.03503,  2.98753],	[-7.01979,  2.94387],	[-7.00343,  2.90052],
        [-6.98601,  2.85745],	[-6.96762,  2.81467],	[-6.94832,  2.77217],	[-6.92816,  2.72995],	[-6.90718,  2.688  ],
        [-6.88538,  2.64632],	[-6.8628 ,  2.60491],	[-6.83946,  2.56377],	[-6.81539,  2.52289],	[-6.7906 ,  2.48227],
        [-6.76512,  2.44192],	[-6.73896,  2.40183],	[-6.71216,  2.36199],	[-6.68473,  2.32241],	[-6.6567 ,  2.28309],
        [-6.6281 ,  2.24402],	[-6.59893,  2.2052 ],	[-6.56924,  2.16662],	[-6.53905,  2.12829],	[-6.50837,  2.09019],
        [-6.47724,  2.05232],	[-6.44566,  2.01468],	[-6.41366,  1.97725],	[-6.38126,  1.94002],	[-6.34847,  1.90299],
        [-6.31533,  1.86616],	[-6.28186,  1.82952],	[-6.2481 ,  1.79309],	[-6.21407,  1.75687],	[-6.1798 ,  1.72086],
        [-6.14531,  1.68505],	[-6.11058,  1.64939],	[-6.07561,  1.61383],	[-6.04036,  1.57832],	[-6.00482,  1.54282],
        [-5.969  ,  1.50728],	[-5.93296,  1.4718 ],	[-5.89685,  1.43653],	[-5.86081,  1.40162],	[-5.82496,  1.36723],
        [-5.78944,  1.3335 ],	[-5.75433,  1.30047],	[-5.71962,  1.26794],	[-5.68526,  1.23572],	[-5.65123,  1.20359],
        [-5.61751,  1.17135],	[-5.58407,  1.1388 ],	[-5.55098,  1.10593],	[-5.51831,  1.07276],	[-5.48615,  1.0393 ],
        [-5.45459,  1.0056 ],	[-5.42372,  0.97167],	[-5.39359,  0.93752],	[-5.36427,  0.90312],	[-5.33579,  0.86844],
        [-5.30821,  0.83344],	[-5.28157,  0.79811],	[-5.25592,  0.7624 ],	[-5.2313 ,  0.72631],	[-5.20775,  0.68982],
        [-5.18531,  0.65294],	[-5.16401,  0.61565],	[-5.1439 ,  0.57795],	[-5.12507,  0.5398 ],	[-5.10766,  0.50119],
        [-5.09181,  0.46206],	[-5.07765,  0.42238],	[-5.06533,  0.38212],	[-5.05494,  0.34126],	[-5.04637,  0.29983],
        [-5.03947,  0.2579 ],	[-5.03408,  0.21552],	[-5.03004,  0.17275],	[-5.0272 ,  0.12964],	[-5.02549,  0.08623],
        [-5.02491,  0.04252],	[-5.02546, -0.0015 ],	[-5.02715, -0.04581],	[-5.02997, -0.09041],	[-5.03392, -0.13531],
        [-5.03896, -0.18048],	[-5.04506, -0.22592],	[-5.05218, -0.2716 ],	[-5.06028, -0.31751],	[-5.06932, -0.36364],
        [-5.07925, -0.40998],	[-5.09004, -0.45651],	[-5.10163, -0.50322],	[-5.11398, -0.55011],	[-5.12704, -0.59716],
        [-5.14076, -0.64435],	[-5.15509, -0.69168],	[-5.16997, -0.73912],	[-5.18535, -0.78665],	[-5.20117, -0.83425],
        [-5.21738, -0.88192],	[-5.23394, -0.92964],	[-5.25081, -0.97744],	[-5.26796, -1.02534],	[-5.28536, -1.07334],
        [-5.30296, -1.12147],	[-5.32071, -1.16972],	[-5.33851, -1.21805],	[-5.35626, -1.26642],	[-5.37384, -1.3148 ],
        [-5.39117, -1.36315],	[-5.40813, -1.41142],	[-5.42468, -1.45961],	[-5.44081, -1.50773],	[-5.45647, -1.55576],
        [-5.47166, -1.60373],	[-5.48634, -1.65162],	[-5.50049, -1.69943],	[-5.51408, -1.74717],	[-5.52706, -1.7948 ],
        [-5.53942, -1.84234],	[-5.5511 , -1.88977],	[-5.56209, -1.93708],	[-5.57235, -1.98426],	[-5.58185, -2.0313 ],
        [-5.59054, -2.07819],	[-5.5984 , -2.12493],	[-5.6054 , -2.17151],	[-5.6115 , -2.21791],	[-5.61667, -2.26412],
        [-5.62089, -2.31014],	[-5.62412, -2.35595],	[-5.62633, -2.40154],	[-5.6275 , -2.4469 ],	[-5.62761, -2.49202],
        [-5.62663, -2.5369 ],	[-5.62456, -2.58151],	[-5.62138, -2.62586],	[-5.61707, -2.66994],	[-5.61156, -2.71372],
        [-5.60476, -2.75716],	[-5.59657, -2.80022],	[-5.58689, -2.84286],	[-5.57561, -2.88504],	[-5.56267, -2.92673],
        [-5.54817, -2.96794],	[-5.53221, -3.00871],	[-5.51492, -3.04906],	[-5.49641, -3.089  ],	[-5.47679, -3.12857],
        [-5.45612, -3.16777],	[-5.43441, -3.2066 ],	[-5.41168, -3.24507],	[-5.38795, -3.28318],	[-5.36321, -3.32092],
        [-5.3375 , -3.35829],	[-5.31084, -3.39531],	[-5.28323, -3.43197],	[-5.25472, -3.46828],	[-5.22532, -3.50424],
        [-5.19505, -3.53984],	[-5.16393, -3.57511],	[-5.13199, -3.61003],	[-5.09923, -3.64461],	[-5.06568, -3.67886],
        [-5.03136, -3.71277],	[-4.99629, -3.74636],	[-4.96048, -3.77962],	[-4.92395, -3.81256],	[-4.88672, -3.84518],
        [-4.8488 , -3.87749],	[-4.81023, -3.90948],	[-4.77101, -3.94117],	[-4.73117, -3.97257],	[-4.69074, -4.00368],
        [-4.64974, -4.03451],	[-4.6082 , -4.06507],	[-4.56614, -4.09536],	[-4.52358, -4.1254 ],	[-4.48054, -4.15519],
        [-4.43705, -4.18475],	[-4.39313, -4.21408],	[-4.34881, -4.24319],	[-4.3041 , -4.27208],	[-4.25902, -4.30078],
        [-4.2136 , -4.32929],	[-4.16785, -4.35762],	[-4.1218 , -4.38578],	[-4.07547, -4.41378],	[-4.02888, -4.44163],
        [-3.98204, -4.46933],	[-3.93497, -4.49689],	[-3.88769, -4.52432],	[-3.84022, -4.55163],	[-3.79257, -4.57882],
        [-3.74476, -4.60593],	[-3.6968 , -4.63295],	[-3.6487 , -4.65992],	[-3.60049, -4.68684],	[-3.55217, -4.7137 ],
        [-3.50376, -4.7405 ],	[-3.45529, -4.76721],	[-3.40677, -4.7938 ],	[-3.35822, -4.82026],	[-3.30966, -4.84658],
        [-3.26108, -4.87274],	[-3.21249, -4.89875],	[-3.16389, -4.9246 ],	[-3.11528, -4.95031],	[-3.06666, -4.97586],
        [-3.01802, -5.00126],	[-2.96937, -5.02649],	[-2.92071, -5.05156],	[-2.87203, -5.07646],	[-2.82335, -5.10118],
        [-2.77465, -5.12573],	[-2.72593, -5.15009],	[-2.6772 , -5.17426],	[-2.62846, -5.19824],	[-2.57971, -5.22202],
        [-2.53094, -5.2456 ],	[-2.48216, -5.26898],	[-2.43336, -5.29214],	[-2.38455, -5.31508],	[-2.33572, -5.33781],
        [-2.28687, -5.3603 ],	[-2.23802, -5.38257],	[-2.18914, -5.40459],	[-2.14025, -5.42637],	[-2.09135, -5.4479 ],
        [-2.04242, -5.46918],	[-1.99349, -5.4902 ],	[-1.94453, -5.51096],	[-1.89556, -5.53144],	[-1.84658, -5.55166],
        [-1.79757, -5.5716 ],	[-1.74855, -5.59125],	[-1.69952, -5.61061],	[-1.65047, -5.62968],	[-1.6014 , -5.64846],
        [-1.55232, -5.66693],	[-1.50321, -5.6851 ],	[-1.4541 , -5.70296],	[-1.40497, -5.72051],	[-1.35582, -5.73772],
        [-1.30665, -5.75458],	[-1.25747, -5.7711 ],	[-1.20827, -5.78725],	[-1.15905, -5.80302],	[-1.10981, -5.8184 ],
        [-1.06056, -5.83339],	[-1.01129, -5.84797],	[-0.962  , -5.86213],	[-0.9127 , -5.87586],	[-0.86338, -5.88915],
        [-0.81404, -5.90199],	[-0.76469, -5.91436],	[-0.71532, -5.92624],	[-0.66594, -5.93762],	[-0.61653, -5.94848],
        [-0.56712, -5.9588 ],	[-0.51768, -5.96855],	[-0.46824, -5.97771],	[-0.41878, -5.98626],	[-0.3693 , -5.99417],
        [-0.31981, -6.00142],	[-0.27032, -6.00801],	[-0.22081, -6.01391],	[-0.17129, -6.01911],	[-0.12175, -6.0236 ],
        [-0.07222, -6.0273 ],	[-0.02268, -6.03014],	[ 0.02686, -6.03202],	[ 0.0764 , -6.03284],	[ 0.12592, -6.03251],
        [ 0.17542, -6.03097],	[ 0.22491, -6.02828],	[ 0.27438, -6.02451],	[ 0.32382, -6.01972],	[ 0.37323, -6.014  ],
        [ 0.4226 , -6.00741],	[ 0.47194, -5.99998],	[ 0.52125, -5.99176],	[ 0.57051, -5.98274],	[ 0.61974, -5.97296],
        [ 0.66893, -5.96244],	[ 0.71808, -5.95119],	[ 0.76719, -5.93924],	[ 0.81625, -5.92662],	[ 0.86527, -5.91334],
        [ 0.91424, -5.89944],	[ 0.96316, -5.88492],	[ 1.01204, -5.86982],	[ 1.06086, -5.85415],	[ 1.10963, -5.83795],
        [ 1.15835, -5.82123],	[ 1.207  , -5.80401],	[ 1.2556 , -5.78632],	[ 1.30414, -5.76816],	[ 1.35261, -5.74956],
        [ 1.40101, -5.73052],	[ 1.44934, -5.71105],	[ 1.49759, -5.69117],	[ 1.54577, -5.6709 ],	[ 1.59386, -5.65023],
        [ 1.64187, -5.6292 ],	[ 1.68979, -5.6078 ],	[ 1.73763, -5.58605],	[ 1.78536, -5.56396],	[ 1.83301, -5.54154],
        [ 1.88055, -5.51881],	[ 1.928  , -5.49576],	[ 1.97534, -5.47242],	[ 2.02258, -5.44878],	[ 2.06971, -5.42486],
        [ 2.11673, -5.40067],	[ 2.16364, -5.37621],	[ 2.21043, -5.35149],	[ 2.25711, -5.32652],	[ 2.30368, -5.3013 ],
        [ 2.35013, -5.27585],	[ 2.39646, -5.25017],	[ 2.44267, -5.22426],	[ 2.48877, -5.19814],	[ 2.53474, -5.1718 ],
        [ 2.58059, -5.14526],	[ 2.62632, -5.11851],	[ 2.67193, -5.09157],	[ 2.71741, -5.06444],	[ 2.76277, -5.03713],
        [ 2.80801, -5.00963],	[ 2.85313, -4.98196],	[ 2.89812, -4.95411],	[ 2.943  , -4.9261 ],	[ 2.98775, -4.89792],
        [ 3.03237, -4.86958],	[ 3.07688, -4.84109],	[ 3.12126, -4.81244],	[ 3.16552, -4.78364],	[ 3.20965, -4.7547 ],
        [ 3.25367, -4.72561],	[ 3.29757, -4.69638],	[ 3.34134, -4.66702],	[ 3.38499, -4.63752],	[ 3.42853, -4.60789],
        [ 3.47195, -4.57813],	[ 3.51524, -4.54824],	[ 3.55842, -4.51823],	[ 3.60149, -4.4881 ],	[ 3.64444, -4.45786],
        [ 3.68727, -4.42749],	[ 3.72999, -4.39702],	[ 3.77259, -4.36643],	[ 3.81508, -4.33573],	[ 3.85746, -4.30492],
        [ 3.89973, -4.27402],	[ 3.94189, -4.243  ],	[ 3.98394, -4.21189],	[ 4.02588, -4.18068],	[ 4.0677 , -4.14936],
        [ 4.10941, -4.11795],	[ 4.15101, -4.08643],	[ 4.19249, -4.05482],	[ 4.23386, -4.02311],	[ 4.27511, -3.9913 ],
        [ 4.31625, -3.95939],	[ 4.35727, -3.92739],	[ 4.39817, -3.89529],	[ 4.43896, -3.8631 ],	[ 4.47963, -3.83081],
        [ 4.52018, -3.79843],	[ 4.5606 , -3.76595],	[ 4.60089, -3.73337],	[ 4.64105, -3.70068],	[ 4.68107, -3.6679 ],
        [ 4.72095, -3.635  ],	[ 4.76068, -3.602  ],	[ 4.80027, -3.56889],	[ 4.8397 , -3.53567],	[ 4.87897, -3.50234],
        [ 4.91808, -3.4689 ],	[ 4.95702, -3.43534],	[ 4.99579, -3.40166],	[ 5.03438, -3.36786],	[ 5.07279, -3.33394],
        [ 5.111  , -3.2999 ],	[ 5.14901, -3.26572],	[ 5.18682, -3.23142],	[ 5.22442, -3.19698],	[ 5.2618 , -3.16241],
        [ 5.29894, -3.12769],	[ 5.33585, -3.09284],	[ 5.37251, -3.05783],	[ 5.40889, -3.02268],	[ 5.445  , -2.98736],
        [ 5.48082, -2.95189],	[ 5.51634, -2.91625],	[ 5.55156, -2.88045],	[ 5.58647, -2.84449],	[ 5.62107, -2.80836],
        [ 5.65535, -2.77206],	[ 5.68927, -2.73558],	[ 5.7228 , -2.69892],	[ 5.75588, -2.66205],	[ 5.78846, -2.62496],
        [ 5.82049, -2.58763],	[ 5.85196, -2.55006],	[ 5.88292, -2.51228],	[ 5.91344, -2.47433],	[ 5.94361, -2.43623],
        [ 5.97348, -2.39802],	[ 6.00312, -2.35972],	[ 6.03256, -2.32136],	[ 6.06178, -2.28292],	[ 6.09077, -2.2444 ],
        [ 6.11952, -2.20579],	[ 6.14802, -2.16709],	[ 6.17626, -2.1283 ],	[ 6.20424, -2.08942],	[ 6.23196, -2.05046],
        [ 6.25943, -2.0114 ],	[ 6.28665, -1.97226],	[ 6.31361, -1.93304],	[ 6.34031, -1.89374],	[ 6.36676, -1.85435],
        [ 6.39295, -1.81489],	[ 6.41887, -1.77534],	[ 6.44453, -1.7357 ],	[ 6.46991, -1.69599],	[ 6.49501, -1.65619],
        [ 6.51984, -1.61631],	[ 6.54438, -1.57635],	[ 6.56863, -1.53631],	[ 6.59258, -1.49618],	[ 6.61623, -1.45597],
        [ 6.63957, -1.41568],	[ 6.6626 , -1.37531],	[ 6.68531, -1.33485],	[ 6.7077 , -1.29431],	[ 6.72974, -1.25368],
        [ 6.75144, -1.21297],	[ 6.77279, -1.17218],	[ 6.79377, -1.1313 ],	[ 6.81438, -1.09034],	[ 6.83461, -1.04929],
        [ 6.85444, -1.00816],	[ 6.87387, -0.96694],	[ 6.89289, -0.92563],	[ 6.91148, -0.88425],	[ 6.92965, -0.84277],
        [ 6.94736, -0.80122],	[ 6.96461, -0.75958],	[ 6.98138, -0.71786],	[ 6.99766, -0.67605],	[ 7.01341, -0.63416],
        [ 7.02864, -0.59218],	[ 7.0433 , -0.55013],	[ 7.05738, -0.50799],	[ 7.07084, -0.46577],	[ 7.08365, -0.42347],
        [ 7.0958 , -0.38109],	[ 7.10724, -0.33864],	[ 7.11795, -0.29612],	[ 7.12792, -0.25353],	[ 7.1371 , -0.21089],
        [ 7.14548, -0.16819],	[ 7.15302, -0.12545],	[ 7.1597 , -0.08267],	[ 7.16549, -0.03986],	[ 7.17035,  0.00298],
        [ 7.17427,  0.04584],	[ 7.17721,  0.08871],	[ 7.17912,  0.13156],	[ 7.17992,  0.17439],	[ 7.17955,  0.21714],
        [ 7.17795,  0.25981],	[ 7.17504,  0.30236],	[ 7.17076,  0.34476],	[ 7.1651 ,  0.38701],	[ 7.15803,  0.42909],
        [ 7.14953,  0.47099],	[ 7.13958,  0.51269],	[ 7.12815,  0.55417],	[ 7.11506,  0.5953 ],	[ 7.10009,  0.63587],
        [ 7.08302,  0.6757 ],	[ 7.0636 ,  0.71457],	[ 7.04161,  0.7523 ],	[ 7.01704,  0.7888 ],	[ 6.99024,  0.82422],
        [ 6.96161,  0.8587 ],	[ 6.93155,  0.89239],	[ 6.90046,  0.92545],	[ 6.8687 ,  0.95802],	[ 6.83631,  0.99011],
        [ 6.80323,  1.02169],	[ 6.7694 ,  1.05273],	[ 6.73473,  1.0832 ],	[ 6.69917,  1.11307],	[ 6.6627 ,  1.14232],
        [ 6.62536,  1.17098],	[ 6.58719,  1.19906],	[ 6.54826,  1.22658],	[ 6.5086 ,  1.25357],	[ 6.46826,  1.28004],
        [ 6.42727,  1.30601],	[ 6.38565,  1.33148],	[ 6.34341,  1.35646],	[ 6.30058,  1.38097],	[ 6.25716,  1.40502],
        [ 6.21318,  1.42861],	[ 6.16865,  1.45176],	[ 6.1236 ,  1.47448],	[ 6.07803,  1.49677],
    ])
    outer_border = np.array([
        [ 6.26406,  2.11468],	[ 5.97275,  2.19752],	[ 5.68228,  2.27994],	[ 5.39245,  2.3627 ],	[ 5.10224,  2.44601],
        [ 4.81188,  2.52927],	[ 4.52208,  2.61265],	[ 4.23264,  2.69643],	[ 3.94381,  2.78059],	[ 3.65603,  2.86552],
        [ 3.36851,  2.95185],	[ 3.08099,  3.03907],	[ 2.79468,  3.12711],	[ 2.51092,  3.21631],	[ 2.2313 ,  3.3078 ],
        [ 1.95965,  3.40219],	[ 1.69757,  3.50414],	[ 1.43345,  3.6201 ],	[ 1.16315,  3.74168],	[ 0.89489,  3.8664 ],
        [ 0.62776,  3.99434],	[ 0.36139,  4.1256 ],	[ 0.09539,  4.25953],	[-0.16998,  4.39579],	[-0.43566,  4.53448],
        [-0.70166,  4.67426],	[-0.96729,  4.81513],	[-1.23345,  4.95698],	[-1.50042,  5.09937],	[-1.76769,  5.24137],
        [-2.03533,  5.38355],	[-2.30475,  5.52561],	[-2.57376,  5.6655 ],	[-2.84006,  5.80467],	[-3.10554,  5.94494],
        [-3.37156,  6.08647],	[-3.6382 ,  6.2285 ],	[-3.90601,  6.37114],	[-4.17606,  6.51343],	[-4.44794,  6.6543 ],
        [-4.72166,  6.79334],	[-5.02604,  6.94296],	[-5.43572,  7.07606],	[-5.97104,  7.05149],	[-6.43042,  6.77271],
        [-6.6865 ,  6.44512],	[-6.86422,  6.17227],	[-7.02773,  5.90882],	[-7.18803,  5.64564],	[-7.3437 ,  5.3819 ],
        [-7.49709,  5.12116],	[-7.65421,  4.85416],	[-7.81184,  4.56743],	[-7.95841,  4.25385],	[-8.07953,  3.90743],
        [-8.15397,  3.52532],	[-8.15705,  3.11442],	[-8.06514,  2.69763],	[-7.88004,  2.32195],	[-7.64   ,  2.00844],
        [-7.37049,  1.75104],	[-7.09032,  1.53765],	[-6.80847,  1.35566],	[-6.5299 ,  1.19427],	[-6.25786,  1.04609],
        [-5.99479,  0.9036 ],	[-5.73079,  0.75592],	[-5.46216,  0.61077],	[-5.21208,  0.47497],	[-5.09441,  0.41645],
        [-5.0486 ,  0.43469],	[-5.05871,  0.39201],	[-5.19871,  0.20796],	[-5.33572, -0.05091],	[-5.47849, -0.32182],
        [-5.61752, -0.59451],	[-5.75452, -0.86386],	[-5.89109, -1.13166],	[-6.02885, -1.39849],	[-6.16725, -1.66512],
        [-6.30581, -1.92908],	[-6.45847, -2.21349],	[-6.62046, -2.61835],	[-6.61031, -3.15271],	[-6.37879, -3.60915],
        [-6.06498, -3.91304],	[-5.75452, -4.1175 ],	[-5.46633, -4.27401],	[-5.20307, -4.4114 ],	[-4.94513, -4.55778],
        [-4.67695, -4.70505],	[-4.41193, -4.85051],	[-4.14698, -4.99589],	[-3.88212, -5.14127],	[-3.61724, -5.28672],
        [-3.35231, -5.4322 ],	[-3.08731, -5.57768],	[-2.82261, -5.72293],	[-2.55869, -5.8682 ],	[-2.29526, -6.01399],
        [-2.03129, -6.16076],	[-1.76779, -6.30685],	[-1.50531, -6.454  ],	[-1.24461, -6.60021],	[-0.97405, -6.75615],
        [-0.66237, -6.91475],	[-0.2917 , -7.0458 ],	[ 0.13903, -7.10006],	[ 0.57594, -7.03362],	[ 0.94984, -6.87909],
        [ 1.24182, -6.70532],	[ 1.50032, -6.55057],	[ 1.75953, -6.39614],	[ 2.01912, -6.2414 ],	[ 2.27805, -6.08716],
        [ 2.53766, -5.93352],	[ 2.79777, -5.7793 ],	[ 3.05757, -5.62533],	[ 3.31745, -5.47155],	[ 3.57812, -5.3174 ],
        [ 3.83883, -5.16231],	[ 4.09885, -5.00707],	[ 4.35911, -4.85145],	[ 4.61881, -4.69504],	[ 4.87858, -4.53847],
        [ 5.13844, -4.38053],	[ 5.39564, -4.22305],	[ 5.65718, -4.06492],	[ 5.93194, -3.89149],	[ 6.21225, -3.68712],
        [ 6.47853, -3.44866],	[ 6.71937, -3.18167],	[ 6.92757, -2.89342],	[ 7.09504, -2.61085],	[ 7.24788, -2.34784],
        [ 7.39993, -2.08588],	[ 7.55196, -1.82274],	[ 7.72471, -1.51634],	[ 7.72471, -1.51634],	[ 7.84633, -1.17666],
        [ 7.94156, -0.86853],	[ 8.02568, -0.55443],	[ 8.09638, -0.22764],	[ 8.14504,  0.11673],	[ 8.15979,  0.48477],
        [ 8.11353,  0.88968],	[ 7.93684,  1.34058],	[ 7.55023,  1.71507],	[ 7.14454,  1.85867],	[ 6.84843,  1.94626],
        [ 6.55595,  2.03109],
    ])
    outer_poly = Polygon(outer_border)
    inner_border = np.array([
        [ 5.97132,  1.08883],	[ 5.68124,  1.17132],	[ 5.39021,  1.2539 ],	[ 5.09882,  1.33711],	[ 4.80804,  1.42058],
        [ 4.51737,  1.50393],	[ 4.22629,  1.58768],	[ 3.93511,  1.67196],	[ 3.64362,  1.7569 ],	[ 3.35167,  1.84306],
        [ 3.06027,  1.93055],	[ 2.76937,  2.0188 ],	[ 2.47793,  2.10842],	[ 2.18506,  2.2005 ],	[ 1.89021,  2.29699],
        [ 1.59095,  2.40112],	[ 1.28981,  2.51835],	[ 1.00039,  2.64515],	[ 0.71945,  2.77153],	[ 0.4396 ,  2.90164],
        [ 0.16159,  3.03479],	[-0.11424,  3.1707 ],	[-0.38812,  3.3086 ],	[-0.66046,  3.44843],	[-0.93062,  3.58945],
        [-1.19969,  3.73085],	[-1.46806,  3.87317],	[-1.73533,  4.01561],	[-2.0017 ,  4.15767],	[-2.26821,  4.29927],
        [-2.53437,  4.44068],	[-2.79963,  4.58054],	[-3.0669 ,  4.71952],	[-3.3363 ,  4.86031],	[-3.60526,  5.00242],
        [-3.87287,  5.14479],	[-4.13971,  5.28694],	[-4.4054 ,  5.42844],	[-4.6701 ,  5.56792],	[-4.93491,  5.70513],
        [-5.20009,  5.83983],	[-5.43723,  5.95858],	[-5.59806,  6.02169],	[-5.66049,  6.03089],	[-5.70611,  5.98949],
        [-5.812  ,  5.83412],	[-5.96376,  5.60023],	[-6.11895,  5.35009],	[-6.2731 ,  5.09704],	[-6.42459,  4.84033],
        [-6.57768,  4.58009],	[-6.72721,  4.32621],	[-6.86112,  4.08349],	[-6.97104,  3.84992],	[-7.05039,  3.62648],
        [-7.09277,  3.41621],	[-7.09586,  3.22376],	[-7.05887,  3.05187],	[-6.97539,  2.88735],	[-6.84727,  2.72235],
        [-6.67914,  2.56351],	[-6.47815,  2.41133],	[-6.25206,  2.26586],	[-6.00754,  2.12443],	[-5.74872,  1.98355],
        [-5.48032,  1.83815],	[-5.21681,  1.69074],	[-4.95365,  1.54857],	[-4.67281,  1.39544],	[-4.31498,  1.15681],
        [-3.99926,  0.62693],	[-4.08817,  0.06212],	[-4.24675, -0.27352],	[-4.39232, -0.54897],	[-4.53138, -0.81279],
        [-4.66688, -1.0786 ],	[-4.80391, -1.34801],	[-4.94195, -1.61869],	[-5.08147, -1.88894],	[-5.22155, -2.15879],
        [-5.36394, -2.43001],	[-5.49797, -2.67772],	[-5.57417, -2.82657],	[-5.57634, -2.8901 ],	[-5.52858, -2.96478],
        [-5.40437, -3.07539],	[-5.2088 , -3.20085],	[-4.96549, -3.33209],	[-4.69295, -3.47446],	[-4.42522, -3.62625],
        [-4.16357, -3.7699 ],	[-3.8987 , -3.91528],	[-3.63373, -4.06067],	[-3.36872, -4.20613],	[-3.10377, -4.35162],
        [-2.83887, -4.49708],	[-2.57402, -4.64248],	[-2.3088 , -4.78801],	[-2.04319, -4.93421],	[-1.77776, -5.08111],
        [-1.51345, -5.22808],	[-1.24831, -5.37507],	[-0.98354, -5.52351],	[-0.71709, -5.67296],	[-0.46412, -5.81912],
        [-0.23803, -5.93598],	[-0.04045, -6.00901],	[ 0.12653, -6.03333],	[ 0.28495, -6.00728],	[ 0.46707, -5.92777],
        [ 0.69323, -5.79038],	[ 0.95334, -5.63466],	[ 1.21341, -5.47973],	[ 1.47303, -5.32497],	[ 1.7334 , -5.16987],
        [ 1.99397, -5.01566],	[ 2.25379, -4.86161],	[ 2.51398, -4.70741],	[ 2.7743 , -4.55337],	[ 3.03392, -4.39985],
        [ 3.2927 , -4.24591],	[ 3.55167, -4.09129],	[ 3.81018, -3.93671],	[ 4.06828, -3.78128],	[ 4.32619, -3.62582],
        [ 4.58287, -3.46982],	[ 4.84116, -3.31167],	[ 5.09689, -3.1571 ],	[ 5.33351, -3.00835],	[ 5.54187, -2.85727],
        [ 5.72566, -2.69285],	[ 5.88949, -2.51131],	[ 6.0347 , -2.3096 ],	[ 6.17451, -2.07168],	[ 6.32537, -1.81207],
        [ 6.47676, -1.55126],	[ 6.62711, -1.29103],	[ 6.7545 , -1.07277],	[ 6.7545 , -1.07277],	[ 6.8333 , -0.84223],
        [ 6.91654, -0.5729 ],	[ 6.98889, -0.30318],	[ 7.04633, -0.03934],	[ 7.08273,  0.21453],	[ 7.09356,  0.45006],
        [ 7.0751 ,  0.64529],	[ 7.0427 ,  0.75871],	[ 7.00235,  0.79971],	[ 6.83211,  0.83864],	[ 6.54858,  0.92247],
        [ 6.26053,  1.00601],
    ])
    inner_poly = Polygon(inner_border)

def reward_shape(params):

    distances_to_waypoints = np.hypot(PARAMS.waypoints[:, 0] - params['x'], PARAMS.waypoints[:, 1] - params['y'])
    closest_waypoint = np.argmin(distances_to_waypoints)

    # Distance
    norm_dist = distances_to_waypoints[closest_waypoint] / (params['track_width'] * 0.5)
    norm_dist = min(norm_dist, 1)

    reward = 1 - (norm_dist ** 0.4)

    coords = Point((params['x'], params['y']))
    if coords.within(PARAMS.inner_poly) or not coords.within(PARAMS.outer_poly):
        reward = 0

    return float(reward)