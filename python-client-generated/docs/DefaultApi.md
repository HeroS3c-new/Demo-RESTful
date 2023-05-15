# swagger_client.DefaultApi

All URIs are relative to *https://f411-145-224-104-33.ngrok.io/corsi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**corsi_corso_id_delete**](DefaultApi.md#corsi_corso_id_delete) | **DELETE** /corsi/{corso_id} | Elimina un corso esistente
[**corsi_corso_id_get**](DefaultApi.md#corsi_corso_id_get) | **GET** /corsi/{corso_id} | Restituisce un corso specifico
[**corsi_corso_id_put**](DefaultApi.md#corsi_corso_id_put) | **PUT** /corsi/{corso_id} | Aggiorna un corso esistente
[**corsi_get**](DefaultApi.md#corsi_get) | **GET** /corsi | Restituisce tutti i corsi
[**corsi_post**](DefaultApi.md#corsi_post) | **POST** /corsi | Crea un nuovo corso

# **corsi_corso_id_delete**
> corsi_corso_id_delete(corso_id)

Elimina un corso esistente

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
corso_id = 56 # int | 

try:
    # Elimina un corso esistente
    api_instance.corsi_corso_id_delete(corso_id)
except ApiException as e:
    print("Exception when calling DefaultApi->corsi_corso_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corso_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corsi_corso_id_get**
> InlineResponse200 corsi_corso_id_get(corso_id)

Restituisce un corso specifico

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
corso_id = 56 # int | 

try:
    # Restituisce un corso specifico
    api_response = api_instance.corsi_corso_id_get(corso_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->corsi_corso_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **corso_id** | **int**|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corsi_corso_id_put**
> InlineResponse2001 corsi_corso_id_put(body, corso_id)

Aggiorna un corso esistente

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.CorsiCorsoIdBody() # CorsiCorsoIdBody | 
corso_id = 56 # int | 

try:
    # Aggiorna un corso esistente
    api_response = api_instance.corsi_corso_id_put(body, corso_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->corsi_corso_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CorsiCorsoIdBody**](CorsiCorsoIdBody.md)|  | 
 **corso_id** | **int**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corsi_get**
> list[InlineResponse200] corsi_get()

Restituisce tutti i corsi

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Restituisce tutti i corsi
    api_response = api_instance.corsi_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->corsi_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **corsi_post**
> InlineResponse200 corsi_post(body)

Crea un nuovo corso

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.CorsiBody() # CorsiBody | 

try:
    # Crea un nuovo corso
    api_response = api_instance.corsi_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->corsi_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CorsiBody**](CorsiBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

