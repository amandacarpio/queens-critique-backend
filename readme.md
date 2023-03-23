# Queens Critique
### Concept
Queens Critique is an online review site where users are able to review their favorite or non-favorite restaurants in Queens, NY. I will be integrating the Yelp Fusion API to populate restaurants in the area and my CRUD functionality will reflect the users comments/reviews for restaurants they select.

### Backend Technologies Used

* Django
* Python

### Routes and CRUD functions
|Path|Action| Description
|----|----|----|
|'/'| Main | Homepage will have a simple display that will include a search bar for users to look for specific restaurants.
|'/writeareview'| Create | Create page will allow user to create a customized order.
|'/:id' | Show | Show page will display a specific restaurant and reviews along with it.
|'/critique/update/:id' | Update | Will update the review.
|'/critique/delete/:id' | Delete | Will delete the review.