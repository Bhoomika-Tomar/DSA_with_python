class Solution:
    def gen_ticket_code (self, N: int ) -> str:

        ticket_code = "A"

        for i in range (2, N+1):

            new_ticket_code = ""
            curr_char = ticket_code[0]
            char_count = 0

            for j in range (len(ticket_code)):
                if ticket_code[j] == curr_char:
                    char_count += 1

                else:
                    new_ticket_code += str(char_count) + curr_char

                    curr_char = ticket_code[j]
                    char_count = 1

            new_ticket_code += str(char_count) + curr_char

            ticket_code = new_ticket_code

        return ticket_code


N = int(input("Enter the no of tickets"))
sol = Solution()
print(sol.gen_ticket_code(N))
                    