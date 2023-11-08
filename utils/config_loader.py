import json

SELECT_CONFIG_PATH = "config.json"

class ConfigLoader:
    @staticmethod
    def load_select_config(theme):
        with open(SELECT_CONFIG_PATH, 'r') as config_file:
            config = json.load(config_file)
            theme_config = config.get(theme, None)
            if theme_config is None:
                raise ValueError(f"No configuration found for theme '{theme}'")
            return theme_config["SELECT"], theme_config["GEOMETRIES"]