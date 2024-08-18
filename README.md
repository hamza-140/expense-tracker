<div align="center">
  
  # Expense Tracker
  
  <img src="https://imgs.search.brave.com/tYMA2XVC8fJrXLXgfPNoSgzBvtIl4Y2T_UaddTEyPiY/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5nYWxsLmNvbS93/cC1jb250ZW50L3Vw/bG9hZHMvNy9CdWRn/ZXQtUE5HLVRyYW5z/cGFyZW50LUhELVBo/b3RvLnBuZw" height="300" alt="avatar" />
  
  [Overview](#🎯-overview) •
  [Features](#✨-features) •
  [Getting Started](#🚀-getting-started) •
  [Usage](#📘-usage) •
  [API](#📚-api)
  
</div>

---

## 🎯 Overview

The **Expense Tracker** is a simple command-line application that helps users manage their personal finances by tracking their expenses. Users can add, update, delete, and view expenses, as well as generate summaries of their expenditures. The main objective is to provide a straightforward tool for monitoring and organizing financial activities.

## ✨ Features

- **Add Expense**: Add a new expense with a description and amount.
- **Update Expense**: Modify the details of an existing expense.
- **Delete Expense**: Remove an expense by its unique ID.
- **List Expenses**: View all recorded expenses in a tabular format.
- **Expense Summary**: Get a summary of total expenses, either overall or for a specific month.

## 🚀 Getting Started

To run the Expense Tracker on your local machine, follow these steps:

### Prerequisites

Ensure you have Python installed on your system.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hamza-140/expense-tracker.git
   cd expense-tracker
   ```

2. The application doesn't require any external dependencies beyond Python's standard library, so you're ready to go!

## 📘 Usage

Here’s how you can use the Expense Tracker:

### Adding an Expense

```bash
python expense_tracker.py add --description "Lunch" --amount 20
# Output: Expense added successfully (ID: 1234)
```

### Listing All Expenses

```bash
python expense_tracker.py list
# Output: 
# ID      Date        Description     Amount
# 1234    2024-08-14  Lunch           $20
# 5678    2024-08-15  Dinner          $10
```

### Updating an Expense

```bash
python expense_tracker.py update --id 1234 --description "Brunch" --amount 25
# Output: Expense updated successfully!
```

### Deleting an Expense

```bash
python expense_tracker.py delete --id 1234
# Output: Expense deleted successfully!
```

### Viewing a Summary of All Expenses

```bash
python expense_tracker.py summary
# Output: Total expenses: $30
```

### Viewing a Summary of Expenses for a Specific Month

```bash
python expense_tracker.py summary --month 8
# Output: Total expenses for August: $30
```

## 📚 API

Here’s a brief overview of the functions available in the Expense Tracker:

### `add_exp(description, amount)`

Adds a new expense to the tracker.

| Parameter    | Type   | Description                         |
|--------------|--------|-------------------------------------|
| `description`| String | The description of the expense.     |
| `amount`     | String | The amount of the expense.          |

**Example**:
```python
add_exp("Lunch", 20)
```

### `update_exp(id, description, amount)`

Updates an existing expense with new details.

| Parameter    | Type   | Description                               |
|--------------|--------|-------------------------------------------|
| `id`         | Int    | The ID of the expense to update.          |
| `description`| String | The new description of the expense.       |
| `amount`     | String | The new amount of the expense.            |

**Example**:
```python
update_exp(1234, "Brunch", 25)
```

### `delete_exp(id)`

Deletes an expense by its ID.

| Parameter | Type | Description                     |
|-----------|------|---------------------------------|
| `id`      | Int  | The ID of the expense to delete.|

**Example**:
```python
delete_exp(1234)
```

### `display()`

Displays all expenses in a tabular format.

**Example**:
```python
display()
```

### `summary(month)`

Provides a summary of total expenses, either for all time or a specific month.

| Parameter | Type | Description                                  |
|-----------|------|----------------------------------------------|
| `month`   | Int  | The month number (1-12) for a specific summary. |

**Example**:
```python
summary(8)
```

---
## CC
https://roadmap.sh/projects/expense-tracker