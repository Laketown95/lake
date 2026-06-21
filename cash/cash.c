#include <cs50.h>
#include <stdio.h>

int calculate_coins(int cents, int coin_value);

int main(void)
{
    // Prompts the user for the change owed in cents
    int cent;
    do
    {
        cent = get_int("Change owed: ");
    }
    while (cent < 0);

    // Calculate how many quarters you should give customer
    int quarters = calculate_coins(cent, 25);

    // Subtract the value of those quarters from cents
    cent -= quarters * 25;

    // Calculate how many dimes you should give customer
    int dimes = calculate_coins(cent, 10);

    // Subtract the value of those dimes from remaining cents
    cent -= dimes * 10;

    // Calculate how many nickles you should give customer
    int nickles = calculate_coins(cent, 5);

    // Subtract the value of those nickles from remaining cents
    cent -= nickles * 5;

    // Calculate how many pennies you should give customer
    int pennies = calculate_coins(cent, 1);

    // Subtract the value of those nickes from remaining cents
    cent -= pennies * 1;

    // Sum all coins and print
    int total = quarters + dimes + nickles + pennies;
    printf("%i\n", total);
}

// General coin calculator
int calculate_coins(int cent, int coin_value)
{
    return cent / coin_value;
}
