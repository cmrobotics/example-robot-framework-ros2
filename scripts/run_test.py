import os
import signal
import robot
import rclpy


package_path = os.path.dirname(os.path.realpath(__file__))
tests_path = os.path.join(package_path, "../tests")
dummy_test = os.path.join(tests_path, "ExampleTest.robot")

if __name__ == '__main__':
    rclpy.init(args=None)
    
    try:
        robot.run(
            dummy_test,
            test="Validate that the robot moves when commanded",
            name="Testing the robot's movement for the first time",
            #log='NONE',
            outputdir=os.path.join(os.curdir, "reports"),
            variable=[],
            timestampoutputs=False
        )
    except KeyboardInterrupt:
        print("Interrupted by the user")
    except Exception as ex:
        print("Interrupted by an exception: {}".format(ex))
    finally:
        rclpy.shutdown()
