from setuptools import setup

package_name = 'example_robot_framework'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/tests', ['tests/turtlesim_example_test.robot']),
        ('share/' + package_name + '/translations', ['translations/TurtlesimExampleLibrary.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Vivian',
    maintainer_email='vivian.li@cm-robotics.com',
    description='TODO: Package description',
    license='Coalescent Mobile Robotics',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_framework_turtlesim_test = example_robot_framework.scripts.turtlesim_run_test:main',
        ],
    },
)
