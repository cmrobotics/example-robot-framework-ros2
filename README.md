# Robot Framework Example
## Summary
This project contains examples of how to use the [Robot Framework] to write automated robot tests in ROS2.

## Execution
### Without Installing the Package
To run the sample without any prior installation, change the directory to that where the package is installed
and prefix your commands with
```shell
PYTHONPATH=${PYTHONPATH}:`pwd`/src
```
to let Python know where to find this package. Then, take a look at the help instructions for the _dummy_ script
```shell
PYTHONPATH=${PYTHONPATH}:`pwd`/src ./scripts/dummy_testing --help
```

## License
Coalescent Mobile Robotics

   [Robot Framework]: <https://robotframework.org/>
