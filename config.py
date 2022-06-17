import yaml
import constant as const


class Config:

    def __init__(self):
        with open(const.CONFIG_YAML) as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
        self.config = config

        self.TSP_INST_URL = config[const.TSP_INST_URL]
        self.TSP_INST_USED = config[const.TSP_INST_USED]

        # print(config)
        # print(const.TSP_INST_URL)
        # print(config.TSP_INST_URL)
        # print(config.TSP_INST_USED)