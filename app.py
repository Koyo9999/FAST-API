from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import math

app = FastAPI()

html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>実質１０００円カットジェネレーター</title>
    <style>
        body {
            text-align: center;
            font-family: 'Arial', sans-serif;
            margin: 50px;
        }
        h1 {
            font-size: 24px;
            font-weight: bold;
        }
        form {
            margin-top: 20px;
        }
        input {
            padding: 5px;
            font-size: 16px;
        }
        button {
            padding: 5px 10px;
            font-size: 16px;
            cursor: pointer;
        }
        div {
            margin-top: 20px;
            font-size: 18px;
        }
    </style>
</head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-TYZNT8XY8S"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-TYZNT8XY8S');
</script>
<body>
    <h1>実質１０００円カットジェネレーター</h1>
    <form method="post" action="/calculate">
        <label for="input_number">カット代を入力してね♪</label>
        <input type="number" name="input_number" step="1">
        <button type="submit">計算する</button>
    </form>
    <div>
        <p>結果 {{ result }} 日です！</p>
    </div>
</body>
</html>
"""

@app.get("/")
def read_root():
    return HTMLResponse(content=html_form.replace('{{ result }}', ''), status_code=200, media_type="text/html")

@app.post("/calculate", response_class=HTMLResponse)
def calculate(input_number: int = Form(None)):
    result = ''
    if input_number is not None:
        result = str(math.ceil((input_number * 30) / 1000))
    return HTMLResponse(content=html_form.replace('{{ result }}', result), status_code=200, media_type="text/html")
