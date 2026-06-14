# qa-test-results-dashboard
Python script that analyzes QA test results, calculates pass rate, and identifies failed tests

# QA Test Results Dashboard
A Python script that analyzes QA test results, calculates pass 
rate, and identifies all failed tests.

## Why I built this
As I transition into QA Engineering, one of the first things 
I wanted to understand is how engineers track quality across 
a test suite. Every time a product ships whether it's a 
Bluetooth headphone, an iOS app, or a wireless device, someone 
needs to know: how many tests ran, how many passed, and exactly 
which ones failed.

Without a clear summary, engineers waste time digging through 
raw logs to find the failures. This script solves that by 
turning a raw list of test results into a clean, readable 
dashboard in seconds.

## What it does
- Reads a list of test results
- Counts total, passed, and failed tests
- Calculates pass rate percentage
- Prints a formatted dashboard
- Lists all failed tests

## Sample Output
```
===== TEST RESULTS DASHBOARD =====
Total Tests:        10
Passed:             7
Failed:             3
Pass Rate:          70.0%
==================================

FAILED TESTS:
Test_2 FAILED Bluetooth
Test_5 FAILED Audio
Test_8 FAILED Firmware

RESULTS BY CATEGORY:
Bluetooth           1 passed  1 failed
Audio               2 passed  1 failed
Firmware            2 passed  1 failed
Pairing             2 passed  0 failed
```
## Skills used
Python • Lists • Loops • f-strings • Basic math
