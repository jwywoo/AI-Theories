import tensorflow as tf

#
#
# # Linear Regression
#
# # hypothesis for linear regression
# # return w*x + b
# def hypothesis(w, b, x):
#     return w * x + b
#
#
# # cost for linear function
# # return average
# def cost_function(w, b, x, y):
#     return tf.reduce_mean(tf.square(hypothesis(w, b, x)) - y)
#
# # gradient descent
# if __name__ == '__main__':
#     print("what")

# if __name__ == 'main':
#     x_data = [1, 2, 3, 4, 5]
#     y_data = [1, 2, 3, 4, 5]
#
#     w = tf.Variable(100)
#     b = tf.Variable(10)
#
#     learning_rate = 0.1
#
#     for i in range(100 + 1):
#         with tf.GradientTape() as tape:
#             hypothesis = w * x_data + b
#             cost = tf.reduce_mean(tf.square(hypothesis - y_data))
#
#         w_grad, b_grad = tape.gradient(cost, [w, b])
#         w.assign_sub(learning_rate * w_grad)
#         b.assign_sub(learning_rate * b_grad)
#
#         if i % 10 == 0:
#             print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, w.numpy(), b.numpy(), cost))

x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]

w = tf.Variable(100)
b = tf.Variable(10)

learning_rate = 0.1

for i in range(100 + 1):
    with tf.GradientTape() as tape:
        hypothesis = w * x_data + b
        cost = tf.reduce_mean(tf.square(hypothesis - y_data))

    w_grad, b_grad = tape.gradient(cost, [w, b])
    w.assign_sub(learning_rate * w_grad)
    b.assign_sub(learning_rate * b_grad)

    if i % 10 == 0:
        print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, w.numpy(), b.numpy(), cost))
