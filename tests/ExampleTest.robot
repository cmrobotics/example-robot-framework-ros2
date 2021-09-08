*** Settings ***
Documentation     An example on how to use ROS2 with Robot Framework
Library           ../libraries/ExampleLibrary.py
Test Setup       Setup actions
Test Teardown    Teardown actions

*** Keywords ***
Setup actions
    ExampleLibrary.Setup

Teardown actions
    ExampleLibrary.Teardown

*** Variables ***
${a}        9
${b}        2
${vel}      0.1

*** Test Cases ***
Do Calculations
    given message    "hello"
    then check that addition is larger than threshold     1   1   1

Validate that the robot moves when commanded
    Given that we publish a velocity    ${vel}
    Then verify that the robot moved