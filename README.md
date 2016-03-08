# Super Simple Stocks
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
- Celery (tested on 3.1.21)
- RabbitMQ (tested on 3.5.1)
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

Export spark to be avalible in your python environement by setting it 
in PYTHONPATH:

```
export SPARK_HOME=path\to\sources
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
```

if you are using virtualenvwrapper:

```
add2virtualenv $SPARK_HOME/python/
```

To make pyspark working first you need to install application dependencies 
from the next step.

### Celery
Celery server should be installed as well as RabbitMQ or another 
messaging system compatible with Celery.

### Application
To install application with all dependencies:

```
pip install git+git://github.com/tgorka/SuperSimpleStocks.git
```

To install in develop mode from the sources you should clone the sources and 
install in in develop mode:

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

HINT: It's always save to use VirtualEnv 
(https://virtualenv.readthedocs.org/en/latest/) and virtualenvwrapper.

## Run

### Celery server

Make sure that RabbitMQ is running.

```
rabbitmq-server --start
```

To run celery server open console in the sources.

```
celery -A supersimplestocks worker --loglevel=INFO --concurrency=1
```

This is example of use of Celery with RabbitMQ. The configuration should be
done in more optimized way. The same is with Spark.

### API

There is an API functions to use the library. The documentation can be 
generated from the comments using reStructuredText.

```
python setup.py build_sphinx
```

The simpe of API use:

```
import supersimplestocs

supersimplestocks.load_dividend_data('example/data.csv')
supersimplestocks.record_dividend_data('TEA', 'Preferred', 45, '12%', 1000)

supersimplestocks.record_trade('TEA', 'SELL', 100, 10.5)
supersimplestocks.record_trade('TEA', 'BUY', 1000, 10.5)

supersimplestocks.stock_price('TEA')
supersimplestocks.dividend_yield('TEA')
supersimplestocks.p_e_ratio('TEA')

supersimplestocks.gbce()
```

### Example of use from the console

#### Load last dividents data
Before calculation of the dividents there historical data needs to be added
from the CSV file.
There is data file in example folder so it needs to be added:

```
python supersimplestocks --action=load_dividents examples/data.csv
```

or it can le load one by one

```
python supersimplestocks --action=load_divident SYMBOL, TYPE, LAST_DIVIDEND, FIXED_DIVIDEND, PAR_VALUE
```

example

```
python supersimplestocks --action=load_divident TEA, Prefered, 8, 0.02, 100
```

#### Record trade

```
python supersimplestocks SYMBOL TYPE QUANTITY PRICE
```

example:

```
python supersimplestocks TEA SELL 1000 90
python supersimplestocks TEA BUY 100 90
```

#### Calculate stock price

```
python supersimplestocks --action=price SYMBOL
```

example:

```
python supersimplestocks --action=price TEA
```

#### Calculate dividend yeild

```
python supersimplestocks --action=dividend SYMBOL
```

example:

```
python supersimplestocks --action=dividend TEA
```

#### Calculate P/E Ratio

```
python supersimplestocks --action=pe SYMBOL
```

example:

```
python supersimplestocks --action=pe TEA
```

#### Calculate GBCE All share index for all stocks

```
python supersimplestocks --action=gbce
```

example:

```
python supersimplestocks --action=gbce
```


## Tests

tests suits are in test folder to run it

```
python setup.py test
```


## Release History
+ 0.3.0 - better interface, testings, bugfixing
+ 0.2.0 - code for the celery and spark
+ 0.1.0 - initial revision.

## Author
Tomasz Górka <http://tomasz.gorka.org.pl>

## License
&copy; 2016 Tomasz Górka

MIT licensed.
