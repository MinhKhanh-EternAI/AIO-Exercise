import random
import math


def regression_loss(num_samples, loss_name):
    if not num_samples.isnumeric():
        print('Number of samples must be an integer number')
        return

    num_samples = int(num_samples)

    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        loss = 0

        if loss_name == 'MAE':
            loss = abs(target - predict)
        elif loss_name == 'MSE':
            loss = (target - predict) ** 2
        elif loss_name == 'RMSE':
            loss = math.sqrt((target - predict) ** 2)
        else:
            print('Invalid loss name')
            return

        print(f"Loss name: {
              loss_name}, Sample: sample-{i}, Predict: {predict}, Target: {target}, Loss: {loss}")


# Sử dụng function với số lượng samples và loss name được nhập từ người dùng
if __name__ == "__main__":
    num_samples = input("Enter number of samples: ")
    loss_name = input("Enter loss name (MAE, MSE, RMSE): ")
    regression_loss(num_samples, loss_name)
