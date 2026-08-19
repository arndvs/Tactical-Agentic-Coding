RUN:
    checkout a new/existing "demo-agentic-coding" git branch

CREATE main_aic.py:
    print "goodbye ai coding"

CREATE main_tac.py:
    print "hello agentic coding"
    print a concise explanation of the definition of ai agents

RUN:
    uv run main_aic.py
    uv run main_tac.py
    git add .
    git commit -m "Demo agentic coding capabilities"

REPORT:
    respond with the exact output of both .py files