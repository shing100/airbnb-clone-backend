# AIRBNB 클론

- poetry
  poetry add django, black, ...

# docs

- https://www.django-rest-framework.org/
- https://www.django-rest-framework.org/api-guide/viewsets/

### Categories

GET POST /categories
GET(Rooms) PUT DELETE / categories/1

### Rooms

GET POST /rooms
GET PUT DELETE /rooms/1
GET /rooms/1/amenities
GET /rooms/1/reviews
GET POST /rooms/1/bookings
GET PUT DELETE /rooms/1/bookings/2
GET POST /amenities
GET PUT DELETE /amenities/1

### Experiences

GET POST /experiences
GET PUT DELETE /experiences/1
GET /experiences/1/perks
GET POST /experiences/1/bookings
