import json

SELECT_CONFIG_PATH = "config.json"

class ConfigLoader:
    @staticmethod
    def load_select_config(theme, data_type=None):
        with open(SELECT_CONFIG_PATH, 'r') as config_file:
            config = json.load(config_file)
            
            theme_config = config.get(theme, None)
            if theme_config is None:
                raise ValueError(f"No configuration found for theme '{theme}'")
            
            if data_type and isinstance(theme_config, dict) and data_type in theme_config:
                type_config = theme_config[data_type]
                return type_config["SELECT"], type_config["GEOMETRIES"]
            elif not data_type or not isinstance(theme_config, dict):
                return theme_config["SELECT"], theme_config["GEOMETRIES"]
            else:
                raise ValueError(f"No configuration found for type '{data_type}' under theme '{theme}'")