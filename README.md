```
global-testing on  master via global-testing took 4s 
➜ pytest                               
=========================================== test session starts ============================================
platform darwin -- Python 3.8.5, pytest-6.0.1, py-1.9.0, pluggy-0.13.1
rootdir: /Users/ph/workspace/playground/global-testing
collected 6 items                                                                                          

tests/services/srva/test_hello.py ..                                                                 [ 33%]
tests/services/srvb/test_common_interaction.py .                                                     [ 50%]
tests/services/srvb/test_goodbye.py .                                                                [ 66%]
tests/tools/tool1/test_tool_one.py .                                                                 [ 83%]
tests/tools/tool2/test_tool_two.py .                                                                 [100%]

============================================ 6 passed in 0.05s =============================================
```