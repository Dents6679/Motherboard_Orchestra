
import music21 as m21


def extract_notes_from_score(score):
    notes = []
    for element in score.flat.notes:
        if isinstance(element, m21.note.Note):
            notes.append(element)
        elif isinstance(element, m21.chord.Chord):
            notes.extend(element.notes)
    return notes


def find_max_overlapping_notes(file_path):
    max_overlapping_notes = 0
    score = m21.converter.parse(file_path)

    chordified_song = score.chordify()

    for forced_chord in chordified_song.recurse().getElementsByClass(m21.chord.Chord):
        chord_length = len(forced_chord.notes)

        if chord_length > max_overlapping_notes:
            max_overlapping_notes = chord_length

    return max_overlapping_notes


def separate_song_overlappings(file_path):
    notes = []
    streams = []
    score = m21.converter.parse(file_path)
    notes = extract_notes_from_score(score)
    max_overlap = find_max_overlapping_notes(file_path)

    note_sets = [[]]*max_overlap  # Create empty note sets

    for i, note in enumerate(notes):  # Distribute notes into note sets.
        note_sets[i % max_overlap].append(note)

    i = 0
    for note in notes:

        if note.offset == 0 and i > max_overlap - 1:
            #Handle chord notes
            i += 1
            continue

        for note_set in note_sets:
            note_set.append(m21.note.Rest(duration=note.duration))

        note_sets[i % 4].pop()
        note_sets[i % 4].append(note)



    for i, note_set in enumerate(note_sets):
        s = note_set.
        fp = f"tmp/{i}.mid"
        s.write("midi", fp)
    print("Written 4 note files to disk.")




# Example usage
file_path = 'Sample Songs/tester2.mid'
separate_song_overlappings(file_path)


