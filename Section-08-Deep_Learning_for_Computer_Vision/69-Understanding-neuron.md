# Understanding a Neuron

* Artificial Neural Networks (ANNs) have basis in biology
* Biological neurons can be mimicked with artificial neuron (perceptron)
* A Biological neuron (such as brain cell) has:
 * Dendrites
   * They feed into the body of the cell
   * There can be multiple dendrites coming to the body of the cell
 * Body
   * Electrical signal gets passed through dendrites to the body of the cell
 * Axon
   * A single output (electrical signal) is passed from body to the Axon and then to some other neuron
* Artificial neuron (perceptron) also has inputs and the output e.g.
 * Input0 and Input1
 * Output
* Inputs contain the value of the features e.g. number of rooms in the house, darkness of the image pixel etc...
* Inputs are multiplied with some sort of weights
 * Weight0 for Input0 and Weight1 for Input1
 * Typically, weights are initialized randomly
* Weighted sum of inputs is passed to the activation function
There are many different activation functions. One simple is step function: if sum >=0 => y = 1, if sum < 0 => y = 0.
* What if the initial input values start with 0? Then the sum = 0 for any values of weights.
 * To fix this, we introduce a bias e.g. 1. 
 * Mathematically: \\( y = \sum\limits_{i = 0}^{N}w_ix_i + b \\)
  * n = number of inputs
  * For many perceptrons in a network, this can be extended in a matrix form
