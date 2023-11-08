import duckdb
from .config_loader import ConfigLoader
from .s3_utils import S3Utils
from .geometry import Geometry

class DataDownloader:
    def __init__(self, theme, release_version, output_file, sw_lat, sw_lon, ne_lat, ne_lon):
        self.theme = theme
        self.release_version = release_version
        self.output_file = output_file
        self.sw_lat = sw_lat
        self.sw_lon = sw_lon
        self.ne_lat = ne_lat
        self.ne_lon = ne_lon

    def download_data(self):
        con = duckdb.connect(database=':memory:', read_only=False)
        con.execute("LOAD spatial")
        con.execute("LOAD https")
        con.execute("SET s3_region='us-west-2'")
        con.execute("SET enable_progress_bar=true")

        s3_path = S3Utils.construct_s3_path(self.release_version, self.theme)
        select_portion, geometries = ConfigLoader.load_select_config(self.theme)
        geometries_in_clause = ", ".join(f"'{geom}'" for geom in geometries)
        polygon_coords = Geometry.construct_polygon(self.sw_lat, self.sw_lon, self.ne_lat, self.ne_lon)

        sql_query = f"""
        COPY (
            SELECT
                {select_portion}
            FROM read_parquet('{s3_path}', filename=true, hive_partitioning=1)
            WHERE ST_GeometryType(ST_GeomFromWkb(geometry)) IN ({geometries_in_clause})
                AND ST_Intersects(
                    ST_GeomFromWkb(geometry),
                    ST_GeomFromText('{polygon_coords}')
                )
        ) TO '{self.output_file}'
        WITH (FORMAT GDAL, DRIVER 'GeoJSON');
        """

        con.execute(sql_query)
        con.close()

        print(f"Data downloaded to {self.output_file}")