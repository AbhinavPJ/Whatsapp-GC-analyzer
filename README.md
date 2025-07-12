# 📊 WhatsApp Group Chat Analyzer

This Python script analyzes a WhatsApp group chat export (`.txt` format) and produces visual statistics about message activity, user contributions, and word usage.

---

## 📁 Input

The script expects a WhatsApp chat exported in `.txt` format (e.g., `batch.txt`) using the "Without Media" option from WhatsApp.
> ✅ Currently supports the US/India-style date and time format from WhatsApp exports.

---

## 📈 Output

The script processes the file and generates the following plots:

| File Name | Description |
|-----------|-------------|
| `1.png`   | Bar graph of number of messages sent per user (top 30 contributors) |
| `2.png`   | Time series plot of total words sent per day |
| `3.png`   | Bar chart showing activity by hour (0–23) |
| `4.png`   | Word Cloud of the most common words used in the chat |

---

## 🔧 Setup & Usage

### 1. 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### 2. 📂 Place your WhatsApp export

Place the exported `batch.txt` file (or rename your own export to this name) in the same directory as the script.

### 3. ▶️ Run the script
If you have exported using an IOS version of whatsapp,run:
```bash
python ios.py
```
and for android:
```bash
python android.py
```
This will produce the image files (`1.png` to `4.png`) in the current directory.

---

## 🧼 Features

- Handles Unicode and formatting issues
- Skips system messages like "Messages are end-to-end encrypted", etc.
- Generates easy-to-understand visualizations
- Compatible with standard WhatsApp export formats

---

## 📌 Notes

- Only English messages are currently well supported (no stemming or lemmatization is applied).
- Modify `STOPWORDS` set in the script if you want to exclude/include additional words in the Word Cloud.

---

## 👨‍💻 Author

Abhinav PJ

---

## 🪪 License

This project is licensed under the MIT License.
