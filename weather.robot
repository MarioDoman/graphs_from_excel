*** Settings ***
Library  Collections
Library  String
Library  RequestsLibrary


*** Test Cases ***

Get Request ${HTTP_LOCAL_SERVER}/persons
    [Tags]  get
    ${resp}=            GET  ${HTTP_LOCAL_SERVER}/persons
    Status Should Be    OK  ${resp}

Get Request on ${HTTP_LOCAL_SERVER}/persons/person1
    [Tags]    get
    ${resp}=    GET    ${HTTP_LOCAL_SERVER}/persons/person1
    Should Be Equal As Strings    ${resp.json()}    {'name': 'Mario', 'surname': 'Doman', 'height': 198, 'age': 40}

Put Request on ${HTTP_LOCAL_SERVER}/persons/person1
    ${resp} = 	Run Process 	curl    -X    PUT    -d    name\=Testname    -d    surname\=TestSurname    -d    height\=150    -d    age\=11    ${HTTP_LOCAL_SERVER}/persons/person1
    Should Be Equal 	${resp.stdout}    {"name": "Testname", "surname": "TestSurname", "height": 150, "age": 11} 	

Delete Request on ${HTTP_LOCAL_SERVER}/persons/person1
    ${resp}= 	Run Process 	curl    -X    DELETE        ${HTTP_LOCAL_SERVER}/persons/person1
    Should Be Equal    204    ${resp.stdout}	

POST Request on ${HTTP_LOCAL_SERVER}/persons
    ${resp}= 	Run Process 	curl    -X    POST    -d    name\=Testname    -d    surname\=TestSurname    -d    height\=150    -d    age\=11        ${HTTP_LOCAL_SERVER}/persons
    Should Be Equal    {"name": "Testname", "surname": "TestSurname", "height": 150, "age": 11}    ${resp.stdout}	

