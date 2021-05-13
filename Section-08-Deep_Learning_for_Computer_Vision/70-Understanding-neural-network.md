# Understanding a Neural Network

* Multiple perceptrons network - dense neural network.
* Layers:
 * Input
    * Real values from the data
 * Hidden
   * Layers in between input and output
   * 3 or more hidden layers is "deep network"
 * Output
   * Final estimate of the output
* As you go forwards through more layers, the level of abstraction increases
* Activation functions:
 * Step
   * y(x) = 0 for x <0, y(x) = 1 for x >= 0
 * Sigmoid
   * \\( f(x) = \frac{1}{1+e^{-x}} \\)
   * pronounce: 1 over 1 + e to the negative x 
   * S-shaped with output between 0 (for infinitely negative x) to 1 (for infinitely positive x)
 * Hyperbolic Tangent: tanh(z)
   * \\(cosh(x) = \frac{e^x+e^-x}{2} \\)
   * \\(sinh(x) = \frac{e^x-e^-x}{2} \\)
   * \\(tanh(x) = \frac{sinh(x)}{cosh(x)} \\)
   * S-shaped with output between -1 (for infinitely negative x) to 1 (for infinitely positive x)
 * Rectified Linear Unit (ReLU)
   * \\( y(x) = max(0, x) \\)
 * tanh and ReLU tend to have the best performance