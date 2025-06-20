
````markdown
# 📰 Insta-News – Flask-Based News Aggregator

Insta-News is a responsive web app built with Flask and Bootstrap that allows users to search and view the latest news across various categories like UK, India, US, Technology, Finance, and more. It fetches real-time data using the [NewsAPI.org](https://newsapi.org/) service.

---

## 🌟 Features

- 🔍 Search news articles by keyword or topic
- 🌍 Explore predefined categories: UK, India, US, World, Finance, etc.
- 🖼️ Clean, card-based UI with article images and links
- ❌ Filters out unwanted articles (e.g., Yahoo News or removed titles)
- 🧱 Built with Flask, HTML, SCSS (compiled to CSS), and Bootstrap 5

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/insta-news.git
cd insta-news
````

### 2. Set Up Virtual Environment (Optional but Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** You may need to create a `requirements.txt` using:

```bash
pip freeze > requirements.txt
```

### 4. Configure API Key

Create a `config.py` file (already included in the repo):

```python
NEWS_API_KEY = "your_api_key_here"
```

Get your API key from [https://newsapi.org](https://newsapi.org).

### 5. Run the App

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🗂️ Project Structure

```
.
├── app.py
├── config.py
├── templates/
│   ├── base.html
│   └── index.html
├── static/
│   └── styles.css (compiled from styles.scss)
├── styles.scss
├── README.md
└── requirements.txt

---

## 🙋‍♂️ Acknowledgments

* [NewsAPI.org](https://newsapi.org/)
* [Bootstrap 5](https://getbootstrap.com/)


