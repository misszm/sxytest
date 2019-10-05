from tasks import app


@app.task
def asd(s):
    print(s)


@app.task
def zxc(s):
    print(s)
