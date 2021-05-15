# Gradient Descent and Back Propagation

## Gradient Descent

* Gradient Descent is an optimization algorithm for finding the minimum of a function. We want to use it to minimize a cost function.
* To find a local minimum, we take steps proportional to the negative of the gradient

[1D gradient descent](https://www.quora.com/In-AI-how-would-1D-gradient-descent-look-like)

1D example: imagine x is actually a weight, w and f(x) is actually a cost function, c(w), which we want to minimize in respect to w:

![](http://fri.oden.utexas.edu/fri/Labs_2020/lab2/gradient_descent.png)

![](https://explained.ai/gradient-boosting/images/1d-vectors.png)

We want to choose w for which c is minimal. Minimum point is at the bottom of this parabola.

We choose a random weight at the beginning.
We then calculate a gradient at that point which is actually a cost function derivative at that point. We follow the negative gradient (negative slope) and get to the next point where we repeate the process.

We follow a negative descent until we reach the minimum.

* Using gradient descent we can figure out the best parameters for minimizing the cost function. For example, we can find the best values for the weights of the neuron inputs.


## Backpropagation

* How to adjust the optimal parameters or weights across the entire network? By using backpropagation.
* Backpropagation is used to calculate the error contribution of each neuron after a batch of data is processed.
* It relies hevily on the chain rule to go back through the network and calculate these errors.
* Backpropagation works by calculating the error at the output and then distibuting it back through network layers.
* It requires a known desired output for each input value (supervised learning).



