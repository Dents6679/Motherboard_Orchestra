
from music21 import *


def extract_notes_from_score(score):
    notes = []
    for element in score.flat.notes:
        if isinstance(element, note.Note):
            notes.append(element)
        elif isinstance(element, chord.Chord):
            notes.extend(element.notes)
    return notes


def find_max_overlapping_notes(file_path):
    max_overlapping_notes = 0
    score = converter.parse(file_path)

    bChords = score.chordify()

    for thisChord in bChords.recurse().getElementsByClass(chord.Chord):
        chord_length = len(thisChord.notes)

        if chord_length > max_overlapping_notes:
            max_overlapping_notes = chord_length

    return max_overlapping_notes


def separate_song_overlappings(file_path):
    score = converter.parse(file_path)
    notes = extract_notes_from_score(score)
    pass





# Example usage
file_path = 'Sample Songs/MiiChannel.mid'
find_max_overlapping_notes(file_path)

# check_note_overlap(notes)


