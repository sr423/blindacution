import art
print(art.logo)

#TODO Compare data dictionary
def find_highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bidding_value=bidding_dictionary[bidder]
        if bidding_value>highest_bid:
            highest_bid=bidding_value
            winner=bidder

    print(f"The winner is {winner} and the highest amount of bid is {highest_bid}")

bids={}
should_continue=True
while should_continue:
    name = input("What is your name:")
    price = float(input("What is your bid price:"))
    bids[name]=price
    direction = input("Are there any bidders 'yes' or 'no'\n").lower()

    if should_continue == "no":
        should_continue = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n*10")
