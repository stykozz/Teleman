import math

series_name = input("Enter the name of the series: ")
num_seasons = int(input("Enter the number of seasons: "))
num_episodes_per_season = int(input("Enter the number of episodes per season: "))
episode_duration = int(input("Enter the duration of a regular episode in minutes: "))

total_time = num_seasons * num_episodes_per_season * episode_duration

special_episode_duration = episode_duration + 12

total_time_special = num_seasons * special_episode_duration

total_time_with_commercials = total_time * 1.25 + total_time_special

total_time_with_commercials = math.ceil(total_time_with_commercials)

print(f"I needed {total_time_with_commercials} minutes to watch the {series_name} all series.")