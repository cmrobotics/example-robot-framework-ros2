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
            test="Check if number is larger than threshold",
            name="Checks if the addition of two numbers is larger than a specified threshold ",
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
