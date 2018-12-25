import project_root_directory
from wikiglass_analyzer.utilities.config_reader import ConfigReader

configreader = ConfigReader()
print(configreader.get('localsettings', 'LOGGER', 'logfile'))