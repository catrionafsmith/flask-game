from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9 </h1><iframe src="https://giphy.com/embed/l2JHVUriDGEtWOx0c" width="480" height="204" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/disneyzootopia-l2JHVUriDGEtWOx0c">via GIPHY</a></p>'

ran_num = random.randint(0, 9)
@app.route('/<int:guess>')
def create_number(guess):
    if guess == ran_num:
        return '<h1>YOU GOT IT!</h1><iframe src="https://giphy.com/embed/4URfklUToxk6A" width="480" height="363" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/zootopia-zootopy-4URfklUToxk6A">via GIPHY</a></p>'
    elif guess > ran_num:
        return '<h1>Nooooooo too high</h1><iframe src="https://giphy.com/embed/3og0IuWMpDm2PdTL8s" width="480" height="306" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/redbull-3og0IuWMpDm2PdTL8s">via GIPHY</a></p>'
    else:
        return'<h1>Too low Joe</h1><iframe src="https://giphy.com/embed/dKpEvFHdGsZBRuszpv" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/chicagodancecrash-breakdance-limbo-backbend-dKpEvFHdGsZBRuszpv">via GIPHY</a></p>'
if __name__ == "__main__":
    app.run(port=8000, debug=True)