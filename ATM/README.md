# Iteration 1

## Business rules
We want to build an ATM machine and the first thing we need to do, is to create the software that will breakdown which bills (notes) and coins to give you when you are trying to make a withdrawal.

The content of the ATM is:

| Value | Type |
|-------|------|
| 500   | bill |
| 200   | bill |
| 100   | bill |
| 50    | bill |
| 20    | bill |
| 10    | bill |
| 5     | bill |
| 2     | coin |
| 1     | coin |

Example

Input:

As a user
I withdraw 434€

Output:

2 bills of 200.
1 bill of 20.
1 bill of 10.
2 coins of 2.

## Possible API for the ATM

### Primitive Obsession and tight couple to the presentation

public interface ATM {
    public String withdraw(int quantity);
}

### Returning list of DTO or Value Objects
public interface ATM {
    public List<Money> withdraw(int quantity);
}

### Outside-in

public interface ATM {
    public void withdraw(int quantity);
}

# Iteration 2

## Business rules
The ATM machine has the following distribution of money.

If the ATM has no more bills or coins should try to use other quantities to allow the user to withdraw the amount.
The initial state of any ATM

| Value | Type | quantity of units |
|-------|------|-------------------|
| 500   | bill | 2                 |
| 200   | bill | 3                 |
| 100   | bill | 4                 |
| 50    | bill | 12                |
| 20    | bill | 20                |
| 10    | bill | 50                |
| 5     | bill | 100               |
| 2     | coin | 250               |
| 1     | coin | 500               |

Examples:
 
initial ATM state:

 
| Value | Type | quantity of units |
|-------|------|-------------------|
| 500   | bill | 2                 |
| 200   | bill | 3                 |
| 100   | bill | 4                 |
| 50    | bill | 12                |
| 20    | bill | 20                |
| 10    | bill | 50                |
| 5     | bill | 100               |
| 2     | coin | 250               |
| 1     | coin | 500               |

Input

As a user
I withdraw 1725€

Output

2 bills of 500.
3 bills of 200.
1 bill of 100.
1 bill of 20.
1 bill of 5.
 

ATM state after the output

| Value | Type | quantity of units |
|-------|------|-------------------|
| 500   | bill | 0                 |
| 200   | bill | 0                 |
| 100   | bill | 4                 |
| 50    | bill | 12                |
| 20    | bill | 19                |
| 10    | bill | 50                |
| 5     | bill | 99                |
| 2     | coin | 250               |
| 1     | coin | 500               |
 

Input

As a user
I withdraw 1825€
Output

4 bills of 100.
12 bills of 50.
19 bills of 20.
44 bills of 10.
1 bill of 5.
 

ATM state after the output

| Value | Type | quantity of units |
|-------|------|-------------------|
| 500   | bill | 0                 |
| 200   | bill | 0                 |
| 100   | bill | 0                 |
| 50    | bill | 0                 |
| 20    | bill | 0                 |
| 10    | bill | 6                 |
| 5     | bill | 99                |
| 2     | coin | 250               |
| 1     | coin | 500               |
 

# Disclaimer
The graphic examples that you see on the kata are not there to be implemented if you don't want to, are there as a reference of how the kata works
