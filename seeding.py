from google.cloud import bigtable
from google.cloud.bigtable import column_family
from google.cloud.bigtable import row_filters
import random
import string
from datetime import datetime, timedelta

# Constants, replace with your values
PROJECT_ID = 'example'
INSTANCE_ID = 'example'
TABLE_ID = 'example'
COLUMN_FAMILY_ID = 'riverdata'

# Constants for the river monitoring data
RIVERS = ['Mississippi', 'Amazon', 'Nile', 'Yangtze', 'Mekong']

# Creating the Bigtable client
client = bigtable.Client(project=PROJECT_ID, admin=True)

# Connecting to the Bigtable instance
instance = client.instance(INSTANCE_ID)

# Creating the table object
table = instance.table(TABLE_ID)

# Check if table exists
if not table.exists():
    print("Creating table: {}".format(TABLE_ID))
    # Creating column family
    table.create(column_families={
        COLUMN_FAMILY_ID: column_family.MaxVersionsGCRule(2)
    })

# Function to generate random river data
def random_river_data():
    river = random.choice(RIVERS)
    time = datetime.now() - timedelta(days=random.randint(1, 365))
    water_level = random.uniform(0.0, 30.0)
    temperature = random.uniform(0.0, 35.0)

    return river, time.isoformat(), water_level, temperature

# Loading data into BigTable
print("Loading data into BigTable")
for i in range(100):  # for example, loading 100 rows
    row_key = 'event{}'.format(i)
    river, time, water_level, temperature = random_river_data()
    row = table.row(row_key)
    row.set_cell(COLUMN_FAMILY_ID, 'river', river)
    row.set_cell(COLUMN_FAMILY_ID, 'time', time)
    row.set_cell(COLUMN_FAMILY_ID, 'water_level', str(water_level))
    row.set_cell(COLUMN_FAMILY_ID, 'temperature', str(temperature))
    row.commit()


print("Data loaded successfully")
