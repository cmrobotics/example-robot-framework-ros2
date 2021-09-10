*** Settings ***
Documentation     An example on how to use ROS2 with Robot Framework
Library           ../translations/TurtlesimExampleLibrary.py
Test Setup       Setup actions
Test Teardown    Teardown actions

*** Keywords ***
Setup actions
    TurtlesimExampleLibrary.Setup

Teardown actions
    TurtlesimExampleLibrary.Teardown

*** Variables ***
${vel}                  0.4
${orientation_rad}      1.57

*** Test Cases ***


Test that the turtle is moving, resetting and rotating
    Given That A Velocity Command Is Published To The Turtle    ${vel}
    And verify that the turtle moved
    Then send a service call to reset the turtle
    And send an action to rotate the turtle    ${orientation_rad}
