
reg_last_digit = 8

min_limit = 250 + (reg_last_digit * 5)
max_limit = 3200 + (reg_last_digit * 50)
variation_limit = 700 + (reg_last_digit * 20)

n = int(input("Enter number of songs: "))

playlist = []

for i in range(n):
    duration = int(input(f"Enter duration of song {i+1} in seconds: "))
    playlist.append(duration)

if any(duration <= 0 for duration in playlist):
    print("\nInvalid Playlist! Durations must be greater than 0.")
    exit()

total_duration = sum(playlist)
number_of_songs = len(playlist)


if total_duration < min_limit:
    category = "Too Short Playlist"
    recommendation = "Add more songs to increase listening time."

elif total_duration > max_limit:
    category = "Too Long Playlist"
    recommendation = "Consider reducing playlist length."

elif len(playlist) != len(set(playlist)):
    category = "Repetitive Playlist"
    recommendation = "Add variety to avoid repetition."

elif (min_limit <= total_duration <= max_limit) and (max(playlist) - min(playlist) <= variation_limit):
    category = "Balanced Playlist"
    recommendation = "Good listening session."

else:
    category = "Irregular Playlist"
    recommendation = "Try balancing song durations."

print("\n--- Playlist Analysis Report ---")
print("Personalized Short Limit:", min_limit)
print("Personalized Long Limit:", max_limit)
print("Total Duration:", total_duration, "seconds")
print("Songs:", number_of_songs)
print("Category:", category)
print("Recommendation:", recommendation)