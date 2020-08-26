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

## Tree structure

```
.
├── README.md
├── __init__.py
├── setup.py
├── requirements.txt
├── libraries
│   ├── __init__.py
│   └── common
│       ├── __init__.py
│       └── name_capitalize.py
├── services
│   ├── __init__.py
│   ├── srva
│   │   ├── __init__.py
│   │   └── hello.py
│   └── srvb
│       ├── __init__.py
│       ├── goodbye.py
│       └── secret.py
└── tools
    ├── tool1
    │   ├── __init__.py
    │   └── toolone.py
    └── tool2
        ├── __init__.py
        └── tooltwo.py
├── tests
│   ├── __init__.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── srva
│   │   │   ├── __init__.py
│   │   │   └── test_hello.py
│   │   └── srvb
│   │       ├── test_common_interaction.py
│   │       └── test_goodbye.py
│   └── tools
│       ├── tool1
│       │   └── test_tool_one.py
│       └── tool2
│           └── test_tool_two.py
```