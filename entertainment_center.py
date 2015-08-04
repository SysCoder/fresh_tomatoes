import media
import fresh_tomatoes

# Create data for movie collection
toy_story = media.Movie(
    "Toy Story",
    "A boy toys comes to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=4KPTXpQehio")
jurassic_park = media.Movie(
    "Jurrasic World",
    "An asset(dino) gets out of control",
    "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
    "https://www.youtube.com/watch?v=RFinNxS5KN4")
mission_impossible_5 = media.Movie(
    "Mission Impossible 5",
    "With the IMF now disbanded and Ethan Hunt (Tom Cruise) out in the " +
    "cold, a new threat -- called the Syndicate -- soon emerges.",
    "http://t1.gstatic.com/images?q=" +
    "tbn:ANd9GcQ2QqFVBlMs6FLqvr_q_NiiylRGzbt47aGTDCHdEEOZqp8zclxe",
    "https://www.youtube.com/watch?v=nmC6rZyByzk")
ant_man = media.Movie(
    "Ant-Man",
    "Forced out of his own company by former protege Darren Cross, " +
    "Dr. Hank Pym (Michael Douglas) recruits the talents of Scott Lang " +
    "(Paul Rudd)," +
    "a master thief just released from prison.",
    "http://t3.gstatic.com/images?q=" +
    "tbn:ANd9GcRvTs_PtoegY0eToOxODXT12cfV-AipOD6GftFO0ze7wbociMNB",
    "https://www.youtube.com/watch?v=pWdKf3MneyI")

movies = [toy_story, jurassic_park, mission_impossible_5, ant_man]

# Creates movie page and open web browser to created page
fresh_tomatoes.open_movies_page(movies)
