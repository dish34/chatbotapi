# from ibm_watson import AssistantV2
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# authenticator = IAMAuthenticator('vKtBA34hgQcdZ824fGMVskfEbWVr5EZ925wKYecxOOYf')
# assistant = AssistantV2(
#     version='v2',
#     authenticator=authenticator
# )

# assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com')
# assistant.set_disable_ssl_verification(True)
# from ibm_watson import ApiException
# try:
#     # Invoke a Watson Assistant method
#     response = assistant.methodName(parameters,headers = { 'Custom-Header': '{header_value}'})
#     assistant.set_detailed_response(True)
#     response = assistant.methodName(parameters)
#     # Access response from methodName
#     print(json.dumps(response.get_result(), indent=2))
#     # Access information in response headers
#     print(response.get_headers())
#     # Access HTTP response status
#     print(response.get_status_code())

# except ApiException as ex:
#     print("Method failed with status code" + str(ex.code) + ": " + ex.message)

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('vKtBA34hgQcdZ824fGMVskfEbWVr5EZ925wKYecxOOYf')
assistant = AssistantV2(
    version='2019-02-28',
    authenticator = authenticator
)

assistant.set_service_url('https://api.us-east.assistant.watson.cloud.ibm.com')
from ibm_watson import ApiException
# try:
response = assistant.message(
        assistant_id='12595fe8-12b9-438a-b109-661346b6b220',
        session_id='1',
        input={
            'message_type': 'text',
            'text': 'Hello'
        }
    ).get_result()
# except ApiException as ex:
#      print("Method failed with status code " + str(ex.code) + ": " + ex.message)

print(json.dumps(response, indent=2))