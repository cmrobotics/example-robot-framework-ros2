*** Settings ***
Library         ../translations/DummyTranslation.py
Force Tags      critical

*** Variables ***
${num_a}        3
${num_b}        7
${product_ab}   21

*** Test Cases ***
Check the product of two numbers
    [Documentation]     This dummy test case confirms that the product of two numbers
    ...                 yields the expected result. Besides, it also shows you that
    ...                 documentation supports HTML formatting such as *bold text* and
    ...                 [https://www.youtube.com/watch?v=lXMskKTw3Bc|link with custom text]

    Given confirm the product of      ${num_a}    ${num_b}    ${product_ab}
    When confirm the product of         1   2   2
    Then confirm the product of is not     2   3   90
