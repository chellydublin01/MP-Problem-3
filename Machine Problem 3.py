# Machine Problem 3

# modifying the 2nd degree polynomial x^2+x+1

# defining the function
def f(x):
    result = x**2+x+1
    return result

def least_norm_err_vec(exp_points,n):
    err_arr=[0]*n #entering blank array of errors
    for i in range(0,n):
        err_arr[i]=exp_points[i][1] - f(exp_points[i][0])
    return err_arr

# input points and display the error array
n=int(input("Enter number of points to input: "))
exp_points=[] #entering blank array of zeros

# output for points
print("Enter the points (x,y) *x space y, enter*: ")
for i in range(0,n):
    exp_points.append([int(j) for j in input("Enter two values: ").split()])

# call the error function and display the result
err_arr = least_norm_err_vec(exp_points,n)
print("Error array is below:\n")
print(err_arr)
# end of code