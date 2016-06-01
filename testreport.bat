cd "TestSuites"
python Test1_test.py  >..\Batch_results.txt 2>&1
cd ..
java -jar "unitth.jar" "TestSuites\test-reports"
pause