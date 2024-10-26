# lint.py
import sys
from pylint import lint

THRESHOLD = 9

# Pylint for Application
run = lint.Run(["app.py"], do_exit=False)
appScore = run.linter.stats["global_note"]
if appScore < THRESHOLD:
    print("Linter failed: appScore < threshold value")

# Pylint for Model Creation
run = lint.Run(["model creation.py"], do_exit=False)
modelScore = run.linter.stats["global_note"]
if modelScore < THRESHOLD:
    print("Linter failed: modelScore < threshold value")

# Pylint for Results
run = lint.Run(["result.py"], do_exit=False)
resultScore = run.linter.stats["global_note"]
if resultScore < THRESHOLD:
    print("Linter failed: resultScore < threshold value")

sys.exit(0)
