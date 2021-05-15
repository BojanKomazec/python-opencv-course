# Cost Functions

* Used to evaluate performance of a neuron (and entire NN)
* Used to measure how far off hypothesis (predicted value) is from the expected value
* Notation:
 * y - true value
 * a - hypothesis (prediction)
 * z = w*x + b (sum)
 * \\( \sigma(z) = a \\) - activation (neuron's prediction)
 <br/>
 <br/>
* **Quadratic cost**
 * \\( C = \sum\limits_{i = 1}^{N}\frac{(y_i - a_i)^2}{N} = \frac{1}{N}\sum\limits_{i = 1}^{N}(y_i - a_i)^2 \\)
 * Larger errors are more prominent due to squaring
 * This calculation can slow down the learning speed
 <br/>
 <br/>
* **Cross Entropy**
 * \\( C = -\frac{1}{N}\sum\limits_{i = 1}^{N}(y_iln(a_i) + (1 - y_i)ln(1 - a_i)) \\)
 * Allows faster learning
 * The larger the difference between _y_ and _a_, the faster the neuron can learn
 <br/>
 <br/>
* Before introducing a concept of "learning" we had to cover first these two concepts:
 * Activation functions
 * Cost function
* **Learning**: using neurons and the measurement of error (cost function) to correct prediction 

 
 
 