from flask import Flask, render_template, jsonify
import random
import os

app = Flask(__name__)

# A set of words that rhyme with "render"
RHYME_WORDS = [
    "render", "sender", "defender", "tender", "mender",
    "bender", "blender", "vendor", "pretender", "splendor",
    "surrender", "remember"
]

# A list of line templates that will include one rhyme word.
TEMPLATES = [
    "I call out to the night, my heart will {word},",
    "On the streets of dreams, the light will {word},",
    "When the world gets cold, my soul will {word},",
    "I paint my days in gold, I choose to {word},",
    "Through storms and thunder, I still {word},",
    "We rise together, never to {word},",
    "A gentle whisper makes me {word},",
    "Lost then found, my hope will {word},",
    "With every step I'm nearer, I will {word},",
    "In echoes of the city, songs {word}."
]

# Build a short verse (4 lines) where each line ends with a rhyme word.
def build_song(lines=4):
    song_lines = []
    choices = random.sample(RHYME_WORDS, k=min(len(RHYME_WORDS), lines))
    for i in range(lines):
        tmpl = random.choice(TEMPLATES)
        word = choices[i]
        line = tmpl.format(word=word)
        song_lines.append(line)
    chorus = "And in the end, the beat will render — hearts remember and surrender."
    return {"lines": song_lines, "chorus": chorus}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/song")
def song():
    return jsonify(build_song(lines=4))

if __name__ == "__main__":
    # Render requires 0.0.0.0 + PORT env variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
