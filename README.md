# Supplier Discovery Platform

An AI-powered supplier discovery platform that helps users find manufacturers and suppliers using natural language queries.

## Features

* Search suppliers using natural language
* Discover company websites using Serper API
* Extract business details using Firecrawl
* Retrieve:

  * Company Name
  * Industry
  * Products
  * Email
  * Phone Number
  * Website
* Interactive Streamlit dashboard
* CSV export functionality

## Tech Stack

* Python
* Streamlit
* Firecrawl
* Serper API
* Pandas

## Example Query

garment manufacturers in delhi

## Example Output

| Company       | Industry              | Email                                                       | Phone             |
| ------------- | --------------------- | ----------------------------------------------------------- | ----------------- |
| Sai Creations | Apparel Manufacturing | [hello@saicreations.co.in](mailto:hello@saicreations.co.in) | (+91) 120-4356635 |

## Installation

```bash
git clone https://github.com/Priyanshujain144/Supplier-Discovery-Platform.git
cd Supplier-Discovery-Platform

pip install -r requirements.txt
```

Create a `.env` file:

```env
SERPER_API_KEY=your_key
FIRECRAWL_API_KEY=your_key
GROQ_API_KEY=your_key
```

Run:

```bash
streamlit run streamlit_app.py
```

## Future Improvements

* SQLite database
* Search history
* Parallel processing
* Improved supplier ranking
* Better contact extraction
