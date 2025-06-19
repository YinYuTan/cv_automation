*** Settings ***
Library      SeleniumLibrary
Library      OperatingSystem
Library      Process
Library      Predict.py
Library      BlackWidow.py

*** Variables ***
${BATCH_SCRIPT}      video.bat
${VIDEO_PATH}        video

*** Keywords ***
Set BlackWidow V4 Keyboard Chroma Spectrum
    Perform Chroma Test BlackWidow V4 Spectrum

Set BlackWidow V4 Keyboard Chroma Wave
    Perform Chroma Test BlackWidow V4 Wave

Set BlackWidow V4 Keyboard Chroma Starlight
    Perform Chroma Test BlackWidow V4 Starlight

Check If Chroma Status Is Complete Spectrum
    ${status}=    Run Keyword And Return Status    Check Status Spectrum
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete Wave
    ${status}=    Run Keyword And Return Status    Check Status Wave
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Check If Chroma Status Is Complete Starlight
    ${status}=    Run Keyword And Return Status    Check Status Starlight
    Should Be True    ${status}    msg=Chroma Setup Incomplete.

Take Video Using Webcam
    Run Process		${CURDIR}/${BATCH_SCRIPT}
    Sleep    5s

Predict From Directory Spectrum
    ${result}=    Predict Directory Spectrum   ${CURDIR}/${VIDEO_PATH}   
    Should Be Equal    ${result}    PASS

Predict From Directory Wave
    ${result}=    Predict Directory Wave   ${CURDIR}/${VIDEO_PATH}   
    Should Be Equal    ${result}    PASS

Predict From Directory Starlight
    ${result}=    Predict Directory Starlight   ${CURDIR}/${VIDEO_PATH}   
    Should Be Equal    ${result}    PASS

Move Video To Class Name
    [Arguments]    ${class}
    ${src}=    Set Variable    ${CURDIR}/${VIDEO_PATH}/recording.mp4
    ${dst}=    Set Variable    ${CURDIR}/${VIDEO_PATH}/${class}.mp4
    Run Keyword And Continue On Failure    File Should Exist    ${src}
    Move File    ${src}    ${dst}
    Set Test Variable     ${VIDEO_FILE}    ${dst}

Log And Embed Frame
    File Should Exist    ${VIDEO_FILE}
    Log Embedded Frame   ${VIDEO_FILE}

List Image Folder
    ${files}=    List Files In Directory    ${CURDIR}/${VIDEO_PATH}
    Log Many     Found image files:    ${files}

Delete Video
    Run Keyword And Ignore Error    File Should Exist    ${VIDEO_FILE}
    Run Keyword And Ignore Error    Remove File          ${VIDEO_FILE}

*** Test Cases ***
Test Image Classification Spectrum
    [Teardown]    Delete Video
    [Documentation]    Check spectrum
    Set BlackWidow V4 Keyboard Chroma Spectrum
    Check If Chroma Status Is Complete Spectrum
    Take Video Using Webcam
    Move Video To Class Name    spectrum
    List Image Folder
    Log And Embed Frame
    Predict From Directory Spectrum

Test Image Classification Wave
    [Teardown]    Delete Video
    [Documentation]    Check wave
    Set BlackWidow V4 Keyboard Chroma Wave
    Check If Chroma Status Is Complete Wave
    Take Video Using Webcam
    Move Video To Class Name    wave
    List Image Folder
    Log And Embed Frame
    Predict From Directory Wave

Test Image Classification Starlight
    [Teardown]    Delete Video
    [Documentation]    Check starlight
    Set BlackWidow V4 Keyboard Chroma Starlight
    Check If Chroma Status Is Complete Starlight
    Take Video Using Webcam
    Move Video To Class Name    starlight
    List Image Folder
    Log And Embed Frame
    Predict From Directory Starlight


# Test Image Faulty Scenario
#     [Documentation]    Check faulty
#     Move Video To Class Name    faulty
#     Log And Embed Frame
#     Predict From Directory Starlight

# Test Image Blade Scenario
#     [Documentation]    Check blade
#     Move Video To Class Name    blade
#     Log And Embed Frame
#     Predict From Directory Wave

Test Image Classification Starlight (Faulty scenario)
    [Teardown]    Delete Video
    [Documentation]    Check starlight
    Set BlackWidow V4 Keyboard Chroma Starlight
    Check If Chroma Status Is Complete Starlight
    Take Video Using Webcam
    Move Video To Class Name    starlight
    List Image Folder
    Log And Embed Frame
    Predict From Directory Starlight