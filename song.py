from flask import Flask, render_template, jsonify
import random
if __name__ == "__main__":
    app.run(debug=True)
app = Flask(__name__)

# A set of words that rhyme with "render"
RHYME_WORDS = [
    "render", "sender", "defender", "tender", "mender",
    "bender", "blender", "vendor", "pretender", "splendor",
    "surrender", "remember"  # "remember" slant-rhyme, keeps it playful
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
    # To keep variety, shuffle rhyme words and pick
    choices = random.sample(RHYME_WORDS, k=min(len(RHYME_WORDS), lines))
    for i in range(lines):
        tmpl = random.choice(TEMPLATES)
        word = choices[i]
        # ensure grammar: if template ends with comma, place word before comma,
        # otherwise place at end. We'll keep template placeholders consistent.
        line = tmpl.format(word=word)
        song_lines.append(line)
    # Optional short chorus that repeats "render"
    chorus = "And in the end, the beat will render — hearts remember and surrender."
    return {"lines": song_lines, "chorus": chorus}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/song")
def song():
    # Each request returns a fresh song
    song_obj = build_song(lines=4)
    return jsonify(song_obj)

if __name__ == "__main__":
    app.run(debug=True)
