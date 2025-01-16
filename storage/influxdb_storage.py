from influxdb_client import InfluxDBClient, Point, WriteOptions

class InfluxDBStorage:
    def __init__(self, url, token, org, bucket):
        """
        Initialize the InfluxDBStorage class.
        :param url: InfluxDB server URL.
        :param token: InfluxDB authentication token.
        :param org: Organization name in InfluxDB.
        :param bucket: Bucket name in InfluxDB.
        """
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.bucket = bucket
        self.org = org
        self.write_api = self.client.write_api(write_options=WriteOptions(batch_size=1))

    def store_measurement(self, measurement_name, value):
        """
        Store a measurement in InfluxDB.
        :param measurement_name: The name of the measurement (e.g., 'voltage').
        :param value: The value of the measurement.
        """
        point = Point(measurement_name).field("value", value)
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)

    def close(self):
        """
        Close the InfluxDB client connection.
        """
        if self.client:
            self.client.close()
