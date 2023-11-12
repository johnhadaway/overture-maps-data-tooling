class S3Utils:
    @staticmethod
    def construct_s3_path(release_version, theme):
        return f's3://overturemaps-us-west-2/release/{release_version}/theme={theme}/type=*/*'