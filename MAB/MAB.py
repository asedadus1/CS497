import numpy as np
import matplotlib.pyplot as plt


avereward_Green = []
avereward_Blue = []
avereward_Red = []


def main():
    print("Multi-armed Bandit")

    green = [4.77317728, 5.99791051, 5.76776377, 4.47913849, 6.21411927, 6.84915318, 8.44082357, 6.15266159, 6.97135381, 7.43452167]
    blue = [6.00449072, 3.34005839, 6.71096916, 4.11113061, 5.68416528, 3.88539945, 3.51181469, 3.67426432, 4.98069804, 4.41366311]
    red = [6.36086896, 5.65584783, 7.62912922, 13.29826146, 5.99876216, 8.14484021, 9.74488991, 6.616229, 14.26793535, 0.98932393]

    Q_values = np.zeros(3)  # Array to store estimated values
    N_counts = np.zeros(3)  # Array to store counts of chosen arms
    e = 0.01  # epsilon default value

    for _ in range(100):
        val = -1
        reward = -1
        if np.random.rand() < e:
            val = np.random.choice([1, 2, 3])
            reward = np.random.choice([green, blue, red][val - 1])
            N_counts[val - 1] += 1
        else:
            highest_arm = np.argmax(Q_values)
            val = highest_arm + 1
            reward = np.random.choice([green, blue, red][highest_arm])
            N_counts[highest_arm] += 1

        Q_values[val - 1] += (1/N_counts[val - 1]) * (reward - Q_values[val - 1])
        print(f"  {Q_values[0]}   {Q_values[1]}   {Q_values[2]}")
        if val == 1:
            avereward_Green.append(Q_values[0])
        elif val == 2:
            avereward_Blue.append(Q_values[1])
        else:
            avereward_Red.append(Q_values[2])

    # Plotting the line graph
    plt.plot(avereward_Green, label='Green', color='green')
    plt.plot(avereward_Blue, label='Blue', color='blue')
    plt.plot(avereward_Red, label='Red', color='red')

    # Adding labels and title
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Line Graph with Index as X-axis')

    # Display the plot
    plt.show()
if __name__ == "__main__":
    main()
