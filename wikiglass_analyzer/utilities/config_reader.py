import configparser
import sys, os
import errno

class ConfigReader:
    def __init__(self):
        self.configurations = {}
        self._load_all_config_files()
        
    ##### APIs #####
    def get(self, filename, section, key):
        '''Return the corresponding configuration settings
        Parameters
        -----------
            :filename The same as that is specified in localsetting.ini's CONFIGURATION_PATH
            section
            :section Section in a .ini file
            :key Key of an item inside a section

        Examples
        ---------
            If I want to get the host name of wikiglass database,
            I should do this::

                configreader = ConfigReader()
                print(configreader.get('localsettings', 'WIKIGLASS_DB', 'db_host'))

        '''
        try:
            if filename in self.configurations and self.configurations[filename].has_option(section, key):
                return self.configurations[filename][section][key]
            else:
                raise KeyError("KeyError: Option does not exist in configuration file-->{}, section-->{}".format(filename, section))
        except KeyError as keyerr:
            print(keyerr)


    ##### Implementation Components #####
    # Implement singleton pattern
    def __new__(cls):
        if not hasattr(ConfigReader, "_instance"):
            ConfigReader._instance = object.__new__(cls)
        return ConfigReader._instance
        
    def _load_all_config_files(self):
        '''Load all configuration files from filesystem
        This function will load the localsettings.ini first.
        Then, it will automatically load other configuration files
        that are specified in localsetting.ini's [CONFIGURATION_PATH]
        section.
        Note: The environment variable WIKIGLASS_LOCALSETTINGS_PATH
        must be set.
        '''
        #Find the root directory of wikiglass analyzer
        env_localsettings_path = os.environ.get('WIKIGLASS_LOCALSETTINGS_PATH', None)
        if not env_localsettings_path:
            raise ValueError('You must have the WIKIGLASS_LOCALSETTINGS environment variable set')

        #Load localsettings.ini
        localsettings_config = self._load_config_file(env_localsettings_path)
        self.configurations['localsettings'] = localsettings_config

        #Load other configuration files
        if localsettings_config.has_section('CONFIGURATION_PATH'):
            for (each_key, each_config_path) in localsettings_config.items('CONFIGURATION_PATH'):
                    self.configurations[each_key] = self._load_config_file(each_config_path)


    def _load_config_file(self, configuration_path)->configparser.ConfigParser:
        '''Helper of _load_all_config_files()
        Loading a single configuration file from filesystem
        '''
        config = configparser.ConfigParser()
        #Check whether the file exist
        try:
            if os.path.isfile(configuration_path):
                config.read(configuration_path)
                return config
            else: 
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), configuration_path)
        except FileNotFoundError as fnf_error:
            print(fnf_error)
