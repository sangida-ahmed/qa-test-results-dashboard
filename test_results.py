results = [
    "Test_1 PASSED Bluetooth",
    "Test_2 FAILED Bluetooth",
    "Test_3 PASSED Audio",
    "Test_4 PASSED Audio",
    "Test_5 FAILED Audio",
    "Test_6 PASSED Firmware",
    "Test_7 PASSED Firmware",
    "Test_8 FAILED Firmware",
    "Test_9 PASSED Pairing",
    "Test_10 PASSED Pairing"
]

total = len(results)
passed = 0
failed = 0

for result in results:
    if "PASSED" in result:
        passed += 1
    else:
        failed += 1

pass_rate = (passed / total) * 100

print("===== TEST RESULTS DASHBOARD =====")
print(f"Total Tests:        {total}")
print(f"Passed:             {passed}")
print(f"Failed:             {failed}")
print(f"Pass Rate:          {pass_rate:.1f}%")
print("==================================")
print()
print("FAILED TESTS:")
for result in results:
    if "FAILED" in result:
        print(result)


# Count results by category
categories = {}

for result in results:
    parts = result.split()
    status = parts[1]
    category = parts[2]
    
    if category not in categories:
        categories[category] = {"passed": 0, "failed": 0}
    
    if status == "PASSED":
        categories[category]["passed"] += 1
    else:
        categories[category]["failed"] += 1

print()
print("RESULTS BY CATEGORY:")
for category, counts in categories.items():
    print(f"{category:<20}{counts['passed']} passed  {counts['failed']} failed")