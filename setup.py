from setuptools import setup
import glob

package_name = 'champ_setup_assistant'
submodules = 'champ_setup_assistant/submodules'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name, submodules],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/' + 'setup_assistant.launch.py']),
        ('share/' + package_name + '/docs/images', glob.glob('docs/images/*')),
        ('share/' + package_name + '/config', glob.glob('config/*')),
        ('share/' + package_name + '/templates', glob.glob('templates/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jimeno Jmm',
    maintainer_email='jimenojmm@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'assistant = champ_setup_assistant.setup_assistant:main',
        ],
    },
) 
 
