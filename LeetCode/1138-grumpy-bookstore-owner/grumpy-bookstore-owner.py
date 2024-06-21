class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)
        unrealized_customers = 0

        # Calculate initial number of unrealized customers in first 'minutes' window
        for i in range(minutes):
            unrealized_customers += customers[i] * grumpy[i]

        max_unrealized_customers = unrealized_customers

        # Slide the 'minutes' window across the rest of the customers array
        for i in range(minutes, n):
            
            unrealized_customers += customers[i] * grumpy[i]
            unrealized_customers -= customers[i - minutes] * grumpy[i - minutes]

            # Update the maximum unrealized customers
            max_unrealized_customers = max(
                max_unrealized_customers, unrealized_customers
            )

        total_customers = max_unrealized_customers

        for i in range(n):
            total_customers += customers[i] * (1 - grumpy[i])

        return total_customers