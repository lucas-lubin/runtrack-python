def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
        
            notes_arrondies.append(note)
        else:
           
            difference = 5 - (note % 5)
            if difference < 3:
                note_arrondie = note + difference
                notes_arrondies.append(note_arrondie)
            else:
                notes_arrondies.append(note)

    return notes_arrondies


liste_notes = [37, 82, 65, 95, 42]
notes_arrondies = arrondir_notes(liste_notes)

print("Notes d'origine   :", liste_notes)
print("Notes arrondies   :", notes_arrondies)
