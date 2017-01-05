import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toy',
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=vwyZH85NQC4')
#print(toy_story.storyline)
avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg',
                     'http://www.youtube.com/watch?v=-9ceBgWV8io')
#print(avatar.storyline)
#avatar.show_trailer()
rio = media.Movie('Rio',
                  'A story of a blue bird',
                  'http://varelanoticias.com.br/wp-content/uploads/2014/11/rio2.jpg',
                  'https://www.youtube.com/watch?v=HMLvMxWncz8')
#print(rio.storyline)
#rio.show_trailer()
the_proposal = media.Movie('The Proposal',
                           'A pushy boss forces her young assistant to marry her in order to keep her visa status in the U.S. and avoid deportation to Canada.',
                           'https://upload.wikimedia.org/wikipedia/en/0/02/The_Proposal.jpg',
                           'https://www.youtube.com/watch?v=RFL8b1p1ELY')
ratatouille = media.Movie('Ratatouille',
                          'Is a mouse who dreams to becoming a great chef',
                          'https://upload.wikimedia.org/wikipedia/pt/8/82/Ratatouille_p%C3%B4ster.jpg',
                          'https://www.youtube.com/watch?v=c3sBBRxDAqk')
the_devil_wears_prada = media.Movie('The Devil wears Prada',
                                    'The movie The Devil Wears Prada tells the story of a young newly-formed dreams to work in journalism in a newspaper famous, but one can put on a fashion magazine called Runaway, not knowing she wasthis magazine one of the biggest fashion magazines.',
                                    'https://upload.wikimedia.org/wikipedia/pt/1/1d/The_Devil_Wears_Prada_p%C3%B4ster.jpg',
                                    'https://www.youtube.com/watch?v=PZnCe9BgO-o')
movies = [toy_story,avatar,rio,the_proposal,ratatouille,the_devil_wears_prada]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__module__)