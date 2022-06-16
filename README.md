# Forage Boutique

## About Forage Boutique
Forage Boutique is a web application targeted at Amsterdam-based individuals who are interested in purchasing plants. As a full-stack e-commerce web application this project was built using Django, Python, HTML, CSS and JavaScript. This is a B2C (Business to Customer) designed to create better user experience to clients and provide useful management tools for the business owner. 

[Forage Boutique live website!](https://forageboutique.herokuapp.com/)

## UX/UI
Using core Design Thinking methods and Agile practices principles the strategy for this web application takes into consideration 2 personas: Business Owner and Client, and their respective needs. 

### User Stories

All user stories are documented with their respective acceptance criteria, story points and MoSCoW prioritization on [my Github Issues](https://github.com/anabramos/forageboutique/issues) or on [this excell google sheet](https://docs.google.com/spreadsheets/d/1tIHWxuTbgwAMaqZkwu3j8kelPhfHuCNg/edit?usp=sharing&ouid=116746214337321598702&rtpof=true&sd=true)

### Agile Practices

#### Wireframes
- All wireframes were designed with Canva tool. These can be found [here](https://github.com/anabramos/forageboutique/tree/main/media/wireframes). Final web application will differ slightly from wireframes as it will utilize more similar structures between different pages for better visual appeal and user experience.

#### Product Backlog & Project Board
- I created my product backlog using [my Github labels](https://github.com/anabramos/forageboutique/issues) with different colors, dividing user stories clusters more or less equally per iteration/epic. This however did not translate the build up order of the project, as I had overestimated how some tasks and features are dependent from others to being build.  
- For information radiators I have made use of [my Github Projects](https://github.com/anabramos/forageboutique/projects/1)

### Scope & Structure

In response to the user stories attributed to business owner and clients, the website and its features are structured withing the following 5 Custom Django apps:

1. Home
    Concerns the design of a Front-End web application that meets accessibility guidelines and provides a set for responsive user interaction via its homepage, navbar and navigation links. It contains a homepage with information about the website and navigation links that will take the client to different website features. 
2. Products
    Concerns the display of all products provided by the business owner, including prices. These are directly linked to the database and can be updated at anytime by admin users. Changes on the database are also immediately  translated to the Front-End of the website.
3. Bag
    Concerns the ability of clients to add and manage their bag contents and wished purchases, including modifying and deleting items from their shopping carts. 
4. Checkout
    Concerns the ability of clients to make and manage their purchases using financial software Stripe. This app also includes the possibility of retreiving information about past orders. This feature is only available for registered users when logged-in. Un-registered users will be requested to create an account if they want to access their purchase history.
5. Accounts
    Concerns the ability of clients to create and manage their account, including modifying the account details and shipping address. This feature is only available for registered users when logged-in. Un-registered users will be requested to create an account if they want to have their details saved for future purchases.

This web application also utilizes built-in django applications, frameworks and libraries to compliment the above mentioned structure and features. 

#### Database Structure

I have connected the database to the Heroku Postgres database from the beginning of deployment. I have created original custom models, the Entity-Relationship Diagram [here](https://github.com/anabramos/forageboutique/blob/main/media/database/database.PNG) shows how the database models relate to each other. 

### Design

#### Colors
The website colors are inspired by tons of green and terracota as key plant store colors. It uses dark green color and white to create contrast between text and background, and the other colors are used intertwined to reinforce borders, banners and highlight certain features/sections in the website.

#### Fonts
The website uses a combination of Pangolin and Roboto Condensed, with a fall back to sans-serif. These fonts are popularly paired together. Pangolin is used in the website for high-level headings and logo while Roboto Condensed is used for regular text and low level headings. The fonts were compared and taken from Google Fonts.

#### Icons
This website makes use of icons from Font Awesome to give a new visual element and reinforce the content already displayed. The Icons are used to indicate social media links on the website's footer.


## Technologies Used

- Languages
    - [HTML5](https://en.wikipedia.org/wiki/HTML)
    - [CSS](https://en.wikipedia.org/wiki/CSS)
    - [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- Libraries & Frameworks
    - [Django](https://www.djangoproject.com/)
    - [Bootstrap](https://getbootstrap.com/)
    - [Google Fonts](https://fonts.google.com/)
    - [Font Awesome](https://fontawesome.com/)
    Many more python libraries, extensions and frameworks can be found under the requirements.txt file

- Tools
    - [Gitpod](https://www.gitpod.io/)
    - [Github](https://github.com/)
    - [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
    - [Heroku](https://dashboard.heroku.com/apps)
    - [Cloudinary](https://cloudinary.com/)
    - [SQLite](https://www.sqlite.org/index.html)
    - [PostgreSQL](https://www.postgresql.org/)
    - [MBalsamiq](https://balsamiq.com/)
    - [Coolors (color schemes generator)](https://coolors.co/)
    - [Unsplash](https://unsplash.com/)
    - [Am I Responsive?](http://ami.responsivedesign.is/)
    - [WebAIM](https://webaim.org/resources/contrastchecker/)
    - [W3C HTML Validation Service](https://validator.w3.org/)
    - [W3C CSS Validation Service](https://validator.w3.org/)
    - [Pep8](http://pep8online.com/)
    - [JSHint](https://jshint.com/)
    - [Stripe](https://en.wikipedia.org/wiki/Stripe_(company))

