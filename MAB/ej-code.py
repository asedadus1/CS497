# Written by EJ Lilagan & Ased Adus

# Implement a MAB that focuse Upper-Confidence-Bound Action Selection algorithm for medical trial situation

# TODO:
#   - Three different treatments with uncertain performance, defined as welfare of a patient after the treatment
#   - Help doctor to prescribe a treatment at one time
#   - Display how estimated value of each treatment evolves over time
#   - Display the average reward you have obtained evolves

# HINT:
#   - int loop number
#   - double QBlue, QGreen, QRed where Q is used for the old/new estimate value
#   - int NBlue, NGreen, NRed = 0, where N is used for the 
#   - double R, where R is reward for the greedy number
#   - double e = 0.01 where e is epsilon-greedy method
#   - set the alpha to be x between 0 < 1 
#       - the alpha determains how far back should we focuse 
#   - loop from 1 to 100
#   - Find the greedy action, find the action to take
#   - Generate the random reward from the list and follow a distribution
#   - Update Q for the action

import random
import math
import numpy as np
import matplotlib.pyplot as plt

avereward_Green = []
avereward_Blue = []
avereward_Red = []
total_average_reward = []

def main():
    # set up of the compiler
    print("Multi-armed Bandit In-Class Project:\n"+
        "Objectives:\n" +
        "  1. Three different treatments with uncertain performance, defined as welfare of a patient after the treatment.\n" +
        "  2. Help doctor to prescribe a treatment at one time.\n" +
        "  3. Display how the average reward change over time\n")
   
    # array for green treatment
    green = [4.77317728, 5.99791051, 5.76776377, 4.47913849, 6.21411927, 6.84915318, 8.44082357, 
             6.15266159, 6.97135381, 7.43452167]
    # array for blue treatment
    blue = [6.00449072, 3.34005839, 6.71096916, 4.11113061, 5.68416528, 3.88539945, 3.51181469, 
            3.67426432, 4.98069804, 4.41366311]
    # array for red treatment
    red = [6.36086896, 5.65584783, 7.62912922, 13.29826146, 5.99876216, 8.14484021, 9.74488991, 
           6.616229, 14.26793535, 0.98932393]

    #set all the average reward to max
    QBlue, QGreen, QRed = max(blue), max(green), max(red)
    NBlue, NGreen, NRed = 0, 0, 0
    UCB_Blue, UCB_Green, UCB_Red = QBlue, QGreen, QRed

    # constant c that will be used for the UCB
    c = 2

    print(f"      ____ G ______ B ______ R ______")

    # average action for all three colors 
    At = []

    # begin the loop for the algorithm
    for loop_num in range(1, 101):
        # val = -1
        # reward = -1
        if(UCB_Blue == UCB_Green and UCB_Blue == UCB_Red and UCB_Green == UCB_Red):
            val = random.choice([1, 2, 3])
            if val == 1: #green 
                reward = np.random.choice(green)
                NGreen += 1
            elif val == 2: #blue
                reward = np.random.choice(blue)
                NBlue += 1
            else: #red
                reward = np.random.choice(red)
                NRed += 1
        else:
            #this will selcect the max from all the QBlue, QGreen, and QRed. and if there is to equal max,it will rendomly select from the remaing max
            max_value = max(UCB_Blue, UCB_Green, UCB_Red) 
            max_colors = [color for color, value in {'QBlue': UCB_Blue, 'QGreen': UCB_Green, 'QRed': UCB_Red}.items() if value == max_value]
            selected_color = random.choice(max_colors)
            if selected_color == 'QGreen':
                val = 1
                reward = np.random.choice(green)
                NGreen += 1
            elif selected_color == 'QBlue':
                val = 2
                reward = np.random.choice(blue)
                NBlue += 1
            elif selected_color == 'QRed':
                val = 3
                reward = np.random.choice(red)
                NRed += 1

        # perform the equation for green
        if val == 1:
            QGreen = QGreen + (1/NGreen)*(reward - QGreen)
            UCB_Green = QGreen + c * (math.sqrt(math.log(loop_num) / NGreen))
            At.append(UCB_Green)
        # perform the equation for blue
        elif val == 2:
            QBlue = QBlue + (1/NBlue)*(reward - QBlue)
            UCB_Blue = QBlue + c * (math.sqrt(math.log(loop_num) / NBlue))
            At.append(UCB_Blue)
        # perform the equation for red
        else:
            QRed = QRed + (1/NRed)*(reward - QRed)
            UCB_Red = QRed + c * (math.sqrt(math.log(loop_num) / NRed))
            At.append(UCB_Red)

        # Calculate total average reward at each step
        total_avg_reward = (NGreen * QGreen + NBlue * QBlue + NRed * QRed) / (NGreen + NBlue + NRed)
        total_average_reward.append(total_avg_reward)

        print(f"Run {loop_num}:   {UCB_Green:.2f}     {UCB_Blue:.2f}     {UCB_Red:.2f}       "
              f"Total average reward {total_avg_reward:.2f} ")        #Epsilon: {e:.2f}")

    # best treatment from all of the other colors
    print("\nBest treatment after all runs:", end=" ")
    if QGreen > QBlue and QGreen > QRed:
        print('"Green"')
        best_color = "Green"
    elif QBlue > QGreen and QBlue > QRed:
        print('"Blue"')
        best_color = "Blue"
    else:
        print('"Red"')
        best_color = "Red"

    # Print the best average treatment after all runs
    best_average_treatment = max(QGreen, QBlue, QRed)
    print(f'Best average treatment after all runs: {best_average_treatment:.1f} ({best_color})')

    fig = plt.figure(figsize=(8, 6))
    gs = fig.add_gridspec(2, 2, width_ratios=[3, 1])

    # Plotting the graph for all three colors
    ax1 = fig.add_subplot(gs[:, 0])

    # action average slope
    At, = ax1.plot(total_average_reward, label='Total Average Reward', color='purple')

    # Adding labels and title
    ax1.set_xlabel('Run number per treatment')
    ax1.set_ylabel('Avarage Reward Value per treatment')
    ax1.set_title('Line Graph with Index as X-axis')

    ax1.set_ylim(0, max(total_average_reward) + 1)

    ax1.legend(loc='upper right')

    plt.tight_layout()

    # Display the plot
    plt.show()
    print('\nEnd of Multi-armed bandit simulation')

if __name__ == "__main__":
    main()
