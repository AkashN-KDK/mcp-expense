 # MCP Expense Tracker

An expense-tracking MCP server built with Python, SQLite, and FastMCP. It lets an MCP-compatible client such as Claude Desktop record expenses, list them by date range, and summarize spending by category.

## Available tools

- `add_expense`: Add an expense with a date, amount, category, optional subcategory, and note.
- `list_expenses`: List expenses between two dates.
- `summarize`: Calculate totals by category, optionally filtered to one category.
- `expense://categories`: Read the available categories from `categories.json`.

Expenses are stored locally in `expenses.db`, which is created automatically when the server starts.

## Run locally

Install dependencies and start the MCP server with:

```bash
uv sync
uv run fastmcp run main.py
```

## Add to Claude Desktop

From the project directory, run:

```bash
uv run fastmcp install claude-desktop main.py --name ExpenseTracker
```

Restart Claude Desktop after installation so it reloads the MCP configuration.
