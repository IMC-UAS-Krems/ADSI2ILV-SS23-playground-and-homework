# Instructions for the Self-Learning

1. Copy the self-learning folder outside public, i.e., in your playground folder

2. Go into the self-learning folder that you just copied, activate your venv (or create a new one), then run `pytest`

3. Verify that the tests fail because the classes are not implemented.

```E       TypeError: Can't instantiate abstract class DynamicArrayList with abstract methods contains, delete_element, insert_element, size, to_string```

4. Implement the List* and DisjointSet classes 

5. Implement more tests and check your coverage. You must achieve a coverage above 90%

## How to check coverage?

Install pytest-cov in your venv

From self-learning folder run the command:

```pytest --cov . --cov-fail-under=90 --cov-config=./.coveragerc --cov-report=term --cov-report=html``

Which means run coverage using the `.coveragerc` file (given to you) as configuration, report the results on the console and as nicely formatted html. Fail with a message if the coverage is below 90%
