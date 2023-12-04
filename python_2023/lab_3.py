# Створимо словник для зберігання найкращих результатів гравців
best_scores = {}

# Дані гравців з прикладу
data = [
    "69485 Jack",
    "95715 qwerty",
    "95715 Alex",
    "83647 M",
    "197128 qwerty",
    "95715 Jack",
    "93289 Alex",
    "95715 Alex",
    "95715 M"
]

# Зчитуємо дані з прикладу і оновлюємо найкращі результати гравців
for line in data:
    score, player = line.split()
    score = int(score)
    # Перевіряємо, чи це кращий результат для гравця
    if player in best_scores:
        if score > best_scores[player]:
            best_scores[player] = score
    else:
        best_scores[player] = score

# Сортуємо гравців за найкращими результатами та їх іменами
sorted_players = sorted(best_scores.keys(), key=lambda x: (-best_scores[x], x))

# Визначаємо переможця та призерів
winners = []
for i, player in enumerate(sorted_players[:3]):
    place = i + 1
    score = best_scores[player]
    winners.append(f"{place} місце. {player} ({score})")

# Виводимо результат
print("\n".join(winners))