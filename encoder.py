
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

    chordified_song = score.chordify()

    for forced_chord in chordified_song.recurse().getElementsByClass(chord.Chord):
        print(f"Chord: {forced_chord} at offset {forced_chord.offset} for {forced_chord.duration.quarterLength} beats. Notes: {forced_chord.notes}")
        chord_length = len(forced_chord.notes)

        if chord_length > max_overlapping_notes:
            max_overlapping_notes = chord_length

    return max_overlapping_notes


def separate_song_overlappings(file_path):







# Example usage
file_path = 'Sample Songs/tester2.mid'
find_max_overlapping_notes(file_path)
# separate_song_overlappings(file_path)

# check_note_overlap(notes)


