
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
    score = m21.converter.parse(file_path)
    notes = extract_notes_from_score(score)

    max_overlap = find_max_overlapping_notes(file_path)
    note_sets = [[]]*max_overlap
    print(note_sets)
    for i, note in enumerate(notes):
        note_sets[i % max_overlap].append(note)

    for i, note_set in enumerate(note_sets):
        s = m21.stream.Stream()
        for note in note_set:
            s.append(note)
        fp = f"tmp/{i}.mid"
        s.write("midi", fp)
    print("Written 4 note files to disk.")



# Example usage
file_path = 'Sample Songs/tester2.mid'
separate_song_overlappings(file_path)


