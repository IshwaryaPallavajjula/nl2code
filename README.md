# NL2Code: Natural-Language-to-Code Generator

A small Python CLI that turns a plain-English task description into working Python code using a free LLM (Groq's Llama 3.3 or a local model through Ollama). The generated code is printed to the terminal and saved to a `.py` file automatically.

## How it works

1. A strict system prompt tells the model to return **only raw code**, with no explanations and no markdown fences.
2. Models still add fences sometimes, so `strip_fences()` removes them before anything is saved.
3. The result is checked with `ast.parse`. If it has a syntax error, the error is sent back to the model and it is asked to fix it (up to 3 attempts).
4. Valid code is printed and saved to `generated/<slug>.py`. Existing files are never overwritten (`_2`, `_3`, ... are appended).

## Setup

```bash
git clone <your-repo-url>
cd nl2code
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Option A: Groq (free, no credit card)

1. Create an API key at https://console.groq.com
2. Copy `.env.example` to `.env` and paste the key:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Option B: Ollama (fully offline)

```bash
ollama pull qwen2.5-coder
ollama serve
```

Then run with `-p ollama`.

## Usage

Single task:

```bash
python codegen.py "write a function that checks if a number is prime"
```

Interactive mode (no arguments):

```bash
python codegen.py
> write a function that reverses the order of words in a sentence
> quit
```

Batch mode (one task per line, `#` lines are ignored):

```bash
python codegen.py --batch tasks.txt
```

Options:

| Flag | Meaning |
| --- | --- |
| `-p, --provider` | `groq` (default) or `ollama` |
| `-m, --model` | Override the model name |
| `-o, --output-dir` | Folder for generated files (default `generated`) |
| `-b, --batch` | Run every task in a text file |
| `--no-save` | Print only, do not write a file |

## The 10 sample tasks

`tasks.txt` covers three areas:

- **String handling:** palindrome check, vowel count, reverse word order
- **Math:** prime check, nth Fibonacci number, factorial
- **List and dict operations:** dedupe preserving order, word frequencies, merge dicts summing shared keys, flatten nested lists

## Tests

```bash
pytest
```

The tests cover fence stripping, syntax validation, filename generation, batch file parsing and the retry logic, using a fake LLM so no API key is needed.

## Project structure

```
nl2code/
├── codegen.py
├── tasks.txt
├── requirements.txt
├── .env.example
├── tests/
│   ├── conftest.py
│   └── test_codegen.py
└── generated/        (created on first run)
```
