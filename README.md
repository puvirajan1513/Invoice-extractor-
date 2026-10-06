# 🧾 AI Invoice Extractor

An AI-powered invoice extraction application that uses a **multimodal Large Language Model (LLM)** to analyze invoice images and extract structured information such as invoice details, vendor/customer information, line items, quantities, prices, taxes, and total amounts.

Built with **Python, Streamlit, Qwen 3.6 27B, and Groq API**.

## 🚀 Features

- 📄 Upload invoice images
- 🤖 Multimodal AI-powered invoice understanding
- 🧾 Extract invoice number and date
- 🏢 Extract vendor and customer details
- 📦 Extract invoice line items
- 🔢 Extract quantities and unit prices
- 💰 Extract tax and total amounts
- ✅ Field-level validation
- ⚠️ Error handling for missing or invalid fields
- 💬 Ask follow-up questions about the invoice
- ⚡ Fast inference using Groq
- 🖥️ Interactive Streamlit interface

## 🧠 How It Works

```text
Invoice Image
     │
     ▼
Image Processing
     │
     ▼
Multimodal LLM
(Qwen 3.6 27B)
     │
     ▼
Structured Information
Extraction
     │
     ▼
Field Validation
     │
     ▼
Invoice Results
     │
     ▼
Natural Language
Follow-up Questions
```

The application uses a multimodal LLM to understand both the **visual layout and textual content** of an invoice. Instead of depending on fixed invoice templates, the model identifies relevant information dynamically.

## 📋 Extracted Information

### Invoice Details

- Invoice Number
- Invoice Date
- Vendor / Supplier
- Customer / Buyer

### Line Items

- Product / Service
- Quantity
- Unit Price
- Amount

### Financial Details

- Tax
- Total Amount
- Other available monetary information

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application |
| Qwen 3.6 27B | Multimodal LLM |
| Groq API | LLM inference |
| Pillow | Image processing |
| Base64 | Image encoding |
| python-dotenv | Environment variable management |

## 💬 Example Queries

After uploading an invoice, users can ask questions such as:

```text
What is the invoice number?

Who is the vendor?

What is the total amount?

What is the tax amount?

How many items are present?

What is the price of the second item?
```

## 📁 Project Structure

```text
Invoice-Extractor/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── ...
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/puvirajan1513/Invoice-Extractor.git
cd Invoice-Extractor
```

### 2. Create a Conda environment

```bash
conda create -n invoice-extractor python=3.11
conda activate invoice-extractor
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

**Never commit your `.env` file or API key to GitHub.**

### 5. Run the application

```bash
streamlit run app.py
```

The application will run at:

```text
http://localhost:8501
```

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

```text
GitHub
   ↓
Streamlit Community Cloud
   ↓
Install Dependencies
   ↓
Configure GROQ_API_KEY
   ↓
Run app.py
   ↓
Live AI Invoice Extractor
```

For cloud deployment, add the API key through **Streamlit Secrets** instead of storing it in the repository.

```toml
GROQ_API_KEY = "your_groq_api_key"
```

## 🎯 Key Concepts

This project demonstrates practical experience with:

- Generative AI
- Multimodal LLMs
- Vision-Language Models
- Document AI
- Information Extraction
- Prompt Engineering
- LLM API Integration
- Structured Data Extraction
- Image Processing
- Data Validation
- Conversational AI
- Streamlit
- Cloud Deployment

## 🔮 Future Enhancements

- 📄 PDF invoice support
- 📊 CSV / Excel export
- 🗄️ Database integration
- 📦 Batch invoice processing
- 🔎 Invoice search and filtering
- 📈 Invoice analytics dashboard
- 🧾 Duplicate invoice detection
- 🧮 Advanced financial validation
- 🌍 Multilingual invoice support

## 👨‍💻 Author

**Puvi Rajan**

B.Tech Artificial Intelligence & Machine Learning

[GitHub](https://github.com/puvirajan1513) • [LinkedIn](https://www.linkedin.com/in/puvirajan-pasupathy-118938258/)

---

⭐ If you find this project useful, consider giving the repository a star.
