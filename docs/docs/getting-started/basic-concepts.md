## Basic Concepts

We first introduce the basic spintop-openhtf concepts with which test benches can be created.

### Test plan

In the context of a test bench implementation on spintop-openhtf, the test plan is the object to which the test phases are loaded and which executes them. 

See :ref:`first-testbench-label`.

### Test phases

The test phases implement the different test cases. They are defined and loaded in the test plan object which executes them one after the other

See :ref:`test-case-label`.

### Test Sequences

The test sequences are intermediary levels of test phases between the test plan and the test cases. They can help implement complex test hierarchies.

See :ref:`test-hierarchy-label`.

### Trigger phase

The trigger phase refers to the first phase of the test bench, in which the dynamic configuration of the test is loaded. Such information can be for example:

- The operator name

- The board or system serial number

- The board or system device type

- The test type to execute on the board or system

See :ref:`trigger-phase-label`.

### Test flow management

Test flow management refers to the dynamic selection of which test cases are executed depending on the inputs given at the beginning of the test bench in the trigger phase and by the results of the test themselves. Such inputs that determine test flow are for example the Device Under Test type and a FAIL result of a critical test.

See :ref:`test-flow-label`.

### Configuration

The configuration refers to all predetermined parameters used to control the flow or the execution of the test. The different configuration types are:

- The parameters configuring the test station itself, that is parameters changing from station to station and test jig to test jig, such as ip adresses, com port, etc.

- The parameters statically configuring the execution of the test plan, such as for example, the maximum number of iterations for a calibration algorithm.

- The parameters dynamically configuring the execution of the test plan, such as those gathered in the trigger phase.


See :ref:`static-config-label` and  :ref:`teststation-config-label`


### Forms

Forms are use to interact with the test operator. They permit the implementation of complex dialogs which allow to operator to both execute manual operations on the test jig to allow the test to continue or to input test result data for verification,

See :ref:`forms-label`.

### Plugs

In the spintop-openhtf context, plugs allow the iteraction of the test logic with the surrounding test equipment. They basically wrap the access to the test equipment automation libraries.

See :ref:`plugs-label`.

 
### Criteria & measures

The criteria refer to the thresholds against which measures are compared to declare a test case PASS or FAIL. In the spintop-openhtf context, the measures module implements the criteria and the comparison against the selected values.

See :ref:`criteria-label`.


### Results

The spintop-openhtf framework outputs a standardized test result record for each test. 

See :ref:`results-label`.