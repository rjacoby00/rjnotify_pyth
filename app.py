from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return '''
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>RJ Notification Service</title>

  <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <link rel="stylesheet" href="https://code.getmdl.io/1.2.1/material.indigo-pink.min.css">
  <script defer src="https://code.getmdl.io/1.2.1/material.min.js"></script>
  <link rel="stylesheet" href="styles/index.css">
</head>

<body>

  <header>
    <h1>RJ Notify</h1>
  </header>

  <main>
    <p>Welcome to RJ Notify.  Press the button below to join and get a key.</p>
    <p>
      <button disabled class="js-push-btn mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect">
        Enable Push RJ Notify
      </button>
    </p>
    <section class="subscription-details js-subscription-details is-invisible">
      <p>Subsribed, here's your key:</p>
      <pre><code class="js-subscription-json"></code></pre>
    </section>
  </main>

  <script src="scripts/main.js"></script>

  <script src="https://code.getmdl.io/1.2.1/material.min.js"></script>
</body>
</html>
	
'''
if __name__ == "__main__":
	app.run()
