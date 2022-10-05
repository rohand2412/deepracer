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
        [ 2.04691499,  2.17353654], [ 1.76534253,  2.06549758], [ 1.48377001,  1.95745647],
        [ 1.20219553,  1.84942198], [ 0.9206205 ,  1.74138951], [ 0.63904531,  1.63335699],
        [ 0.35746974,  1.525325  ], [ 0.0758935 ,  1.41729507], [-0.20568219,  1.30926356],
        [-0.48725559,  1.20122632], [-0.76883277,  1.09319884], [-1.05042401,  0.98520672],
        [-1.33200449,  0.8771881 ], [-1.61291243,  0.77571633], [-1.89214043,  0.68721108],
        [-2.16794401,  0.61807261], [-2.43811288,  0.57360581], [-2.70000733,  0.55830136],
        [-2.9504004 ,  0.57636597], [-3.18517006,  0.63212033], [-3.39913889,  0.72975481],
        [-3.58264277,  0.87732239], [-3.74195592,  1.05827009], [-3.87956492,  1.2661211 ],
        [-3.99938601,  1.49418941], [-4.1059916 ,  1.73628199], [-4.23370522,  1.97082612],
        [-4.37901469,  2.18230751], [-4.54185317,  2.36657128], [-4.72184865,  2.51866311],
        [-4.91788229,  2.63246772], [-5.12799695,  2.6961849 ], [-5.34488534,  2.7149318 ],
        [-5.56354769,  2.6871311 ], [-5.77730347,  2.60768132], [-5.98019806,  2.4834728 ],
        [-6.1677383 ,  2.32015817], [-6.33696532,  2.12420037], [-6.48588063,  1.9018515 ],
        [-6.61232192,  1.65858738], [-6.71496805,  1.40036771], [-6.79348288,  1.13265742],
        [-6.84752062,  0.85968518], [-6.87655877,  0.58481919], [-6.88038859,  0.31086906],
        [-6.85896518,  0.04017774], [-6.81228723, -0.22525951], [-6.74028623, -0.48364637],
        [-6.6339675 , -0.72936047], [-6.50008125, -0.9619305 ], [-6.34269132, -1.18080995],
        [-6.16553669, -1.38582673], [-5.97132376, -1.57654528], [-5.76237202, -1.75253253],
        [-5.54082219, -1.91354954], [-5.30855992, -2.05949247], [-5.06722793, -2.19033394],
        [-4.8179168 , -2.30530293], [-4.56173373, -2.40366552], [-4.2991452 , -2.48245298],
        [-4.03110605, -2.53852747], [-3.75880762, -2.56738416], [-3.48392411, -2.56109753],
        [-3.20858223, -2.53164688], [-2.9333332 , -2.48214405], [-2.65848699, -2.41529422],
        [-2.38420002, -2.33382872], [-2.11055035, -2.23989871], [-1.83756425, -2.13544876],
        [-1.56520642, -2.02254559], [-1.29341611, -1.90294116], [-1.02213348, -1.77797062],
        [-0.75136685, -1.648157  ], [-0.48087485, -1.52348026], [-0.210547  , -1.40618325],
        [ 0.05930735, -1.29884128], [ 0.32823401, -1.2039686 ], [ 0.59561992, -1.12400353],
        [ 0.86063792, -1.06153312], [ 1.12224017, -1.01903153], [ 1.37906298, -0.99920099],
        [ 1.62931234, -1.00507323], [ 1.87006081, -1.04155559], [ 2.09720192, -1.11385882],
        [ 2.30402332, -1.22919914], [ 2.47777782, -1.39731083], [ 2.62862461, -1.59395224],
        [ 2.76206184, -1.80989887], [ 2.88574466, -2.03839741], [ 3.02423853, -2.25396517],
        [ 3.18079865, -2.45198204], [ 3.35857463, -2.62663437], [ 3.56773032, -2.75735451],
        [ 3.79729232, -2.84797967], [ 4.03949411, -2.90254166], [ 4.28861219, -2.92382215],
        [ 4.54005323, -2.91497052], [ 4.79034589, -2.87838066], [ 5.03677702, -2.81631885],
        [ 5.27730113, -2.73102354], [ 5.51032651, -2.62438171], [ 5.73421347, -2.49735205],
        [ 5.94742457, -2.35083796], [ 6.14659697, -2.18316501], [ 6.3270086 , -1.99255093],
        [ 6.47919898, -1.7755406 ], [ 6.60423545, -1.53933531], [ 6.70501102, -1.28955522],
        [ 6.78368325, -1.02994843], [ 6.84178253, -0.76331885], [ 6.88043359, -0.49195585],
        [ 6.90063963, -0.2178519 ], [ 6.90339324,  0.05724296], [ 6.88973509,  0.33181992],
        [ 6.8607142 ,  0.60461088], [ 6.81706314,  0.87447252], [ 6.75908839,  1.14022595],
        [ 6.68671959,  1.40054878], [ 6.5990167 ,  1.65353276], [ 6.49510723,  1.89686276],
        [ 6.37337443,  2.12708996], [ 6.23264202,  2.34006646], [ 6.07160938,  2.53012434],
        [ 5.88953579,  2.68991713], [ 5.68721368,  2.81116163], [ 5.46854224,  2.89152892],
        [ 5.23913417,  2.94020667], [ 5.00134884,  2.96253327], [ 4.75624446,  2.96133824],
        [ 4.50463126,  2.93928504], [ 4.24700064,  2.8983434 ], [ 3.98388525,  2.84076081],
        [ 3.71592568,  2.76907103], [ 3.44380303,  2.68574716], [ 3.16823698,  2.59314342],
        [ 2.88993079,  2.4933616 ], [ 2.6097765 ,  2.38883521], [ 2.32849705,  2.2815485 ]
    ])
    optimal_speed = np.array([
        4.        , 4.        , 4.        , 4.        , 4.        ,
        4.        , 4.        , 4.        , 4.        , 4.        ,
        3.83088124, 3.33214721, 2.92296083, 2.57532151, 2.30419144,
        2.02639251, 2.02639251, 2.02639251, 2.02639251, 2.02639251,
        2.45536793, 2.78602729, 2.99274159, 2.6803418 , 2.39099798,
        2.04652889, 2.04652889, 2.04652889, 2.04652889, 2.04652889,
        2.06118383, 2.06118383, 2.06118383, 2.28702238, 2.51403975,
        2.78523324, 3.05753565, 3.25720818, 3.4438063 , 3.56787941,
        3.5131244 , 3.45559499, 2.91790395, 2.91790395, 2.91790395,
        2.91790395, 2.91790395, 3.1944467 , 3.39807953, 3.62535565,
        3.79379291, 3.93617155, 4.        , 3.98025309, 3.73367582,
        3.43572471, 3.04479586, 3.04479586, 3.04479586, 3.04479586,
        3.04479586, 3.78197209, 4.        , 4.        , 4.        ,
        4.        , 4.        , 4.        , 4.        , 4.        ,
        4.        , 4.        , 4.        , 4.        , 3.67363313,
        3.31071204, 2.90545778, 2.57471864, 2.26861013, 2.        ,
        2.        , 2.        , 2.        , 2.        , 2.68374477,
        2.94793156, 2.22335657, 2.22335657, 2.22335657, 2.22335657,
        2.22335657, 2.42239744, 2.63799989, 2.81605392, 3.00654706,
        3.15496114, 3.29123376, 3.39527776, 3.16619304, 2.79737144,
        2.79737144, 2.79737144, 2.79737144, 2.79737144, 3.04287082,
        3.35577845, 3.62505579, 3.84826694, 4.        , 4.        ,
        4.        , 4.        , 4.        , 4.        , 3.7087148 ,
        3.3866306 , 3.03262932, 2.68827041, 2.39867142, 2.32915238,
        2.32915238, 2.32915238, 2.32915238, 2.32915238, 2.66256911,
        2.9823011 , 3.26473101, 3.61623517, 3.98356913, 4.        ,
        4.        , 4.        , 4.        , 4.        , 4.        ,
        4.        , 4.        , 4.        
    ])
    waypoints_poly = Polygon(waypoints)
    inner_border = np.array([
        [ 2.23797297,  1.67552805], [ 1.95642602,  1.56749904], [ 1.67484903,  1.45945597],
        [ 1.39326704,  1.35141897], [ 1.111691  ,  1.24338603], [ 0.83011502,  1.13535297],
        [ 0.54853678,  1.02732003], [ 0.26696029,  0.91929013], [-0.01460899,  0.81126112],
        [-0.2961857 ,  0.70322269], [-0.57780272,  0.59517968], [-0.859402  ,  0.48718441],
        [-1.14078403,  0.37924221], [-1.42214501,  0.2710802 ], [-1.70466495,  0.1625182 ],
        [-1.98787904,  0.05494946], [-2.26713705, -0.05072557], [-2.58073211, -0.1724571 ],
        [-2.9810729 , -0.2631416 ], [-3.44458389, -0.2426554 ], [-3.89354396, -0.06082643],
        [-4.23978281,  0.2459673 ], [-4.48403406,  0.62545413], [-4.60436821,  1.04332995],
        [-4.6323719 ,  1.41064596], [-4.63893223,  1.71414495], [-4.65424109,  1.97451198],
        [-4.68837023,  2.18316197], [-4.74541521,  2.32740402], [-4.83653593,  2.42916203],
        [-4.96747589,  2.50915504], [-5.14225101,  2.56016302], [-5.33692694,  2.58194399],
        [-5.50612688,  2.56743407], [-5.64587021,  2.51084208], [-5.77768803,  2.40532994],
        [-5.90581894,  2.24788809], [-6.02488899,  2.04731202], [-6.13184214,  1.81644595],
        [-6.22729206,  1.56436396], [-6.31482601,  1.29562497], [-6.39786816,  1.01906395],
        [-6.47357893,  0.74258423], [-6.53946686,  0.4685182 ], [-6.59226322,  0.1994848 ],
        [-6.62698889, -0.05665408], [-6.63583708, -0.28042999], [-6.60959482, -0.45948511],
        [-6.53373384, -0.62480873], [-6.4089632 , -0.8037529 ], [-6.2499609 , -0.98130512],
        [-6.05773592, -1.15277302], [-5.84623814, -1.32263696], [-5.62290096, -1.48106802],
        [-5.38775587, -1.63257205], [-5.14393711, -1.77718401], [-4.89345598, -1.91552496],
        [-4.63738585, -2.0480361 ], [-4.3758378 , -2.17596292], [-4.11335087, -2.2990911 ],
        [-3.88972211, -2.39905095], [-3.71468496, -2.44196796], [-3.56821609, -2.4373889 ],
        [-3.39847207, -2.36924601], [-3.15423703, -2.23957109], [-2.87704992, -2.10686898],
        [-2.61050105, -1.973593  ], [-2.33929396, -1.83939302], [-2.06913495, -1.705598  ],
        [-1.79888904, -1.57173097], [-1.52861595, -1.43787503], [-1.25836098, -1.30402303],
        [-0.98810661, -1.17017198], [-0.7178455 , -1.03631198], [-0.44761309, -0.90248042],
        [-0.1773867 , -0.7685985 ], [ 0.09326839, -0.6345377 ], [ 0.36122119, -0.50235391],
        [ 0.63875651, -0.3614057 ], [ 0.97642487, -0.2125981 ], [ 1.37318504, -0.1248946 ],
        [ 1.76945806, -0.1138632 ], [ 2.15826797, -0.1692235 ], [ 2.54555511, -0.2977024 ],
        [ 2.93633389, -0.54047853], [ 3.2427969 , -0.94338   ], [ 3.36550498, -1.39799595],
        [ 3.37170291, -1.76459205], [ 3.37302804, -2.06590509], [ 3.37238002, -2.31563902],
        [ 3.390522  , -2.45252609], [ 3.45037794, -2.52956605], [ 3.56746888, -2.60728407],
        [ 3.74732804, -2.66982007], [ 3.96875405, -2.7129221 ], [ 4.2084322 , -2.72827101],
        [ 4.45890188, -2.71925712], [ 4.71169186, -2.68744707], [ 4.96171713, -2.63401508],
        [ 5.20300913, -2.56034803], [ 5.43544579, -2.46326709], [ 5.66392994, -2.34335303],
        [ 5.88019609, -2.20867205], [ 6.06950903, -2.06302691], [ 6.22644997, -1.904392  ],
        [ 6.35186577, -1.72862506], [ 6.44919491, -1.52999401], [ 6.52250385, -1.30632603],
        [ 6.57452679, -1.06043994], [ 6.6088438 , -0.79792529], [ 6.62852907, -0.52342808],
        [ 6.63745499, -0.24332491], [ 6.63526487,  0.0357021 ], [ 6.62087822,  0.31022581],
        [ 6.59144783,  0.58169079], [ 6.54791594,  0.85230958], [ 6.49064112,  1.11996198],
        [ 6.41945219,  1.38346398], [ 6.33473778,  1.64086998], [ 6.23577404,  1.88984597],
        [ 6.12320518,  2.12674403], [ 5.99762678,  2.34389901], [ 5.86600304,  2.52526093],
        [ 5.75155497,  2.64047003], [ 5.6222558 ,  2.69405794], [ 5.42926311,  2.72083902],
        [ 5.20520687,  2.72432804], [ 5.20520687,  2.72432804], [ 4.97431087,  2.69213009],
        [ 4.73090506,  2.63196397], [ 4.48483801,  2.54865694], [ 4.21861792,  2.436795  ],
        [ 3.92919803,  2.32246494], [ 3.64417601,  2.21473098], [ 3.36385012,  2.10786009],
        [ 3.08299804,  1.99984598], [ 2.80124998,  1.89159203], [ 2.5195291 ,  1.78353   ]
    ])
    outer_border = np.array([
        [ 1.85585701,  2.67154503], [ 1.57425904,  2.56349611], [ 1.29269099,  2.45545697],
        [ 1.01112401,  2.34742498], [ 0.72955   ,  2.239393  ], [ 0.44797561,  2.13136101],
        [ 0.1664027 ,  2.02332997], [-0.1151733 ,  1.91530001], [-0.3967554 ,  1.807266  ],
        [-0.67832547,  1.69922996], [-0.95986283,  1.59121799], [-1.24144602,  1.48322904],
        [-1.52322495,  1.37513399], [-1.80487001,  1.26686299], [-2.08538508,  1.15907001],
        [-2.36606789,  1.05246401], [-2.65096998,  0.9446311 ], [-2.89874911,  0.8458392 ],
        [-3.08435297,  0.79864722], [-3.2211659 ,  0.8004874 ], [-3.32810211,  0.84379381],
        [-3.42849803,  0.93870062], [-3.51167703,  1.06429696], [-3.55310297,  1.22472703],
        [-3.56666303,  1.45888197], [-3.57305098,  1.75841904], [-3.59484005,  2.09993196],
        [-3.66512609,  2.48487997], [-3.84182501,  2.89449   ], [-4.14705706,  3.24321508],
        [-4.52657509,  3.48058105], [-4.92797709,  3.60522199], [-5.33237123,  3.64873409],
        [-5.761621  ,  3.60318708], [-6.17895603,  3.43489909], [-6.52133703,  3.17021489],
        [-6.77708483,  2.86348391], [-6.96753788,  2.54678702], [-7.11484623,  2.23089099],
        [-7.23337793,  1.91912103], [-7.33287382,  1.61443806], [-7.42328596,  1.31331003],
        [-7.50682592,  1.00803196], [-7.58181095,  0.69563538], [-7.64488888,  0.37280759],
        [-7.69016218,  0.03123751], [-7.70054102, -0.3472825 ], [-7.63257122, -0.76210958],
        [-7.46447182, -1.14614296], [-7.24759912, -1.46310997], [-7.00485897, -1.73509002],
        [-6.74796677, -1.966187  ], [-6.48924923, -2.17387104], [-6.22079182, -2.36457801],
        [-5.94896889, -2.53982091], [-5.67405605, -2.7029469 ], [-5.39657497, -2.85623503],
        [-5.11697388, -3.00095701], [-4.83671522, -3.13807297], [-4.55309582, -3.27104092],
        [-4.22411823, -3.41208696], [-3.81276298, -3.50425005], [-3.35878301, -3.48342991],
        [-2.96483111, -3.34393406], [-2.6756041 , -3.19297194], [-2.40830898, -3.06517196],
        [-2.13542509, -2.92877102], [-1.866009  , -2.79545999], [-1.59564495, -2.66156411],
        [-1.32539296, -2.52769303], [-1.05514705, -2.39385104], [-0.78488779, -2.25999594],
        [-0.5146271 , -2.12614202], [-0.24437711, -1.99228799], [ 0.02591162, -1.858428  ],
        [ 0.29616591, -1.72453296], [ 0.5660165 , -1.59087002], [ 0.838974  , -1.45619595],
        [ 1.09926403, -1.32369196], [ 1.31141996, -1.22543597], [ 1.50248301, -1.18383002],
        [ 1.70843995, -1.17891705], [ 1.91611695, -1.20817697], [ 2.10079503, -1.26736701],
        [ 2.22471809, -1.33525205], [ 2.28271389, -1.40846598], [ 2.3073709 , -1.53368998],
        [ 2.30491805, -1.77024901], [ 2.30624604, -2.07210803], [ 2.31125498, -2.4255209 ],
        [ 2.41189098, -2.87719393], [ 2.69995904, -3.28781009], [ 3.0752809 , -3.55375791],
        [ 3.4606111 , -3.69736791], [ 3.83035898, -3.77070594], [ 4.19225502, -3.7949481 ],
        [ 4.54435921, -3.78262806], [ 4.88984394, -3.73926592], [ 5.22950411, -3.66665792],
        [ 5.56480789, -3.56392407], [ 5.88883114, -3.42893004], [ 6.19442081, -3.26890302],
        [ 6.48964977, -3.08424497], [ 6.77729511, -2.86121297], [ 7.04328108, -2.59057689],
        [ 7.26765823, -2.27578712], [ 7.43659306, -1.93385994], [ 7.55223179, -1.58511496],
        [ 7.62588787, -1.24127901], [ 7.67016697, -0.90587962], [ 7.69389009, -0.57882208],
        [ 7.70417881, -0.256082  ], [ 7.70157623,  0.06800238], [ 7.68424416,  0.39575011],
        [ 7.64872885,  0.72388703], [ 7.59647894,  1.04872406], [ 7.5275259 ,  1.37082303],
        [ 7.4413991 ,  1.68954504], [ 7.33747911,  2.00497699], [ 7.21358585,  2.31639695],
        [ 7.06701422,  2.62402296], [ 6.89002895,  2.9284339 ], [ 6.66453123,  3.23266196],
        [ 6.34079504,  3.52977109], [ 5.92209911,  3.71785307], [ 5.51938105,  3.78382611],
        [ 5.1408968 ,  3.78918791], [ 5.1408968 ,  3.78918791], [ 4.77462912,  3.74007607],
        [ 4.43243122,  3.65615892], [ 4.10772514,  3.54657888], [ 3.81653905,  3.42492199],
        [ 3.5446651 ,  3.31755209], [ 3.26559091,  3.21209598], [ 2.98236799,  3.10411906],
        [ 2.70022106,  2.99560905], [ 2.41891003,  2.88752294], [ 2.137465  ,  2.779567  ]
    ])
    turn_points = np.array([
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0.,
        0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0.
    ])
    turn_curvatures = np.array([
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.94683412, 0.94683412, 0.94683412, 0.94683412, 0.94683412,
        0.94683412, 0.94683412, 0.94683412, 0.94683412, 0.94683412,
        0.94683412, 0.94683412, 0.94683412, 0.94683412, 0.94683412,
        0.94683412, 0.94683412, 0.94683412, 0.94683412, 0.94683412,
        0.94683412, 0.94683412, 0.94683412, 0.94683412, 0.94683412,
        0.94683412, 0.        , 0.        , 0.        , 0.        ,
        1.96321896, 1.96321896, 1.96321896, 1.96321896, 1.96321896,
        1.96321896, 1.96321896, 1.96321896, 1.96321896, 1.96321896,
        0.        , 0.        , 0.        , 2.13768209, 2.13768209,
        2.13768209, 2.13768209, 2.13768209, 2.13768209, 2.13768209,
        2.13768209, 2.13768209, 2.13768209, 2.13768209, 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.92233088,
        0.92233088, 0.92233088, 0.92233088, 0.92233088, 0.92233088,
        0.92233088, 0.92233088, 0.92233088, 0.92233088, 0.92233088,
        0.92233088, 0.92233088, 0.92233088, 0.92233088, 0.92233088,
        0.92233088, 0.92233088, 0.92233088, 0.92233088, 0.        ,
        0.        , 0.        , 0.        , 1.80437595, 1.80437595,
        1.80437595, 1.80437595, 1.80437595, 1.80437595, 1.80437595,
        1.80437595, 1.80437595, 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 1.25089991,
        1.25089991, 1.25089991, 1.25089991, 1.25089991, 1.25089991,
        1.25089991, 1.25089991, 1.25089991, 1.25089991, 1.25089991,
        1.25089991, 1.25089991, 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        
    ])
    straight_avg_speeds = np.array([
        4.        , 4.        , 4.        , 4.        , 4.        ,
        4.        , 4.        , 4.        , 4.        , 4.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 3.33160738, 3.33160738, 3.33160738, 3.33160738,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        3.90998815, 3.90998815, 3.90998815, 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 4.        ,
        4.        , 4.        , 4.        , 4.        , 4.        ,
        4.        , 4.        , 4.        , 4.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 3.21200493,
        3.21200493, 3.21200493, 3.21200493, 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 3.97832385, 3.97832385, 3.97832385,
        3.97832385, 3.97832385, 3.97832385, 3.97832385, 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 0.        , 0.        , 0.        ,
        0.        , 0.        , 3.96361857, 3.96361857, 3.96361857,
        3.96361857, 3.96361857, 3.96361857, 3.96361857, 3.96361857,
        3.96361857, 3.96361857, 3.96361857
    ])
    last_milestone = 0
    prev_on_turn = False
    turn_reward = 0
    prev_on_straight = False
    unpardonable_action_on_straight = False
    speed_sum = 0
    nspeeds = 0

