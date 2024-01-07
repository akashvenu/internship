class SongSuggestionProgram:
    def __init__(self):
        self.song_attributes = {
            "Happy Pop Song": "Happy, Pop",
            "Sad Ballad Song": "Sad, Ballad",
            "Energetic Rock Song": "Energetic, Rock",
            "Chill Indie Song": "Chill, Indie",
            "Romantic Jazz Song": "Romantic, Jazz",
            "Motivational Hip Hop Song": "Motivational, Hip Hop"
        }

    def get_suggested_songs(self, mood, genre):
        suggested_songs = [song for song, attributes in self.song_attributes.items()
                           if mood.lower() in attributes.lower() and genre.lower() in attributes.lower()]
        return suggested_songs

    def run_program(self):
        print("Welcome to the Song Suggestion Program!")
        print("Please select your preferences:")

        mood = input("Enter your mood (Happy, Sad, Energetic, Chill, Romantic, Motivational): ")
        genre = input("Enter your preferred genre (Pop, Ballad, Rock, Indie, Jazz, Hip Hop): ")

        suggested_songs = self.get_suggested_songs(mood, genre)

        print("\nSuggestions based on your preferences:")
        for song in suggested_songs:
            print("- " + song)

        input("\nPress Enter to exit.")


if __name__ == "__main__":
    program = SongSuggestionProgram()
    program.run_program()
