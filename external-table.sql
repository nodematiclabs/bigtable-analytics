CREATE EXTERNAL TABLE demonstration.BigtableTable
OPTIONS (
  format = 'CLOUD_BIGTABLE',
  uris = ['https://googleapis.com/bigtable/projects/example/instances/example/tables/example'],
  bigtable_options =
    """
    {
      columnFamilies: [
        {
          "familyId": "riverdata",
          "columns": [
            {
              "qualifierString": "river",
              "type": "STRING"
            },
            {
              "qualifierString": "time",
              "type": "STRING"
            },
            {
              "qualifierString": "water_level",
              "type": "STRING"
            },
            {
              "qualifierString": "temperature",
              "type": "STRING"
            }
          ]
        }
      ],
      readRowkeyAsString: true
    }
    """
);