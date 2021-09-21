import traceback


class ContextException(Exception):
    """
    Forcefully append the last traceback of an exception since the RobotFramework only shows the exception message.
    This change is needed to make it easier to figure things out when an exception occurs.
    """

    def __init__(self, message):
        # Fetch the stack trace
        trace = traceback.extract_stack()

        # Iterate through the stack and look for occurences that refer to this package
        context = ""
        for stack in trace[:-1]:
            if stack[0].find("example_robot_framework") > 1:
                context += stack[2] + "."

        # Flip everything to have it in the correct order
        context = context[:-1]

        # Hand it over the our parent
        super(ContextException, self).__init__("{}: {}".format(context, message))