def reward_function(params):
    def minimum(arr):
        LOW = None
        for val in arr:
            if LOW is None:
                LOW = val
            else:
                LOW = min(LOW, val)
        return LOW

    def maximum(arr):
        HIGH = None
        for val in arr:
            if HIGH is None:
                HIGH = val
            else:
                HIGH = max(HIGH, val)
        return HIGH
    
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
        PARAMS.prev_on_turn = False
        PARAMS.turn_reward = 0
        PARAMS.prev_on_straight = False
        PARAMS.unpardonable_action_on_straight = False
        PARAMS.speed_sum = 0
        PARAMS.nspeeds = 0

    #Calculate the speed reward
    MIN_SPEED = 2.0
    MAX_SPEED = 4.0
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

    curve_bonus = 0
    if on_turn and not PARAMS.prev_on_turn:
        MAX_TURN_REWARD = 400
        MIN_TURN_REWARD = 200
        sharpest_curvature = minimum(PARAMS.turn_curvatures[PARAMS.turn_curvatures != 0])
        mildest_curvature = maximum(PARAMS.turn_curvatures)
        reward_scalar = (MAX_TURN_REWARD - MIN_TURN_REWARD) / ((1 / sharpest_curvature) - (1 / mildest_curvature))
        reward_asymptote = MAX_TURN_REWARD - (reward_scalar / sharpest_curvature)
        PARAMS.turn_reward = (reward_scalar / PARAMS.turn_curvatures[closest_route_point]) + reward_asymptote
        PARAMS.prev_on_turn = True
    elif not on_turn and PARAMS.prev_on_turn:
        curve_bonus = PARAMS.turn_reward
        PARAMS.turn_reward = 0
        PARAMS.prev_on_turn = False

    straight_section_bonus = 0
    if on_straight and not PARAMS.prev_on_straight:
        PARAMS.speed_sum = 0
        PARAMS.nspeeds = 0
        PARAMS.unpardonable_action_on_straight = False
        PARAMS.prev_on_straight = True
    if on_straight:
        PARAMS.speed_sum += speed
        PARAMS.nspeeds += 1
    if (not on_straight and PARAMS.prev_on_straight) or params['progress'] == 100:
        if not PARAMS.unpardonable_action_on_straight:
            avg_speed = PARAMS.speed_sum / PARAMS.nspeeds
            MAX_STRAIGHT_REWARD = 400
            MIN_STRAIGHT_REWARD = 200
            fastest_avg_speed = maximum(PARAMS.straight_avg_speeds)
            slowest_avg_speed = minimum(PARAMS.straight_avg_speeds[PARAMS.straight_avg_speeds != 0])
            reward_scalar = (MAX_STRAIGHT_REWARD - MIN_STRAIGHT_REWARD) / ((1 / fastest_avg_speed) - (1 / slowest_avg_speed))
            reward_asymptote = MAX_STRAIGHT_REWARD - (reward_scalar / fastest_avg_speed)
            straight_section_bonus = (reward_scalar / avg_speed) + reward_asymptote
        PARAMS.prev_on_straight = False

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
    HC = ( 5 * heading_reward * steering_angle_maintain_bonus )
    #distance component of reward
    DC = ( 5 * distance_reward * distance_reduction_bonus )
    #speed component of reward
    SC = ( 10 * speed_reward * speed_maintain_bonus )
    #Immediate component of reward
    IC = ( HC + DC + SC ) ** 2 + ( HC * DC * SC )

    #If an unpardonable action is taken, then the immediate reward is 0
    if unpardonable_action_taken():
        IC = 1e-3
        PARAMS.turn_reward = 0
        curve_bonus = 0
        PARAMS.unpardonable_action_on_straight = True
        straight_section_bonus = 0
        intermediate_progress_bonus = 0

    #Long term component of reward
    LC = ( curve_bonus + intermediate_progress_bonus + straight_section_bonus )

    return max(IC + LC,1e-3)