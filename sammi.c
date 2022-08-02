#include <stdio.h>

int main()
{
  int cost = 5000, total = 0, num_pass = 0, tickets;
  printf("%d\n", cost);
  while (num_pass <= 70)
  {
    printf("ENTER NUMBER OF TICKETS: ");
    scanf("%d", &tickets);
    if (tickets == -1)
    {
      total = num_pass * cost;
      printf("Total number if Passengers = %d\n", num_pass);
      printf("Total Amount: %d\n", total);
      break;
    }
    num_pass = tickets + num_pass;

    if (num_pass > 70)
    {
      printf("Sorry max number of passengers is 70\n");
      num_pass = num_pass - tickets;
    }
    else if (num_pass == 70)
    {
      total = num_pass * cost;
      printf("Total number if passengers = %d\n", num_pass);
      printf("Total Amount: %d\n", total);
      break;
    }

    printf("Actual number if passengers = %d\n", num_pass);
  }
}