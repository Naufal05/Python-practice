# 1. Ask the user for inputs

# 2. save data in a dictionary

#3 whether if new bid needs to added - yes or no

#4 Compare the bids in dictionary and print the winner with highest bid

# name = input("What is your name?: ")
# price = int(input("What is your bid?: $"))

# bids[name] = price


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidder? Type 'Yes' or 'No'").lower()
    if should_continue == "no":
        continue_bidding = False
        # find the highest bidder and print the winner
    elif should_continue == "yes":
        print("\n" * 20)

# print(bids)
find_highest_bidder(bids)

"""
We can also use the max() function to find the highest bid and the winner. Here's how you can do it:
def find_highest_bidder(bidding_record):
    winner = max(bidding_record, key=bidding_record.get)
    highest_bid = bidding_record[winner]
    print(f"The winner is {winner} with a bid of ${highest_bid}")
"""