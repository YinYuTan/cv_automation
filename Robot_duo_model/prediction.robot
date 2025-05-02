*** Settings ***
Library      SeleniumLibrary
Library      OperatingSystem
Library      Process
Library      Predict.py
Library      BlackWidow.py

*** Variables ***
${BATCH_SCRIPT}      video.bat
${MULTICLASS_MODEL_PATH}          ${EXECDIR}/models/multiclass_duo_model.h5
${DUO_MODEL_PATH}                ${EXECDIR}/models/binary_model.h5
${IMAGE_PATH}        pictures

*** Keywords ***
Set BlackWidow V4 Keyboard Chroma Green
    Perform Chroma Test BlackWidow V4 Green

Set BlackWidow V4 Keyboard Chroma Red
    Perform Chroma Test BlackWidow V4 Red

Set BlackWidow V4 Keyboard Chroma Pink
    Perform Chroma Test BlackWidow V4 Pink

Set BlackWidow V4 Keyboard Chroma White
    Perform Chroma Test BlackWidow V4 White

Set BlackWidow V4 Keyboard Chroma Cyan
    Perform Chroma Test BlackWidow V4 Cyan

Set BlackWidow V4 Keyboard Chroma Blue
    Perform Chroma Test BlackWidow V4 Blue

Set BlackWidow V4 Keyboard Chroma Orange
    Perform Chroma Test BlackWidow V4 Orange

Set BlackWidow V4 Keyboard Chroma Yellow
    Perform Chroma Test BlackWidow V4 Yellow

Check If Chroma Status Is Complete Green
    ${status}=    Run Keyword And Return Status    Check Status Green
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete Red
    ${status}=    Run Keyword And Return Status    Check Status Red
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete Pink
    ${status}=    Run Keyword And Return Status    Check Status Pink
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete White
    ${status}=    Run Keyword And Return Status    Check Status White
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete Cyan
    ${status}=    Run Keyword And Return Status    Check Status Cyan
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete Blue
    ${status}=    Run Keyword And Return Status    Check Status Blue
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete Orange
    ${status}=    Run Keyword And Return Status    Check Status Orange
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete Yellow
    ${status}=    Run Keyword And Return Status    Check Status Yellow
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Take Pictures Using Webcam
    Run Process		${CURDIR}/${BATCH_SCRIPT}
    Sleep    5s

Predict From Directory Green
    ${result}=    Predict Directory Colour   ${MULTICLASS_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}    green
    Should Be Equal    ${result}    PASS

Predict From Directory Red
    ${result}=    Predict Directory Colour     ${MULTICLASS_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}    red
    Should Be Equal    ${result}    PASS

Predict From Directory Pink
    ${result}=    Predict Directory Colour     ${MULTICLASS_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}    pink   
    Should Be Equal    ${result}    PASS

Predict From Directory White
    ${result}=    Predict Directory Colour     ${MULTICLASS_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}    white   
    Should Be Equal    ${result}    PASS

Predict From Directory Cyan
    ${result}=    Predict Directory Colour     ${MULTICLASS_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}    cyan   
    Should Be Equal    ${result}    PASS

Predict From Directory Blue
    ${result}=    Predict Directory Colour     ${MULTICLASS_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}    blue   
    Should Be Equal    ${result}    PASS
    
Predict From Directory Orange
    ${result}=    Predict Directory Colour     ${MULTICLASS_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}    orange   
    Should Be Equal    ${result}    PASS

Predict From Directory Yellow
    ${result}=    Predict Directory Colour    ${MULTICLASS_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}    yellow   
    Should Be Equal    ${result}    PASS

Predict from Directory Faulty
    ${result}=    Predict Directory Faulty     ${DUO_MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS

Move Image To Color Name
    [Arguments]    ${color}
    ${src}=    Set Variable    ${CURDIR}/${IMAGE_PATH}/photo.jpg
    ${dst}=    Set Variable    ${CURDIR}/${IMAGE_PATH}/${color}.jpg
    Move File    ${src}    ${dst}
    Set Suite Variable    ${IMAGE_FILE}    ${dst}

Log And Embed Image
    File Should Exist    ${IMAGE_FILE}
    Log Embedded Image   ${IMAGE_FILE}

Delete Image
    File Should Exist    ${IMAGE_FILE}
    Remove File          ${IMAGE_FILE}

*** Test Cases ***
Test Image Classification Green
    [Teardown]    Delete Image
    [Documentation]    Check static green or flag faulty
    Set BlackWidow V4 Keyboard Chroma Green
    Check If Chroma Status Is Complete Green
    Take Pictures Using Webcam
    Move Image To Color Name    green
    Log And Embed Image
    Predict From Directory Green
    Predict from Directory Faulty

Test Image Classification Red
    [Teardown]    Delete Image
    [Documentation]    Check static red or flag faulty
    Set BlackWidow V4 Keyboard Chroma Red
    Check If Chroma Status Is Complete Red
    Take Pictures Using Webcam
    Move Image To Color Name    red
    Log And Embed Image
    Predict From Directory Red
    Predict from Directory Faulty

Test Image Classification Pink
    [Teardown]    Delete Image
    [Documentation]    Check static pink or flag faulty
    Set BlackWidow V4 Keyboard Chroma Pink
    Check If Chroma Status Is Complete Pink
    Take Pictures Using Webcam
    Move Image To Color Name    pink
    Log And Embed Image
    Predict From Directory Pink
    Predict from Directory Faulty

Test Image Classification White
    [Teardown]    Delete Image
    [Documentation]    Check static white or flag faulty
    Set BlackWidow V4 Keyboard Chroma White
    Check If Chroma Status Is Complete White
    Take Pictures Using Webcam
    Move Image To Color Name    white
    Log And Embed Image
    Predict From Directory White
    Predict from Directory Faulty

Test Image Classification Cyan
    [Teardown]    Delete Image
    [Documentation]    Check static cyan or flag faulty
    Set BlackWidow V4 Keyboard Chroma Cyan
    Check If Chroma Status Is Complete Cyan
    Take Pictures Using Webcam
    Move Image To Color Name    cyan
    Log And Embed Image
    Predict From Directory Cyan
    Predict from Directory Faulty

Test Image Classification Blue
    [Teardown]    Delete Image
    [Documentation]    Check static blue or flag faulty
    Set BlackWidow V4 Keyboard Chroma Blue
    Check If Chroma Status Is Complete Blue
    Take Pictures Using Webcam
    Move Image To Color Name    blue
    Log And Embed Image
    Predict From Directory Blue
    Predict from Directory Faulty

Test Image Classification Orange
    [Teardown]    Delete Image
    [Documentation]    Check static orange or flag faulty
    Set BlackWidow V4 Keyboard Chroma Orange
    Check If Chroma Status Is Complete Orange
    Take Pictures Using Webcam
    Move Image To Color Name    orange
    Log And Embed Image
    Predict From Directory Orange
    Predict from Directory Faulty

Test Image Classification Yellow
    [Teardown]    Delete Image
    [Documentation]    Check static yellow or flag faulty
    Set BlackWidow V4 Keyboard Chroma Yellow
    Check If Chroma Status Is Complete Yellow
    Take Pictures Using Webcam
    Move Image To Color Name    yellow
    Log And Embed Image
    Predict From Directory Yellow
    Predict from Directory Faulty

Test Image Faulty Scenario (Indiv)
    [Documentation]    Check static yellow or flag faulty
    Predict From Directory Yellow
    Predict from Directory Faulty