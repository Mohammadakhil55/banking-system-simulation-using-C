#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_ACCOUNTS 10

struct Account {
    char name[20];
    char acc_no[12];
    int balance;
    char account_type[12]; 
};

struct Account accounts[MAX_ACCOUNTS]; 
int total_accounts = 0;

void menu();
void create_account();
void deposit_money();
void withdraw_money();
void transfer_money();
void account_details();
int find_account(int acc_no);

void initialize_predefined_account() {
    if (total_accounts < MAX_ACCOUNTS) {
        struct Account predefined1 = { "Mohammad Akhil", 12345678910, 6000, "Savings" };
        struct Account predefined2 = { "sumanth M", 12345678920, 4000, "Savings" };
        struct Account predefined3 = { "pushkar M", 12345678930, 90000, "current" };
        struct Account predefined4 = { "murali K", 12345678940, 20000, "current" };
        accounts[total_accounts] = predefined1;
        accounts[total_accounts] = predefined2;
        accounts[total_accounts] = predefined3;
        accounts[total_accounts] = predefined4;
        total_accounts++;
        printf("Predefined account added: Mohammad Akhil, Account Number: 1234567890, Balance: 2000, Type: Savings\n");
        printf("Predefined account added: sumanth M, Account Number: 12345678920, Balance: 4000, Type: Savings\n");
        printf("Predefined account added: pushkar M, Account Number: 12345678930, Balance: 90000, Type: current\n");
        printf("Predefined account added: murali K, Account Number: 12345678940, Balance: 20000, Type: current\n");
    } else {
        printf("Cannot add predefined account, account limit reached!\n");
    }
}

int main() {
    int choice;

    initialize_predefined_account();

    while (1) {
        menu();
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1: create_account(); break;
            case 2: deposit_money(); break;
            case 3: withdraw_money(); break;
            case 4: transfer_money(); break;
            case 5: account_details(); break;
            case 6: exit(0);
            default: printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}

void menu() {
    printf("\nMAIN MENU\n");
    printf("1. Create account\n");
    printf("2. Deposit money\n");
    printf("3. Withdraw money\n");
    printf("4. Transfer money\n");
    printf("5. Account details\n");
    printf("6. Exit\n");
}

void create_account() {
    if (total_accounts >= MAX_ACCOUNTS) {
        printf("Account limit reached! Cannot create more accounts.\n");
        return;
    }

    printf("Enter name: ");
    scanf("%s", accounts[total_accounts].name);
    while (1){
    printf("Enter account number (11 digits): ");
    scanf("%s",&accounts[total_accounts].acc_no);
    if (strlen(accounts[total_accounts].acc_no)==11{
        break;
    }
    else { printf("invalid account number! it must be exactly")}

    int account_type_choice;
    printf("Select account type:\n");
    printf("1. Savings\n");
    printf("2. Current\n");
    printf("Enter your choice: ");
    scanf("%d", &account_type_choice);

    switch (account_type_choice) {
        case 1: strcpy(accounts[total_accounts].account_type, "Savings"); break;
        case 2: strcpy(accounts[total_accounts].account_type, "Current"); break;
        default:
            printf("Invalid choice! Defaulting to Savings.\n");
            strcpy(accounts[total_accounts].account_type, "Savings");
            break;
    }
    accounts[total_accounts].balance = 2000; 
    printf("Account created successfully with initial balance of 2000.\n");
    total_accounts++;
}

void deposit_money() {
    int acc_no, amount;
    printf("Enter account number: ");
    scanf("%d", &acc_no);
    int index = find_account(acc_no);
    if (index == -1) {
        printf("Account not found!\n");
        return;
    }

    printf("Enter amount to deposit: ");
    scanf("%d", &amount);
    accounts[index].balance += amount;
    printf("Amount deposited successfully. Current balance: %d\n", accounts[index].balance);
}

void withdraw_money() {
    int acc_no, amount;
    printf("Enter account number: ");
    scanf("%d", &acc_no);
    int index = find_account(acc_no);
    if (index == -1) {
        printf("Account not found!\n");
        return;
    }

    printf("Enter amount to withdraw: ");
    scanf("%d", &amount);
    if (amount > accounts[index].balance) {
        printf("Insufficient balance!\n");
    } else {
        accounts[index].balance -= amount;
        printf("Amount withdrawn successfully. Current balance: %d\n", accounts[index].balance);
    }
}

void transfer_money() {
    int source_acc, target_acc, amount;
    printf("Enter your account number: ");
    scanf("%d", &source_acc);
    int source_index = find_account(source_acc);
    if (source_index == -1) {
        printf("Source account not found!\n");
        return;
    }

    printf("Enter target account number: ");
    scanf("%d", &target_acc);
    int target_index = find_account(target_acc);
    if (target_index == -1) {
        printf("Target account not found!\n");
        return;
    }

    printf("Enter amount to transfer: ");
    scanf("%d", &amount);
    if (amount > accounts[source_index].balance) {
        printf("Insufficient balance in source account!\n");
    } else {
        accounts[source_index].balance -= amount;
        accounts[target_index].balance += amount;
        printf("Amount transferred successfully. Current balance: %d\n", accounts[source_index].balance);
    }
}

void account_details() {
    int acc_no;
    printf("Enter account number: ");
    scanf("%d", &acc_no);
    int index = find_account(acc_no);
    if (index == -1) {
        printf("Account not found!\n");
        return;
    }

    printf("\nAccount details\n");
    printf("Name: %s\n", accounts[index].name);
    printf("Account Number: %d\n", accounts[index].acc_no);
    printf("Account Type: %s\n", accounts[index].account_type);
    printf("Current Balance: %d\n", accounts[index].balance);
}

int find_account(int acc_no) {
    for (int i = 0; i < total_accounts; i++) {
        if (accounts[i].acc_no == acc_no)
            return i;
    }
    return -1;
}
