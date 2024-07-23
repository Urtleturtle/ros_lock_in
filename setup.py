from setuptools import find_packages, setup

package_name = 'ros_lock_in'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='andywang',
    maintainer_email='turtlewang3@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['publisher = ros_lock_in.publisher:main',
                            'subscriber = ros_lock_in.subscriber:main',
                            'subscriber2 = ros_lock_in.bluerov2_sensors:main',
                            'physicssubscriber = ros_lock_in.physics_sim:main',
                            'drivepub = ros_lock_in.rovdrive:main',
                            'armdisarm = ros_lock_in.armdisarm:main'
        ],
    },
)
