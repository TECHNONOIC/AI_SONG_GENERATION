from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = "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"

def generate_song_lyrics(user_input):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "System prompt..."},
            {"role": "user", "content": user_input}
        ]
    )
    response = completion.choices[0].message['content']
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    generated_lyrics = ""
    if request.method == "POST":
        Rhymescheme = request.form.get("rhymescheme")
        Artist = request.form.get("artist")
        Genre = request.form.get("genre")
        Seedtext = request.form.get("seedtext")

        user_input = f"Rhymescheme: {Rhymescheme}\nArtist: {Artist}\nGenre: {Genre}\nSeedtext: {Seedtext}"
        generated_lyrics = generate_song_lyrics(user_input)

    return render_template("index.html", generated_lyrics=generated_lyrics)

if __name__ == "__main__":
    app.run(debug=True)
