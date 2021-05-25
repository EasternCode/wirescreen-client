![alt text](logo.png)
---------------------------------------------------------------------------------------------------
`wirescreen-api` is a custom client written to interact with the API which supports
 https://wirescreen.ai.
 
 The below document shows to use Python version of this client.

## Initializing the client
The client token can be declared as a variable and passed directly to the client.
```python
from python.client import WireScreenAPI

host = "https://sample.host"
token = "sample_token_value"
client = WireScreenAPI(host, token)
```
Or the token can be set as an environment variable.
```Python
import os

from python.client import WireScreenAPI

host = "https://sample.host"
os.environ["WIRESCREEN_API_TOKEN"] = "sample_token_value"
client = WireScreenAPI(host)
```

## Search
Conducts a general search for both organizations and people. Search results are returned in descending order based on a
similarity ranking relative to the search term provided.
```python
from python.client import WireScreenAPI

host = "https://sample.host"
token = "sample_token_value"

client = WireScreenAPI(host, token)

client.search("Alibaba")

# You can limit the number of results returned by providing a limit.
client.search("Alibaba", 1)
```
### Advanced Search
Conducts an advanced search for organizations.
Available parameters include:
- `limit_to_public` (Boolean): Should only public (listed) companies be returned?
- `limit_to_government` (Boolean): Should only government companies be returned?
- `limit_to_operating` (Boolean): Should only companies which are currently operating be returned?
- `region` (String): A region to search for companies within.

All parameters are optional.
```python
from python.client import WireScreenAPI

host = "https://sample.host"
token = "sample_token_value"

client = WireScreenAPI(host, token)

# By adding limit_to_public=True when searching for a listed company,
# we can cut down on the number of results returned.
client.advanced_search("ZTE", limit_to_public=True)

# By adding region, we can subset the the search results even further.
client.advanced_search("ZTE", limit_to_public=True, region="Guangdong")
```

## Organization Data
To retrieve data for a specific organization, we can provide the company's unique identifier to the client's
`get_organization` method. Have multiple companies you wish to see? Use the `get_organizations` method to
 retrieve data on multiple organizations.
 ```python
from uuid import UUID

from python.client import WireScreenAPI

host = "https://sample.host"
token = "sample_token_value"

client = WireScreenAPI(host, token)

organization_uuid = UUID('ba1251e0-8cd8-5b6b-bf9c-9d56634efff4')
client.get_organization(organization_uuid)

organization_uuids = [UUID('362d51d5-633a-4c01-ac8e-c58157ce6990'), UUID('72cf9dc2-aa47-4def-8a2a-184071aec937')]
client.get_organizations(organization_uuids)
 ```

## Person Data
To retrieve data for a specific person, we can provide the person's unique identifier to the client's
`get_person` method. Have multiple persons you wish to see? Use the `get_persons` method to
 retrieve data on multiple persons.
 ```python
from uuid import UUID

from python.client import WireScreenAPI

host = "https://sample.host"
token = "sample_token_value"

client = WireScreenAPI(host, token)

person_uuid = UUID('3e4558de-da72-43d3-a5c1-a4d0d2b28d95')
client.get_person(person_uuid)

person_uuids = [UUID('3e4558de-da72-43d3-a5c1-a4d0d2b28d95'), UUID('49ee3434-2d21-4461-88d8-d405b7d8dbb3')]
client.get_persons(person_uuids)
 ```

# Endpoints
If you wish to interact with the WireScreen API using other programming languages or methods, please find a full list
of available endpoints below. They can be queried using any method, as long as proper authentication is provided.

| Endpoint Name   |                          Path                         |      Method       |
| --------------- |:-----------------------------------------------------:| -----------------:|
| Search          |                    /rest/search/search                |        GET        |
| Advanced Search |                    /rest/search/advancedsearch        |        POST       |
| Organization    |                    /rest/data/organization            |        GET        |
| Organizations   |                    /rest/data/organizations           |        POST       |
| Person          |                    /rest/data/person                  |        GET        |
| Persons         |                    /rest/data/persons                 |        POST       |