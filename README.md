# SuperSimpleStocks
Simple example to calculate metrics for given stocks

## Description
The source code that will :

- For a given stock, 
    - calculate the dividend yield
    - calculate the P/E Ratio
    - record a trade, with timestamp, quantity of shares, buy or sell indicator and price
    - Calculate Stock Price based on trades recorded in past 15 minutes
- Calculate the GBCE All Share Index using the geometric mean of prices for all stocks

## Requirements

- Python 3.x (tested on 3.4)
- Spark 1.6.0
- Java >= 1.7 (tested on 1.8)
- NumPy
- Celery
- RabbitMQ
- Tested on MacOS X

## Installation


### Spark
First ensure you have installed Python 3.x, Java >=1.7 and Spark 1.6.0.

To install Spark download the sources, install Scala. Clean an build sources:

```
export SBT_OPTS="-Xmx2g -XX:MaxPermSize=512M -XX:ReservedCodeCacheSize=512m"
sbt clean 
sbt assembly
```

Export spark to be avalible in your python environement by setting it in PYTHONPATH:

```
export SPARK_HOME=path\to\sources
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
```

if you are using virtualenvwrapper:

```
add2virtualenv $SPARK_HOME/python/
```

To make pyspark working first you need to install application dependencies from the next step.

### Application
To install application with all dependencies:

```
pip install git+git://github.com/tgorka/SuperSimpleStocks.git
```

To install in develop mode from the sources you should clone the sources and install in in develop mode:

```
pip install -e /path/to/sources --no-binary :all: pytest
```

To check if the application was installed:

```
python -c "import sys; import supersimplestocks; print('supersimplestocks' in sys.modules)"
```

It should print True or throw an ImportError.

To check if pyspark is working:

```
python -c "import sys; import pyspark; print('pyspark' in sys.modules)"
```

To uninstall application:

```
pip uninstall supersimplestocks
```

HINT: It's always save to use VirtualEnv (https://virtualenv.readthedocs.org/en/latest/) and virtualenvwrapper.

## Run



## Release History
+ 0.0.1 - initial revision.

## Author
Tomasz Górka <http://tomasz.gorka.org.pl>

## License
&copy; 2016 Tomasz Górka

MIT licensed.
