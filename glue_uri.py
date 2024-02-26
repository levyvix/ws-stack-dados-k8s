import boto3

# get glue uri
# Create Glue client
glue_client = boto3.client('glue', region_name='us-east-1')

response = glue_client.get_connection(
    Name='string',
    HidePassword=True|False
)