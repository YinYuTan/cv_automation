*** Settings ***
Library      SeleniumLibrary
Library      OperatingSystem
Library      Process
Library      Predict.py
Library      BlackWidow.py

*** Variables ***
${BATCH_SCRIPT}      video.bat
${MODEL_PATH}        cv-dentrite\models\image_multiclass_model.h5
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
    ${result}=    Predict Directory Green   ${CURDIR}/${MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS

Predict From Directory Red
    ${result}=    Predict Directory Red     ${CURDIR}/${MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS

Predict From Directory Pink
    ${result}=    Predict Directory Pink     ${CURDIR}/${MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS

Predict From Directory White
    ${result}=    Predict Directory White     ${CURDIR}/${MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS

Predict From Directory Cyan
    ${result}=    Predict Directory Cyan     ${CURDIR}/${MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS

Predict From Directory Blue
    ${result}=    Predict Directory Blue     ${CURDIR}/${MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS
    
Predict From Directory Orange
    ${result}=    Predict Directory Orange     ${CURDIR}/${MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS

Predict From Directory Yellow
    ${result}=    Predict Directory Yellow     ${CURDIR}/${MODEL_PATH}    ${CURDIR}/${IMAGE_PATH}   
    Should Be Equal    ${result}    PASS


*** Test Cases ***
Test Image Classification Green
    [Documentation]    Check static green or flag faulty
    Set BlackWidow V4 Keyboard Chroma Green
    Check If Chroma Status Is Complete Green
    Take Pictures Using Webcam
    Predict From Directory Green

Test Image Classification Red
    [Documentation]    Check static red or flag faulty
    Set BlackWidow V4 Keyboard Chroma Red
    Check If Chroma Status Is Complete Red
    Take Pictures Using Webcam
    Predict From Directory Red

Test Image Classification Pink
    [Documentation]    Check static pink or flag faulty
    Set BlackWidow V4 Keyboard Chroma Pink
    Check If Chroma Status Is Complete Pink
    Take Pictures Using Webcam
    Predict From Directory Pink

Test Image Classification White
    [Documentation]    Check static white or flag faulty
    Set BlackWidow V4 Keyboard Chroma White
    Check If Chroma Status Is Complete White
    Take Pictures Using Webcam
    Predict From Directory White

Test Image Classification Cyan
    [Documentation]    Check static cyan or flag faulty
    Set BlackWidow V4 Keyboard Chroma Cyan
    Check If Chroma Status Is Complete Cyan
    Take Pictures Using Webcam
    Predict From Directory Cyan

Test Image Classification Blue
    [Documentation]    Check static blue or flag faulty
    Set BlackWidow V4 Keyboard Chroma Blue
    Check If Chroma Status Is Complete Blue
    Take Pictures Using Webcam
    Predict From Directory Blue

Test Image Classification Orange
    [Documentation]    Check static orange or flag faulty
    Set BlackWidow V4 Keyboard Chroma Orange
    Check If Chroma Status Is Complete Orange
    Take Pictures Using Webcam
    Predict From Directory Orange

Test Image Classification Yellow
    [Documentation]    Check static yellow or flag faulty
    Set BlackWidow V4 Keyboard Chroma Yellow
    Check If Chroma Status Is Complete Yellow
    Take Pictures Using Webcam
    Predict From Directory Yellow

