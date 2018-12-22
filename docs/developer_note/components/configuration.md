# Configuration #
This note records the convention of doing configuration for the system.

## Four Ways to do Configuration ##
By referencing [this post](https://hackernoon.com/4-ways-to-manage-the-configuration-in-python-4623049e841b), we know that there are four ways to do configuration. Including:

1. Using built-in data structure
2. Using external configuration file
3. Using environment variables
4. Using dynamic loading

By comparing the pros and cons, we choose the second way to do configuration for our system.

## Structure of Configuration Files ##

### localsettings.conf ###
This configuration file is located at the ``root`` directory of the project. Users of the program can do the following configuration in this file:

1. Database settings
2. Logger settings

