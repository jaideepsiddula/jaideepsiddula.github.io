import media
import backendcode
ghazi=media.Movie("GHAZI",
	"XXXXX",
	"https://upload.wikimedia.org/wikipedia/en/thumb/e/e7/The_Ghazi_Attack_Poster.jpg/220px-The_Ghazi_Attack_Poster.jpg",
	"https://www.youtube.com/watch?v=1gKddowLVo0")
logan=media.Movie("LOGAN",
	"XXXXX",
	"https://upload.wikimedia.org/wikipedia/en/3/37/Logan_2017_poster.jpg",
	"https://www.youtube.com/watch?v=Div0iP65aZo")
Rangoon=media.Movie("RANGOON",
	"XXXXX",
	"https://upload.wikimedia.org/wikipedia/en/thumb/b/b3/RangoonPoster.jpg/220px-RangoonPoster.jpg",
	"https://www.youtube.com/watch?v=B-tC0wcIu24")
passengers=media.Movie("PASSENGERS",
	"XXXXX",
	"https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Passengers_2016_film_poster.jpg/220px-Passengers_2016_film_poster.jpg",
	"https://www.youtube.com/watch?v=7BWWWQzTpNU")
raaes=media.Movie("RAAES",
	"XXXXX",
	"https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg",
	"https://www.youtube.com/watch?v=J7_1MU3gDk0")
schoolofrock=media.Movie("SCHOOL OF ROCK",
	"XXXXX",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=XCwy6lW5Ixc")
movies=[raaes,passengers,Rangoon,logan,ghazi,schoolofrock]
backendcode.open_movies_page(movies)