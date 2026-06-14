results = [
    "Test_1 PASSED",
    "Test_2 FAILED",
    "Test_3 PASSED",
    "Test_4 PASSED",
    "Test_5 FAILED",
    "Test_6 PASSED",
    "Test_7 PASSED",
    "Test_8 FAILED",
    "Test_9 PASSED",
    "Test_10 PASSED"
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