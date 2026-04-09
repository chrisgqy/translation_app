# ✨ PyLate — A Stylish Desktop Translator

> Translate text instantly with a sleek, modern UI built using PyQt5.

PyLate is a lightweight desktop translation app that combines a clean developer-friendly backend with a polished dark-themed interface. It supports multiple languages and lets you quickly swap, reset, and translate text in just a few clicks.


## 🚀 Features

* 🌍 Multi-language translation (powered by `googletrans`)
* 🔄 Reverse input/output with one click
* 🧹 Reset fields instantly
* 🎨 Modern dark UI (Qt + QSS styling)
* ⚡ Fast and simple — no bloat


## 🖼️ Preview

*(Add a screenshot here if you want — it’ll look great in your repo)*


## 🛠️ Tech Stack

* Python 3
* PyQt5 (GUI)
* googletrans (translation API)
* QSS (Qt styling)


## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/your-username/pylate.git
cd pylate
```

Install dependencies:

```bash
pip install PyQt5 googletrans==4.0.0-rc1
```

> ⚠️ Note: `googletrans` is unofficial and can occasionally break. If it does, that’s not your fault 🙂



## ▶️ Running the App

```bash
python main.py
```

That’s it — the app window should launch instantly.



## 🧠 How It Works

1. Enter text in the input box
2. Select source + target language
3. Click **Translate Now**
4. (Optional) Use:

   * 🔄 Reverse → swap languages & text
   * 🧹 Reset → clear everything


## 📁 Project Structure

```text
pylate/
│
├── main.py        # Main PyQt app
├── style.qss      # UI styling (optional but recommended)
└── languages.py   # Language mappings
```


## ⚠️ Known Limitations

* `googletrans` is not an official API (can be unstable)
* Async calls are handled simply (may block UI briefly)

## 💡 Future Ideas

* 🔊 Text-to-speech
* 📋 Copy button
* 🌐 Auto-detect language
* 🧵 Threaded async (non-blocking UI)
* 🎨 Theme switching


## 📜 License

MIT — do whatever you want
