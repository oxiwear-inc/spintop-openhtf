.. _static-config-label:

## Static configuration

The static configuration are the parameters statically configuring the execution of the test plan. They are used to modify the flow of the test without changing the test cases or test tools code itself. The following examples illustrate test parameters that should be defined in the static configuration.

### Definition

In the context of a test bench implementation on spintop-openhtf, the static configuration is defined as classes of parameters accessible across the test bench sources.

Create a new file called static.py in the same folder as your test bench main. In the file, let's define a class building the parameters of the sleep test. Add the following code to the file:

```python
class SleepConfig():
    SLEEP_TIME = 5
    SLEEP_ITERATIONS = 2
```



### Use of parameters

To access the configuration in the test bench code, simply import the class.

```python
from static import SleepConfig
```

and access directly the instanciated parameters. 

```python
@plan.testcase('Sleep')
def sleep_test(test):
    """Waits five seconds"""
    
    for x in range(SleepConfig.SLEEP_ITERATIONS):
        print ("Sleep iteration {} - sleep time {}".format(x, 
                                            SleepConfig.SLEEP_TIME))
        sleep(SleepConfig.SLEEP_TIME)
```

Add the use of the static configuration use to your latest test bench and run it.

The test will execute a 5 second sleep twice as determined 
```bat
Sleep iteration 0 - sleep time 5
Sleep iteration 1 - sleep time 5
```

### Use in Complex Test Benches

Multiple classes can be defined in the same configuration file. The pattern used for the definition is up to the developper. Each test case can have its own class of parameters, or they can be split according to product features across multiple test cases.

The static configuration as proposed is very useful in the definition of complex test benches, for example one managing the tests of different versions of the same products. In this case, the difference between the products can be parametrized using two classes with the same variables at different values.

```python
class ProductVersionA():
    TRX_CNT = 2
    TEMP_SENSOR_I2C_ADDR = 0x49

    
class ProductVersionB():
    TRX_CNT = 1
    TEMP_SENSOR_I2C_ADDR = 0x48
```

Add the product version selection in the trigger phase and import dynamically the right class depending on the selected product. As illustrated below, using the custom trigger phase from the :ref:`custom-trigger-phase-label` tutorial. 

```python
if test.state["product"] == "A":
    from static import ProductVersionA as ProductConfig
elif test.state["product"] == "B":
    from static import ProductVersionB as ProductConfig   

print ("I2C Address: {}".format(ProductConfig.TEMP_SENSOR_I2C_ADDR))
```
Add the above code to the sleep test case and run it again. Enter "A" for the product when prompted and the right configuration for product A will be imported.

```bat
I2C Address: 0x49
```


:download:`Tutorial source <../tutorials/main_static_config.py>`

:download:`Configuration file <../tutorials/static.py>`

