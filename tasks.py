from invoke import task

@task
def start(c):
    c.run("python3 src/interface.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests", pty=True)

@task
def coverage_report(ctx):
    """Generate coverage report."""
    ctx.run("coverage run --source=src -m pytest src/tests")
    ctx.run("coverage report")
    ctx.run("coverage html")
import sys
print(sys.path)
