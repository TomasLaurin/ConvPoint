# ConvPoint Module

## Compiling the K-nearest neighbors library

The ```nearest_neighbors``` directory contains a very small wrapper for [NanoFLANN](https://github.com/jlblancoc/nanoflann) with OpenMP.
To compile the module:

```
cd knn
python setup.py install --home="."
```

On windows, the naming directories may be different. Move the created nearest_neighbours.py and .pyd to ./lib/python


