import argparse
from data_downloader.data_downloader import DataDownloader

def main():
    parser = argparse.ArgumentParser(description='Download data from Overture Maps.')
    parser.add_argument('--theme', type=str, required=True, help='The theme of the data to download.')
    parser.add_argument('--release_version', type=str, required=True, help='The release version of the dataset.')
    parser.add_argument('--output_file', type=str, required=True, help='The output file path.')
    parser.add_argument('--sw_lat', type=float, required=True, help='The southwest latitude of the bounding box.')
    parser.add_argument('--sw_lon', type=float, required=True, help='The southwest longitude of the bounding box.')
    parser.add_argument('--ne_lat', type=float, required=True, help='The northeast latitude of the bounding box.')
    parser.add_argument('--ne_lon', type=float, required=True, help='The northeast longitude of the bounding box.')
    parser.add_argument('--type', type=str, required=False, help='The type of the data to download (e.g., locality, administrativeBoundary).')
    parser.add_argument('--admin_level', type=int, required=False, help='The administrative level to filter by.')

    args = parser.parse_args()

    downloader = DataDownloader(args.theme, args.release_version, args.output_file, args.sw_lat, args.sw_lon, args.ne_lat, args.ne_lon, data_type=args.type)
    downloader.download_data()

if __name__ == '__main__':
    main()