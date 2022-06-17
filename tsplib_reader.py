import config as cfg

class ReadTSPlib:

    def __init__(self, config=cfg.Config()):
        self.path = config.TSP_INST_URL
        self.instances = config.TSP_INST_USED

        self.distance_formula_dict = {
            'EUC_2D': self.distance_euc,
            'ATT': self.distance_att,
            'GEO': self.distance_geo
        }
    
    @staticmethod
    def distance_euc(zi, zj):
        delta_x = zi[0] - zj[0]
        delta_y = zi[1] - zj[1]
        return round(np.sqrt(delta_x ** 2 + delta_y ** 2), 0)

    @staticmethod
    def distance_att(zi, zj):
        delta_x = zi[0] - zj[0]
        delta_y = zi[1] - zj[1]
        rij = np.sqrt((delta_x ** 2 + delta_y ** 2) / 10.0)
        tij = float(rij)
        if tij < rij:
            dij = tij + 1
        else:
            dij = tij
        return dij

    @staticmethod
    def distance_geo(zi, zj):
        RRR = 6378.388
        lat_i, lon_i = ReadTSPlib.get_lat_long(zi)
        lat_j, lon_j = ReadTSPlib.get_lat_long(zj)
        q1 = np.cos(lon_i - lon_j)
        q2 = np.cos(lat_i - lat_j)
        q3 = np.cos(lat_i + lat_j)
        return float(RRR * np.arccos(0.5 * ((1.0 + q1) * q2 - (1.0 - q1) * q3)) + 1.0)
