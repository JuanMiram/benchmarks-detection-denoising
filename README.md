# A benchmark for time-frequency denoising/ detecting methods

## What is this benchmark?
A benchmark is a comparison between different methods when running an standardized test. The goal of this benchmark is to compare different methods for denoising / detecting a signal based on different characterizations of the of the time-frequency representation of the signal. This particular benchmark has been created for evaluating the performance of techniques based on the zeros of the spectrogram and to contrast them with more traditional methods, like those based on the ridges of that time-frequency distribution.

Nevertheless, with the purpose of making this benchmark more useful, the methods to compare, the tests, and the performance evaluation functions were conceived as different modules, so that one can assess new methods without modifying the tests or the signals. The only restriction this pose is that the methods should satisfy some requirements regarding the shape of their input an output parameters. On the one hand, the tests and the performance evaluation functions, are encapsulated in the class `Benchmark`. On the other hand, the signals used in this benchmark are generated by the methods in the class `SignalBank`.

The notebook *demo_benchmark.ipynb* introduces de idea of the benchmark and give two minimal working examples of how to use it. The notebook *demo_signal_bank.ipynb* shows the signals produced by the `SignalBank` class.### Signal: linearChirp
|    | Method + Param         |   SNRin: 10dB |   SNRin: 20dB |   SNRin: 30dB |
|---:|:-----------------------|--------------:|--------------:|--------------:|
|  0 | delaunay_triangulation |       5.66706 |       26.0966 |       35.8629 |
|  1 | empty_space            |       7.08653 |       24.5534 |       34.187  |
|  2 | hard_thresholding      |      17.8015  |       27.2299 |       36.5867 |
|  3 | a_new_method+Params0   |      10       |       20      |       30      |
|  4 | a_new_method+Params1   |      10       |       20      |       30      |
|  5 | a_new_method+Params2   |      10       |       20      |       30      |
### Signal: cosChirp
|    | Method + Param         |   SNRin: 10dB |   SNRin: 20dB |   SNRin: 30dB |
|---:|:-----------------------|--------------:|--------------:|--------------:|
|  0 | delaunay_triangulation |       3.41992 |       22.8806 |       34.7139 |
|  1 | empty_space            |       4.59727 |       23.0732 |       32.1396 |
|  2 | hard_thresholding      |      16.9018  |       26.0958 |       35.8779 |
|  3 | a_new_method+Params0   |      10       |       20      |       30      |
|  4 | a_new_method+Params1   |      10       |       20      |       30      |
|  5 | a_new_method+Params2   |      10       |       20      |       30      |
### Signal: multiComponentPureTones
|    | Method + Param         |   SNRin: 10dB |   SNRin: 20dB |   SNRin: 30dB |
|---:|:-----------------------|--------------:|--------------:|--------------:|
|  0 | delaunay_triangulation |       1.06964 |       7.26603 |      12.3192  |
|  1 | empty_space            |       1.252   |       7.18496 |       5.40836 |
|  2 | hard_thresholding      |       8.18038 |      19.2142  |      23.6129  |
|  3 | a_new_method+Params0   |      10       |      20       |      30       |
|  4 | a_new_method+Params1   |      10       |      20       |      30       |
|  5 | a_new_method+Params2   |      10       |      20       |      30       |
