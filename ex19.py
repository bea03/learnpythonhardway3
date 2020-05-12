#ex19 Functions & Variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f'you have {cheese_count} slices of cheese & {boxes_of_crackers} boxes of crackers')
    print('thats enough for a party')
    print('get a blanket')

print("Give them directly to function:")
cheese_and_crackers(50, 10)

print('or we can def within the script(globally):')
amount_of_cheeses = 55
amount_of_crackers = 12

cheese_and_crackers(amount_of_cheeses, amount_of_crackers)

print('we can even do math inside the arg params:')
cheese_and_crackers(10+5, 5+1)

print('and we can comb with variables too:')
cheese_and_crackers(amount_of_cheeses + 6, amount_of_crackers + 1)
