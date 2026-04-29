import pypokerprob

cards_evaluate_one = [[5, 'hearts'], [3, 'hearts'], [14, 'hearts'], [7, 'hearts']]
print(pypokerprob.evaluate_all_known_cards(cards_evaluate_one))

Mylist=pypokerprob.card_list()
print(Mylist)

starting_prob_high=pypokerprob.starting_probabililty_high_card()
print(starting_prob_high)

cards_structure_flush=[[1, 'clubs'], [8, 'clubs'], [3, 'clubs'], [13, 'clubs'], [10, 'clubs']]
flush_check=pypokerprob.flush_structure(cards_structure_flush)
print(flush_check)

chosen_cards=pypokerprob.draw_cards_random(7)
print(chosen_cards)