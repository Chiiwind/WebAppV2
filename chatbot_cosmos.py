import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import config
from azure.cosmos import CosmosClient
import uuid

# Configuration
HOST = config.settings['host']
MASTER_KEY = config.settings['master_key']
DATABASE_ID = config.settings['database_id']
CONTAINER_ID = config.settings['container_id']

# Initialize the Cosmos client
client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})
database = client.get_database_client(DATABASE_ID)
container = database.get_container_client(CONTAINER_ID)

def create_item(container, item):
    try:
        container.create_item(body=item)
        print("Item created successfully!")
    except exceptions.CosmosHttpResponseError as e:
        print(f"Failed to create item: {e}")

def handle_user_input(name, company, email, phone):
    # Create a new item
    item = {
        'id': str(uuid.uuid4()),
        'name': name,
        'company': company,
        'email': email,
        'phone': phone
    }

    # Store the item in the specified container
    create_item(container, item)
    print("User data stored successfully!")