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
#   - set the alph to be x between 0 < 1 
#       - the alpha determains how far back should we focuse 
#   - loop from 1 to 100
#   - Find the greedy action, find the action to take
#   - Generate the random reward from the list and follow a distribution
#   - Update Q for the action

import random
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

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
        "  3. Display how estimated value of each treatment evolves over time.\n" +
        "  4. Display the average reward you have obtained evolves.")

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
    # QBlue, QGreen, QRed = 15, 15, 15
    max_val = max(QBlue, QGreen, QRed) 
    QBlue, QGreen, QRed = max_val, max_val, max_val
    
    

    # set the size as the size for the color
    NBlue, NGreen, NRed = 0, 0, 0
    c = 2
    print(f"      ___ G _____ B _____ R ___")
    At = []
    # begin the loop for the algorithm
    for loop_num in range(1, 101):
        val = -1
        reward = -1
        if(QBlue == QGreen and QBlue == QRed and QGreen == QRed):
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
            max_value = max(QBlue, QGreen, QRed) 
            max_colors = [color for color, value in {'QBlue': QBlue, 'QGreen': QGreen, 'QRed': QRed}.items() if value == max_value]
            selected_color = random.choice(max_colors)
            if selected_color == 'QGreen':
                val = 1
                reward = np.random.choice(green)
                NGreen += 1
            elif selected_color == 'QBlue':
                val = 2
                reward = np.random.choice(blue)
                NBlue += 1
            else:
                val = 3
                reward = np.random.choice(red)
                NRed += 1

        # perform the equation for green
        if val == 1:
            QGreen = QGreen + (1/NGreen)*(reward - QGreen)
        # perform the equation for blue
        elif val == 2:
            QBlue = QBlue + (1/NBlue)*(reward - QBlue)
        # perform the equation for red
        else:
            QRed = QRed + (1/NRed)*(reward - QRed)

        # this should be the equation at found at the end of the slide
        if val == 1:
            UCB_Green = QGreen + c * (math.sqrt(math.log(loop_num) / NGreen))
            At.append(UCB_Green)
        elif val == 2:
            UCB_Blue = QBlue + c * (math.sqrt(math.log(loop_num) / NBlue))
            At.append(UCB_Blue)
        else:
            UCB_Red = QRed + c * (math.sqrt(math.log(loop_num) / NRed))
            At.append(UCB_Red)

        # Calculate total average reward at each step
        total_avg_reward = (NGreen * QGreen + NBlue * QBlue + NRed * QRed) / (NGreen + NBlue + NRed)
        total_average_reward.append(total_avg_reward)
        # set those values as placeholders to use in the graph
        avereward_Green.append(QGreen)
        avereward_Blue.append(QBlue)
        avereward_Red.append(QRed)

        print(f"Run {loop_num}:   {QGreen:.2f}     {QBlue:.2f}     {QRed:.2f}       "
              f"Total average reward {total_avg_reward:.2f} ")        #Epsilon: {e:.2f}")

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

    green_line, = ax1.plot(avereward_Green, label='Green', color='green')
    blue_line, = ax1.plot(avereward_Blue, label='Blue', color='blue')
    red_line, = ax1.plot(avereward_Red, label='Red', color='red')
    At, = ax1.plot(total_average_reward, label='Total Average Reward', color='purple')

    # Adding labels and title
    ax1.set_xlabel('Run number per treatment')
    ax1.set_ylabel('Avarage Reward Value per treatment')
    ax1.set_title('Line Graph with Index as X-axis')

    ax1.legend(loc='upper right')

    # Create CheckButtons
    ax2 = fig.add_subplot(gs[:, 1])
    labels = ('Green', 'Blue', 'Red', 'Average')
    visibility = [green_line.get_visible(), blue_line.get_visible(), red_line.get_visible(), At.get_visible()]
    check_buttons = CheckButtons(ax2, labels, visibility)

    # function to label for the colors
    def func(label):
        if label == 'Green':
            green_line.set_visible(not green_line.get_visible())
        elif label == 'Blue':
            blue_line.set_visible(not blue_line.get_visible())
        elif label == 'Red':
            red_line.set_visible(not red_line.get_visible())
        elif label == 'Average':
            At.set_visible(not At.get_visible())

        # Redraw the plot to reflect the changes in visibility
        plt.draw()

    check_buttons.on_clicked(func)
    plt.tight_layout()

    # Display the plot
    plt.show()
    print('\nEnd of Multi-armed bandit simulation')

if __name__ == "__main__":
    main()