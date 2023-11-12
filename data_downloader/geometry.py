class Geometry:
    @staticmethod
    def construct_polygon(sw_lat, sw_lon, ne_lat, ne_lon):
        return f"POLYGON(({sw_lon} {sw_lat}, {sw_lon} {ne_lat}, {ne_lon} {ne_lat}, {ne_lon} {sw_lat}, {sw_lon} {sw_lat}))"