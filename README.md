# Robot Framework Example
## Summary
This project contains examples of how to use the [Robot Framework] to write automated robot tests in ROS2.

## Installation
### Dependencies
```bash
pip install robotframework
```

## Execution
### Without Installing the Package
To run the sample without any prior installation, change the directory to that where the package is installed
and prefix your commands with
```bash
PYTHONPATH=${PYTHONPATH}:`pwd`/src
```
to let Python know where to find this package. Then, take a look at the help instructions for the _dummy_ script
```bash
PYTHONPATH=${PYTHONPATH}:`pwd`/src ./scripts/dummy_testing --help
```

### TurtleSim Example
To run the Turtlesim example 


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
