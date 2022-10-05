import math
import numpy as np


class Reward:
    def __init__(self, verbose=False):
        self.first_racingpoint_index = None
        self.verbose = verbose
        self.prev_steps = None

    def reward_function(self, params):

        ################## HELPER FUNCTIONS ###################

        def closest_2_racing_points_index(racing_coords, car_coords):
            distances_from_route_points = np.hypot(racing_coords[:, 0] - car_coords[0], racing_coords[:, 1] - car_coords[1])
            closest_route_points = np.argpartition(distances_from_route_points, 2)
            return closest_route_points[:2]

        def dist_to_racing_line(racing_coords, closest_points, car_coords):
            closest_coord_x = racing_coords[closest_points[0], 0]
            closest_coord_y = racing_coords[closest_points[0], 1]
            second_closest_coord_x = racing_coords[closest_points[1], 0]
            second_closest_coord_y = racing_coords[closest_points[1], 1]

            # Calculate the distances between 2 closest racing points
            a = math.hypot(closest_coord_x - second_closest_coord_x, closest_coord_y - second_closest_coord_y)

            # Distances between car and closest and second closest racing point
            b = math.hypot(car_coords[0] - closest_coord_x, car_coords[1] - closest_coord_y)
            c = math.hypot(car_coords[0] - second_closest_coord_x, car_coords[1] - second_closest_coord_y)

            # Calculate distance between car and racing line (goes through 2 closest racing points)
            # try-except in case a=0 (rare bug in DeepRacer)
            try:
                distance = abs(-(a**4) + 2*(a**2)*(b**2) + 2*(a**2)*(c**2) -
                               (b**4) + 2*(b**2)*(c**2) - (c**4))**0.5 / (2*a)
            except:
                distance = b

            return distance

        # Calculate which one of the closest racing points is the next one and which one the previous one
        def next_prev_racing_point(racing_coords, closest_points):
            if closest_points[0] == len(racing_coords) - 1 and closest_points[1] == 0:
                return racing_coords[[0, len(racing_coords) - 1]]
            elif closest_points[0] == 0 and closest_points[1] == len(racing_coords) - 1:
                return racing_coords[[0, len(racing_coords) - 1]]
            else:
                return racing_coords[[max(closest_points), min(closest_points)]]

        def racing_direction_diff(racing_coords, closest_points, heading):

            # Calculate the direction of the center line based on the closest waypoints
            next_point, prev_point = next_prev_racing_point(racing_coords, closest_points)

            # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
            track_direction = math.atan2(
                next_point[1] - prev_point[1], next_point[0] - prev_point[0])

            # Convert to degree
            track_direction = math.degrees(track_direction)

            # Calculate the difference between the track direction and the heading direction of the car
            direction_diff = abs(track_direction - heading)
            if direction_diff > 180:
                direction_diff = 360 - direction_diff

            return direction_diff

        # Gives back indexes that lie between start and end index of a cyclical list 
        # (start index is included, end index is not)
        def indexes_cyclical(start, end, array_len):

            if end < start:
                end += array_len

            return [index % array_len for index in range(start, end)]

        # Calculate how long car would take for entire lap, if it continued like it did until now
        def projected_time(first_index, closest_index, step_count, times_list):

            # Calculate how much time has passed since start
            current_actual_time = (step_count-1) / 15

            # Calculate which indexes were already passed
            indexes_traveled = indexes_cyclical(first_index, closest_index, len(times_list))

            # Calculate how much time should have passed if car would have followed optimals
            current_expected_time = sum([times_list[i] for i in indexes_traveled])

            # Calculate how long one entire lap takes if car follows optimals
            total_expected_time = sum(times_list)

            # Calculate how long car would take for entire lap, if it continued like it did until now
            try:
                projected_time = (current_actual_time/current_expected_time) * total_expected_time
            except:
                projected_time = 9999

            return projected_time

        #################### RACING LINE ######################

        # Optimal racing line for the Spain track
        # Each row: [x,y,speed,timeFromPreviousPoint]
        racing_track = np.array([
            [-6.98943482e+00,  9.43785328e-01,  1.00000000e+00, 2.82997109e-01],
            [-7.04721071e+00,  6.63214022e-01,  1.00000000e+00, 2.86458219e-01],
            [-7.08960062e+00,  3.76978830e-01,  1.00000000e+00, 2.89357028e-01],
            [-7.11723677e+00,  8.68253908e-02,  1.00000000e+00, 2.91466593e-01],
            [-7.13047669e+00, -2.05478778e-01,  1.00000000e+00, 2.92603866e-01],
            [-7.12947581e+00, -4.98169272e-01,  1.00000000e+00, 2.92692205e-01],
            [-7.11444703e+00, -7.89602360e-01,  1.00000000e+00, 2.91820337e-01],
            [-7.08563836e+00, -1.07838034e+00,  9.44978890e-01, 3.07108879e-01],
            [-7.04256079e+00, -1.36312221e+00,  8.45444500e-01, 3.40627871e-01],
            [-6.98470047e+00, -1.64249929e+00,  7.72094550e-01, 3.69521773e-01],
            [-6.91125642e+00, -1.91512885e+00,  7.72094550e-01, 3.65692139e-01],
            [-6.81955943e+00, -2.17862187e+00,  7.72094550e-01, 3.61345213e-01],
            [-6.70729146e+00, -2.43038273e+00,  7.72094550e-01, 3.57026914e-01],
            [-6.57011387e+00, -2.66593762e+00,  7.72094550e-01, 3.53049026e-01],
            [-6.40408396e+00, -2.87947205e+00,  8.60238450e-01, 3.14431869e-01],
            [-6.20702770e+00, -3.06328863e+00,  9.28013650e-01, 2.90384128e-01],
            [-5.98822091e+00, -3.22038206e+00,  9.91269460e-01, 2.71732272e-01],
            [-5.75315865e+00, -3.35269316e+00,  9.44725190e-01, 2.85523805e-01],
            [-5.50583550e+00, -3.46198401e+00,  9.44725190e-01, 2.86215066e-01],
            [-5.24921143e+00, -3.54978552e+00,  9.44725190e-01, 2.87098008e-01],
            [-4.98558917e+00, -3.61761148e+00,  9.44725190e-01, 2.88134315e-01],
            [-4.71677137e+00, -3.66701564e+00,  9.44725190e-01, 2.89311565e-01],
            [-4.44382575e+00, -3.69769135e+00,  1.00000000e+00, 2.74663996e-01],
            [-4.16717141e+00, -3.69862415e+00,  1.00000000e+00, 2.76655913e-01],
            [-3.88992492e+00, -3.67461438e+00,  1.00000000e+00, 2.78284181e-01],
            [-3.61351187e+00, -3.63050899e+00,  1.00000000e+00, 2.79909735e-01],
            [-3.33852629e+00, -3.57015447e+00,  1.00000000e+00, 2.81531059e-01],
            [-3.06516964e+00, -3.49654677e+00,  1.00000000e+00, 2.83093539e-01],
            [-2.79344690e+00, -3.41207160e+00,  1.00000000e+00, 2.84551053e-01],
            [-2.52321559e+00, -3.31891256e+00,  1.00000000e+00, 2.85838359e-01],
            [-2.25433465e+00, -3.21859329e+00,  1.00000000e+00, 2.86985916e-01],
            [-1.98663005e+00, -3.11246123e+00,  1.00000000e+00, 2.87975289e-01],
            [-1.71990501e+00, -3.00173899e+00,  1.00000000e+00, 2.88793458e-01],
            [-1.45395029e+00, -2.88754613e+00,  1.00000000e+00, 2.89433796e-01],
            [-1.18853479e+00, -2.77098916e+00,  1.00000000e+00, 2.89880863e-01],
            [-9.23465903e-01, -2.65293906e+00,  1.00000000e+00, 2.90167781e-01],
            [-6.61409078e-01, -2.53552783e+00,  1.00000000e+00, 2.87157059e-01],
            [-4.00630179e-01, -2.41938827e+00,  1.00000000e+00, 2.85471595e-01],
            [-1.40637273e-01, -2.30428116e+00,  1.00000000e+00, 2.84334236e-01],
            [ 1.18825318e-01, -2.19009711e+00,  1.00000000e+00, 2.83476337e-01],
            [ 3.77897946e-01, -2.07679903e+00,  1.00000000e+00, 2.82763296e-01],
            [ 6.36666147e-01, -1.96436254e+00,  1.00000000e+00, 2.82139941e-01],
            [ 8.95172786e-01, -1.85278913e+00,  1.00000000e+00, 2.81556936e-01],
            [ 1.15344155e+00, -1.74207613e+00,  1.00000000e+00, 2.80998439e-01],
            [ 1.41147827e+00, -1.63224426e+00,  1.00000000e+00, 2.80438921e-01],
            [ 1.66927734e+00, -1.52333885e+00,  1.00000000e+00, 2.79858444e-01],
            [ 1.92681218e+00, -1.41548185e+00,  1.00000000e+00, 2.79208392e-01],
            [ 2.18405396e+00, -1.30880485e+00,  1.00000000e+00, 2.78483960e-01],
            [ 2.44096295e+00, -1.20348610e+00,  1.00000000e+00, 2.77658546e-01],
            [ 2.69748433e+00, -1.09977035e+00,  1.00000000e+00, 2.76695094e-01],
            [ 2.95356424e+00, -9.97902384e-01,  1.00000000e+00, 2.75597538e-01],
            [ 3.20907748e+00, -8.98431899e-01,  1.00000000e+00, 2.74192256e-01],
            [ 3.46388631e+00, -8.01965571e-01,  1.00000000e+00, 2.72457872e-01],
            [ 3.71781050e+00, -7.09286878e-01,  1.00000000e+00, 2.70308776e-01],
            [ 3.97061922e+00, -6.21426556e-01,  1.00000000e+00, 2.67640963e-01],
            [ 4.22220567e+00, -5.39660399e-01,  1.00000000e+00, 2.64540065e-01],
            [ 4.47362065e+00, -4.59151288e-01,  9.83481120e-01, 2.68425007e-01],
            [ 4.72493933e+00, -3.79462311e-01,  8.40251280e-01, 3.13775386e-01],
            [ 4.97943609e+00, -2.99249799e-01,  8.40251280e-01, 3.17569576e-01],
            [ 5.23275449e+00, -2.13031996e-01,  8.40251280e-01, 3.18462730e-01],
            [ 5.48258382e+00, -1.15073484e-01,  8.40251280e-01, 3.19366180e-01],
            [ 5.72503566e+00,  1.88155818e-04,  8.40251280e-01, 3.19493830e-01],
            [ 5.95458042e+00,  1.38156156e-01,  8.55360050e-01, 3.13104450e-01],
            [ 6.16275707e+00,  3.04514562e-01,  9.11881630e-01, 2.92233065e-01],
            [ 6.34721920e+00,  4.95185553e-01,  9.45517390e-01, 2.80582363e-01],
            [ 6.50875877e+00,  7.04673342e-01,  9.74238010e-01, 2.71532874e-01],
            [ 6.64744179e+00,  9.29361044e-01,  9.51185350e-01, 2.77591322e-01],
            [ 6.76338597e+00,  1.16617112e+00,  9.08498200e-01, 2.90226631e-01],
            [ 6.85614533e+00,  1.41262570e+00,  8.30894690e-01, 3.16926795e-01],
            [ 6.92533368e+00,  1.66630930e+00,  7.49657150e-01, 3.50759569e-01],
            [ 6.97045095e+00,  1.92479650e+00,  6.74488850e-01, 3.89028111e-01],
            [ 6.99049873e+00,  2.18554602e+00,  6.01293640e-01, 4.34927390e-01],
            [ 6.98409715e+00,  2.44572904e+00,  6.01293640e-01, 4.32836377e-01],
            [ 6.94926108e+00,  2.70204656e+00,  6.01293640e-01, 4.30195753e-01],
            [ 6.88168820e+00,  2.94976261e+00,  6.01293640e-01, 4.27024447e-01],
            [ 6.77629324e+00,  3.18179231e+00,  6.01293640e-01, 4.23827556e-01],
            [ 6.62811052e+00,  3.38800141e+00,  6.99896400e-01, 3.62810463e-01],
            [ 6.43251458e+00,  3.55259063e+00,  7.79264310e-01, 3.28041897e-01],
            [ 6.20656735e+00,  3.68032759e+00,  8.77125350e-01, 2.95915699e-01],
            [ 5.95874179e+00,  3.77436407e+00,  9.69099530e-01, 2.73518576e-01],
            [ 5.69556395e+00,  3.83882883e+00,  1.00000000e+00, 2.70958079e-01],
            [ 5.42154936e+00,  3.87681929e+00,  1.00000000e+00, 2.76635628e-01],
            [ 5.14036269e+00,  3.89138612e+00,  1.00000000e+00, 2.81563733e-01],
            [ 4.85496485e+00,  3.88532955e+00,  1.00000000e+00, 2.85462098e-01],
            [ 4.56771851e+00,  3.86105880e+00,  1.00000000e+00, 2.88269889e-01],
            [ 4.28047468e+00,  3.82060233e+00,  1.00000000e+00, 2.90078858e-01],
            [ 3.99463208e+00,  3.76570540e+00,  1.00000000e+00, 2.91066427e-01],
            [ 3.71118553e+00,  3.69791515e+00,  1.00000000e+00, 2.91440328e-01],
            [ 3.43082884e+00,  3.61845004e+00,  1.00000000e+00, 2.91401059e-01],
            [ 3.15404598e+00,  3.52823833e+00,  1.00000000e+00, 2.91113215e-01],
            [ 2.88110301e+00,  3.42817774e+00,  1.00000000e+00, 2.90706014e-01],
            [ 2.61212864e+00,  3.31906008e+00,  1.00000000e+00, 2.90265181e-01],
            [ 2.34721717e+00,  3.20146874e+00,  1.00000000e+00, 2.89837558e-01],
            [ 2.08658630e+00,  3.07558152e+00,  1.00000000e+00, 2.89440914e-01],
            [ 1.83075701e+00,  2.94097349e+00,  1.00000000e+00, 2.89081212e-01],
            [ 1.58063162e+00,  2.79662476e+00,  1.00000000e+00, 2.88789312e-01],
            [ 1.33754855e+00,  2.64095108e+00,  1.00000000e+00, 2.88658403e-01],
            [ 1.10352912e+00,  2.47157064e+00,  1.00000000e+00, 2.88885491e-01],
            [ 8.75873661e-01,  2.29296260e+00,  1.00000000e+00, 2.89357633e-01],
            [ 6.53097815e-01,  2.10740620e+00,  1.00000000e+00, 2.89931466e-01],
            [ 4.34113085e-01,  1.91650803e+00,  1.00000000e+00, 2.90510625e-01],
            [ 2.18013974e-01,  1.72157201e+00,  1.00000000e+00, 2.91030716e-01],
            [ 3.94947787e-03,  1.52380201e+00,  1.00000000e+00, 2.91438812e-01],
            [-2.08939212e-01,  1.32439904e+00,  1.00000000e+00, 2.91690142e-01],
            [-4.22136389e-01,  1.12382967e+00,  1.00000000e+00, 2.92713355e-01],
            [-6.36527331e-01,  9.25161201e-01,  1.00000000e+00, 2.92288619e-01],
            [-8.53326346e-01,  7.30422259e-01,  9.81870440e-01, 2.96799912e-01],
            [-1.07381032e+00,  5.41992463e-01,  8.56647480e-01, 3.38567162e-01],
            [-1.29915168e+00,  3.62571800e-01,  7.45496430e-01, 3.86381472e-01],
            [-1.53032968e+00,  1.95383800e-01,  6.47385760e-01, 4.40692820e-01],
            [-1.76799780e+00,  4.45095308e-02,  5.70998400e-01, 4.93017685e-01],
            [-2.01210657e+00, -8.49833354e-02,  5.00000000e-01, 5.52657196e-01],
            [-2.26140632e+00, -1.86956710e-01,  5.00000000e-01, 5.38698188e-01],
            [-2.51291149e+00, -2.54243467e-01,  5.00000000e-01, 5.20700905e-01],
            [-2.76142789e+00, -2.79186030e-01,  5.00000000e-01, 4.99529909e-01],
            [-2.99897737e+00, -2.54127601e-01,  5.00000000e-01, 4.77734991e-01],
            [-3.21406124e+00, -1.73619959e-01,  5.68372030e-01, 4.04061871e-01],
            [-3.38791459e+00, -3.37080397e-02,  6.32163470e-01, 3.53009770e-01],
            [-3.52281098e+00,  1.43721416e-01,  6.87012480e-01, 3.24428134e-01],
            [-3.62196276e+00,  3.47938445e-01,  7.41931360e-01, 3.05978025e-01],
            [-3.68670183e+00,  5.72907162e-01,  8.10944050e-01, 2.88673949e-01],
            [-3.71768289e+00,  8.14007850e-01,  6.96740910e-01, 3.48885854e-01],
            [-3.71649250e+00,  1.06671323e+00,  6.03873330e-01, 4.18478795e-01],
            [-3.68477675e+00,  1.32657964e+00,  5.21614950e-01, 5.01892540e-01],
            [-3.62561251e+00,  1.58537128e+00,  5.21614950e-01, 5.08935743e-01],
            [-3.59239701e+00,  1.83795788e+00,  5.21614950e-01, 4.88408513e-01],
            [-3.59289662e+00,  2.08155515e+00,  5.21614950e-01, 4.67006903e-01],
            [-3.63358960e+00,  2.31174398e+00,  5.21614950e-01, 4.48142886e-01],
            [-3.72184835e+00,  2.52180613e+00,  5.69543520e-01, 4.00057577e-01],
            [-3.86871875e+00,  2.69826947e+00,  6.32471470e-01, 3.62999891e-01],
            [-4.06237585e+00,  2.83728515e+00,  6.92413520e-01, 3.44284361e-01],
            [-4.29148033e+00,  2.93630012e+00,  7.46867340e-01, 3.34176228e-01],
            [-4.54455928e+00,  2.99321466e+00,  7.92270060e-01, 3.27413268e-01],
            [-4.80974327e+00,  3.00800535e+00,  8.36938850e-01, 3.17342356e-01],
            [-5.07677188e+00,  2.98288838e+00,  7.98594410e-01, 3.35849173e-01],
            [-5.33827098e+00,  2.92208645e+00,  7.98594410e-01, 3.36184022e-01],
            [-5.58979155e+00,  2.83029110e+00,  7.98594410e-01, 3.35274053e-01],
            [-5.82807299e+00,  2.71025071e+00,  7.98594410e-01, 3.34099893e-01],
            [-6.05059102e+00,  2.56430056e+00,  7.98594410e-01, 3.33225763e-01],
            [-6.25422258e+00,  2.39317332e+00,  8.75100290e-01, 3.03953012e-01],
            [-6.43119574e+00,  2.19343448e+00,  9.62715110e-01, 2.77196835e-01],
            [-6.58349214e+00,  1.97181665e+00,  1.00000000e+00, 2.68902689e-01],
            [-6.71373373e+00,  1.73316222e+00,  1.00000000e+00, 2.71880137e-01],
            [-6.82389925e+00,  1.48073829e+00,  1.00000000e+00, 2.75416561e-01],
            [-6.91536813e+00,  1.21691806e+00,  1.00000000e+00, 2.79226914e-01]
        ])

        ################## INPUT PARAMETERS ###################

        # Read all input parameters
        all_wheels_on_track = params['all_wheels_on_track']
        x = params['x']
        y = params['y']
        heading = params['heading']
        progress = params['progress']
        steps = params['steps']
        speed = params['speed']
        track_width = params['track_width']

        ############### OPTIMAL X,Y,SPEED,TIME ################

        # Get closest indexes for racing line (and distances to all points on racing line)
        closest_index, second_closest_index = closest_2_racing_points_index(
            racing_track, [x, y])

        # Get optimal [x, y, speed, time] for closest and second closest index
        optimals = racing_track[closest_index]
        optimals_second = racing_track[second_closest_index]

        # Save first racingpoint of episode for later
        if self.verbose == True:
            self.first_racingpoint_index = 0 # this is just for testing purposes
        if self.prev_steps is None or steps < self.prev_steps:
            self.first_racingpoint_index = closest_index

        ################ REWARD AND PUNISHMENT ################

        ## Define the default reward ##
        reward = 1

        ## Reward if car goes close to optimal racing line ##
        DISTANCE_MULTIPLE = 1
        dist = dist_to_racing_line(racing_track, [closest_index, second_closest_index], [x, y])
        distance_reward = max(1e-3, 1 - (dist/(track_width*0.5)))
        reward += distance_reward * DISTANCE_MULTIPLE

        ## Reward if speed is close to optimal speed ##
        SPEED_DIFF_NO_REWARD = 1
        SPEED_MULTIPLE = 2
        speed_diff = abs(optimals[2]-speed)
        if speed_diff <= SPEED_DIFF_NO_REWARD:
            # we use quadratic punishment (not linear) bc we're not as confident with the optimal speed
            # so, we do not punish small deviations from optimal speed
            speed_reward = (1 - (speed_diff/(SPEED_DIFF_NO_REWARD))**2)**2
        else:
            speed_reward = 0
        reward += speed_reward * SPEED_MULTIPLE

        # Reward if less steps
        REWARD_PER_STEP_FOR_FASTEST_TIME = 1 
        STANDARD_TIME = 50
        FASTEST_TIME = 35
        times_list = racing_track[:, 3]
        projected_time = projected_time(self.first_racingpoint_index, closest_index, steps, times_list)
        try:
            steps_prediction = projected_time * 15 + 1
            reward_prediction = max(1e-3, (-REWARD_PER_STEP_FOR_FASTEST_TIME*(FASTEST_TIME) /
                                           (STANDARD_TIME-FASTEST_TIME))*(steps_prediction-(STANDARD_TIME*15+1)))
            steps_reward = min(REWARD_PER_STEP_FOR_FASTEST_TIME, reward_prediction / steps_prediction)
        except:
            steps_reward = 0
        reward += steps_reward

        # Zero reward if obviously wrong direction (e.g. spin)
        direction_diff = racing_direction_diff(racing_track, [closest_index, second_closest_index], heading)
        if direction_diff > 30:
            reward = 1e-3

        # Zero reward of obviously too slow
        speed_diff_zero = optimals[2]-speed
        if speed_diff_zero > 0.5:
            reward = 1e-3

        ## Incentive for finishing the lap in less steps ##
        REWARD_FOR_FASTEST_TIME = 1500 # should be adapted to track length and other rewards
        STANDARD_TIME = 50  # seconds (time that is easily done by model)
        FASTEST_TIME = 35  # seconds (best time of 1st place on the track)
        if progress == 100:
            finish_reward = max(1e-3, (-REWARD_FOR_FASTEST_TIME /
                      (15*(STANDARD_TIME-FASTEST_TIME)))*(steps-STANDARD_TIME*15))
        else:
            finish_reward = 0
        reward += finish_reward
        
        ## Zero reward if off track ##
        if all_wheels_on_track == False:
            reward = 1e-3

        self.prev_steps = steps

        ####################### VERBOSE #######################
        
        if self.verbose == True:
            print("Closest index: %i" % closest_index)
            print("Distance to racing line: %f" % dist)
            print("=== Distance reward (w/out multiple): %f ===" % (distance_reward))
            print("Optimal speed: %f" % optimals[2])
            print("Speed difference: %f" % speed_diff)
            print("=== Speed reward (w/out multiple): %f ===" % speed_reward)
            print("Direction difference: %f" % direction_diff)
            print("Predicted time: %f" % projected_time)
            print("=== Steps reward: %f ===" % steps_reward)
            print("=== Finish reward: %f ===" % finish_reward)

        #################### RETURN REWARD ####################
        
        # Always return a float value
        return float(reward)


reward_object = Reward() # add parameter verbose=True to get noisy output for testing


def reward_function(params):
    return reward_object.reward_function(params)
