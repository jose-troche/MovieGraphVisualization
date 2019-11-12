# MovieGraphVisualization

## Website
* 1000 movies
  * https://jose-troche.github.io/MovieGraphVisualization/web/index.html
  * https://movie-visualizer.s3-us-west-2.amazonaws.com/index.html

* All movies (graph gets children of first 3 children of root). It takes a while to load the first time, but then is fine
  * https://movie-visualizer.s3-us-west-2.amazonaws.com/index_full.html




General approch:

* Cleaned the data using pandas to produce:
  * **ratings**: The ratings csv file was processed to get average rating per movie
  * **movies**: was merged with the ratings data. 
    * Size: 45463 rows × 6 columns
    * Efficiency can be calculated as: avg(rating)/budget * 10M

 ```json
{
    "budget": 65000000,
    "collections": [1, 455],
    "id": 8844,
    "rating": 3.7601626016,
    "talent": [205, 511],
    "title": "Jumanji"
}
```
  * **talent**: united cast and crew data and then merged with movies and ratings to produce the following structure:
    * Size: 353358 rows × 8 columns
    * Revenue: sum of revenue across all movies that talent participated in
    * Rating: average rating across all movies that talent participated in
    * movies: All movies talent participated in
    * role_order: Role order, 0 is more important, primary role. All crew has role_order 0
    * genres: list of all genres of all movies talent participated in
    * job: all roles/jobs that talent had across all movies
```json
{
  "talent_id": 1,
  "name": "George Lucas",
  "revenue": 24640912129,
  "rating": 1.5837354681,
  "movies": [
    636,
    10372,
    11,
    55676
  ],
  "role_order": [
    0,
    2,
    14,
    21,
    24,
    58,
    27
  ],
  "genres": [
    10752,
    10402,
    99,
    35,
    36,
    10751
  ],
  "job": [
    "Screenplay",
    "Author",
    "Executive Producer",
    "Editor",
    "Producer",
    "Director",
    "Writer",
    "Characters",
    "Story",
    "Actor"
  ]
}
```
  * **collections**: list of collections ids and names
  * **genres**: list of movie gender ids and names

These new structures make it easy to build the graph of movies and talent with the correspondent data for each

## Source dataset
An application to visualize data from https://www.kaggle.com/rounakbanik/the-movies-dataset
