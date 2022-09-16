# Useful tools for idle loops
import math

level = int(input("Enter current action % ")) + 1
total_actions = 0
while level <= 100:
    total_actions += level
    level += 1
print(total_actions, 'actions to max this skill')
time_min = int(input("How many minutes does your loop take? "))
time_sec = int(input("Seconds? "))
time = time_min*60 + time_sec
actions_per_loop = int(input("How many actions do you achieve per loop? If you have glasses, "
                             "a pickaxe, or something similar, multiply by that "))
progress_boost = int(input("What percentage boost does this action have? Enter an integer equal to the % boost "))
actions_per_loop = actions_per_loop*(1 + (0.01 * progress_boost))
loops_until_max = math.ceil(total_actions/actions_per_loop)
print(loops_until_max, "loops until max")
seconds_until_done = loops_until_max * time
minutes_until_done = math.floor(seconds_until_done / 60)
seconds_until_done -= 60*minutes_until_done
print(str(minutes_until_done) + "m " + str(seconds_until_done) + "s until this skill is maxed")