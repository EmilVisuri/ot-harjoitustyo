from invoke import task

@task
def start(ctx):
    """
    Käynnistä ohjelma.
    """
    ctx.run("poetry run python src/interface.py")

@task
def test(ctx):
    ctx.run("pytest tests", pty=True)

@task
def coverage(ctx):
    """Generate coverage report."""
    ctx.run("coverage run -m pytest tests")
    ctx.run("coverage report")
    ctx.run("coverage html")