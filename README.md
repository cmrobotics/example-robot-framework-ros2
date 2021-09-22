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
## Package Content
### The required content without installing the package
* `src/<package_name>` - a directory with the same name as your package inside _src_. This directory will include all the custom python libraries and ROS2 nodes.
* `tests` - includes all the Robot Framework test scripts _(*.robot files)_.
* `translations` - folder includes scripts which "translates" the custom python library to a Robot Framework readable library.
* `scripts` - includes the main file that can execute the Robot Framework tests with python, and other related files.


### The required content and structure to build and install the package
* `/<package_name>` - a directory with the same name as your package inside _src_. This directory will include all the custom python libraries and ROS2 nodes. 
   * The `scripts` folder must be inside the directory with the same name as your package `/<package_name>/scripts` _(not inside 'src')_. Includes the file that can execute the Robot Framework tests with python, and other related files.
* `tests` - folder includes all the Robot Framework tests _(*.robot files)_.
* `translations` - folder includes scripts which "translates" the custom python library to a Robot Framework readable library.
* `resource/<package_name> file` - This is required for ROS2 to find your package
* `package.xml` - file containing meta information about the package.
* `setup.py` - containing instructions for how to install the package.
* `setup.cfg` - is required when a package has executables, so ros2 run can find them.

## Dummy Execution
### Without Installing the Package
To run the sample without any prior installation, change the directory to that where the package is installed
and prefix your commands with:
```bash
PYTHONPATH=${PYTHONPATH}:`pwd`/src
```
to let Python know where to find this package. Then, take a look at the help instructions for the _dummy_ script
```bash
PYTHONPATH=${PYTHONPATH}:`pwd`/src ./scripts/dummy_testing --help
```

## Turtlesim Execution
### Without Installing the Package
To run the sample without any prior installation, change the directory to that where the package is installed
and prefix your commands with:
```bash
PYTHONPATH=${PYTHONPATH}:`pwd`/example_robot_framework
```
Run the example with:
```bash
python3 ./example_robot_framework/scripts/turtlesim_run_test.py
```
### With the Package installed
To run the Turtlesim example, build the package in a workspace and run:
```bash
ros2 run example-robot-framework-ros2 robot_framework_turtlesim_test
```

## Combining Reports
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
