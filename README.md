# Robot Framework Example
## Summary
This project contains examples of how to use the [Robot Framework] to write automated robot tests in ROS2.
There are two main examples in this project, a  `dummy` example and a `Turtlesim` example. 
The `dummy` example confirms that the product of two numbers yields the expected result. 
The `Turtlesim` example is testing a ROS2 publisher, subscriber, acition and service.

## Installation
### Dependencies
```bash
pip install robotframework
```
## Basics
The structure of the package directory are described below
### The required contents without installing the package
* `src/<package_name>` - a directory with the same name as your package inside _src_. This directory will include all the custom python libraries and ROS2 nodes.
* `tests` - includes all the Robot Framework tests _(*.robot files)_
* `translations` - includes the "translation" from a custom python library to a Robot Framework library
* `scripts` - includes the main file that can execute the Robot Framework tests with python, and other related files


### The required contents and structure build and install the package
* `/<package_name>/scripts ` - the `scripts` folder must be inside a directory with the same name as your package _(not 'src')_. Includes the file that can execute the Robot Framework tests with python, and other related files
* `tests` - includes all the Robot Framework tests _(*.robot files)_
* `translations` - includes the "translation" from a custom python library to a Robot Framework library
* `package.xml` file containing meta information about the package
* `setup.py` containing instructions for how to install the package
* `setup.cfg` is required when a package has executables, so ros2 run can find them

## Dummy Execution
### Without Installing the Package
To run the sample without any prior installation, change the directory to that where the package is installed
and prefix your commands with
```bash
PYTHONPATH=${PYTHONPATH}:`pwd`/example_robot_framework
```
to let Python know where to find this package. Then, take a look at the help instructions for the _dummy_ script
```bash
PYTHONPATH=${PYTHONPATH}:`pwd`/example_robot_framework ./scripts/dummy_testing --help
```

## Turtlesim Execution
### Without Installing the Package
To run the sample without any prior installation, change the directory to that where the package is installed
and prefix your commands with
```bash
PYTHONPATH=${PYTHONPATH}:`pwd`/example_robot_framework
```
Run the example with
```bash
python3 ./example_robot_framework/scripts/turtlesim_run_test.py
```
### With the Package installed
To run the Turtlesim example, build the package in a workspace and run:
```bash
ros2 run example-robot-framework-ros2 robot_framework_turtlesim_test
```

### Combining Reports
To merge the multiple reports (the `.xml` files) use the `rebot` tool provided with the Robot Framework package.
```bash
python -m robot.rebot --help
```

As an example, run the following command to merge all the reports (`.xml` files) in the current directory, producing
a unified one entitled `Merged Results of the Dummy Tests`:
```bash
python -m robot.rebot --report merged.html --reporttitle "Merged Results of the Dummy Tests" *.xml
```

## License
Coalescent Mobile Robotics

   [Robot Framework]: <https://robotframework.org/>
