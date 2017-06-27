from flask_script import Command
import code

class REPL(COmmand):
    "runs the shell"

    def run(self):
        code.interact(local=locals())
