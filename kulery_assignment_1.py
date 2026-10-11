def hawkid():
    return(["Karin Ulery", "kulery"])



def import_data(filename):
   participants = []
   with open(filename, 'r') as f:
       for line in f:
           parts = line.strip().split(',')
           name = parts[0]
           ptype = parts[1]
           hp = float(parts[2])
           dmg = float(parts[3])
           participants.append([name, ptype, hp,dmg])
   return (participants) 


pokemon = import_data('test_input.csv')


# print(pokemon)



def attack_multiplier(attacker_type, defender_type):
    if attacker_type == 'Water' and defender_type == 'Fire':
        return 2.5
    elif attacker_type == 'Electric' and defender_type == 'Water':
            return 1.3
    elif attacker_type == 'Ground' and defender_type == 'Electric':
            return 2.0
    elif attacker_type == 'Fire' and defender_type == 'Grass':
            return 3.0
    elif attacker_type == 'Grass' and defender_type == 'Water':
            return 1.5
    else:
        return 1.0



# print(attack_multiplier("Water", "Fire"))     # 2.5
# print(attack_multiplier("Electric", "Water")) # 1.3
# print(attack_multiplier("Fire", "Electric"))  # 1.0



def fight(participant1, participant2, first2attack):
    hp1 = participant1[2]
    hp2 = participant2[2]
    rounds = 0
    while hp1 > 0 and hp2 > 0:
        if first2attack == 1:
            attacker_type = participant1[1]
            defender_type = participant2[1]
            base_damage = participant1[3]
            mult = attack_multiplier(attacker_type, defender_type)
            damage = base_damage * mult
            hp2 -= damage
          
        else:
            attacker_type = participant2[1]
            defender_type = participant1[1]
            base_damage = participant2[3]
            mult = attack_multiplier(attacker_type, defender_type)   
            damage = base_damage * mult
            hp1 -= damage

        rounds += 1
        
        if first2attack == 1:
            first2attack = 2
        else:
            first2attack = 1

    if hp1 > 0:
        winner = 1
    else:
        winner = 2
    
    return[winner, rounds]



# print(fight(pokemon[0], pokemon[1], 1))  # Baltoy vs Flareon
# print(fight(pokemon[2], pokemon[4], 2))  # Alomomola vs Pikachu
# print(fight(pokemon[3], pokemon[2], 1))  # Gogoat vs Alomomola


def tournament(participants):
    wins = [0] * len(participants)

    for i in range(len(participants)):
        for j in range(i + 1, len(participants)):

            # Home Game
            result_home = fight(participants[i], participants[j], 1)
            if result_home[0] == 1:
                wins[i] += 1
            else:
                wins[j] += 1

            # Away Game
            result_away = fight(participants[i], participants[j], 2)
            if result_away[0] == 1:
                wins[i] += 1
            else:
                wins[j] += 1

    # returing results with names
    results = []
    for i in range(len(participants)):
        name = participants[i][0]
        results.append((name, wins[i]))

    return results



print(tournament(pokemon))