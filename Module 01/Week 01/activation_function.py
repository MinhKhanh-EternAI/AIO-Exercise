import math


def is_number(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    if x <= 0:
        return 0
    else:
        return x


def elu(x, alpha=0.01):
    if x <= 0:
        return alpha * (math.exp(x) - 1)
    else:
        return x


def check_activation_function_name(af_name, x):
    if af_name.lower() in ["sigmoid", "relu", "elu"]:
        if af_name == "sigmoid":
            result = sigmoid(x)
        elif af_name == "relu":
            result = relu(x)
        else:
            result = elu(x)
        print(f"{af_name}: f({x}) = {result}")
    else:
        print(f"{af_name} is not supported")


if __name__ == "__main__":
    x = input("Enter x value: ")
    if not is_number(x):
        print("x must be a number")
    else:
        x = float(x)
        af_name = input(
            "Enter the activation function name (sigmoid|relu|elu): ")
        check_activation_function_name(af_name, x)
