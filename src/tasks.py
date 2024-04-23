from invoke import task

@task
def start(c):
    c.run("python3 interface.py")

@task
def test(ctx):
    ctx.run("pytest tests", pty=True)

@task
def coverage_report(ctx):
    """Generate coverage report."""
    ctx.run("coverage run -m pytest tests")
    ctx.run("coverage report")
    ctx.run("coverage html")
    
